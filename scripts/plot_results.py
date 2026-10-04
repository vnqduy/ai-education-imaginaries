import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/figures'
OUT.mkdir(parents=True,exist_ok=True)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
data=json.load((ROOT/'results/outlet_comparison.json').open())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.spines.bottom':False,'pdf.fonttype':42})
colors=['#246A91','#C16A2E']
legend=[Line2D([0],[0],marker='o',color=colors[0],linestyle='none',label='Public/central'),Line2D([0],[0],marker='s',color=colors[1],linestyle='none',label='Commercial/general')]
def panel(ax,title,items):
    for i,(k,label) in enumerate(items):
        a,b=data[k]['A']['pct'],data[k]['B']['pct']
        ax.plot([a,b],[i,i],color='#B9C3CA',lw=1.5,zorder=1)
        ax.scatter(a,i,color=colors[0],marker='o',s=40,zorder=3)
        ax.scatter(b,i,color=colors[1],marker='s',s=34,zorder=3)
    ax.set_yticks(range(len(items)),[x[1] for x in items])
    ax.set_ylim(len(items)-.4,-.6);ax.set_xlim(-1,101);ax.set_xticks([0,25,50,75,100])
    ax.grid(axis='x',color='#E7ECEF',lw=.7);ax.set_axisbelow(True)
    ax.tick_params(axis='y',length=0,pad=8,labelsize=9)
    ax.set_title(title,loc='left',fontsize=13,weight='bold',pad=12)
    ax.set_xlabel('Articles with indicator (%)',fontsize=9)
groups=[('A. Vision',[
('future_role__augmentation','Learning assistance'),('future_role__literacy','AI literacy / capabilities'),('future_role__talent','Specialist talent / innovation'),('future_role__harm','Harm / misuse'),('future_role__governed_use','Governed / conditional use'),('certainty__asserted','Asserted / expected'),('certainty__aspirational','Aspirations / plans'),('certainty__possible','Possible / conditional')]),
('B. Desirability',[
('desirability__positive','Positive evaluation'),('desirability__negative','Negative evaluation'),('desirability__ambivalent','Both positive and negative'),('rationale__learning_quality','Educational-quality rationale'),('rationale__protection','Integrity / safety / agency rationale'),('rationale__modernization','Change / adaptation rationale'),('rationale__national','National / strategic rationale')]),
('C. Futures',[
('timespan__dated','Explicit calendar date / period'),('timespan__era','Broad era / developmental phase'),('timespan__unspecified_future','Unspecified future'),('space__institutional','Institutional / immediate setting'),('space__national','Named country / nationwide')]),
('D. Technological object',[
('technology_object__general','General / unspecified AI'),('technology_object__generative','Generative / conversational AI'),('technology_object__educational_platforms','Educational AI applications'),('education_context__school','School / early childhood'),('education_context__higher','Higher education')]),
('E. Speaker',[
('speaker__government','Government / public authorities'),('speaker__institutions','Educational institutions'),('speaker__educators_experts','Educators / experts'),('speaker__industry','Companies / industry'),('speaker__learners','Learners / young people')]),
('F. Implications',[
('action__adoption','Adoption / deployment'),('action__training','Education / skills / curricula'),('action__development','System research / development'),('action__governance','Rules / verification / safeguards'),('responsibility__government','Government responsibility'),('responsibility__institutions','Institutional responsibility'),('responsibility__learners','Learner responsibility')])]
fig,axes=plt.subplots(3,2,figsize=(13.7,11.6),layout='constrained')
for ax,(title,items) in zip(axes.flat,groups):panel(ax,title,items)
fig.legend(handles=legend,loc='outside upper center',ncol=2,frameon=False)
fig.savefig(OUT/'figure1.png',dpi=200,bbox_inches='tight');plt.close(fig)
actors=[('A. Speakers',[
('speaker__government','Government / public authorities'),('speaker__institutions','Educational institutions'),('speaker__educators_experts','Educators / researchers / experts'),('speaker__industry','Companies / industry'),('speaker__learners','Learners / young people'),('speaker__families','Parents / families'),('speaker__civil_society','Civil society / collective organizations'),('speaker__media','Journalists / article authors'),('speaker__ai_voice','AI-generated voice'),('speaker__institutional_document','Institutional document')]),
('B. Affected entities',[
('affected_entities__learners','Learners / young people'),('affected_entities__educators','Educators / researchers'),('affected_entities__institutions','Educational institutions'),('affected_entities__families','Parents / families'),('affected_entities__workforce','Workforce / business'),('affected_entities__society','Society / general public'),('affected_entities__knowledge','Knowledge / culture / resources')]),
('C. Responsibility',[
('responsibility__government','Government / public authorities'),('responsibility__institutions','Educational institutions'),('responsibility__educators_experts','Educators / researchers / experts'),('responsibility__industry','Companies / industry'),('responsibility__learners','Learners / young people'),('responsibility__families','Parents / families'),('responsibility__civil_society','Civil society / collective organizations'),('responsibility__media','Journalists / article authors')])]
fig,axes=plt.subplots(3,1,figsize=(10.2,12.3),layout='constrained',gridspec_kw={'height_ratios':[10,7,8]})
for ax,(title,items) in zip(axes,actors):panel(ax,title,items)
fig.legend(handles=legend,loc='outside upper center',ncol=2,frameon=False)
fig.savefig(OUT/'figure2.png',dpi=200,bbox_inches='tight');plt.close(fig)
