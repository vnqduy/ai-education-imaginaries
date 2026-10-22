-- Shared title/abstract pages and native editable Word table typography.
local function text(x) return pandoc.utils.stringify(x or '') end
local function paragraph(s) return pandoc.Para(pandoc.Inlines({pandoc.Str(s)})) end
local function styled(s, style)
  if FORMAT:match('latex') and style == 'Title' then
    return pandoc.Div({pandoc.RawBlock('latex', '\\begingroup\\fontsize{16}{20}\\selectfont\\bfseries'),
      paragraph(s), pandoc.RawBlock('latex', '\\par\\endgroup\\vspace{1em}')})
  end
  return pandoc.Div({paragraph(s)}, pandoc.Attr('', {}, {['custom-style']=style}))
end
local function pagebreak()
  if FORMAT:match('docx') then
    return pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
  end
  return pandoc.RawBlock('latex', '\\clearpage')
end
local function frontmatter(doc)
  local m = doc.meta
  if not m['lmt-frontmatter'] then return doc end
  local front = pandoc.Blocks({styled(text(m.title), 'Title')})
  if m.subtitle then front:insert(styled(text(m.subtitle), 'Subtitle')) end
  if not m.anonymous or text(m.anonymous) == 'false' then
    front:insert(paragraph(text(m['lmt-author'])))
    front:insert(paragraph(text(m['lmt-affiliation'])))
    front:insert(paragraph('Corresponding author: '..text(m['lmt-email'])))
  end
  if m.abstract then
    front:insert(pagebreak())
    front:insert(pandoc.Header(1, 'Abstract', pandoc.Attr('abstract', {'unnumbered'})))
    for _, block in ipairs(m.abstract) do front:insert(block) end
    local keywords = {}
    for _, item in ipairs(m.keywords or {}) do table.insert(keywords, text(item)) end
    front:insert(paragraph('Keywords: '..table.concat(keywords, '; ')))
  end
  front:insert(pagebreak())
  front:extend(doc.blocks)
  doc.blocks = front
  -- Explicit front matter avoids different metadata layouts in PDF and DOCX.
  m.title=nil; m.subtitle=nil; m.author=nil; m.abstract=nil; m.keywords=nil; m.date=nil
  return doc
end
local function word_table(t)
  if not FORMAT:match('docx') then return t end
  local function rowstyle(rows)
    for _, row in ipairs(rows) do
      for i, cell in ipairs(row.cells) do
        local alignment = cell.alignment
        if alignment == 'AlignDefault' and t.colspecs[i] then alignment = t.colspecs[i][1] end
        local style = alignment == 'AlignRight' and 'Table Number' or 'Table Text'
        local function wrap(p)
          return pandoc.Div({pandoc.Para(p.content)}, pandoc.Attr('', {}, {['custom-style']=style}))
        end
        cell.contents = pandoc.Div(cell.contents):walk({Plain=wrap, Para=wrap}).content
      end
    end
  end
  rowstyle(t.head.rows)
  for _, body in ipairs(t.bodies) do rowstyle(body.head); rowstyle(body.body) end
  rowstyle(t.foot.rows)
  return t
end
return {{Table=word_table}, {Pandoc=frontmatter}}
