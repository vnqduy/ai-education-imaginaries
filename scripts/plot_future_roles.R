library(tidyverse)
library(jsonlite)
library(patchwork)

# Nature-inspired: clean axes, sans-serif text, restrained colours.
theme_set(theme_classic(base_size = 11, base_family = "sans") +
  theme(axis.line = element_line(linewidth = .35),
        axis.ticks = element_line(linewidth = .3),
        panel.grid.major.x = element_line(colour = "grey92", linewidth = .3),
        strip.background = element_blank(), strip.text = element_text(face = "bold"),
        legend.position = "bottom", legend.title = element_blank(),
        plot.title = element_text(face = "bold"),
        plot.caption = element_text(colour = "grey40", hjust = 0)))

# Run from the project root, scripts/, or manuscript/.
root <- if (file.exists("results/article_coding.csv")) "." else ".."
articles <- read_csv(file.path(root, "results/article_coding.csv"),
                     show_col_types = FALSE) |> filter(main_sample == 1)
roles <- c(FR_LEARNING_PARTNER = "Learning Partner",
           FR_AI_LITERACY = "AI Literacy",
           FR_EDUCATIONAL_JUDGMENT = "Educational Judgment",
           FR_NATIONAL_DEVELOPMENT = "National Development",
           FR_EDUCATIONAL_MANAGEMENT = "Educational Management")
categories <- c(CERT_CONFIDENT = "Confident", CERT_POSSIBLE = "Possible",
                CERT_DENIED = "Denied", CERT_UNRESOLVED = "Unresolved",
                DES_POSITIVE = "Desirable", DES_NEGATIVE = "Undesirable",
                DES_MIXED = "Mixed", DES_UNDECIDED = "Undecided", MISSING = "Missing")
colours <- list(
  certainty = c(Confident = "#084594", Possible = "#2171B5", Denied = "#6BAED6",
                Unresolved = "#BDD7E7", Missing = "#EFF3FF"),
  desirability = c(Desirable = "#006D2C", Undesirable = "#31A354", Mixed = "#74C476",
                   Undecided = "#BAE4B3", Missing = "#EDF8E9"))

prevalence <- articles |>
  select(article_id, outlet_group, starts_with("future_role__FR_")) |>
  pivot_longer(starts_with("future_role__"), names_prefix = "future_role__",
               names_to = "role", values_to = "present") |>
  filter(present == 1) |>
  (function(d) bind_rows(d, mutate(d, outlet_group = "All")))() |>
  count(outlet_group, role, name = "N")

# CSV unions cannot establish same-account links; recover these from source coding.
linked <- readLines(file.path(root, "data/sipc_future_coding/coded_corpus.jsonl")) |>
  map(~ fromJSON(.x, simplifyVector = FALSE)) |>
  keep(~ .x$ID %in% articles$article_id) |>
  map_dfr(function(record) map_dfr(record$accounts, function(a) {
    if (!any(unlist(a$codes$future_role) %in% names(roles))) return(tibble())
    crossing(role = intersect(unlist(a$codes$future_role), names(roles)),
             field = c("certainty", "desirability")) |>
      mutate(article_id = record$ID,
             code = map(field, ~ unlist(a$codes[[.x]]))) |> unnest_longer(code)
  })) |>
  left_join(select(articles, article_id, outlet_group), by = "article_id")
linked <- bind_rows(linked, mutate(linked, outlet_group = "All"))

# Missing = no substantive code in any account carrying this role in the article.
profiles <- linked |> group_by(outlet_group, role, field, article_id) |>
  summarise(code = list(if (all(code == "MISSING")) "MISSING" else
    unique(code[code != "MISSING"])), .groups = "drop") |>
  unnest_longer(code) |> count(outlet_group, role, field, code, name = "n") |>
  group_by(outlet_group, role, field) |>
  complete(code = names(categories), fill = list(n = 0)) |>
  ungroup() |>
  filter(code == "MISSING" | (field == "certainty" & str_starts(code, "CERT_")) |
           (field == "desirability" & str_starts(code, "DES_"))) |> left_join(prevalence, by = c("outlet_group", "role")) |>
  mutate(percent = n / N,
         role = factor(roles[role], levels = rev(unname(roles))),
         category = factor(categories[code], levels = unname(categories)),
         outlet_group = factor(outlet_group,
           levels = c("All", "public/central", "commercial/general"),
           labels = c("All", "Public/central", "Commercial/general")))

# Stacks normalise overlapping article-code counts, including Missing, to 100%.
profile_plot <- function(field_name, groups) {
  profiles |> filter(field == field_name, outlet_group %in% groups) |>
    ggplot(aes(n, role, fill = category)) +
    geom_col(position = position_fill(reverse = TRUE), width = .65,
             colour = "white", linewidth = .25, orientation = "y") +
    geom_text(aes(label = if_else(n > 0, as.character(n), ""),
                  colour = category %in% names(colours[[field_name]])[1:2]),
              position = position_fill(vjust = .5, reverse = TRUE), size = 2.5) +
    facet_wrap(~outlet_group, ncol = 1) +
    scale_fill_manual(values = colours[[field_name]], drop = TRUE) +
    scale_colour_manual(values = c("FALSE" = "#222222", "TRUE" = "white"),
                        guide = "none") +
    scale_x_continuous(labels = scales::label_percent(), breaks = seq(0, 1, .25),
                       expand = expansion(mult = c(0, .01))) +
    labs(title = str_to_title(field_name), x = "Share of article-code counts (%)", y = NULL) +
    guides(fill = guide_legend(nrow = 2, byrow = TRUE))
}

figure_overall <- (
  prevalence |> filter(outlet_group == "All") |>
    ggplot(aes(N, factor(roles[role], levels = rev(unname(roles))))) +
    geom_col(fill = "#3C5488", width = .55) +
    geom_text(aes(label = N), hjust = -.25, size = 3.5) +
    scale_x_continuous(expand = expansion(mult = c(0, .12))) +
    labs(title = "Educational AI futures", x = "Articles", y = NULL)
) / (profile_plot("certainty", "All") | profile_plot("desirability", "All")) +
  plot_layout(heights = c(1, 2.4)) +
  plot_annotation(caption = "Main corpus: 828 articles. Labels: article counts. Stacks: share of summed counts, including Missing; categories overlap.")

figure_groups <- (
  profile_plot("certainty", c("Public/central", "Commercial/general")) |
  profile_plot("desirability", c("Public/central", "Commercial/general"))
) + plot_annotation(caption = paste(
  "Public/central: 424 articles; commercial/general: 404.",
  "Labels: article counts. Stacks: share of summed counts, including Missing; categories overlap."))


# Align comparable categories only; absent categories are not coded zeros.
actors <- tribble(
  ~code, ~actor,
  "SPK_LEARNER", "Learners",
  "RESP_LEARNER", "Learners",
  "AFFECT_LEARNER", "Learners",
  "SPK_ED_LEADERSHIP", "Educational organisations / leadership",
  "RESP_ED_ORG", "Educational organisations / leadership",
  "AFFECT_ED_ORG", "Educational organisations / leadership",
  "RESP_ED_WORKER", "Education and research workers",
  "AFFECT_ED_WORKER", "Education and research workers",
  "SPK_ACADEMIC_EXPERT", "Educators, researchers and specialists",
  "SPK_PUBLIC", "Public authorities",
  "RESP_PUBLIC", "Public authorities",
  "SPK_BUSINESS", "Commercial actors",
  "RESP_BUSINESS", "Commercial actors",
  "AFFECT_EMPLOYER", "Employers / non-education occupations",
  "SPK_FAMILY", "Families and caregivers",
  "RESP_FAMILY", "Families and caregivers",
  "AFFECT_FAMILY", "Families and caregivers",
  "SPK_COLLECTIVE", "Civic / international organisations",
  "RESP_COLLECTIVE", "Civic / wider collectives",
  "AFFECT_PUBLIC", "Wider communities / society",
  "SPK_AUTHOR", "Article's authorial voice"
)

counts <- articles |>
  select(article_id, outlet_group, matches("^(speaker|responsibility|affected_entities)__")) |>
  pivot_longer(contains("__"), names_to = c("field", "code"), names_sep = "__",
               values_to = "present") |>
  inner_join(actors, by = "code") |>
  mutate(present = replace_na(present, 0),
         actor = factor(actor, levels = rev(unique(actors$actor))),
         field = factor(field, levels = c("speaker", "responsibility", "affected_entities"),
                        labels = c("Speaking", "Responsible", "Affected")))

figure_actors <- counts |>
  group_by(actor, field) |>
  summarise(percent = mean(present), .groups = "drop") |>
  complete(actor, field) |>
  ggplot(aes(field, actor, fill = percent)) +
  geom_tile(colour = "white", linewidth = 1) +
  geom_text(aes(label = if_else(is.na(percent), "—", scales::percent(percent, accuracy = .1)),
                colour = !is.na(percent) & percent > .5), size = 3.5) +
  scale_fill_gradient(low = "#EFF3FF", high = "#084594", limits = c(0, 1),
                      na.value = "grey95", guide = "none") +
  scale_colour_manual(values = c("FALSE" = "#222222", "TRUE" = "white"), guide = "none") +
  labs(title = "Who speaks, acts and is affected?", x = NULL, y = NULL,
       caption = "Percentage of articles. — = no corresponding codebook category.") +
  theme(axis.line = element_blank(), axis.ticks = element_blank(), panel.grid = element_blank())

speaker_comparison <- counts |> filter(field == "Speaking") |>
  group_by(outlet_group, actor) |>
  summarise(percent = mean(present), .groups = "drop") |>
  pivot_wider(names_from = outlet_group, values_from = percent) |>
  mutate(gap = 100 * (`commercial/general` - `public/central`),
         actor = fct_reorder(actor, gap))

figure_speakers <- (
  ggplot(speaker_comparison, aes(y = actor)) +
    geom_segment(aes(x = `public/central`, xend = `commercial/general`, yend = actor),
                 colour = "grey65", linewidth = 1) +
    geom_point(aes(x = `public/central`, colour = "Public/central"), size = 3) +
    geom_point(aes(x = `commercial/general`, colour = "Commercial/general"), size = 3) +
    scale_colour_manual(values = c("Public/central" = "#3C5488", "Commercial/general" = "#E64B35")) +
    scale_x_continuous(labels = scales::label_percent(), expand = expansion(mult = .08)) +
    labs(x = "Articles within outlet group (%)", y = NULL)
) | (
  ggplot(speaker_comparison, aes(gap, actor)) +
    geom_vline(xintercept = 0, colour = "grey65", linetype = 2) +
    geom_segment(aes(x = 0, xend = gap, yend = actor), colour = "grey65") +
    geom_point(colour = "#3C5488", size = 2.5) +
    geom_text(aes(label = sprintf("%+.1f", gap)), nudge_y = .25, size = 3) +
    scale_x_continuous(expand = expansion(mult = .2)) +
    labs(x = "Difference (percentage points)", y = NULL) +
    theme(axis.text.y = element_blank(), axis.ticks.y = element_blank())
)
figure_speakers <- figure_speakers + plot_layout(widths = c(2, 1)) +
  plot_annotation(title = "Whose voices enter the discussion?",
                  caption = "Difference = commercial/general minus public/central. Positive values favour commercial/general.")


figure_misc <- articles |>
  select(starts_with("technology_object__"), starts_with("education_context__")) |>
  pivot_longer(everything(), names_to = c("field", "code"), names_sep = "__",
               values_to = "present") |>
  mutate(present = replace_na(present, 0)) |>
  group_by(field, code) |>
  summarise(n = sum(present), percent = mean(present), .groups = "drop") |>
  filter(code != "missing" | n > 0) |>
  mutate(label = recode(code,
    OBJ_GENERATIVE = "Generative AI", OBJ_PREDICTIVE = "Predictive / discriminative AI",
    OBJ_UNSPECIFIED = "AI form unspecified", CTX_SCHOOL = "School education",
    CTX_HIGHER = "Higher education", CTX_VOCATIONAL = "Vocational education",
    CTX_PROFESSIONAL = "Professional / workplace development",
    CTX_COMMUNITY = "Community / informal education", missing = "Context not specified"),
    label = fct_reorder(label, percent),
    field = factor(field, levels = c("technology_object", "education_context"),
                   labels = c("Technology", "Education context"))) |>
  ggplot(aes(percent, label, fill = field)) +
  geom_col(width = .6, show.legend = FALSE) +
  geom_text(aes(label = paste0(scales::percent(percent, accuracy = .1), " (", n, ")")),
            hjust = -.1, size = 3) +
  facet_wrap(~field, scales = "free_y", nrow = 1) +
  scale_fill_manual(values = c("#3C5488", "#00A087")) +
  scale_x_continuous(labels = scales::label_percent(), limits = c(0, .85),
                     expand = expansion(mult = c(0, .02))) +
  labs(title = "Which technologies and educational settings receive attention?",
       x = "Articles (%)", y = NULL,
       caption = "Labels: percentage (article count). Base: 828 articles; categories can overlap.")


print(figure_overall)
print(figure_groups)
print(figure_actors)
print(figure_speakers)

print(figure_misc)
