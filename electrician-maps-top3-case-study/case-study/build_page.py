#!/usr/bin/env python3
"""Electrician Maps Top 3 — case study page.
Same family as the Honest Local SEO case study. Video ID is a placeholder
(YOUTUBE_VIDEO_ID) until the video is published — then swap + zip.
RULES (user-locked 2026-10-20):
- article text written FRESH. No slide copy-paste. No slide PNGs reused.
- section figures = the 7 AI-generated study visuals only.
- NO meta-talk: no mention of transcripts, source material, or the working process.
- fancy text animation: gold underline draw on headings, word-stagger lead,
  kicker shimmer, figure zoom on reveal, step-number pop.
"""
import os, glob, shutil

BASE = os.path.expanduser("~/workspace/goals/electrician-maps-top3-video/files")
TG = os.path.expanduser("~/workspace/goals/local-seo-video/files/case-study/index.html")
OUT = os.path.join(BASE, "case-study")
IMG = os.path.join(OUT, "images")
VID = "isf7tTfh1Tw"

EXTRA_CSS = """
  .timeline{width:100%;border-collapse:collapse;margin:1.6rem 0 2.4rem;font-size:1.1rem}
  .timeline th{text-align:left;padding:.9rem 1.1rem;color:var(--gold);border-bottom:2px solid var(--line);font-size:.95rem;letter-spacing:.12em}
  .timeline td{padding:.9rem 1.1rem;border-bottom:1px solid var(--line);color:var(--ink)}
  .timeline td:first-child{white-space:nowrap;font-weight:700;color:var(--gold)}
  .timeline tr:last-child td{border-bottom:none}
  /* ---- fancy text animation pack ---- */
  h2.sec{position:relative;padding-bottom:.6rem}
  h2.sec::after{content:"";position:absolute;left:0;bottom:0;height:3px;width:0;
    background:linear-gradient(90deg,var(--gold),rgba(245,185,66,.15));
    border-radius:2px;transition:width 1s ease .25s}
  h2.sec.in::after{width:88px}
  h2.sec .n{display:inline-block;transform:scale(.6);opacity:0;
    transition:transform .55s cubic-bezier(.2,1.7,.4,1) .15s,opacity .4s ease .15s}
  h2.sec.in .n{transform:scale(1);opacity:1}
  .kicker{position:relative;overflow:hidden}
  .kicker::before{content:"";position:absolute;top:0;left:-80%;width:60%;height:100%;
    background:linear-gradient(105deg,transparent,rgba(245,185,66,.35),transparent);
    animation:sheen 3.2s ease-in-out infinite}
  @keyframes sheen{0%{left:-80%}55%,100%{left:130%}}
  figure.diagram img{transform:scale(1.07);transition:transform 1.5s cubic-bezier(.2,.7,.2,1)}
  figure.diagram.in img{transform:scale(1)}
  figure.diagram figcaption{opacity:0;transform:translateX(-14px);
    transition:opacity .6s ease .35s,transform .6s ease .35s}
  figure.diagram.in figcaption{opacity:1;transform:none}
  .lead .w{display:inline-block;opacity:0;transform:translateY(10px);
    transition:opacity .45s ease,transform .45s ease}
  .lead.in .w{opacity:1;transform:none}
  .takeaway{border-left:4px solid var(--gold);background:rgba(245,185,66,.07);
    padding:1.1rem 1.4rem;border-radius:0 12px 12px 0;margin:1.8rem 0;font-size:1.12rem}
"""

EXTRA_JS = """
  // word-stagger on the lead paragraph
  document.querySelectorAll('.lead').forEach(function(p){
    var words = p.textContent.trim().split(/\\s+/);
    p.innerHTML = words.map(function(w,i){
      return '<span class="w" style="transition-delay:'+(i*28)+'ms">'+w+'</span>';
    }).join(' ');
  });
"""

def build():
    os.makedirs(IMG, exist_ok=True)
    tg = open(TG).read()

    head = tg[:tg.index("</style>") + len("</style>")] + "\n</head>"
    head = head.replace("</style>", EXTRA_CSS + "</style>")
    head = head.replace("<title>Honest Local SEO Playbook — Case Study</title>",
                        "<title>Electrician Maps Top 3 — Case Study</title>")
    head = head.replace(
        '<meta name="description" content="How a garage door client hit the top three in Google Maps in 60 days — the full local SEO roadmap. No hype. No stopwatch.">',
        '<meta name="description" content="An electrician\'s Google Maps profile is live but stuck. Seven steps, in order, to move it into the top three — no ads, no tricks, no timeline promises.">')
    head = head.replace(
        '<meta property="og:title" content="Honest Local SEO Playbook.">',
        '<meta property="og:title" content="Electrician Maps Top 3.">')
    head = head.replace(
        '<meta property="og:description" content="Top three in Google Maps in 60 days. The full local SEO roadmap — profile, reviews, website, listings, and 60 days of real posting.">',
        '<meta property="og:description" content="Seven steps in order for an electrician stuck on Google Maps — address, real name, citations, profile, website match, reviews, one story everywhere.">')
    head = head.replace(
        '<meta property="og:url" content="https://imamul-localads.github.io/portfolio/honest-local-seo-case-study/">',
        '<meta property="og:url" content="https://imamul-localads.github.io/portfolio/electrician-maps-top3-case-study/">')
    head = head.replace(
        '<meta name="twitter:title" content="Honest Local SEO Playbook.">',
        '<meta name="twitter:title" content="Electrician Maps Top 3.">')

    tail = tg[tg.index("<script>"):]
    tail = tail.replace("</script>", EXTRA_JS + "\n</script>", 1)

    body = f"""
<body>
<div class="progress" id="progress"></div>

<header class="hero">
  <div class="wrap">
    <span class="kicker">CASE STUDY</span>
    <h1>Electrician Maps <span class="hl">Top 3.</span></h1>
    <p class="deck">The profile is live. It's visible. And it's stuck — sitting at number six while the top three take the calls. These are the <strong>seven steps that move it up, in the order I'd do them</strong>. No ads. No tricks. No timeline promises.</p>
    <div class="meta">
      <span>&#x1F4F9; Companion video</span><span>&#x23F1; 7 min read</span><span>&#x1F9EE; Practitioner framework</span>
    </div>
  </div>
  <div class="scroll-hint">SCROLL</div>
</header>

<section class="video-sec">
  <div class="wrap">
    <div class="video-embed">
      <!-- REPLACE YOUTUBE_VIDEO_ID with the published video ID before zipping -->
      <iframe src="https://www.youtube.com/embed/{VID}" title="How an Electrician Gets to Top 3 on Google Maps (7 Steps, No Ads)"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen loading="lazy"></iframe>
    </div>
  </div>
</section>

<article>
<div class="wrap">

<p class="lead reveal">The last video was about starting from zero. This one is the opposite problem. Your Google Maps profile exists, customers can find it, and it still doesn't ring. You are not invisible. You are just not in the top three. And on Google Maps, everything below the top three might as well be page two.</p>

<h2 class="sec reveal"><span class="n">1</span>Put your address where the work is</h2>
<figure class="diagram reveal">
  <img src="images/fig-01-proximity.png" alt="Stylized map with a gold pin and service-area radius: Google ranks by where you are">
  <figcaption>Google ranks by where you are — not where you wish you were.</figcaption>
</figure>
<p class="reveal">Google Maps ranking starts with something you can't out-optimize: distance. When someone searches "electrician near me," Google weighs how close your address is to the searcher. That's not a trick you can hack. It's physics.</p>
<p class="reveal">So the first step is honest placement. Your address should sit inside the city you actually want to win — not a P.O. box, not a virtual office, not a home address forty minutes outside town. And if you do both residential and commercial work, pick a base that doesn't box you out of half your market. Every step after this one multiplies an address that's in the right place — or fights an address that isn't.</p>

<h2 class="sec reveal"><span class="n">2</span>Use your real name. No games.</h2>
<figure class="diagram reveal">
  <img src="images/fig-02-name.png" alt="Clean business card with a checkmark next to a keyword-stuffed card with a red X">
  <figcaption>The honest step: your real name, nothing added.</figcaption>
</figure>
<p class="reveal">This is the step where most electricians get tempted — and where this framework draws its line. You'll see competitors with names like "Best Electrician Dallas 24/7 Cheap." It looks like free keywords. It's actually against Google's rules: your profile name has to match your real-world business name, the one on your signage, your website, your invoices. Adding services or city names you don't legally own breaks the guideline.</p>
<p class="reveal">And Google enforces it. A stuffed name can get edited by Google, reported by a competitor, and repeat violations can get the whole profile suspended. That's not a scare tactic — it's the written policy. So step two is simple and non-negotiable: your real legal name, nothing added. Every competitor gaming this step is one report away from disappearing. You won't be.</p>
<div class="takeaway reveal"><strong>The rule:</strong> if it's not on your truck, it doesn't go in your profile name.</div>

<h2 class="sec reveal"><span class="n">3</span>Get listed where it counts — for free</h2>
<figure class="diagram reveal">
  <img src="images/fig-03-citations.png" alt="Directory listing cards with matching name, address and phone connected by gold lines">
  <figcaption>A few trusted directories, all matching. That's the whole job.</figcaption>
</figure>
<p class="reveal">Citations are other websites confirming you exist: your name, address, and phone number listed on directories Google already trusts. Yelp, Nextdoor, Angi, the Better Business Bureau. These listings are free — the platforms will try to sell you ads and upgrades on the way in, and you can walk straight past all of it. If it's free, take it. Paid upgrades are optional, never required.</p>
<p class="reveal">And that's the entire job. A handful of trusted directories with identical information beats a pile of obscure ones every time. Blasting your business onto two hundred junk directories is a leftover tactic from a decade ago — it doesn't move the needle, and messy inconsistent data across low-quality sites can do more harm than good. Match the big ones. Skip the rest.</p>

<h2 class="sec reveal"><span class="n">4</span>Fill out the profile completely</h2>
<figure class="diagram reveal">
  <img src="images/fig-04-profile.png" alt="Profile completeness ring nearly full with checklist items around it">
  <figcaption>Categories first. Then every field like you mean it.</figcaption>
</figure>
<p class="reveal">Categories come first, because the primary category is one of the strongest signals telling Google what kind of business you are. Pick the one that describes your main work most precisely — then add secondary categories only for services you genuinely offer. Don't dilute it with things you did once two years ago.</p>
<p class="reveal">Then fill out everything else like you mean it: every service with a real description, full hours including holidays, photos of actual work — not stock photos — and a complete business description. Every blank field is a field a competitor has filled. A half-empty profile tells Google, and the customer reading it, that the business might not be serious.</p>

<h2 class="sec reveal"><span class="n">5</span>Make your website say the same thing</h2>
<figure class="diagram reveal">
  <img src="images/fig-05-match.png" alt="Two browser windows, map profile and website, connected by a gold arrow with a checkmark">
  <figcaption>Same service, same city, in both places. One identity.</figcaption>
</figure>
<p class="reveal">This is the quiet killer. The profile says "electrician" and targets one city, but the website's homepage talks about general contracting across three counties. Google looks at both, can't tell what the business is actually best at — and ranks it for nothing.</p>
<p class="reveal">The fix is boring and it works: pick your main service and your main area, and say it the same way in both places. Your homepage represents your whole business, so it should clearly match your primary Google category. One identity, everywhere. When the profile and the website agree, Google stops guessing.</p>

<h2 class="sec reveal"><span class="n">6</span>Reviews decide everything</h2>
<figure class="diagram reveal">
  <img src="images/fig-06-reviews.png" alt="Five gold stars above customer review cards">
  <figcaption>Reviews with real service words in the text. Then never stop.</figcaption>
</figure>
<p class="reveal">If you only do one step properly, make it this one. Reviews are the heaviest weight in the top-three fight — and not just the star count. When a customer writes "rewired our whole panel in a day," those exact service words sit on your profile where Google and your next customer both read them. That's relevance you can't buy.</p>
<p class="reveal">So ask for them. After every finished job, send the direct review link while the customer is still happy. Reply to every review that lands — the next customer reads your replies before they ever call. And here's the part people treat as a project when it's actually a habit: the stream never stops. A profile gaining reviews every month looks alive. One frozen at the same number for a year looks abandoned. Keep the pace human and steady, and never let it go quiet.</p>
<div class="takeaway reveal"><strong>The rule:</strong> real customers, service words in the text, reply to all of them — every month, forever.</div>

<h2 class="sec reveal"><span class="n">7</span>Tell one story everywhere</h2>
<figure class="diagram reveal">
  <img src="images/fig-07-ai.png" alt="AI chat bubble connected to website, map pin and social nodes by gold lines">
  <figcaption>AI reads the same web your customers read. Give it one story.</figcaption>
</figure>
<p class="reveal">Here's the step most people miss: customers aren't the only ones reading your profile anymore. AI assistants answer "who's a good electrician near me" by pulling from the same web — your website, your profile, your reviews, your posts. If those sources tell five different stories, the AI can't recommend you with confidence. If they all say the same thing, you become the easy answer.</p>
<p class="reveal">So keep the story consistent everywhere: same name, same services, same city — on your site, your profile, your directory listings. And use the free tools Google gives you: posts about recent jobs, and FAQs that answer the questions customers actually ask. They're fresh signals attached directly to your profile, and they feed both the map ranking and the AI answers. One story, everywhere, kept current.</p>

<h2 class="sec reveal">The checklist, in order</h2>
<table class="timeline reveal">
  <tr><th>STEP</th><th>DO THIS</th><th>THE HONEST CHECK</th></tr>
  <tr><td>1</td><td>Address inside your target city</td><td>No P.O. boxes, no virtual offices</td></tr>
  <tr><td>2</td><td>Real legal business name</td><td>Nothing added — stuffing risks suspension</td></tr>
  <tr><td>3</td><td>Free listings: Yelp, Nextdoor, Angi, BBB</td><td>Take the free listing, skip the upsell</td></tr>
  <tr><td>4</td><td>Complete profile, categories first</td><td>Every field filled like you mean it</td></tr>
  <tr><td>5</td><td>Website matches the profile</td><td>Same service, same city, both places</td></tr>
  <tr><td>6</td><td>Review stream with service words</td><td>Real customers, reply to all, never stop</td></tr>
  <tr><td>7</td><td>One consistent story + posts &amp; FAQs</td><td>AI reads the same web — feed it well</td></tr>
</table>
<div class="rule reveal"><p><span class="r1">No timeline promises.</span><span class="r2">No tricks.</span><span class="r3">Find the hole. Fix the hole. Then grow.</span></p></div>

<h2 class="sec reveal">Sources</h2>
<p class="reveal" style="font-size:1.05rem">Every research claim in this video comes from a named source:</p>
<ul class="reveal" style="font-size:1.05rem;line-height:2">
<li><strong><a href="https://www.searchenginejournal.com/ranking-factors/relevance-distance-prominence/" target="_blank" rel="noopener">Search Engine Journal — Google's local ranking factors</a></strong> — local results are based primarily on relevance, distance, and prominence; more reviews and positive ratings can improve local ranking.</li>
<li><strong><a href="https://www.webmarketingacademy.in/digital-marketing-blogs/google-business-profile-optimization-for-service-businesses-a-practical-guide/" target="_blank" rel="noopener">Web Marketing Academy — Google Business Profile optimization guide</a></strong> — the profile name must match the real-world business name; adding services or locations breaks the rules, and Google can edit a stuffed name or suspend repeat violators. The primary category is one of the strongest relevance signals.</li>
<li><strong><a href="https://hypetrix.com/resources/google-business-profile-checklist/" target="_blank" rel="noopener">Hypetrix — Google Business Profile checklist (2026)</a></strong> — business name must match signage, website, and invoices; keyword-stuffed names break guidelines and get profiles suspended or reported by competitors.</li>
<li><strong><a href="https://blog.zinggrow.com/2024/05/24/google-business-profile-business-name-guidelines/" target="_blank" rel="noopener">ZingGrow — Google Business Profile naming rules</a></strong> — no keywords or location descriptors in the business name unless they're part of the registered name.</li>
</ul>

<h2 class="sec reveal">A note on what's real</h2>
<p class="reveal" style="font-size:1.05rem;color:var(--muted)">This is a practitioner framework — the seven steps in the order I'd actually do them for an electrician's profile that's already live but stuck. What's hype-free here by design: no ranking-time guarantees (rankings are earned, not scheduled), no keyword-stuffed business names (against Google's rules, and the suspension risk is real), no bulk-citation blasts, no tricks. The directories named here all offer genuinely free listings — paid upgrades are optional, never required. And reviews aren't a one-time project: the stream never stops, because that's what keeps the profile alive.</p>

</div>
</article>

<section class="social-sec">
<div class="wrap">
  <h3 class="reveal">&#x1F4F2; Let's connect</h3>
  <p class="reveal">Follow for more breakdowns on ads, tracking, and getting customers — not just leads.</p>
  <div class="socials">
    <a class="soc yt reveal" href="https://www.youtube.com/watch?v={VID}" target="_blank" rel="noopener">
      <div class="sic"><svg viewBox="0 0 24 24"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4L15.8 12l-6.2 3.6z"/></svg></div>
      <h4>YouTube</h4><p>Watch the full video</p>
    </a>
    <a class="soc li reveal" href="https://www.linkedin.com/in/imamul-hassan-26a21a435/" target="_blank" rel="noopener">
      <div class="sic"><svg viewBox="0 0 24 24"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z"/></svg></div>
      <h4>Facebook</h4><p>Follow the page</p>
    </a>
  </div>
</div>
</section>

<footer>
  <div class="wrap">
    <p>Case study companion to the video "How an Electrician Gets to Top 3 on Google Maps (7 Steps, No Ads)."<br>A practitioner framework — seven steps, in order, for a profile that's live but stuck. No timeline promises, no tricks.</p>
    <p style="margin-top:1.2rem">
      <a href="https://www.linkedin.com/in/imamul-hassan-26a21a435/" target="_blank" rel="noopener" style="color:var(--gold);text-decoration:none;margin:0 .8rem">LinkedIn</a>&middot;<a href="https://www.facebook.com/profile.php?id=61572277707806" target="_blank" rel="noopener" style="color:var(--gold);text-decoration:none;margin:0 .8rem">Facebook</a>&middot;<a href="https://www.youtube.com/watch?v={VID}" target="_blank" rel="noopener" style="color:var(--gold);text-decoration:none;margin:0 .8rem">YouTube</a>
    </p>
  </div>
</footer>
"""

    html = head + body + "\n" + tail
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(html)

    # figures: the 7 generated study visuals, renamed cleanly
    names = ["fig-01-proximity", "fig-02-name", "fig-03-citations", "fig-04-profile",
             "fig-05-match", "fig-06-reviews", "fig-07-ai"]
    for i, n in enumerate(names, 1):
        src = glob.glob(os.path.join(BASE, "case-study", "images",
                                     f"media-generation-visual-step{i}-*.png"))
        assert src, f"missing visual for step {i}"
        shutil.copy(src[0], os.path.join(IMG, f"{n}.png"))
    print(f"built {os.path.join(OUT, 'index.html')} with {len(names)} generated figures")
    print("video ID placeholder: YOUTUBE_VIDEO_ID (swap after publish, then zip)")

if __name__ == "__main__":
    build()
