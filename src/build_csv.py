import csv, sys
sys.path.insert(0, 'src')
from products import P, BASE, VENDOR, body_html
hdr = next(csv.reader(open('src/shopify-official-template.csv', encoding='utf-8-sig'))) + ["Collection"]
STOCK = {"Sauces": 72, "Rubs": 60, "Bundles & Gift Sets": 24, "Accessories": 30, "Merch": 18}
rows = []
def blank(): return {h: "" for h in hdr}
for p in P:
    imgs = p["images"]
    for i, v in enumerate(p["variants"]):
        r = blank(); r["URL handle"] = p["handle"]
        if i == 0:
            r.update({"Title": p["title"], "Description": body_html(p), "Vendor": VENDOR, "Product category": p["cat"],
                      "Type": p["type"], "Tags": p["tags"], "Published on online store": "TRUE", "Status": "active",
                      "SEO title": p["seo_t"], "SEO description": p["seo_d"], "Gift card": "FALSE", "Collection": p["collection"]})
            if p["options"]:
                for k, (name, _) in enumerate(p["options"]): r[f"Option{k+1} name"] = name
            else:
                r["Option1 name"] = "Title"
        for k, val in enumerate(v["opts"]): r[f"Option{k+1} value"] = val
        g = v["grams"]
        r.update({"SKU": v["sku"], "Price": v["price"], "Compare-at price": v["cmp"], "Cost per item": v["cost"],
                  "Charge tax": "TRUE", "Inventory tracker": "shopify", "Inventory quantity": str(STOCK[p["collection"]]),
                  "Continue selling when out of stock": "DENY", "Weight value (grams)": str(g),
                  "Weight unit for display": "lb" if g >= 900 else "oz", "Requires shipping": "TRUE", "Fulfillment service": "manual"})
        if v.get("img"): r["Variant image URL"] = BASE + v["img"]
        if i < len(imgs):
            r["Product image URL"] = BASE + imgs[i][0]; r["Image position"] = str(i+1); r["Image alt text"] = imgs[i][1]
        rows.append(r)
    for j in range(len(p["variants"]), len(imgs)):
        r = blank(); r["URL handle"] = p["handle"]
        r["Product image URL"] = BASE + imgs[j][0]; r["Image position"] = str(j+1); r["Image alt text"] = imgs[j][1]
        rows.append(r)
with open('products.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=hdr, lineterminator="\n"); w.writeheader(); w.writerows(rows)
print(len(rows), "rows,", len(P), "products,", sum(len(p["variants"]) for p in P), "variants")
