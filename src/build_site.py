import sys, os, json, html, shutil
sys.path.insert(0, 'src')
from products import P, GIFT, COLLECTIONS
E = html.escape
OUT = 'public'
for d in ['collections', 'products', 'assets']:
    shutil.rmtree(f'{OUT}/{d}', ignore_errors=True)
os.makedirs(f'{OUT}/assets', exist_ok=True)
open(f'{OUT}/assets/site.css', 'w').write(open('src/base.css').read() + "\n" + open('src/extra.css').read())
BYH = {p['handle']: p for p in P}
COLH = {c[0]: c for c in COLLECTIONS}

def money(x):
    x = float(x); return f"${x:.0f}" if x.is_integer() else f"${x:.2f}"
def heat(h, big=False):
    if not h: return ''
    return f'<span class="heat" aria-label="Heat {h} of 5" title="Heat {h} of 5">' + ''.join('<i class="on"></i>' if i < h else '<i></i>' for i in range(5)) + '</span>'
def size_hint(p):
    if p['collection'] == 'Merch': return 'S–XXL' if p['type'] == 'T-Shirt' else '2 colors'
    if p['options'] and p['collection'] in ('Sauces', 'Rubs'): return ' · '.join(p['options'][0][1])
    return ''

LOGO = '''<svg viewBox="0 0 48 48" fill="none" aria-hidden="true"><circle cx="24" cy="24" r="22.5" stroke="#9E3B26" stroke-width="2.4"/><path d="M8 29c5-2 9 1.5 16 0s11-2 16 0" stroke="#1F1A16" stroke-width="2.2" stroke-linecap="round"/><path d="M10 34c5-1.6 9 1.2 14 0s10-1.6 14 0" stroke="#1F1A16" stroke-width="2" stroke-linecap="round" opacity=".6"/><rect x="14" y="23.5" width="20" height="3.2" rx="1" fill="#9E3B26"/><path d="M17 23V15m0 0c-3-.6-3.6-5 0-6 3.6 1 3 5.4 0 6M32 23V13.5m0 0c-3.4-.7-4-5.6 0-6.8 4 1.2 3.4 6.1 0 6.8" stroke="#1F1A16" stroke-width="1.8" stroke-linecap="round"/></svg>'''
NAV = [("Shop all", "/collections/all/"), ("Sauces", "/collections/sauces/"), ("Rubs", "/collections/rubs/"), ("Gift sets", "/collections/gift-sets/"), ("Accessories", "/collections/accessories/"), ("Merch", "/collections/merch/"), ("Our story", "/#about")]

def page(title, desc, body, og="/images/w900/hero.jpg", extra_js=""):
    nav = ''.join(f'<a href="{u}">{n}</a>' for n, u in NAV)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><meta name="robots" content="noindex">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="https://jc-shopify-demo.pages.dev{og}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@500;600;700&family=Libre+Franklin:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css"></head><body>
<div class="ann"><b>Free US shipping on orders $60+</b> &nbsp;·&nbsp; Holiday gift boxes ship through Dec 18</div>
<header><div class="wrap hd">
 <a class="logo" href="/" aria-label="Low Water Smoke Co. home">{LOGO}<span><b>LOW WATER</b><small>SMOKE CO.</small></span></a>
 <nav class="main">{nav}</nav>
 <div class="icons">
  <svg class="s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
  <span class="cart" aria-label="Cart"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 8h14l-1.2 12H6.2z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg><i id="cc">0</i></span>
  <button class="burger" aria-label="Menu" onclick="document.querySelector('.mnav').classList.toggle('open')"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
 </div></div><nav class="mnav">{nav}</nav></header>
{body}
<footer><div class="wrap">
 <div class="fg">
  <div><a class="logo" href="/"><svg viewBox="0 0 48 48" fill="none" aria-hidden="true"><circle cx="24" cy="24" r="22.5" stroke="#D9783A" stroke-width="2.4"/><path d="M8 29c5-2 9 1.5 16 0s11-2 16 0" stroke="#F7F1E6" stroke-width="2.2" stroke-linecap="round"/><rect x="14" y="23.5" width="20" height="3.2" rx="1" fill="#D9783A"/></svg><span><b>LOW WATER</b><small>SMOKE CO.</small></span></a>
   <p style="max-width:32ch;margin-top:18px">Small-batch BBQ sauce and rubs from the Texas Hill Country.</p></div>
  <div><h4>Shop</h4><ul><li><a href="/collections/sauces/">Sauces</a></li><li><a href="/collections/rubs/">Rubs</a></li><li><a href="/collections/gift-sets/">Gift sets</a></li><li><a href="/collections/accessories/">Accessories</a></li><li><a href="/collections/merch/">Merch</a></li><li><a href="/products/gift-card/">Gift card</a></li></ul></div>
  <div><h4>Help</h4><ul><li><a href="#">Shipping</a></li><li><a href="#">FAQ</a></li><li><a href="#">Wholesale</a></li><li><a href="#">Contact</a></li></ul></div>
  <div><h4>About</h4><ul><li><a href="/#about">Our story</a></li><li><a href="/#notes">Pit notes</a></li></ul></div>
 </div>
 <div class="legal"><span class="concept">Concept store by <a href="https://thejacobsconsultancy.com" style="text-decoration:underline">Jacobs Consultancy</a>. Low Water Smoke Co. is a fictional brand, and nothing here is for sale.</span>
 <span class="pay"><span>VISA</span><span>MC</span><span>AMEX</span><span>SHOP PAY</span><span>APPLE PAY</span></span></div>
</div></footer>
<div class="toast" id="toast" role="status"></div>
<script>
var cc=+(sessionStorage.getItem('lwcc')||0);var ce=document.getElementById('cc');ce.textContent=cc;ce.style.display=cc?'':'none';
function toast(m){{var t=document.getElementById('toast');t.textContent=m;t.classList.add('show');clearTimeout(window._tt);window._tt=setTimeout(function(){{t.classList.remove('show')}},3200)}}
function addCart(n,label){{cc+=n;sessionStorage.setItem('lwcc',cc);ce.textContent=cc;ce.style.display='';toast('Added '+label+'. This is a concept store, so checkout is switched off.')}}
{extra_js}
</script>
</body></html>'''

def card(p):
    vs = p['variants']; v0 = vs[0]; img = p['images'][0]
    low = min(float(v['price']) for v in vs); multi = len({v['price'] for v in vs}) > 1
    ptxt = ('From ' if multi else '') + money(low)
    cmp = f'<s>{money(v0["cmp"])}</s>' if v0['cmp'] else ''
    if v0['cmp']: badge = f'<span class="badge">Save {money(float(v0["cmp"]) - float(v0["price"]))}</span>'
    elif (p.get('heat') or 0) >= 4: badge = '<span class="badge hot">Hot</span>'
    elif 'best-seller' in p['tags']: badge = '<span class="badge">Best seller</span>'
    else: badge = ''
    alt = f'<img class="alt" src="/images/w900/{p["images"][1][0]}" alt="" loading="lazy">' if len(p['images']) > 1 else ''
    meta = heat(p.get('heat')) if p.get('heat') else (f'<span class="mono">{E(size_hint(p))}</span>' if size_hint(p) else '')
    return f'''<a class="card" href="/products/{p["handle"]}/" data-price="{low}" data-title="{E(p["title"])}"><div class="ph">{badge}<img src="/images/w900/{img[0]}" alt="{E(img[1])}" loading="lazy">{alt}</div>
<div class="cb"><span class="ty">{E(p["type"])}</span><h3>{E(p["title"])}</h3><p>{E(p["short"])}</p>
<div class="pr"><span>{ptxt} {cmp}</span>{meta}</div></div></a>'''

def gift_card_tile():
    return f'''<a class="card" href="/products/gift-card/" data-price="25" data-title="{GIFT["title"]}"><div class="ph"><img src="/images/w900/gift-card-1.jpg" alt="{E(GIFT["image"][1])}" loading="lazy"></div>
<div class="cb"><span class="ty">Gift Card</span><h3>{GIFT["title"]}</h3><p>{GIFT["short"]}</p><div class="pr"><span>From $25</span><span class="mono">Email</span></div></div></a>'''

# ---------- HOME ----------
tiles = ''.join(f'<a class="tile" href="/collections/{h}/"><img src="/images/w900/{img}" alt="" loading="lazy"><span>{E(t if t != "Bundles & Gift Sets" else "Gift sets")}<small>{n} products</small></span></a>'
    for (t, h, _, _), img, n in zip(COLLECTIONS, ["sauce-carolina-gold-1.jpg", "rub-brisket-1.jpg", "bundle-pitmaster-box-1.jpg", "acc-thermometer-1.jpg", "tee-natural-1.jpg"],
                                     [sum(1 for p in P if p['collection'] == c[0]) for c in COLLECTIONS]))
feat = ''.join(card(BYH[h]) for h in ["original-post-oak-bbq-sauce", "carolina-gold-mustard-bbq-sauce", "hot-peach-habanero-bbq-sauce", "hill-country-hot-honey",
                                       "brisket-rub", "yard-bird-lemon-pepper-rub", "three-sauce-sampler", "low-water-crossing-tee"])
pit = BYH['the-pitmaster-box']
inbox = ''.join(f'<li><span>{E(n)}</span><span>{E(s)}</span></li>' for n, s in pit['includes'])
home = f'''
<section class="hero" style="padding:0">
 <img src="/images/w900/hero.jpg" alt="Low Water sauces on a plank table beside a smoker and a Hill Country creek crossing at golden hour" fetchpriority="high">
 <div class="wrap">
  <div class="eyebrow">Small-batch · Llano County, Texas</div>
  <h1>Sauce from the bottom of the road.</h1>
  <p>Six sauces and four rubs, cooked 40 gallons at a time in a rented kitchen outside Llano and bottled by hand.</p>
  <div class="btns"><a class="btn p" href="/collections/all/">Shop everything</a><a class="btn g" href="/collections/gift-sets/">Gift sets</a></div>
 </div>
</section>
<div class="strip"><ul>
 <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3c2 4 6 5 6 10a6 6 0 0 1-12 0c0-3 2-4 2-7 2 1 3 2 4 4 0-3 0-5 0-7z"/></svg>Real wood smoke, never liquid</li>
 <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 3h10M9 3v4l-3 4v10h12V11l-3-4V3"/></svg>Filled &amp; labeled by hand</li>
 <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/></svg>Ships Mon–Thu from Texas</li>
 <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m5 12 4 4 10-10"/></svg>No high-fructose corn syrup</li>
</ul></div>
<section><div class="wrap">
 <div class="sh"><div><div class="eyebrow">Shop by kind</div><h2>The pantry</h2></div><a class="btn d" href="/collections/all/">Shop all {len(P)} products</a></div>
 <div class="tiles">{tiles}</div>
</div></section>
<section style="padding-top:0"><div class="wrap">
 <div class="sh"><div><div class="eyebrow">Where most people start</div><h2>The ones we reorder ourselves</h2></div></div>
 <div class="grid">{feat}</div>
</div></section>
<section class="fb" id="bundle"><div class="wrap fbg">
 <a class="ph" href="/products/the-pitmaster-box/"><span class="badge">Save $8</span><img src="/images/w900/bundle-pitmaster-box-1.jpg" alt="{E(pit["images"][0][1])}" loading="lazy"></a>
 <div>
  <div class="eyebrow">Featured gift set</div>
  <h2>The Pitmaster Box</h2>
  <p style="max-width:46ch;margin:16px 0 0">{E(pit["intro"][0])}</p>
  <div class="price"><b>$62</b><s>$70</s><span class="save">You save $8</span></div>
  <ul class="inbox">{inbox}</ul>
  <a class="btn p" href="/products/the-pitmaster-box/">View the box</a>
  <p class="note">Ships gift-ready in a lidded kraft box. Add a note at checkout and we'll hand-write the card.</p>
 </div>
</div></section>
<section id="notes"><div class="wrap">
 <div class="sh"><div><div class="eyebrow">Pit notes</div><h2>Which bottle, which cook?</h2></div></div>
 <div class="uses">
  <div class="use"><span class="n">01 · BRISKET</span><h3>Brisket Rub, then Original on the side</h3><p>A tablespoon of rub per pound, 250°F over post oak, wrap in butcher paper around 165°F, pull when it probes like butter (usually 200–205°F). Original goes on the table, not the meat.</p></div>
  <div class="use"><span class="n">02 · PULLED PORK</span><h3>Sweet Pecan, finished with Carolina Gold</h3><p>Rub a bone-in shoulder the night before, cook at 250°F to about 203°F, rest an hour, pull, then toss with warm Carolina Gold.</p></div>
  <div class="use"><span class="n">03 · CHICKEN</span><h3>Yard Bird rub, Alabama White to dunk</h3><p>Spatchcock, rub, smoke at 325°F until the thigh reads 175°F. Dunk the pieces straight into a bowl of Alabama White while they're hot.</p></div>
 </div>
</div></section>
<section class="ab" id="about"><div class="wrap abg">
 <div>
  <div class="eyebrow">Our story</div>
  <h2>It started when the creek came up.</h2>
  <p style="margin-top:20px">In the spring of 2019 rain flooded the crossing at the bottom of our road outside Llano and kept us home with a smoker, a brisket and nothing to do but wait. That batch of sauce got passed around the whole road. By fall we were filling bottles in a rented church kitchen on Tuesday nights.</p>
  <p>It's still just the two of us, Wade and Celia, plus a neighbor on labeling nights. When the creek's up we're slow to ship. When it's down, we're cooking.</p>
  <div class="stats"><div><b>40 gal</b><span>per batch, max</span></div><div><b>16-mesh</b><span>black pepper</span></div><div><b>0</b><span>drops of liquid smoke</span></div></div>
 </div>
 <div class="ph"><img src="/images/w900/about.jpg" alt="Hands stirring a stockpot of BBQ sauce in a small kitchen" loading="lazy"></div>
</div></section>
<div class="nl"><div class="wrap nlg">
 <div><h2>Get the pit notes.</h2><p>One email a month: a recipe and what's coming off the stove next. 10% off your first order.</p></div>
 <form onsubmit="toast('Concept store: sign-up is switched off.');return false"><input type="email" placeholder="Email address" aria-label="Email address"><button>Sign up</button></form>
</div></div>'''
open(f'{OUT}/index.html', 'w').write(page("Low Water Smoke Co. | Small-batch Texas BBQ sauce, rubs & gifts", "Small-batch BBQ sauces, dry rubs, gift boxes and pit gear from a fictional Texas Hill Country brand. A Shopify store concept by Jacobs Consultancy.", home))

# ---------- COLLECTIONS ----------
SORT_JS = """var g=document.querySelector('.grid'),sel=document.getElementById('sort');if(sel){sel.onchange=function(){var a=[].slice.call(g.children);var k=sel.value;a.sort(function(x,y){if(k=='lo')return x.dataset.price-y.dataset.price;if(k=='hi')return y.dataset.price-x.dataset.price;if(k=='az')return x.dataset.title.localeCompare(y.dataset.title);return x.dataset.i-y.dataset.i});a.forEach(function(c){g.appendChild(c)})}}"""
cols = [("All products", "all", None, "Everything we make: sauces, rubs, gift sets, a few tools and some shirts.")] + list(COLLECTIONS)
for t, h, tag, blurb in cols:
    items = P if h == 'all' else [p for p in P if p['collection'] == t]
    cards = [card(p) for p in items] + ([gift_card_tile()] if h in ('all', 'gift-sets') else [])
    cards = [c.replace('<a class="card"', f'<a class="card" data-i="{i}"', 1) for i, c in enumerate(cards)]
    chips = ''.join(f'<a href="/collections/{hh}/" class="{"on" if hh == h else ""}">{E("Gift sets" if tt == "Bundles & Gift Sets" else ("All" if hh == "all" else tt))}</a>' for tt, hh, _, _ in cols)
    title = "Gift sets" if t == "Bundles & Gift Sets" else t
    body = f'''<div class="wrap"><div class="crumb"><a href="/">Home</a> / {E(title)}</div>
<div class="ch"><h1>{E(title)}</h1><p>{E(blurb)}</p></div>
<div class="toolbar"><div class="chips">{chips}</div><div style="display:flex;gap:14px;align-items:center"><span class="count">{len(cards)} products</span>
<label><span class="sr" style="position:absolute;left:-9999px">Sort</span><select id="sort"><option value="f">Featured</option><option value="lo">Price, low to high</option><option value="hi">Price, high to low</option><option value="az">Alphabetically, A–Z</option></select></label></div></div></div>
<section class="cp"><div class="wrap"><div class="grid">{"".join(cards)}</div></div></section>'''
    os.makedirs(f'{OUT}/collections/{h}', exist_ok=True)
    open(f'{OUT}/collections/{h}/index.html', 'w').write(page(f"{title} | Low Water Smoke Co.", blurb, body, extra_js=SORT_JS))

# ---------- PRODUCTS ----------
PDP_JS = """var D=JSON.parse(document.getElementById('pd').textContent),sel=D.variants[0].opts.slice();
function fm(x){x=+x;return '$'+(x%1?x.toFixed(2):x.toFixed(0))}
function cur(){return D.variants.find(function(v){return v.opts.every(function(o,i){return o===sel[i]})})}
function show(src){document.getElementById('mi').src='/images/w900/'+src;document.querySelectorAll('.thumbs button').forEach(function(b){b.classList.toggle('on',b.dataset.src===src)})}
function upd(){var v=cur();if(!v)return;document.getElementById('pb').textContent=fm(v.price);var s=document.getElementById('ps');s.textContent=v.cmp?fm(v.cmp):'';var sv=document.getElementById('pv');sv.style.display=v.cmp?'':'none';if(v.cmp)sv.textContent='Save '+fm(v.cmp-v.price);document.getElementById('sku').textContent='SKU '+v.sku;document.getElementById('atc').textContent='Add to cart · '+fm(v.price);if(v.img)show(v.img);document.querySelectorAll('.opt').forEach(function(o,i){o.querySelector('.lab span').textContent=sel[i];o.querySelectorAll('button').forEach(function(b){b.classList.toggle('on',b.dataset.v===sel[i])})})}
document.querySelectorAll('.opt').forEach(function(o,i){o.querySelectorAll('button').forEach(function(b){b.onclick=function(){sel[i]=b.dataset.v;upd()}})});
document.querySelectorAll('.thumbs button').forEach(function(b){b.onclick=function(){show(b.dataset.src)}});
var q=document.getElementById('q');document.getElementById('qm').onclick=function(){q.value=Math.max(1,+q.value-1)};document.getElementById('qp').onclick=function(){q.value=+q.value+1};
document.getElementById('atc').onclick=function(){var v=cur();addCart(+q.value||1,D.title+(v.opts[0]!=='Default Title'?' ('+v.opts.join(', ')+')':''))};upd();"""

def pdp(p):
    v0 = p['variants'][0]
    imgs = p['images']
    thumbs = '' if len(imgs) < 2 else '<div class="thumbs">' + ''.join(f'<button data-src="{i[0]}" class="{"on" if k == 0 else ""}" aria-label="Show image {k+1}"><img src="/images/w900/{i[0]}" alt=""></button>' for k, i in enumerate(imgs)) + '</div>'
    opts = ''
    for k, (name, vals) in enumerate(p['options']):
        if len(vals) == 1 and len(p['options']) == 1:
            opts += f'<div class="opt" style="display:none"><div class="lab">{E(name)}: <span></span></div><div class="vals"><button data-v="{E(vals[0])}"></button></div></div>'
            continue
        opts += f'<div class="opt"><div class="lab">{E(name)}: <span>{E(vals[0])}</span></div><div class="vals">' + ''.join(f'<button data-v="{E(x)}">{E(x)}</button>' for x in vals) + '</div></div>'
    meta = []
    if p.get('heat'): meta.append(f'Heat {heat(p["heat"])} {p["heat"]}/5')
    meta.append(E(p['net']))
    acc = [("Details", f"<p>{E(p['intro'][1])}</p>" if len(p['intro']) > 1 else '')]
    acc = []
    if p.get('includes'): acc.append(("What's in the box", '<ul>' + ''.join(f'<li>{E(n)} ({E(s)})</li>' for n, s in p['includes']) + '</ul>'))
    if p.get('ingredients'): acc.append(("Ingredients & allergens", f"<p>{E(p['ingredients'])}</p><p>{E(p.get('allergen',''))}</p>"))
    elif p.get('allergen') and not p.get('includes'): acc.append(("Allergens", f"<p>{E(p['allergen'])}</p>"))
    elif p.get('allergen'): acc.append(("Allergens", f"<p>{E(p['allergen'])}</p>"))
    if p.get('details'): acc.append(("Specs", '<ul>' + ''.join(f'<li>{E(d)}</li>' for d in p['details']) + '</ul>'))
    acc.append(("Pairs with", f"<p>{E(p['pairs'])}</p>"))
    acc.append(("Size, storage & care", f"<p>{E(p['net'])}. {E(p['storage'])}</p>"))
    acc.append(("Shipping", "<p>We ship to all 50 US states, Monday to Thursday, so glass doesn't sit in a warehouse over the weekend. Flat $7.95, free on orders $60+. If a bottle arrives broken, email us a photo within 7 days and we'll send a new one.</p>"))
    accs = ''.join(f'<details{" open" if i == 0 else ""}><summary>{E(t)}</summary>{b}</details>' for i, (t, b) in enumerate(acc))
    data = dict(title=p['title'], variants=[dict(opts=list(v['opts']), price=float(v['price']), cmp=float(v['cmp']) if v['cmp'] else 0, sku=v['sku'], img=v.get('img')) for v in p['variants']])
    related = [q for q in P if q['collection'] == p['collection'] and q['handle'] != p['handle']]
    related += [q for q in P if q['collection'] != p['collection'] and q['collection'] in ('Bundles & Gift Sets', 'Sauces') and q['handle'] != p['handle']]
    rel = ''.join(card(q) for q in related[:4])
    ctitle = "Gift sets" if p['collection'] == "Bundles & Gift Sets" else p['collection']
    ch = COLH[p['collection']][1]
    body = f'''<div class="wrap"><div class="crumb"><a href="/">Home</a> / <a href="/collections/{ch}/">{E(ctitle)}</a> / {E(p["title"])}</div>
<div class="pdp">
 <div class="gal"><div class="main"><img id="mi" src="/images/w900/{imgs[0][0]}" alt="{E(imgs[0][1])}"></div>{thumbs}</div>
 <div class="info">
  <span class="ty">{E(p["type"])}</span>
  <h1>{E(p["title"])}</h1>
  <p class="lead">{E(p["short"])}</p>
  <div class="pp"><b id="pb">{money(v0["price"])}</b><s id="ps"></s><span class="save" id="pv" style="display:none"></span></div>
  <div class="meta">{" · ".join(meta)}</div>
  {opts}
  <div class="buy"><div class="qty"><button id="qm" aria-label="Decrease">−</button><input id="q" value="1" inputmode="numeric" aria-label="Quantity"><button id="qp" aria-label="Increase">+</button></div><button class="btn p" id="atc">Add to cart</button></div>
  <p class="ship">Ships Monday to Thursday from Texas. Free US shipping on orders $60+.</p>
  <div class="desc">{"".join(f"<p>{E(x)}</p>" for x in p["intro"])}</div>
  {accs}
  <div class="sku" id="sku">SKU {v0["sku"]}</div>
 </div>
</div></div>
<section style="padding-top:0"><div class="wrap"><div class="sh"><div><div class="eyebrow">Keep browsing</div><h2>Goes well with</h2></div></div><div class="grid">{rel}</div></div></section>
<script type="application/json" id="pd">{json.dumps(data)}</script>'''
    os.makedirs(f'{OUT}/products/{p["handle"]}', exist_ok=True)
    open(f'{OUT}/products/{p["handle"]}/index.html', 'w').write(page(p['seo_t'], p['seo_d'], body, og=f"/images/w900/{imgs[0][0]}", extra_js=PDP_JS))

for p in P: pdp(p)
# gift card page (in Shopify this one is created by hand, not by CSV)
gp = dict(handle='gift-card', title=GIFT['title'], collection='Bundles & Gift Sets', type='Gift Card', short=GIFT['short'], intro=[GIFT['body']],
          net='Digital, delivered by email', storage='Never expires', pairs='Anyone who owns a smoker', heat=None, tags='',
          seo_t='Low Water Gift Card | Low Water Smoke Co.', seo_d=GIFT['body'], options=[("Amount", ["$25", "$50", "$100"])],
          variants=[dict(opts=(f"${d[:-3]}",), price=d, cmp='', sku=f"GIFT-{d[:-3]}", grams=0, cost='') for d in GIFT['denoms']],
          images=[GIFT['image']])
pdp(gp)
print("built", len(P) + 1, "product pages,", len(cols), "collections")
