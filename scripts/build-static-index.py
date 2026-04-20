"""
Generate a single index.html in the project root that works when opened via file://
(double-click). Run: python scripts/build-static-index.py
"""
from __future__ import annotations

import base64
import json
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    locales: dict[str, object] = {}
    for code in ("en", "es", "zh", "tl", "vi", "ru"):
        path = root / "src" / "messages" / f"{code}.json"
        locales[code] = json.loads(path.read_text(encoding="utf-8"))

    ideas = json.loads((root / "ideas.json").read_text(encoding="utf-8"))
    payload = {"locales": locales, "ideas": ideas}
    raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    b64 = base64.b64encode(raw).decode("ascii")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>EquityBridge</title>
  <meta name="description" content="Partnership discovery for founders — open locally without a server." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&subset=latin,latin-ext,cyrillic&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --void: #050507;
      --ink: #0a0a0f;
      --lime: #c8ff00;
      --mist: #8a8f9e;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      min-height: 100vh;
      background: var(--void);
      color: #fff;
      font-family: "DM Sans", system-ui, sans-serif;
      -webkit-font-smoothing: antialiased;
    }}
    .font-display {{ font-family: "Bebas Neue", system-ui, sans-serif; }}
    a {{ color: inherit; text-decoration: none; }}
    .noise {{
      pointer-events: none;
      position: fixed;
      inset: 0;
      opacity: 0.04;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.35'/%3E%3C/svg%3E");
      mix-blend-mode: soft-light;
      z-index: 1;
    }}
    .bg-grid {{
      pointer-events: none;
      position: fixed;
      inset: 0;
      z-index: 0;
      background:
        linear-gradient(to bottom, rgba(5,5,7,0) 0%, rgba(5,5,7,0.85) 55%, rgba(5,5,7,1) 100%),
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(200,255,0,0.12), transparent);
    }}
    header {{
      position: fixed;
      inset: 0 0 auto;
      z-index: 50;
      border-bottom: 1px solid rgba(255,255,255,0.06);
      background: rgba(5,5,7,0.72);
      backdrop-filter: blur(16px);
    }}
    .wrap {{
      max-width: 72rem;
      margin: 0 auto;
      padding: 1rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    .logo {{
      width: 2.25rem;
      height: 2.25rem;
      border-radius: 999px;
      border: 1px solid rgba(200,255,0,0.45);
      background: rgba(200,255,0,0.1);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--lime);
      box-shadow: 0 0 24px rgba(200,255,0,0.25);
    }}
    .brand-text {{
      font-family: "Bebas Neue", system-ui, sans-serif;
      font-size: 1.35rem;
      letter-spacing: 0.12em;
    }}
    .brand-text span {{ color: var(--lime); }}
    nav.nav-desk {{
      display: none;
      gap: 2rem;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--mist);
    }}
    @media (min-width: 768px) {{
      nav.nav-desk {{ display: flex; }}
    }}
    nav.nav-desk a:hover {{ color: #fff; }}
    .hdr-actions {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    select.lang {{
      cursor: pointer;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.1);
      background: rgba(255,255,255,0.05);
      color: #fff;
      font-size: 11px;
      padding: 0.35rem 0.75rem;
      outline: none;
    }}
    select.lang:focus {{ border-color: rgba(200,255,0,0.5); }}
    .btn-ghost {{
      display: none;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.15);
      padding: 0.5rem 1rem;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.9);
    }}
    @media (min-width: 640px) {{
      .btn-ghost {{ display: inline-block; }}
    }}
    .btn-ghost:hover {{ border-color: rgba(200,255,0,0.45); color: #fff; }}
    .btn-lime {{
      border-radius: 999px;
      background: var(--lime);
      color: var(--void);
      padding: 0.5rem 1rem;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      border: none;
      cursor: pointer;
      box-shadow: 0 0 32px rgba(200,255,0,0.35);
    }}
    .btn-lime:hover {{ filter: brightness(1.05); }}
    main {{
      position: relative;
      z-index: 10;
      padding-top: 5.5rem;
    }}
    section.page {{
      display: none;
    }}
    section.page.is-active {{
      display: block;
    }}
    .container {{
      max-width: 72rem;
      margin: 0 auto;
      padding: 2.5rem 1.25rem 4rem;
    }}
    .eyebrow {{
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.35em;
      text-transform: uppercase;
      color: var(--lime);
    }}
    h1.hero-title {{
      margin: 1.5rem 0 0;
      font-family: "Bebas Neue", system-ui, sans-serif;
      font-size: clamp(3rem, 8vw, 7.5rem);
      line-height: 0.92;
      letter-spacing: 0.02em;
    }}
    h1.hero-title .accent {{ color: var(--lime); }}
    .hero-lead {{
      margin-top: 2rem;
      max-width: 42rem;
      font-size: 1.125rem;
      line-height: 1.7;
      color: var(--mist);
    }}
    @media (min-width: 640px) {{
      .hero-lead {{ font-size: 1.25rem; }}
    }}
    .hero-cta {{
      margin-top: 2.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
    }}
    .grid-3 {{
      display: grid;
      gap: 2rem;
    }}
    @media (min-width: 900px) {{
      .grid-3 {{ grid-template-columns: repeat(3, 1fr); }}
    }}
    .card {{
      border-radius: 1.5rem;
      border: 1px solid rgba(255,255,255,0.1);
      background: rgba(255,255,255,0.03);
      padding: 2rem;
    }}
    .idea-card {{
      position: relative;
      overflow: hidden;
      border-radius: 1.5rem;
      border: 1px solid rgba(255,255,255,0.1);
      background: linear-gradient(to bottom, rgba(255,255,255,0.06), transparent);
      padding: 1.5rem;
    }}
    .idea-card:hover {{
      border-color: rgba(200,255,0,0.3);
      box-shadow: 0 0 48px rgba(200,255,0,0.08);
    }}
    .idea-card .sector {{
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      color: var(--lime);
    }}
    .idea-card h3 {{
      margin: 0.75rem 0 0;
      font-family: "Bebas Neue", system-ui, sans-serif;
      font-size: 1.75rem;
      letter-spacing: 0.06em;
    }}
    .idea-card p.tagline {{
      margin: 0.75rem 0 0;
      font-size: 0.875rem;
      color: var(--mist);
      line-height: 1.6;
    }}
    .idea-meta {{
      margin-top: 1.5rem;
      padding-top: 1.5rem;
      border-top: 1px solid rgba(255,255,255,0.1);
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.18em;
      color: var(--mist);
    }}
    .idea-meta dd {{
      margin: 0.35rem 0 0;
      font-size: 1rem;
      font-weight: 600;
      letter-spacing: normal;
      text-transform: none;
    }}
    .idea-meta dd.equity {{ color: var(--lime); }}
    footer.site {{
      border-top: 1px solid rgba(255,255,255,0.1);
      background: var(--ink);
      position: relative;
      z-index: 10;
    }}
    .footer-inner {{
      max-width: 72rem;
      margin: 0 auto;
      padding: 4rem 1.25rem;
    }}
    .muted {{ color: var(--mist); }}
    .stack {{ display: flex; flex-direction: column; gap: 0.75rem; }}
    input, select.field {{
      width: 100%;
      margin-top: 0.5rem;
      border-radius: 1rem;
      border: 1px solid rgba(255,255,255,0.1);
      background: rgba(255,255,255,0.05);
      color: #fff;
      padding: 0.75rem 1rem;
      font-size: 0.875rem;
      outline: none;
    }}
    input:focus {{ border-color: rgba(200,255,0,0.45); }}
    .pricing-grid {{
      display: grid;
      gap: 1.5rem;
    }}
    @media (min-width: 1024px) {{
      .pricing-grid {{ grid-template-columns: repeat(3, 1fr); }}
    }}
    .plan {{
      border-radius: 1.5rem;
      border: 1px solid rgba(255,255,255,0.1);
      padding: 2rem;
      display: flex;
      flex-direction: column;
    }}
    .plan.hot {{
      border-color: rgba(200,255,0,0.45);
      background: linear-gradient(to bottom, rgba(200,255,0,0.12), transparent);
      box-shadow: 0 0 60px rgba(200,255,0,0.12);
    }}
    .badge {{
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--lime);
      margin-bottom: 0.5rem;
    }}
    ul.check {{
      list-style: none;
      padding: 0;
      margin: 2rem 0 0;
      flex: 1;
    }}
    ul.check li {{
      display: flex;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
      font-size: 0.875rem;
      color: rgba(255,255,255,0.85);
    }}
    ul.check li::before {{ content: "✓"; color: var(--lime); }}
    .local-note {{
      margin: 1.5rem 1.25rem;
      padding: 0.9rem 1.15rem;
      border-radius: 0.75rem;
      border: 1px solid rgba(255,255,255,0.12);
      background: rgba(255,255,255,0.04);
      font-size: 0.8125rem;
      line-height: 1.55;
      color: var(--mist);
      max-width: 48rem;
      margin-left: auto;
      margin-right: auto;
    }}
    .grid-how {{
      display: grid;
      gap: 1rem;
      margin-top: 2.5rem;
      grid-template-columns: 1fr;
    }}
    @media (min-width: 640px) {{
      .grid-how {{ grid-template-columns: 1fr 1fr; }}
    }}
  </style>
</head>
<body>
  <div class="bg-grid" aria-hidden="true"></div>
  <div class="noise" aria-hidden="true"></div>

  <div id="eb-seed" hidden data-b64="{b64}"></div>

  <header>
    <div class="wrap">
      <a href="#home" class="brand" data-nav>
        <span class="logo">EB</span>
        <span class="brand-text">EQUITY<span>BRIDGE</span></span>
      </a>
      <nav class="nav-desk" aria-label="Primary">
        <a href="#ideas" data-nav data-i18n="nav.ideas"></a>
        <a href="#how" data-nav data-i18n="nav.how"></a>
        <a href="#pricing" data-nav data-i18n="nav.pricing"></a>
      </nav>
      <div class="hdr-actions">
        <select class="lang" id="lang-select" aria-label="Language">
          <option value="en">English</option>
          <option value="es">Español</option>
          <option value="zh">中文</option>
          <option value="tl">Tagalog</option>
          <option value="vi">Tiếng Việt</option>
          <option value="ru">Русский</option>
        </select>
        <a href="#register" class="btn-ghost" data-nav data-i18n="nav.signIn"></a>
        <a href="#register" class="btn-lime" data-nav data-i18n="simple.bigCta"></a>
      </div>
    </div>
  </header>

  <p class="local-note" id="local-note" data-i18n="simple.banner"></p>

  <main>
    <section id="page-home" class="page is-active">
      <div class="container" style="text-align:center;max-width:42rem">
        <h1 class="hero-title">
          <span data-i18n="hero.titleLine1"></span><br />
          <span class="accent" data-i18n="hero.titleLine2"></span>
        </h1>
        <p class="hero-lead" style="margin-top:1.75rem" data-i18n="simple.intro"></p>
        <div class="hero-cta" style="margin-top:2rem;justify-content:center;flex-wrap:wrap">
          <a href="#register" class="btn-lime" data-nav data-i18n="simple.bigCta"></a>
          <a href="#ideas" class="btn-ghost" style="display:inline-block" data-nav data-i18n="hero.ctaPrimary"></a>
          <a href="#pricing" class="btn-ghost" style="display:inline-block;opacity:0.9" data-nav data-i18n="hero.ctaSecondary"></a>
        </div>
      </div>
      <div style="border-top:1px solid rgba(255,255,255,0.1);background:rgba(255,255,255,0.02);margin-top:3rem;padding:3rem 0 4rem" id="how">
        <div class="container">
          <h2 class="font-display" style="font-size:clamp(2rem,4vw,3rem);letter-spacing:0.08em;text-align:center" data-i18n="how.title"></h2>
          <p class="muted" style="max-width:40rem;margin:1rem auto 0;text-align:center" data-i18n="how.subtitle"></p>
          <div class="grid-how" id="how-steps"></div>
        </div>
      </div>
      <div class="container">
        <div style="display:flex;flex-wrap:wrap;gap:2rem;justify-content:space-between;align-items:flex-end">
          <div>
            <h2 class="font-display" style="font-size:clamp(2rem,4vw,3rem);letter-spacing:0.08em" data-i18n="ideasPreview.title"></h2>
            <p class="muted" style="max-width:36rem;margin-top:1rem" data-i18n="ideasPreview.subtitle"></p>
          </div>
          <a href="#ideas" class="btn-ghost" style="display:inline-block;border-color:rgba(200,255,0,0.45);color:var(--lime)" data-nav data-i18n="ideasPreview.viewAll"></a>
        </div>
        <div class="grid-3" style="margin-top:3rem" id="ideas-preview"></div>
      </div>
      <div class="container" style="text-align:center;padding-bottom:5rem;max-width:36rem;margin:0 auto">
        <p class="muted" style="line-height:1.65;font-size:0.875rem" data-i18n="simple.trustShort"></p>
        <a href="#register" class="btn-lime" style="margin-top:1.75rem;display:inline-block;background:#fff;color:var(--void)" data-nav data-i18n="simple.bigCta"></a>
      </div>
    </section>

    <section id="page-ideas" class="page">
      <div class="container">
        <h1 class="font-display hero-title" style="font-size:clamp(2.5rem,6vw,4rem)" data-i18n="ideasPage.title"></h1>
        <p class="hero-lead" data-i18n="ideasPage.subtitle"></p>
        <p class="eyebrow" style="margin-top:1rem;display:inline-block;border:1px solid rgba(255,255,255,0.1);border-radius:999px;padding:0.5rem 1rem" data-i18n="ideasPage.filterPlaceholder"></p>
        <div class="grid-3" style="margin-top:3rem;grid-template-columns:1fr" id="ideas-all"></div>
      </div>
    </section>

    <section id="page-idea-detail" class="page">
      <div class="container" id="idea-detail-root"></div>
    </section>

    <section id="page-pricing" class="page">
      <div class="container">
        <h1 class="font-display hero-title" style="font-size:clamp(2.5rem,6vw,4rem)" data-i18n="pricing.title"></h1>
        <p class="hero-lead" data-i18n="pricing.subtitle"></p>
        <div style="display:flex;justify-content:center;gap:0.5rem;margin-top:2rem">
          <button type="button" class="btn-lime" id="bill-monthly" style="box-shadow:none"> </button>
          <button type="button" class="btn-ghost" id="bill-annual" style="display:inline-block"> </button>
        </div>
        <div class="pricing-grid" style="margin-top:3rem" id="pricing-plans"></div>
        <p class="muted" style="text-align:center;margin-top:3rem;font-size:0.75rem" data-i18n="pricing.footnote"></p>
      </div>
    </section>

    <section id="page-register" class="page">
      <div class="container" style="max-width:32rem">
        <p class="eyebrow">EquityBridge</p>
        <h1 class="font-display hero-title" style="font-size:2.75rem" data-i18n="auth.register.title"></h1>
        <p class="muted" data-i18n="auth.register.subtitle"></p>
        <form id="reg-form" class="stack" style="margin-top:2rem">
          <label><span class="eyebrow" style="letter-spacing:0.2em" data-i18n="auth.register.email"></span><input type="email" required /></label>
          <label><span class="eyebrow" style="letter-spacing:0.2em" data-i18n="auth.register.password"></span><input type="password" required /></label>
          <fieldset style="border:none;padding:0;margin:0">
            <legend class="eyebrow" style="letter-spacing:0.2em" data-i18n="auth.register.role"></legend>
            <div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin-top:0.75rem">
              <label><input type="radio" name="role" value="founder" checked /> <span data-i18n="auth.register.roleFounder"></span></label>
              <label><input type="radio" name="role" value="partner" /> <span data-i18n="auth.register.rolePartner"></span></label>
              <label><input type="radio" name="role" value="both" /> <span data-i18n="auth.register.roleBoth"></span></label>
            </div>
          </fieldset>
          <button type="submit" class="btn-lime" data-i18n="auth.register.submit"></button>
        </form>
        <p class="muted" style="margin-top:2rem;font-size:0.75rem;text-align:center" data-i18n="auth.register.note"></p>
      </div>
    </section>

    <section id="page-verify" class="page">
      <div class="container" style="max-width:32rem">
        <h1 class="font-display hero-title" style="font-size:2.75rem" data-i18n="verify.title"></h1>
        <p class="muted" data-i18n="verify.subtitle"></p>
        <div class="stack" style="margin-top:2rem" id="verify-ui"></div>
      </div>
    </section>

    <section id="page-dashboard" class="page">
      <div class="container">
        <h1 class="font-display hero-title" style="font-size:clamp(2.5rem,6vw,4rem)" data-i18n="dashboard.title"></h1>
        <p class="hero-lead" data-i18n="dashboard.subtitle"></p>
        <div class="pricing-grid" style="margin-top:2rem" id="dashboard-grid"></div>
      </div>
    </section>
  </main>

  <footer class="site">
    <div class="footer-inner">
      <div style="display:flex;flex-wrap:wrap;gap:3rem;justify-content:space-between">
        <div style="max-width:20rem">
          <p class="font-display" style="font-size:1.75rem;letter-spacing:0.08em">EQUITY<span style="color:var(--lime)">BRIDGE</span></p>
          <p class="muted" style="margin-top:1rem;font-size:0.875rem;line-height:1.6" data-i18n="footer.tagline"></p>
        </div>
        <div style="display:flex;gap:3rem;flex-wrap:wrap">
          <div>
            <p class="eyebrow" style="color:var(--mist)" data-i18n="footer.cols.product"></p>
            <div class="stack" style="margin-top:1rem;font-size:0.875rem;color:rgba(255,255,255,0.8)">
              <a href="#ideas" data-nav data-i18n="footer.links.ideas"></a>
              <a href="#pricing" data-nav data-i18n="footer.links.pricing"></a>
              <a href="#how" data-nav data-i18n="footer.links.how"></a>
            </div>
          </div>
          <div>
            <p class="eyebrow" style="color:var(--mist)" data-i18n="footer.cols.company"></p>
            <div class="stack" style="margin-top:1rem;font-size:0.875rem;color:rgba(255,255,255,0.8)">
              <a href="mailto:hello@equitybridge.example" data-i18n="footer.links.contact"></a>
            </div>
          </div>
          <div>
            <p class="eyebrow" style="color:var(--mist)" data-i18n="footer.cols.legal"></p>
            <div class="stack" style="margin-top:1rem;font-size:0.875rem;color:rgba(255,255,255,0.55)">
              <span data-i18n="footer.links.privacy"></span>
              <span data-i18n="footer.links.terms"></span>
            </div>
          </div>
        </div>
      </div>
      <p class="muted" style="margin-top:3rem;font-size:0.75rem" id="footer-rights"></p>
    </div>
  </footer>

  <script>
(function () {{
  const seed = document.getElementById("eb-seed");
  const b64 = seed && seed.getAttribute("data-b64");
  if (!b64) return;
  const bytes = Uint8Array.from(atob(b64), (c) => c.charCodeAt(0));
  const text = new TextDecoder("utf-8").decode(bytes);
  const EB = JSON.parse(text);

  const LS_LANG = "equitybridge-static-lang";
  const LS_VER = "equitybridge-demo-verified";

  let lang = "en";
  try {{
    lang = localStorage.getItem(LS_LANG) || "en";
  }} catch (e) {{}}

  let route = {{ name: "home", slug: null }};
  let billingAnnual = false;
  /** Fallback when localStorage throws (file://, private mode, corporate policy) */
  let demoVerified = false;

  function isVerified() {{
    if (demoVerified) return true;
    try {{
      return localStorage.getItem(LS_VER) === "1";
    }} catch (e) {{
      return false;
    }}
  }}

  function setDemoVerified() {{
    demoVerified = true;
    try {{
      localStorage.setItem(LS_VER, "1");
    }} catch (e) {{
      console.warn("[EquityBridge] localStorage blocked — demo state kept in memory only.");
    }}
  }}

  const t = () => EB.locales[lang] || EB.locales.en;

  function getPath(obj, path) {{
    return path.split(".").reduce((o, k) => (o && o[k] !== undefined ? o[k] : null), obj);
  }}

  function applyI18n() {{
    const tr = t();
    document.documentElement.lang = lang === "zh" ? "zh-Hans" : lang === "ru" ? "ru" : lang;
    document.title = tr.meta && tr.meta.title ? tr.meta.title : "EquityBridge";

    document.querySelectorAll("[data-i18n]").forEach((el) => {{
      const key = el.getAttribute("data-i18n");
      const val = getPath(tr, key);
      if (val != null) el.textContent = val;
    }});

    const rights = getPath(tr, "footer.rights") || "";
    const fr = document.getElementById("footer-rights");
    if (fr) fr.textContent = rights.replace("{{year}}", String(new Date().getFullYear()));

    const sel = document.getElementById("lang-select");
    if (sel) sel.value = lang;

    renderHow();
    renderIdeasPreview();
    renderIdeasAll();
    renderPricing();
    renderDashboard();
    if (route.name === "idea" && route.slug) renderIdeaDetail(route.slug);
    if (route.name === "verify") renderVerify();
  }}

  function renderHow() {{
    const root = document.getElementById("how-steps");
    if (!root) return;
    const steps = getPath(t(), "how.steps") || [];
    root.innerHTML = steps
      .map(
        (s, i) => `
      <div class="card" style="padding:1.25rem;border-radius:1rem">
        <span style="display:inline-flex;width:1.75rem;height:1.75rem;border-radius:999px;align-items:center;justify-content:center;font-size:11px;font-weight:700;background:rgba(200,255,0,0.15);color:var(--lime)">${{i + 1}}</span>
        <h3 class="font-display" style="font-size:1.15rem;letter-spacing:0.1em;margin-top:0.85rem">${{escapeHtml(s.title)}}</h3>
        <p class="muted" style="margin-top:0.5rem;line-height:1.65;font-size:0.8125rem">${{escapeHtml(s.body)}}</p>
      </div>`
      )
      .join("");
  }}

  function money(n) {{
    return new Intl.NumberFormat("en-US", {{ style: "currency", currency: "USD", maximumFractionDigits: 0 }}).format(n);
  }}

  function ideaCardHTML(idea, openLabel) {{
    const tr = t();
    const raiseL = getPath(tr, "ideasPage.raise");
    const eqL = getPath(tr, "ideasPage.equity");
    return `
    <article class="idea-card">
      <p class="sector">${{escapeHtml(idea.sector)}}</p>
      <h3>${{escapeHtml(idea.title)}}</h3>
      <p class="tagline">${{escapeHtml(idea.tagline)}}</p>
      <dl class="idea-meta">
        <div><dt>${{escapeHtml(raiseL)}}</dt><dd>${{escapeHtml(money(idea.raiseUsd))}}</dd></div>
        <div><dt>${{escapeHtml(eqL)}}</dt><dd class="equity">${{escapeHtml(String(idea.equityPercent))}}%</dd></div>
      </dl>
      <a href="#idea/${{encodeURIComponent(idea.slug)}}" data-nav style="margin-top:1.25rem;display:inline-flex;align-items:center;gap:0.35rem;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase">${{escapeHtml(openLabel)}} ↗</a>
    </article>`;
  }}

  function renderIdeasPreview() {{
    const root = document.getElementById("ideas-preview");
    if (!root) return;
    const openLabel = getPath(t(), "ideasPage.openListing");
    root.innerHTML = EB.ideas.slice(0, 3).map((idea) => ideaCardHTML(idea, openLabel)).join("");
  }}

  function renderIdeasAll() {{
    const root = document.getElementById("ideas-all");
    if (!root) return;
    const openLabel = getPath(t(), "ideasPage.openListing");
    root.innerHTML = EB.ideas.map((idea) => ideaCardHTML(idea, openLabel)).join("");
  }}

  function renderIdeaDetail(slug) {{
    const root = document.getElementById("idea-detail-root");
    if (!root) return;
    const idea = EB.ideas.find((x) => x.slug === slug);
    const tr = t();
    if (!idea) {{
      root.innerHTML = "<p class=\\"muted\\">Not found.</p>";
      return;
    }}
    const sec = getPath(tr, "ideaDetail.sections") || {{}};
    const back = getPath(tr, "ideaDetail.back");
    const disc = getPath(tr, "ideaDetail.disclaimer");
    const contact = getPath(tr, "ideaDetail.contact");
    const raiseL = getPath(tr, "ideasPage.raise");
    const eqL = getPath(tr, "ideasPage.equity");
    const body = `
      <a href="#ideas" data-nav class="eyebrow" style="color:var(--mist);display:inline-block;margin-bottom:2rem">← ${{escapeHtml(back)}}</a>
      <p class="sector">${{escapeHtml(idea.sector)}}</p>
      <h1 class="font-display hero-title" style="font-size:clamp(2.5rem,6vw,4rem)">${{escapeHtml(idea.title)}}</h1>
      <p class="hero-lead">${{escapeHtml(idea.tagline)}}</p>
      <dl class="idea-meta" style="margin-top:2rem;border:1px solid rgba(255,255,255,0.1);border-radius:1rem;padding:1.5rem">
        <div><dt>${{escapeHtml(raiseL)}}</dt><dd>${{escapeHtml(money(idea.raiseUsd))}}</dd></div>
        <div><dt>${{escapeHtml(eqL)}}</dt><dd class="equity">${{escapeHtml(String(idea.equityPercent))}}%</dd></div>
      </dl>
      <div class="stack" style="margin-top:3rem">
        ${{idea.sections
          .map(
            (s) => `
          <section>
            <h2 class="font-display" style="font-size:1.5rem;letter-spacing:0.12em">${{escapeHtml(sec[s.titleKey] || s.titleKey)}}</h2>
            <p class="muted" style="margin-top:0.75rem;line-height:1.7;font-size:0.875rem">${{escapeHtml(s.body)}}</p>
          </section>`
          )
          .join("")}}
      </div>
      <div class="card" style="margin-top:3rem;border-color:rgba(200,255,0,0.3);background:rgba(200,255,0,0.05)">
        <p class="muted" style="font-size:0.875rem;line-height:1.7">${{escapeHtml(disc)}}</p>
        <button type="button" class="btn-lime" style="margin-top:1.25rem">${{escapeHtml(contact)}}</button>
      </div>
    `;
    root.innerHTML = body;
  }}

  function renderPricing() {{
    const tr = t();
    const plans = getPath(tr, "pricing.plans") || [];
    const root = document.getElementById("pricing-plans");
    const bm = document.getElementById("bill-monthly");
    const ba = document.getElementById("bill-annual");
    if (bm) {{
      bm.textContent = getPath(tr, "pricing.monthly");
      bm.classList.toggle("btn-lime", !billingAnnual);
      bm.classList.toggle("btn-ghost", billingAnnual);
      bm.style.display = "inline-block";
      bm.style.boxShadow = billingAnnual ? "none" : "";
      bm.style.border = billingAnnual ? "1px solid rgba(255,255,255,0.15)" : "none";
      bm.style.background = billingAnnual ? "transparent" : "";
      bm.style.color = billingAnnual ? "#fff" : "var(--void)";
    }}
    if (ba) {{
      ba.textContent = getPath(tr, "pricing.annual");
      ba.classList.toggle("btn-lime", billingAnnual);
      ba.classList.toggle("btn-ghost", !billingAnnual);
      ba.style.background = billingAnnual ? "var(--lime)" : "transparent";
      ba.style.color = billingAnnual ? "var(--void)" : "";
    }}
    if (!root) return;
    root.innerHTML = plans
      .map((p) => {{
        const price = billingAnnual ? p.priceAnnual : p.priceMonthly;
        const suffix = billingAnnual ? getPath(tr, "pricing.perYear") : getPath(tr, "pricing.perMonth");
        const hot = p.highlighted ? " hot" : "";
        const badge = p.highlighted ? `<div class="badge">${{escapeHtml(getPath(tr, "pricing.popularBadge"))}}</div>` : "";
        const feats = (p.features || []).map((f) => `<li>${{escapeHtml(f)}}</li>`).join("");
        return `
        <div class="plan${{hot}}">
          ${{badge}}
          <h2 class="font-display" style="font-size:1.75rem;letter-spacing:0.1em">${{escapeHtml(p.name)}}</h2>
          <p style="margin-top:1rem" class="muted"><span style="font-size:2.25rem;font-weight:700;color:#fff">${{escapeHtml(price)}}</span> <span style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em">${{escapeHtml(suffix)}}</span></p>
          <p class="muted" style="margin-top:1rem;line-height:1.6;font-size:0.875rem">${{escapeHtml(p.desc)}}</p>
          <ul class="check">${{feats}}</ul>
          <button type="button" class="btn-lime" style="margin-top:1.5rem;width:100%;${{p.highlighted ? "" : "background:transparent;border:1px solid rgba(255,255,255,0.2);color:#fff;box-shadow:none"}}">${{escapeHtml(getPath(tr, "pricing.cta"))}}</button>
        </div>`;
      }})
      .join("");
  }}

  function renderDashboard() {{
    const root = document.getElementById("dashboard-grid");
    if (!root) return;
    const tr = t();
    const verified = isVerified();
    const vtext = verified ? getPath(tr, "dashboard.verified") : getPath(tr, "dashboard.notVerified");
    root.innerHTML = `
      <div class="card">
        <h2 class="font-display" style="font-size:1.5rem;letter-spacing:0.1em">${{escapeHtml(getPath(tr, "dashboard.cards.profile"))}}</h2>
        <p class="muted" style="margin-top:1rem;font-size:0.875rem">${{escapeHtml(vtext)}}</p>
        <a href="#verify" class="eyebrow" data-nav style="margin-top:1rem;display:inline-block;color:var(--lime)">${{escapeHtml(getPath(tr, "verify.title"))}} →</a>
      </div>
      <div class="card" style="border-color:rgba(200,255,0,0.25);background:rgba(200,255,0,0.05)">
        <h2 class="font-display" style="font-size:1.5rem;letter-spacing:0.1em">${{escapeHtml(getPath(tr, "dashboard.cards.subscription"))}}</h2>
        <p class="muted" style="margin-top:1rem;font-size:0.875rem"><span style="color:#fff">${{escapeHtml(getPath(tr, "dashboard.plan"))}}:</span> ${{escapeHtml((getPath(tr, "pricing.plans") || [])[0]?.name || "")}}</p>
        <a href="#pricing" data-nav class="eyebrow" style="margin-top:1rem;display:inline-block;color:var(--lime)">${{escapeHtml(getPath(tr, "dashboard.manage"))}}</a>
      </div>
      <div class="card">
        <h2 class="font-display" style="font-size:1.5rem;letter-spacing:0.1em">${{escapeHtml(getPath(tr, "dashboard.cards.listings"))}}</h2>
        <p class="muted" style="margin-top:1rem;font-size:0.875rem">${{escapeHtml(getPath(tr, "dashboard.draftHint"))}}</p>
        <button type="button" class="btn-ghost" style="margin-top:1rem;display:inline-block">${{escapeHtml(getPath(tr, "dashboard.newListing"))}}</button>
      </div>
      <div class="card">
        <h2 class="font-display" style="font-size:1.5rem;letter-spacing:0.1em">${{escapeHtml(getPath(tr, "dashboard.cards.messages"))}}</h2>
        <p class="muted" style="margin-top:1rem;font-size:0.875rem">${{escapeHtml(getPath(tr, "dashboard.messagesHint"))}}</p>
      </div>
    `;
  }}

  function escapeHtml(s) {{
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }}

  function parseHash() {{
    const h = (location.hash || "#home").replace(/^#/, "");
    if (h === "home" || h === "") route = {{ name: "home", slug: null }};
    else if (h === "ideas") route = {{ name: "ideas", slug: null }};
    else if (h === "pricing") route = {{ name: "pricing", slug: null }};
    else if (h === "register") route = {{ name: "register", slug: null }};
    else if (h === "verify") route = {{ name: "verify", slug: null }};
    else if (h === "dashboard") route = {{ name: "dashboard", slug: null }};
    else if (h === "how") {{
      route = {{ name: "home", slug: null }};
      requestAnimationFrame(() => document.getElementById("how") && document.getElementById("how").scrollIntoView());
    }} else if (h.startsWith("idea/")) route = {{ name: "idea", slug: decodeURIComponent(h.slice(5)) }};
    else route = {{ name: "home", slug: null }};
  }}

  function showPage() {{
    const map = {{
      home: "page-home",
      ideas: "page-ideas",
      idea: "page-idea-detail",
      pricing: "page-pricing",
      register: "page-register",
      verify: "page-verify",
      dashboard: "page-dashboard",
    }};
    document.querySelectorAll("main section.page").forEach((p) => p.classList.remove("is-active"));
    const id = map[route.name] || "page-home";
    const el = document.getElementById(id);
    if (el) el.classList.add("is-active");
    window.scrollTo({{ top: 0, behavior: "instant" in window ? "instant" : "auto" }});
    if (route.name === "idea" && route.slug) renderIdeaDetail(route.slug);
    if (route.name === "verify") renderVerify();
  }}

  let verifyStep = 0;
  function renderVerify() {{
    const root = document.getElementById("verify-ui");
    if (!root) return;
    const tr = t();
    const steps = [getPath(tr, "verify.step1"), getPath(tr, "verify.step2"), getPath(tr, "verify.step3")];
    const verified = isVerified();
    const bars = steps.map((_, i) => `<div style="flex:1;height:4px;border-radius:999px;background:${{i <= verifyStep ? "var(--lime)" : "rgba(255,255,255,0.1)"}}"></div>`).join("");
    root.innerHTML = `
      <div style="display:flex;gap:0.5rem">${{bars}}</div>
      <div class="card" style="margin-top:1rem">
        <p style="font-weight:500">${{escapeHtml(steps[verifyStep])}}</p>
        <label class="muted" style="margin-top:1rem;display:flex;flex-direction:column;align-items:center;justify-content:center;border:1px dashed rgba(255,255,255,0.2);border-radius:1rem;padding:2.5rem;cursor:pointer">
          <input type="file" hidden accept="image/*,.pdf" />
          ${{escapeHtml(getPath(tr, "verify.upload"))}}
        </label>
        <div style="display:flex;gap:0.75rem;margin-top:1rem;flex-wrap:wrap">
          ${{verifyStep > 0 ? `<button type="button" class="btn-ghost" id="v-back" style="display:inline-block">${{escapeHtml(getPath(tr, "verify.back"))}}</button>` : ""}}
          <button type="button" class="btn-lime" id="v-next">${{escapeHtml(verifyStep < steps.length - 1 ? getPath(tr, "verify.continue") : getPath(tr, "verify.complete"))}}</button>
        </div>
      </div>
      <div class="card" style="margin-top:1rem">
        <p class="muted">${{escapeHtml(verified ? getPath(tr, "verify.statusOk") : getPath(tr, "verify.statusPending"))}}</p>
        ${{verified ? "" : `<button type="button" class="eyebrow" id="v-skip" style="margin-top:0.75rem;border:none;background:none;cursor:pointer;color:var(--lime)">${{escapeHtml(getPath(tr, "verify.complete"))}}</button>`}}
      </div>
      <a href="#dashboard" data-nav class="eyebrow" style="text-align:center;color:#fff">${{escapeHtml(getPath(tr, "dashboard.title"))}} →</a>
    `;
    const back = document.getElementById("v-back");
    if (back) back.onclick = () => {{ verifyStep = Math.max(0, verifyStep - 1); renderVerify(); }};
    const next = document.getElementById("v-next");
    if (next)
      next.onclick = () => {{
        if (verifyStep < steps.length - 1) verifyStep++;
        else setDemoVerified();
        renderVerify();
        applyI18n();
      }};
    const skip = document.getElementById("v-skip");
    if (skip)
      skip.onclick = () => {{
        setDemoVerified();
        renderVerify();
        applyI18n();
      }};
  }}

  document.addEventListener("click", (e) => {{
    const a = e.target.closest("a[data-nav]");
    if (!a) return;
    const href = a.getAttribute("href");
    if (href && href.startsWith("#")) {{
      e.preventDefault();
      location.hash = href.slice(1);
    }}
  }});

  document.getElementById("lang-select").addEventListener("change", (e) => {{
    lang = e.target.value;
    try {{
      localStorage.setItem(LS_LANG, lang);
    }} catch (err) {{}}
    verifyStep = 0;
    applyI18n();
    showPage();
  }});

  document.getElementById("bill-monthly").addEventListener("click", () => {{
    billingAnnual = false;
    applyI18n();
  }});
  document.getElementById("bill-annual").addEventListener("click", () => {{
    billingAnnual = true;
    applyI18n();
  }});

  document.getElementById("reg-form").addEventListener("submit", (e) => {{
    e.preventDefault();
    location.hash = "verify";
  }});

  window.addEventListener("hashchange", () => {{
    parseHash();
    applyI18n();
    showPage();
  }});

  parseHash();
  applyI18n();
  showPage();
}})();
  </script>
</body>
</html>"""

    (root / "index.html").write_text(html, encoding="utf-8")
    print("Wrote", root / "index.html")


if __name__ == "__main__":
    main()
