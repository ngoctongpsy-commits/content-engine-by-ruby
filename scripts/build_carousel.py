#!/usr/bin/env python3
"""Reusable CAROUSEL builder (locked templates A/B/C, 1080x1350, 7 slides).

Turns a JSON content spec into 7 on-brand PNG slides + copies the caption.
Templates (CAROUSEL-TEMPLATES.md):
  A Spotlight   - airy/premium: centered Inter-Black headline + chip pills + soft circle.
  B Bold Magazine - high energy: top clay->deep block kicker + huge left headline on cream.
  C Deep-tech Console - futuristic: HUD corner brackets + dark terminal card + glowing node row.
Slide roles (7): hook, problem, inside, main, main, conclusion, cta.

Usage:
  python build_carousel.py spec.json [out_dir]
Spec:
  {"template":"A|B|C","slug":"my-topic","date":"YYYY-MM-DD","caption":"...",
   "slides":[{"role":"hook","kicker":"...","title":"...","sub":"...","lines":["..."],"term":"$ cmd"} , ... x7]}
Run with no args -> renders a built-in demo spec to ./_carousel-demo so you can eyeball all 3 templates.
"""
import os, sys, json, math
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
LOGO = os.environ.get("CAROUSEL_LOGO", "")  # optional brand logo path (png); empty = no logo
W, H = 1080, 1350
CREAM = (246, 244, 239); WHITE = (255, 255, 255); INK = (20, 22, 28)
CLAY = (217, 119, 87); CLAY_D = (183, 90, 62); DEEP = (32, 30, 46); MUTE = (122, 120, 130)
FA_PATH = "/usr/share/fonts-font-awesome/fonts/FontAwesome.otf"
WORDMARK = ""  # optional brand wordmark drawn by the header; set via spec brand.wordmark

def F(size, weight=700):
    f = ImageFont.truetype(os.path.join(FONTS, "InterG.ttf"), size)
    try: f.set_variation_by_axes([weight])
    except Exception: pass
    return f
def MONO(size): return ImageFont.truetype(os.path.join(FONTS, "JetBrainsMono-Bold.ttf"), size)

def tw(d, t, f): b = d.textbbox((0,0), t, font=f); return b[2]-b[0], b[3]-b[1]
def wrap(d, t, f, maxw):
    out=[]; 
    for para in t.split("\n"):
        words=para.split(); line=""
        for w in words:
            test=(line+" "+w).strip()
            if tw(d,test,f)[0]<=maxw: line=test
            else:
                if line: out.append(line)
                line=w
        out.append(line)
    return out
def rrect(d, xy, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)
def paste_logo(img, x, y, h=34):
    if not os.path.exists(LOGO): return
    lg=Image.open(LOGO).convert("RGBA"); w=int(lg.width*h/lg.height)
    lg=lg.resize((w,h)); img.paste(lg,(x,y),lg)

def header(img, d, idx, total, dark=False):
    col = WHITE if dark else INK
    paste_logo(img, 64, 60, 30)
    if WORDMARK:
        d.text((104, 62), WORDMARK, font=F(22,700), fill=col)
    tag=f"{idx:02d} / {total:02d}"
    w,_=tw(d,tag,MONO(22)); d.text((W-64-w,64), tag, font=MONO(22), fill=CLAY)

def footer(img, d, role, dark=False):
    col = MUTE if not dark else (150,150,165)
    if role!="cta":
        d.text((64, H-72), "swipe →", font=F(24,700), fill=CLAY)

# ---------- shared blocks ----------
def kicker(d, x, y, text, on_dark=False):
    f=MONO(24); w,h=tw(d,text.upper(),f)
    rrect(d,(x,y,x+w+34,y+h+22), 8, fill=CLAY)
    d.text((x+17,y+9), text.upper(), font=f, fill=WHITE)
    return y+h+22

def chips(d, x, y, items, maxw):
    f=F(26,600); cx=x; cy=y; gap=14; lh=58
    for it in items:
        w,_=tw(d,it,f); bw=w+44
        if cx+bw> x+maxw: cx=x; cy+=lh
        rrect(d,(cx,cy,cx+bw,cy+46), 23, fill=WHITE, outline=(225,222,214), width=2)
        d.text((cx+22,cy+9), it, font=f, fill=INK)
        cx+=bw+gap
    return cy+46

def bullets(d, x, y, lines, maxw, col=INK):
    f=F(30,500); cy=y
    for ln in lines:
        d.ellipse((x,cy+12,x+12,cy+24), fill=CLAY)
        for i,seg in enumerate(wrap(d,ln,f,maxw-34)):
            d.text((x+30,cy), seg, font=f, fill=col); cy+=42
        cy+=14
    return cy

# ---------- TEMPLATE A: Spotlight ----------
def render_A(slide, idx, total):
    img=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(img)
    # soft clay circle motif
    glow=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
    gd.ellipse((W-360,120,W+160,640),fill=(217,119,87,28)); img.paste(glow,(0,0),glow)
    header(img,d,idx,total)
    y=300
    if slide.get("kicker"): y=kicker(d,64,y,slide["kicker"])+34
    title=slide.get("title",""); tf=F(82 if slide["role"]=="hook" else 66, 900)
    for seg in wrap(d,title,tf,W-128):
        d.text((64,y), seg, font=tf, fill=INK); y+=tf.size+8
    y+=18
    if slide.get("sub"):
        sf=F(34,500)
        for seg in wrap(d,slide["sub"],sf,W-128): d.text((64,y),seg,font=sf,fill=MUTE); y+=44
    if slide.get("lines"): y=bullets(d,72,y+10,slide["lines"],W-160)
    if slide.get("chips"): chips(d,64,y+10,slide["chips"],W-128)
    d.line((64,H-150,W-64,H-150),fill=(225,222,214),width=2)
    if slide["role"]=="cta": _cta(img,d,slide)
    footer(img,d,slide["role"]); return img

# ---------- TEMPLATE B: Bold Magazine ----------
def render_B(slide, idx, total):
    img=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(img)
    blk=520
    grad=Image.new("RGB",(W,blk),CLAY)
    for i in range(blk):
        t=i/blk; r=int(217+(32-217)*t); g=int(119+(30-119)*t); b=int(87+(46-87)*t)
        ImageDraw.Draw(grad).line((0,i,W,i),fill=(r,g,b))
    img.paste(grad,(0,0))
    header(img,d,idx,total,dark=True)
    y=180
    if slide.get("kicker"):
        f=MONO(26); d.text((64,y),slide["kicker"].upper(),font=f,fill=(255,225,210)); y+=54
    tf=F(86 if slide["role"]=="hook" else 70, 900)
    for seg in wrap(d,slide.get("title",""),tf,W-128):
        d.text((64,y),seg,font=tf,fill=WHITE); y+=tf.size+6
    y=blk+70
    if slide.get("sub"):
        sf=F(38,600)
        for seg in wrap(d,slide["sub"],sf,W-128): d.text((64,y),seg,font=sf,fill=INK); y+=50
    if slide.get("lines"): y=bullets(d,72,y+10,slide["lines"],W-160)
    if slide.get("chips"): chips(d,64,y+10,slide["chips"],W-128)
    if slide["role"]=="cta": _cta(img,d,slide)
    footer(img,d,slide["role"]); return img

# ---------- TEMPLATE C: Deep-tech Console ----------
def hud(d):
    c=CLAY; L=46; m=54
    for (x,y,dx,dy) in [(m,m,1,1),(W-m,m,-1,1),(m,H-m,1,-1),(W-m,H-m,-1,-1)]:
        d.line((x,y,x+dx*L,y),fill=c,width=4); d.line((x,y,x,y+dy*L),fill=c,width=4)
def render_C(slide, idx, total):
    img=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(img)
    # ethereal bottom bokeh (no grid)
    bok=Image.new("RGBA",(W,H),(0,0,0,0)); bd=ImageDraw.Draw(bok)
    import random; random.seed(idx*7+3)
    for _ in range(22):
        rx=random.randint(0,W); ry=random.randint(H-360,H); rr=random.randint(20,90)
        bd.ellipse((rx-rr,ry-rr,rx+rr,ry+rr),fill=(217,119,87,16))
    img.paste(bok,(0,0),bok); hud(d); header(img,d,idx,total)
    y=300
    if slide.get("kicker"): y=kicker(d,64,y,slide["kicker"])+30
    tf=F(78 if slide["role"]=="hook" else 64, 900)
    for seg in wrap(d,slide.get("title",""),tf,W-128):
        d.text((64,y),seg,font=tf,fill=INK); y+=tf.size+8
    y+=16
    if slide.get("sub"):
        sf=F(32,500)
        for seg in wrap(d,slide["sub"],sf,W-128): d.text((64,y),seg,font=sf,fill=MUTE); y+=42
    if slide.get("term"):
        ty=y+20; th=150
        rrect(d,(64,ty,W-64,ty+th),16,fill=DEEP)
        for i,c in enumerate([(255,95,86),(255,189,46),(39,201,63)]):
            d.ellipse((92+i*28,ty+24,108+i*28,ty+40),fill=c)
        d.text((92,ty+66),slide["term"],font=MONO(28),fill=(230,228,238))
        cx=92+tw(d,slide["term"],MONO(28))[0]+8; d.rectangle((cx,ty+64,cx+14,ty+96),fill=CLAY)
        y=ty+th+24
    if slide.get("lines"): y=bullets(d,72,y+6,slide["lines"],W-160)
    if slide.get("nodes"):
        nx=80; ny=y+24
        for i,n in enumerate(slide["nodes"]):
            if i: d.line((nx-26,ny+22,nx,ny+22),fill=CLAY,width=4)
            d.ellipse((nx,ny,nx+44,ny+44),fill=CLAY)
            d.text((nx+58,ny+6),n,font=F(28,700),fill=INK); 
            nx+=58+tw(d,n,F(28,700))[0]+40
    if slide["role"]=="cta": _cta(img,d,slide)
    footer(img,d,slide["role"]); return img

def _cta(img,d,slide):
    y=H-250
    rrect(d,(64,y,W-64,y+150),18,fill=CLAY)
    d.text((96,y+30),slide.get("title","Want this for your team?"),font=F(44,800),fill=WHITE)
    d.text((96,y+92),slide.get("sub","yourbrand.com"),font=MONO(34),fill=(255,232,222))

RENDER={"A":render_A,"B":render_B,"C":render_C}

DEMO={"template":"C","slug":"demo","date":"0000-00-00","caption":"demo caption",
 "slides":[
  {"role":"hook","kicker":"the mix-up","title":"Skill? Connector? MCP?","sub":"Three words people blur together."},
  {"role":"problem","kicker":"why it matters","title":"You can't wire what you can't name","lines":["Pick the wrong piece and your build stalls.","Each one solves a different job."]},
  {"role":"inside","kicker":"the standard","title":"MCP is the language","sub":"One open standard every app speaks to Claude.","term":"channel = mcp"},
  {"role":"main","kicker":"the hands","title":"A connector = access","lines":["An app plugged in over MCP.","Read files, send a message, take an action."],"nodes":["Read","Send","Act"]},
  {"role":"main","kicker":"the know-how","title":"A skill = the playbook","lines":["A SKILL.md that teaches the workflow.","Steps + rules Claude follows every time."]},
  {"role":"conclusion","kicker":"keep it straight","title":"Language. Hands. Playbook.","lines":["MCP = the language.","Connector = the hands.","Skill = the playbook."]},
  {"role":"cta","title":"Want this wired for your tools?","sub":"yourbrand.com"}]}


def apply_brand(spec):
    """Override module colors + logo from spec['brand'] (brand-neutral; defaults = clay/cream)."""
    global CREAM, WHITE, INK, CLAY, CLAY_D, DEEP, MUTE, LOGO, WORDMARK
    b = (spec or {}).get("brand") or {}
    def hexrgb(h, d):
        if not h: return d
        h = h.lstrip("#")
        try: return tuple(int(h[i:i+2],16) for i in (0,2,4))
        except Exception: return d
    CREAM = hexrgb(b.get("bg"), CREAM); INK = hexrgb(b.get("ink"), INK)
    CLAY = hexrgb(b.get("accent"), CLAY); CLAY_D = hexrgb(b.get("accent_dark"), CLAY_D)
    DEEP = hexrgb(b.get("deep"), DEEP)
    if b.get("logo"):
        globals()["LOGO"] = b["logo"]
    WORDMARK = b.get("wordmark", WORDMARK)

def build(spec, out_dir):
    apply_brand(spec)
    os.makedirs(out_dir, exist_ok=True)
    tpl=spec.get("template","A").upper(); fn=RENDER.get(tpl,render_A)
    slides=spec["slides"]; total=len(slides)
    for i,s in enumerate(slides,1):
        img=fn(s,i,total); img.save(os.path.join(out_dir,f"slide_{i}.png"))
    cap=spec.get("caption","")
    open(os.path.join(out_dir,"caption.txt"),"w",encoding="utf-8").write(cap)
    print(f"built {total} slides (template {tpl}) -> {out_dir}")

if __name__=="__main__":
    if len(sys.argv)<2:
        build(DEMO, os.path.join(HERE,"..","_carousel-demo")); 
    else:
        spec=json.load(open(sys.argv[1],encoding="utf-8"))
        out=sys.argv[2] if len(sys.argv)>2 else os.path.join(HERE,"..","output","carousel",
            f"{spec.get('date','0000')}-{spec.get('slug','carousel')}")
        build(spec,out)
