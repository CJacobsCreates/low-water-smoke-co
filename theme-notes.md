# Building Low Water Smoke Co. on Shopify's Dawn theme

The goal is a real store that matches `public/index.html` (live preview: https://jc-shopify-demo.pages.dev/) using only the free **Dawn** theme and the theme editor, with no paid apps and no custom code except one optional CSS snippet.

## 0. Order of work
1. Create the store (or a Shopify Partner development store), then set **Settings > General**: store name "Low Water Smoke Co.", currency USD, unit system Imperial, default weight unit oz.
2. Import products (step 1), create the gift card by hand (step 2), then set up collections (3), theme settings (4), the homepage (5), pages (6), navigation (7), shipping and policies (8).

## 1. Import products
- **Products > Import**, upload `products.csv`, and tick *Publish new products to all sales channels*. Leave *Overwrite products with matching handles* unticked on the first import.
- The file uses Shopify's current product CSV headers (from the official template on help.shopify.com) plus a `Collection` column. Catalogue v2 (22 Oct 2026): **18 products, 30 variants** (tee has Color x Size, cap has Color), with SKUs, weights in grams, cost per item, Standard Product Taxonomy categories, SEO titles and descriptions, image alt text and variant images. Compare-at prices are set only on the three bundles (Sampler $33 to $29, Crossing Gift Box $43 to $38, Pitmaster Box $70 to $62).
- Images are pulled from `https://jc-shopify-demo.pages.dev/images/...` at import time. Shopify copies them to its CDN, so the Pages project can be removed afterwards.
- Inventory is set per collection (sauces 72, rubs 60, bundles 24, accessories 30, merch 18 per variant), tracked by Shopify, and stops selling at 0. Change this to the client's real stock.

## 2. Gift card (manual; Shopify can't create gift cards by CSV)
**Products > Gift cards > Add gift card product**
- Title: Low Water Gift Card. Denominations: $25, $50, $100.
- Image: `https://jc-shopify-demo.pages.dev/images/gift-card-1.jpg` (download it and upload it).
- Description: "Can't decide between sweet and hot? Let them pick. Our digital gift card is delivered by email instantly and never expires."
- Add it to a manual collection named **Gift Cards**.

## 3. Collections
The CSV's `Collection` column creates manual collections. For less upkeep, rebuild them as automated collections by tag:

| Collection | Handle | Automated condition | Products |
|---|---|---|---|
| Sauces | `sauces` | Product tag = `sauce` | Original Post Oak, Mesquite Molasses, Carolina Gold Mustard, Alabama White, Hot Peach Habanero, Hill Country Hot Honey |
| Rubs | `rubs` | Product tag = `rub` | Brisket Rub, Sweet Pecan, Yard Bird Lemon Pepper, Smoked Paprika & Garlic |
| Gift sets | `gift-sets` | Product tag = `bundle` | Three-Sauce Sampler, The Crossing Gift Box, The Pitmaster Box (+ gift card, added manually) |
| Accessories | `accessories` | Product tag = `accessory` | Basting Brush, Instant-Read Thermometer, Waxed Canvas Pit Apron |
| Merch | `merch` | Product tag = `merch` | Crossing Tee, Creek Patch Trucker Cap |

Note: the Pitmaster Box carries both `bundle` and `accessory` tags, so with tag rules it also appears under Accessories. Use `Product type = Gift Set` or a manual collection if that's not wanted.

## 4. Theme settings (Online Store > Themes > Customize > Theme settings)
**Colors.** Create these color schemes:

| Scheme | Background | Text | Solid button bg | Solid button label | Outline button | Shadow |
|---|---|---|---|---|---|---|
| Scheme 1 (default page) | `#EFE6D6` | `#1F1A16` | `#9E3B26` | `#F7F1E6` | `#1F1A16` | `#1F1A16` |
| Scheme 2 (cards / bundle band) | `#F7F1E6` | `#1F1A16` | `#9E3B26` | `#F7F1E6` | `#1F1A16` | `#1F1A16` |
| Scheme 3 (dark: about, footer) | `#1F1A16` | `#F7F1E6` | `#D9783A` | `#1F1A16` | `#F7F1E6` | `#000000` |
| Scheme 4 (newsletter) | `#9E3B26` | `#F7F1E6` | `#F7F1E6` | `#9E3B26` | `#F7F1E6` | `#000000` |
| Scheme 5 (announcement) | `#5F6B4E` | `#F7F1E6` | `#F7F1E6` | `#5F6B4E` | `#F7F1E6` | `#000000` |

**Typography.** Headings: *Zilla Slab* Bold, scale 110%. Body: *Libre Franklin* Regular, scale 100%. Both are in Shopify's font library.

**Layout.** Page width 1200px; space between sections 0 (each section sets its own padding).

**Buttons.** Border thickness 2, opacity 100, corner radius 2, no shadow.

**Product cards.** Style: Standard. Image padding 0. Text alignment left. Corner radius 4. Border 0. Shadow 0. Tick *Show second image on hover* (Original sauce has a lifestyle second image).

**Badges.** Position: top left. Sale badge colour scheme: create a Scheme 6 with background `#D9783A` and text `#1F1A16`, and assign it.

**Cart.** Type: Drawer. Tick *Show vendor* off. Add a cart note for gift messages.

**Social media.** Instagram and Facebook links.

**Favicon.** Export the round creek-crossing badge from the preview header (SVG in `public/index.html`) at 64px.

## 5. Homepage sections (Home page template)
Build in this order to match the preview:

1. **Announcement bar** (header group): Scheme 5. Text: "Free shipping on orders $60+ · Holiday gift boxes ship through Dec 18".
2. **Header**: logo image (wordmark plus badge, 190px wide desktop), menu "Main menu", desktop logo position *middle left*, sticky header *On scroll up*, Scheme 1.
3. **Image banner**: image `hero.jpg`, height *Large*, desktop content position *bottom left*, show container *off*, image overlay opacity 45%. Heading: "Sauce from the bottom of the road." Text: "Post oak smoke, coarse black pepper and no shortcuts. Six sauces and four rubs, cooked 40 gallons at a time in a rented kitchen outside Llano and bottled by hand." Button 1 "Shop sauces & rubs" to /collections/all (solid); Button 2 "Build a gift box" to /collections/gift-sets (outline). On mobile, select *Show content below image* off and *Stack images* off.
4. **Multicolumn** (proof strip): Scheme 3, 4 columns, no images, column text in small sizes: "Real post oak smoke, never liquid" / "Filled & labeled by hand" / "Ships in 2 business days" / "No high-fructose corn syrup". Padding 16/16. On mobile: *Enable swipe*.
5. **Featured collection**: heading "Everything we make", collection *All*, 10 products, desktop columns 5, mobile columns 2, *Enable view all button*, Scheme 1. (Dawn has no filter tabs on the homepage; the preview's tabs map to the collection links in the main menu.)
6. **Featured product**: product *The Pitmaster Box*, Scheme 2, media size Large, show quantity selector off, show dynamic checkout on. Add a **Text** block: "Ships gift-ready. Add a note at checkout and we'll hand-write the card."
7. **Multicolumn** "Which bottle, which cook?": 3 columns, no images, Scheme 1, button "Read the recipes" to /blogs/pit-notes. Copy is in the preview (01 Brisket / 02 Ribs / 03 Chicken).
8. **Image with text** "It started when the creek came up.": image `about.jpg`, image on the right on desktop, Scheme 3, text from brand.md, button "Read our story" to /pages/about.
9. **Email signup**: Scheme 4, heading "Get the pit notes.", text "One email a month: a recipe, a new batch, no spam. 10% off your first order." Pair it with a WELCOME10 discount code.
10. **Footer**: Scheme 3, menus *Shop* and *Help*, email signup off (already on the page), payment icons on, country/region selector off.

Optional polish (Theme settings > Custom CSS):
```css
.card__heading{font-family:var(--font-heading-family);font-weight:600}
.badge{font-family:"IBM Plex Mono",monospace;letter-spacing:.08em;text-transform:uppercase;border-radius:2px}
.banner__heading{letter-spacing:-.01em;line-height:.95}
```

## 6. Pages (Online Store > Pages)
- **About** (`/pages/about`): story from brand.md, `about.jpg`, and the three stats (40 gal per batch, 16-mesh pepper, 0 drops of liquid smoke). Template: page. Add an **Image with text** section via a custom `page.about` template if desired.
- **Shipping** (`/pages/shipping`): "We ship to all 50 US states from Texas, Monday to Thursday so sauces don't sit in a warehouse over the weekend. Orders placed by 12 p.m. CT ship within 2 business days. Flat $7.95 shipping; free on orders $60+. Glass is packed in molded pulp; if anything arrives broken, email a photo within 7 days and we'll replace it. We don't ship outside the US yet."
- **FAQ** (`/pages/faq`): use Dawn's **Collapsible content** section. Suggested questions: Do sauces need refrigeration? (After opening, yes; unopened 12 months in the pantry.) Are your products gluten-free? (All sauces and rubs are made without gluten ingredients; check each label.) Allergens? (Sweet Pecan Rub contains tree nuts; Alabama White contains egg; Original and the bundles contain fish via Worcestershire; several sauces contain mustard.) How hot is Hot Peach? (4 of 5: a slow build, not a punch.) Does Alabama White need the fridge? (Not until it's opened; then use within 6 weeks.) Is the hot honey safe for kids? (Not for infants under 1 year.) Do you sell wholesale? (Yes, to shops and butchers; use the contact form.) Can I add a gift note? (Yes, in the cart.)
- **Contact** (`/pages/contact`): template `page.contact`.
- **Pit Notes** blog (`/blogs/pit-notes`): three posts matching the "Which bottle" cards.

## 7. Navigation (Online Store > Navigation)
- **Main menu:** Shop all (/collections/all) · Sauces · Rubs · Gift sets · Merch · Our story (/pages/about)
- **Footer "Shop":** Sauces · Rubs · Gift sets · Merch · Gift cards
- **Footer "Help":** Shipping · FAQ · Wholesale (contact) · Contact · Refund policy

## 8. Shipping, tax and policies
- **Settings > Shipping and delivery:** a US zone with a flat rate of $7.95, and a free rate on orders $60.00+. Package: a medium box at 12 x 9 x 6 in. Product weights come from the CSV.
- **Settings > Taxes:** US, collect in the home state; Shopify Tax handles it, and the CSV's taxonomy categories set the right food and apparel rates.
- **Settings > Policies:** generate the refund, privacy, terms and shipping templates, then edit the shipping policy to match the Shipping page.
- **Product disclosures:** the Sweet Pecan Rub description already lists the tree-nut allergen.

## 9. Before launch
- Swap the demo copy for the client's real ingredients, nutrition panels and cottage-food or manufacturing licensing (a real food brand needs this).
- Replace the AI-generated photos with real product photography when the client has it. Keep the same limestone, cream and left-light setup so the grid stays consistent.
- Run a test order with Shopify's Bogus Gateway, and check emails under **Settings > Notifications** (set the accent colour to `#9E3B26` and upload the logo).


## Preview site (v2, 22 Oct 2026)
- Multi-page static preview: `/` home, `/collections/{all,sauces,rubs,gift-sets,accessories,merch}/`, `/products/<handle>/` (18 products + gift card). Variant pickers, sort and add-to-cart work as a demo; checkout and sign-up are switched off.
- Built from `src/products.py` by `src/build_site.py`; CSV by `src/build_csv.py`. Deploy: `npx wrangler pages deploy public --project-name jc-shopify-demo --branch main` (run from a folder with its own package.json, e.g. /tmp/wdeploy, because of a cache-permission quirk).
- Footer: "Concept store by Jacobs Consultancy. Low Water Smoke Co. is a fictional brand, and nothing here is for sale."
- Product photos are AI-generated. The 18 fl oz Original variant reuses the 12 oz photo.
