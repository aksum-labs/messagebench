from pathlib import Path
import re, json, hashlib, importlib.metadata
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from xml.sax.saxutils import escape
r=Path(__file__).resolve().parents[1];p=r/'paper';f=p/'figures';f.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'messagebench-20261001','font.size':10})
fig,ax=plt.subplots(figsize=(7.1,2.65));ax.barh(['Core semantic branches','Targeted mutants killed','Differential classifications','Synthetic expected outcomes'],[99/102,1,1,1],color=['#a78234','#364c63','#364c63','#364c63'])
for i,label in enumerate(['99 / 102','40 / 40','200 / 200','100 / 100']):ax.text(.99,i,label,ha='right',va='center',color='white')
ax.set_xlim(0,1);ax.set_xlabel('Fraction within each explicitly defined measurement');ax.spines[['top','right']].set_visible(False);fig.tight_layout()
fig.savefig(f/'bounded-results.svg',metadata={'Date':None});fig.savefig(f/'bounded-results.png',dpi=180,metadata={'Software':'MessageBench evidence rendering'});plt.close(fig)
(f/'README.md').write_text('# Figure provenance\n\nThe chart uses only committed counts: 99/102 selected core branches, 40/40 defined mutants, 200/200 differential classifications and 100/100 curated expected outcomes. These denominators differ; no global quality score or independent-review claim is inferred. Vector source is included.\n')
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='BodyMB',fontName='Helvetica',fontSize=10.3,leading=14.1,spaceAfter=8));styles.add(ParagraphStyle(name='HMB',fontName='Helvetica-Bold',fontSize=14,leading=18,spaceBefore=12,spaceAfter=10));styles.add(ParagraphStyle(name='SubMB',fontName='Helvetica-Bold',fontSize=11.3,leading=15,spaceBefore=9,spaceAfter=7))
def inline(s):
 s=escape(s);s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s);s=re.sub(r'`([^`]+)`',r'<font face="Courier">\1</font>',s);return s

def footer(canvas,doc):
 canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor('#52606d'));canvas.drawString(45,30,'MessageBench · unreviewed engineering preprint · 0.2.0-rc.1');canvas.drawRightString(550,30,str(doc.page))

def render(md,dest,break_before=()):
 flow=[];paragraph=[];table=[];code=[];incode=False
 def flush():
  if paragraph:flow.append(Paragraph(inline(' '.join(paragraph)),styles['BodyMB']));paragraph.clear()
 def ft():
  if table:
   rows=[[Paragraph(inline(c.strip()),styles['BodyMB']) for c in line.strip('|').split('|')] for line in table if not re.fullmatch(r'[| :\-]+',line)]
   t=Table(rows,colWidths=[(505/len(rows[0]))]*len(rows[0]),repeatRows=1);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eef2f5')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.5,colors.HexColor('#8799aa')),('BOTTOMPADDING',(0,0),(-1,-1),5)]));flow.append(t);flow.append(Spacer(1,8));table.clear()
 for line in md.splitlines():
  if line.startswith('```'):
   flush();ft();incode=not incode
   if not incode:flow.append(Preformatted('\n'.join(code),ParagraphStyle('code',fontName='Courier',fontSize=7,leading=10)));code.clear()
   continue
  if incode:code.append(line);continue
  if line.startswith('|'):flush();table.append(line);continue
  ft()
  if line.startswith('#'):
   flush();title=line.lstrip('#').strip()
   if any(title.startswith(x) for x in break_before):flow.append(PageBreak())
   style=styles['Title'] if line.startswith('# ') else styles['HMB'] if line.startswith('## ') else styles['SubMB'];flow.append(Paragraph(inline(title),style))
  elif not line.strip():flush()
  else:paragraph.append(line)
 flush();ft();SimpleDocTemplate(str(dest),pagesize=(595,842),rightMargin=45,leftMargin=45,topMargin=44,bottomMargin=49,title='MessageBench information-preservation benchmark',author='Aksum Labs',invariant=1).build(flow,onFirstPage=footer,onLaterPages=footer)
render((p/'messagebench-benchmark.md').read_text(),p/'messagebench-benchmark.pdf',('2. Problem','4. Preservation','6. Corpus','8. Experimental','10. Performance','12. Prior','14. Reproducibility','16. Future'))
brief='''# MessageBench — technical brief
## Declared preservation at the adapter boundary

MessageBench is an offline toolkit for asking whether financial-message adapters preserved the information they explicitly promised to preserve. Engineers supply source and target files; MessageBench runs no adapter and connects to no financial system. It produces deterministic, privacy-conscious results with visible coverage limits.

### What the demonstration establishes

Two XML messages can both pass an exact XSD while a reference is truncated, a leading zero is removed or a repeated remittance element disappears. The synthetic proof pairs demonstrate these losses. Identity and explicitly permitted message-ID regeneration pass. Schema validators are performing their intended task; MessageBench adds a relationship check rather than replacing them.

### Technical scope

Candidate 0.2.0-rc.1 supports pacs.008.001.08 and pacs.002.001.10. Ten contracts contain 38 required assertion declarations over 27 extractable fields. A required UNSUPPORTED or INDETERMINATE check prevents overall PASS. Coverage distinguishes examined, excluded, unsupported and unexamined information. A PASS covers only listed assertions, never the whole document.

The architecture is bounded local files → secure XML/exact XSD → version-specific facts → typed declarative contract → comparison/coverage → JSON, text, escaped HTML or JUnit. Identifiers stay strings, amounts use Decimal with separate currency semantics, repeated elements retain multiplicity and normalization is explicit. Batch association requires declared unique keys.

### Measured synthetic evidence

100 paired cases; 140 tests; 99/102 selected core semantic branches covered; 40/40 defined targeted mutants killed; two XSD processors agree across 200 documents; 100,000 parser fuzz iterations and 10,000 contract mutations completed. These are automated measurements against curated expectations, not independently reviewed cases or production defect estimates.

## Evaluation, security and practical limits

### How an institution can evaluate it

Clone https://github.com/aksum-labs/messagebench and record the commit. Follow docs/reproduce.md to install the reviewed profile and run corpus verification, differential validation, mutations and security checks. For a local adapter, emit XML files separately and hand them to MessageBench with an explicit contract. Private inputs stay institution-local and must not be attached to issues or CI.

The prepared Linux x86_64 CPython 3.12 bundle can be installed offline. Canonical report bytes contain no timestamp. Hashes bind assets but do not anonymize financial data. Two matching clean unsigned Python builds in one environment establish same-environment equality, not independent reproduction.

### Security posture

Secure parsing disables DTD/entities/XInclude/network resolution; input size, depth, element count, text size and assertion count are bounded. Contracts contain no executable code or unrestricted XPath. Reports omit raw customer fields and escape HTML. There is no server, telemetry, plugin execution or adapter shell command. Limits are not an OS sandbox, and bounded fuzzing is not exhaustive security assurance.

### Performance context

The historical single-host run cycles six small pairs over 1,000 in-process comparisons, including per-pair schema compilation. It measured 80.624 pairs/s, p50 11.741 ms, p95 15.584 ms and peak RSS 40,360 KiB. This is not an SLA, batch-scale benchmark or cross-product performance comparison.

### Rights, review and recognition

Original code and synthetic corpus use Apache-2.0. The two standard XSDs retain separate terms. camt.053.001.08 is excluded because complete joint-contributor redistribution permission was not established. No independent human review, adoption, official endorsement or certification is claimed. Foundation applications and badges must be checked against actual official results in external/recognition-matrix.json.

This engineering artifact does not implement payment operations, sovereign rails, Ethiopian scheme rules or regulatory authority. Public claims are limited to observed tests, exact scope and authenticated evidence. The next substantive step is independent review of semantics, expectations and rights, followed by actual maintainership and constructive upstream use.
'''
(p/'technical-brief.md').write_text(brief);render(brief,p/'technical-brief.pdf',('Evaluation, security',))
(p/'rendering.json').write_text(json.dumps({'source':'paper/messagebench-benchmark.md','toolchain':{x:importlib.metadata.version(x) for x in ['reportlab','matplotlib']},'renderer':'paper/render_materials.py','date':'2026-10-01','independent_review':False},indent=2)+'\n')
(p/'render_materials.py').write_text(Path(__file__).read_text().replace("r=Path(__file__).resolve().parents[1];p=r/'paper';", "r=Path(__file__).resolve().parents[1];p=r/'paper';"))
import fitz
for name in ['messagebench-benchmark.pdf','technical-brief.pdf']:print(name,len(fitz.open(p/name)))
