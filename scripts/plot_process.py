"""Create vector workflow figures with ReportLab and SVG (no corpus data)."""
from pathlib import Path
from html import escape
from reportlab.pdfgen import canvas

out=Path('results/figures');out.mkdir(parents=True,exist_ok=True)
W,H=600,760
pdf=canvas.Canvas(str(out/'process.pdf'),pagesize=(W,H))
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<title>Workflow for analysing educational AI futures in news coverage</title>',
'<desc>Six stages from corpus construction to account review, followed by relational interpretation and descriptive outlet comparison. Recovery and correction loops return to extraction and coding.</desc>',
'<rect width="600" height="760" fill="white"/>']

def text(x,y,s,size=12,bold=False,rotation=0):
 font='Helvetica-Bold' if bold else 'Helvetica'
 pdf.saveState();pdf.setFillColorRGB(.12,.12,.12);pdf.setFont(font,size)
 if rotation:
  pdf.translate(x,H-y);pdf.rotate(-rotation);pdf.drawCentredString(0,0,s)
 else:pdf.drawCentredString(x,H-y,s)
 pdf.restoreState()
 transform=f' transform="rotate({rotation} {x} {y})"' if rotation else ''
 svg.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial, sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="#222"{transform}>{escape(s)}</text>')

def box(x,y,w,h,title,lines):
 pdf.setStrokeColorRGB(.2,.2,.2);pdf.setFillColorRGB(.98,.98,.98);pdf.setLineWidth(.8);pdf.rect(x,H-y-h,w,h,fill=1,stroke=1)
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fafafa" stroke="#333" stroke-width=".8"/>')
 text(x+w/2,y+22,title,13,bold=True)
 for i,s in enumerate(lines):text(x+w/2,y+44+15*i,s,11.3)

def line(points,dashed=False,head=False):
 pdf.setStrokeColorRGB(.35,.35,.35);pdf.setLineWidth(.8);pdf.setDash(4,3) if dashed else pdf.setDash()
 p=pdf.beginPath();p.moveTo(points[0][0],H-points[0][1])
 for x,y in points[1:]:p.lineTo(x,H-y)
 pdf.drawPath(p)
 dash=' stroke-dasharray="4 3"' if dashed else ''
 svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+'" fill="none" stroke="#555" stroke-width=".8"'+dash+'/>')
 if head:
  x,y=points[-1];px,py=points[-2];dx,dy=x-px,y-py;n=(dx*dx+dy*dy)**.5;dx/=n;dy/=n
  tri=[(x,y),(x-7*dx+3*dy,y-7*dy-3*dx),(x-7*dx-3*dy,y-7*dy+3*dx)]
  pdf.setFillColorRGB(.35,.35,.35);pdf.setDash();p=pdf.beginPath();p.moveTo(tri[0][0],H-tri[0][1])
  for tx,ty in tri[1:]:p.lineTo(tx,H-ty)
  p.close();pdf.drawPath(p,fill=1,stroke=0)
  svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in tri)+'" fill="#555"/>')

steps=[
('1  Corpus construction',['Search, screen titles, consolidate duplicate hits,','and retrieve article texts']),
('2  Structured extraction',['Extract twelve SIPC fields; preserve evidence,','qualifications and distinct voices']),
('3  Source review and eligibility assessment',['Assess source adequacy and educational futurity separately;','recover incomplete sources where possible']),
('4  Codebook development',['Develop field categories from the full extraction corpus;','review definitions and freeze the codebook']),
('5  Account-level coding',['Apply the codebook to attributed future accounts;','retain primary and secondary positions']),
('6  Review and validation',['Check coverage, evidence, attribution and account consistency;','document amendments to affected records'])]
for i,(title,body) in enumerate(steps):
 y=15+100*i;box(90,y,420,72,title,body)
 if i:line([(300,y-28),(300,y)],head=True)
line([(90,251),(40,251),(40,151),(90,151)],dashed=True,head=True)
text(25,201,'Re-extract recovered texts',10,rotation=-90)
line([(510,551),(560,551),(560,451),(510,451)],dashed=True,head=True)
text(578,501,'Correct affected records',10,rotation=90)
line([(300,587),(300,620),(155,620),(155,640)],head=True)
line([(300,620),(445,620),(445,640)],head=True)
box(20,640,270,80,'Interpretation of educational futures',['Examine links among purposes, roles,','evaluations and actor positions'])
box(310,640,270,80,'Descriptive outlet comparison',['Compare constituent patterns; examine','composition and sensitivity'])
text(300,746,'Dashed arrows indicate targeted re-extraction or correction.',9)
svg.append('</svg>');(out/'process.svg').write_text('\n'.join(svg))
pdf.setTitle('Process for SIPC analysis of educational AI futures');pdf.showPage();pdf.save()
print('Created process.svg and process.pdf')
