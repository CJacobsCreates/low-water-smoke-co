# Screenshots of the local build (run from the repo root). Needs Google Chrome.
U=${1:-file://$PWD/public/index.html}
mkdir -p .review
shot(){ d=$(mktemp -d /tmp/chrlw.XXXX); google-chrome --user-data-dir=$d --headless=new --no-sandbox --disable-gpu --hide-scrollbars --no-first-run "$@" 2>/dev/null; rm -rf $d; }
shot --window-size=1440,900 --virtual-time-budget=10000 --screenshot=.review/lw-da.png "$U"
shot --window-size=1440,4800 --virtual-time-budget=10000 --screenshot=.review/lw-df.png "$U"
shot --window-size=390,844 --force-device-scale-factor=2 --virtual-time-budget=10000 --screenshot=.review/lw-ma.png "$U"
shot --window-size=390,6900 --force-device-scale-factor=2 --virtual-time-budget=10000 --screenshot=.review/lw-mf.png "$U"
