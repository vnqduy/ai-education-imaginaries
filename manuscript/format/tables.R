# One table API: editable Pandoc tables in Word, styled longtables in PDF.
lmt_table <- function(data, col.names = names(data), widths = NULL,
                      groups = NULL, font_size = 9, align = NULL) {
  if (is.null(align)) align <- c("l", rep("r", ncol(data) - 1L))
  if (!knitr::is_latex_output()) {
    if (!is.null(groups)) {
      # Preserve field grouping as explicit rows in the editable Word table.
      parts <- list(); start <- 1L
      for (i in seq_along(groups)) {
        label <- as.data.frame(as.list(rep("", ncol(data))), stringsAsFactors = FALSE)
        names(label) <- names(data); label[1, 1] <- paste0("**", names(groups)[i], "**")
        last <- start + groups[[i]] - 1L
        parts[[length(parts) + 1L]] <- label
        parts[[length(parts) + 1L]] <- as.data.frame(data[start:last, , drop = FALSE])
        start <- last + 1L
      }
      data <- do.call(rbind, parts)
    }
    return(knitr::kable(data, format = "pipe", col.names = col.names, align = align))
  }
  out <- kableExtra::kbl(data, format = "latex", booktabs = TRUE,
    longtable = TRUE, linesep = "", col.names = col.names, align = align) |>
    kableExtra::kable_styling(latex_options = "repeat_header", font_size = font_size,
      repeat_header_text = "(continued)")
  if (!is.null(widths)) for (i in seq_along(widths)) {
    out <- kableExtra::column_spec(out, i, width = paste0(widths[[i]], "cm"))
  }
  if (!is.null(groups)) out <- kableExtra::pack_rows(out, index = groups,
    indent = FALSE, latex_gap_space = "0.4em")
  out
}
