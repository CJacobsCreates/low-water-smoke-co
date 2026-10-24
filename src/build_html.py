import sys, html
sys.path.insert(0,'src')
from products import P, GIFT
heat={"original-bbq-sauce":1,"mesquite-molasses-bbq-sauce":1,"hot-peach-bbq-sauce":4}
def card(p):
    v=p["variants"][0]; img=p["images"][0]
    alt=p["images"][1][0] if len(p["images"])>1 else None
    price=f'${float(v[1]):.0f}' if float(v[1]).is_integer() else f'${v[1]}'
    low=min(float(x[1]) for x in p["variants"]); multi=len({x[1] for x in p["variants"]})>1
    ptxt=(f'From ${low:.0f}' if multi else f'${low:.0f}')
    cmp=f'<s>${float(v[2]):.0f}</s>' if v[2] else ''
    badge='<span class="badge">Sale</span>' if v[2] else ('<span class="badge hot">Hot</span>' if heat.get(p["handle"],0)>=4 else '')
    meta=""
    if p["handle"] in heat:
        h=heat[p["handle"]]; meta=f'<span class="heat" aria-label="Heat {h} of 5">{"".join("<i class=on></i>" if i<h else "<i></i>" for i in range(5))}</span>'
    elif p["opt"]=="Size" and p["collection"]=="Merch": meta='<span class="mono">S–XXL</span>'
    elif p["opt"]: meta='<span class="mono">6 oz · 1 lb</span>'
    hov=f'<img class="alt" src="images/w900/{alt}" alt="" loading="lazy">' if alt else ''
    return f'''<a class="card" href="#" data-col="{p["collection"]}"><div class="ph">{badge}<img src="images/w900/{img[0]}" alt="{html.escape(img[1])}" loading="lazy">{hov}</div>
<div class="cb"><span class="ty">{html.escape(p["type"])}</span><h3>{html.escape(p["title"])}</h3><p>{html.escape(p["short"])}</p>
<div class="pr"><span>{ptxt} {cmp}</span>{meta}</div></div></a>'''
cards="\n".join(card(p) for p in P)
gc=f'''<a class="card" href="#" data-col="Gift Cards"><div class="ph"><img src="images/w900/gift-card-1.jpg" alt="Low Water gift card" loading="lazy"></div>
<div class="cb"><span class="ty">Gift Card</span><h3>{GIFT["title"]}</h3><p>Delivered by email instantly. Never expires.</p><div class="pr"><span>From $25</span><span class="mono">Email delivery</span></div></div></a>'''
tpl=open('src/index.tpl.html').read()
open('public/index.html','w').write(tpl.replace('{{CARDS}}',cards+"\n"+gc))
print("ok")
