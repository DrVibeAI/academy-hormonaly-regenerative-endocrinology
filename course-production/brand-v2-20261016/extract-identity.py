from pathlib import Path
import pymupdf as fitz
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
import xml.etree.ElementTree as ET
import sys
ROOT=Path(__file__).resolve().parents[2]
base=ROOT/'public/assets/brand/v2'
pdf=fitz.open(sys.argv[1])
p=pdf[11]
# Preserve the supplied vector logo, including its original outlined lettering.
root=ET.fromstring(p.get_svg_image(text_as_path=True))
root.set('viewBox','110 294 466 70');root.set('width','466');root.set('height','70')
# Remove page ground/panel fills so the original logo is transparent.
for parent in root.iter():
 for child in list(parent):
  if child.tag.endswith('path') and (child.get('fill') in ('#f7f7f5','#ffffff','#f0f4f9') or (child.get('fill')=='#3c4043' and child.get('fill-opacity'))):
   parent.remove(child)
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
svg=ET.tostring(root,encoding='unicode')
(base/'hormonaly-wordmark.svg').write_text(svg)
svgdoc=fitz.open(stream=svg.encode(),filetype='svg')
logo=fitz.open('pdf',svgdoc.convert_to_pdf())
logo[0].get_pixmap(matrix=fitz.Matrix(2,2),alpha=True).save(base/'hormonaly-wordmark.png')
# Brand-book v2 re-colours the existing orbit; geometry stays intact.
mark=(ROOT/'public/assets/brand/hormonaly-mark-flat.svg').read_text().replace('#0071E3','#1F1F1F')
(base/'hormonaly-mark-flat.svg').write_text(mark)
icon=(ROOT/'public/assets/brand/hormonaly-app-icon.svg').read_text().replace('#0071E3','#1F1F1F').replace('rx="14"','rx="16"')
(base/'hormonaly-app-icon.svg').write_text(icon)
for name in ['GoogleSansFlex','NotoSansArabic']:
 f=TTFont(base/'fonts'/f'{name}.ttf');f.flavor='woff2';f.save(base/'fonts'/f'{name}.woff2')
 for weight in [400,500,600]:
  f=TTFont(base/'fonts'/f'{name}.ttf')
  axes={a.axisTag:(weight if a.axisTag=='wght' else a.defaultValue) for a in f['fvar'].axes}
  f=instantiateVariableFont(f,axes,inplace=True)
  f.save(base/'fonts'/f'{name}-{weight}.ttf')
(base/'fonts.css').write_text('''@font-face { font-family: 'Google Sans Flex'; src: url('./fonts/GoogleSansFlex.woff2') format('woff2'); font-style: normal; font-weight: 100 1000; font-display: swap; }\n@font-face { font-family: 'Noto Sans Arabic'; src: url('./fonts/NotoSansArabic.woff2') format('woff2'); font-style: normal; font-weight: 100 900; font-display: swap; }\n''')
