# Regenerates every page from this one file: python3 build.py .
# You can also just edit the .html files directly.
import sys, pathlib
out = pathlib.Path(sys.argv[1])

# Replace with your real Calendly link.
CALENDLY = "https://calendly.com/your-calendly-name"
BOOK = f'href="{CALENDLY}" target="_blank" rel="noopener"'

LOGO = '''<svg viewBox="0 0 200 200" role="img" aria-label="Theofania" fill="none" stroke="#7a3f2c" stroke-width="3" stroke-linecap="round">
  <line x1="100" y1="6" x2="100" y2="194"/>
  <path d="M100 30 A70 70 0 1 1 30 100 L12 100"/>
  <path d="M100 54 A46 46 0 1 0 146 100"/>
  <path d="M100 78 A22 22 0 1 1 78 100"/>
  <circle cx="100" cy="100" r="6" fill="#7a3f2c" stroke="none"/>
  <text x="106" y="186" fill="#9a958c" stroke="none" font-family="Figtree, sans-serif" font-size="13">theofania</text>
</svg>'''

NAV = [("index.html","Home"),("qhht.html","QHHT"),("bqh.html","BQH"),("about.html","About"),("contact.html","Contact"),("faq.html","FAQ")]

def page(fname, title, desc, body):
    links = "\n".join(
        f'        <li><a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a></li>' for h,t in NAV)
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="index.html" aria-label="Theofania home">
        {LOGO}
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu"><span></span><span></span><span></span></button>
      <nav class="nav" id="site-nav" aria-label="Main">
        <ul>
{links}
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="wrap">
      {LOGO}
      <p>&copy; 2026 Theofania. All rights reserved.</p>
      <nav aria-label="Legal"><a href="impressum.html">Impressum</a> <a href="privacy.html">Privacy</a></nav>
    </div>
  </footer>

  <script>
    var t = document.querySelector('.nav-toggle'), n = document.getElementById('site-nav');
    t.addEventListener('click', function () {{
      var open = n.classList.toggle('open');
      t.setAttribute('aria-expanded', open);
    }});
  </script>
</body>
</html>
'''
    (out / fname).write_text(html)

PLR = '''        <p>I offer Past Life Regression sessions in the QHHT and BQH methodologies, both based on Dolores Cannon's work.</p>
        <p>During a Past Life Regression, you relive one or multiple past lives. Your Higher Self guides the experience, determining which past life is most beneficial for your current circumstances. This ensures your safety and ensures that you relive a past life that offers insight and growth.</p>
        <p>The insights gained from a past life regression offer profound understanding of your present life circumstances. You will gain valuable lessons from past experiences and have the opportunity to clear and release karmic patterns that no longer serve you.</p>
        <p>We also establish a direct connection with your Higher Self, allowing for direct communication. This enables us to explore your big-life-questions together. Your Higher Self, prioritizing your purpose and well-being, provides invaluable and transformative information.</p>'''

FAQS = [
 ("What does a session feel like?", "Past life regression session feels like a very deep, guided meditation or a vivid daydream. You remain in control and aware, but your conscious mind steps back to allow your inner history to surface gracefully."),
 ("How many sessions will I need?", "Most people achieve significant breakthroughs after one meeting. By bridging the gap with your higher self, we ensure every detail serves your current path and your deeper spiritual development."),
]
FAQS_MORE = [
 ("What is the difference between QHHT and BQH?", "Both are based on Dolores Cannon's work. QHHT follows a structured method and takes place in person. BQH is more free form, can include intuitive or psychic insights, and is available in person and online."),
 ("Can I do a session online?", "BQH sessions and Readings &amp; Consultations are available online. QHHT is only available in person in Berlin."),
 ("How do I prepare?", '<span class="todo">Add your preparation notes here, for example writing down your questions beforehand and leaving the rest of the day free.</span>'),
 ("How long does a session take and what does it cost?", '<span class="todo">Add session length and prices here.</span>'),
]

CARDS = [
 ("qhht", "QHHT", "qhht.html", '''<p>QHHT (Quantum Healing Hypnosis Technique) is a technique developed by Dolores Cannon that allows for deep, structured regression to one or more past lives.</p>
            <p>As part of the session, you'll also have the opportunity to connect with your Higher Self and ask any questions you may have.</p>
            <p>Only available <strong>in person.</strong></p>'''),
 ("bqh", "BQH", "bqh.html", '''<p>BQH (Beyond Quantum Healing) can be conceived as a more 'free form' technique to access past or alternate realities and guidance from your Higher Self or other guides.</p>
            <p>It also involves hypnosis and it allows for the mix of other modalities, e.g. intuitive or psychic insights.</p>
            <p>Available <strong>in person and online.</strong></p>'''),
 ("readings", "Readings &amp; Consultations", "readings.html", '''<p>As a trained psychic, I offer intuitive readings and consultations.</p>
            <p>I'm passionate about bringing people in touch with their own inner guidance and deinstitutionalizing spirituality. I'll always ask for insight to help you develop your own gifts and abilities.</p>
            <p>Available <strong>in person and online.</strong></p>'''),
]

def faq_details(items):
    return "\n".join(f'''        <details class="faq">
          <summary>{q}</summary>
          <p>{a}</p>
        </details>''' for q,a in items)

# ---------- Home ----------
cards = "\n".join(f'''          <article class="card">
            <img src="assets/img/{img}.jpg" alt="" loading="lazy" width="620" height="349">
            <h3>{t}</h3>
            <div class="body">
            {b}
            </div>
            <a class="btn" href="{h}">Learn More &amp; Book</a>
          </article>''' for img,t,h,b in CARDS)

faq_home = "\n".join(f'''        <div>
          <h3>{q}</h3>
          <p>{a}</p>
        </div>''' for q,a in FAQS)

page("index.html", "Theofania · Past Life Regression in Berlin and Online",
 "QHHT and BQH past life regression sessions and psychic readings in Berlin and online.", f'''    <section class="hero">
      <div class="wrap">
        <div class="hero-text">
          <h1>Wondering who you were in a past life? What your life purpose is?</h1>
          <p>Find out with a past life regression session in Berlin and online.</p>
          <p>Go deeper into yourself and relaxation to connect with your higher wisdom. You have all the answers you need.</p>
          <a class="btn" {BOOK}>Book Your Journey</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <h2>What is a Past Life Regression?</h2>
        <div>
{PLR}
        </div>
      </div>
    </section>

    <section class="section section-linen" aria-label="Services">
      <div class="wrap">
        <div class="cards">
{cards}
        </div>
      </div>
    </section>

    <section class="section section-linen center">
      <div class="wrap">
        <h2>Testimonials</h2>
        <div class="quotes">
          <!-- Replace these with real client quotes (with their permission) before launch. -->
          <figure class="quote">
            <blockquote>"My past life regression with Fani was deeply healing. I finally understood the root of a lifelong pattern and felt so safe throughout the entire process."</blockquote>
            <figcaption>Sarah M., Berlin</figcaption>
          </figure>
          <figure class="quote">
            <blockquote>"The psychic reading provided such clarity during a transition period. Fani has a gift for connecting with higher wisdom in the most grounded way."</blockquote>
            <figcaption>Marc L., London</figcaption>
          </figure>
          <figure class="quote">
            <blockquote>"A transformative experience. I walked in a skeptic and left with a profound sense of peace and a clearer understanding of my soul's journey."</blockquote>
            <figcaption>Elena R., Online</figcaption>
          </figure>
        </div>
        <a class="btn" {BOOK}>Book Your Journey</a>
      </div>
    </section>

    <section class="section section-linen center">
      <div class="wrap">
        <img class="moon" src="assets/img/moon.png" alt="" width="186" height="230">
        <h2>Frequently Asked Questions</h2>
        <div class="faq-grid">
{faq_home}
        </div>
        <p style="margin-top:56px"><a class="btn btn-ghost" href="faq.html">More questions</a></p>
      </div>
    </section>
''')

def service(fname, title, eyebrow, h1, lead, img, sections, where):
    page(fname, f"{title} · Theofania", lead, f'''    <section class="page-hero">
      <div class="wrap">
        <span class="eyebrow">{eyebrow}</span>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
        <a class="btn" {BOOK}>Book a session</a>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <img src="assets/img/{img}.jpg" alt="" width="620" height="349">
        <div class="prose">
{sections}
        </div>
      </div>
    </section>

    <section class="section section-linen center">
      <div class="wrap">
        <h2>{where}</h2>
        <p><a class="btn" {BOOK}>Book Your Journey</a></p>
      </div>
    </section>
''')

service("qhht.html", "QHHT", "Quantum Healing Hypnosis Technique", "QHHT",
 "A deep, structured regression to one or more past lives, developed by Dolores Cannon.", "qhht", '''          <h2>What is QHHT?</h2>
          <p>QHHT (Quantum Healing Hypnosis Technique) is a technique developed by Dolores Cannon that allows for deep, structured regression to one or more past lives.</p>
          <p>As part of the session, you'll also have the opportunity to connect with your Higher Self and ask any questions you may have.</p>
          <h2>How a session works</h2>
          <p>We begin with a conversation about your life and the questions you bring. You are then guided into a deeply relaxed state, where your Higher Self chooses the past life or lives that are most helpful for you now. Afterwards, we speak with your Higher Self directly about your questions.</p>
          <p class="todo">Add session length, price and any preparation notes here.</p>''',
 "QHHT is only available in person in Berlin.")

service("bqh.html", "BQH", "Beyond Quantum Healing", "BQH",
 "A more free form approach to past and alternate realities, with guidance from your Higher Self or other guides.", "bqh", '''          <h2>What is BQH?</h2>
          <p>BQH (Beyond Quantum Healing) can be conceived as a more 'free form' technique to access past or alternate realities and guidance from your Higher Self or other guides.</p>
          <p>It also involves hypnosis and it allows for the mix of other modalities, e.g. intuitive or psychic insights.</p>
          <h2>How a session works</h2>
          <p>Like QHHT, a BQH session begins with a conversation about what you would like to explore, followed by a guided hypnosis. Because the method is more open, the session can follow wherever your guidance leads.</p>
          <p class="todo">Add session length, price and any preparation notes here.</p>''',
 "BQH is available in person in Berlin and online.")

service("readings.html", "Readings &amp; Consultations", "Psychic readings", "Readings &amp; Consultations",
 "Intuitive readings and consultations to help you reconnect with your own inner guidance.", "readings", '''          <h2>What to expect</h2>
          <p>As a trained psychic, I offer intuitive readings and consultations.</p>
          <p>I'm passionate about bringing people in touch with their own inner guidance and deinstitutionalizing spirituality. I'll always ask for insight to help you develop your own gifts and abilities.</p>
          <p class="todo">Add session length, price and format (video call, phone, in person) here.</p>''',
 "Readings are available in person in Berlin and online.")

page("about.html", "About · Theofania", "About Fani and Theofania.", '''    <section class="page-hero">
      <div class="wrap">
        <span class="eyebrow">About</span>
        <h1>Hi, I'm Fani.</h1>
        <p class="lead">I guide past life regressions in the QHHT and BQH methods and offer intuitive readings, in Berlin and online.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap prose">
        <p>I'm passionate about bringing people in touch with their own inner guidance and deinstitutionalizing spirituality. In every session, my aim is to help you connect with your higher wisdom, because you have all the answers you need.</p>
        <p class="todo">Tell your story here: how you came to this work, your training in QHHT and BQH, and what a session with you is like. A photo of you would sit well at the top of this section.</p>
        <p><a class="btn" href="contact.html">Get in touch</a></p>
      </div>
    </section>
''')

page("contact.html", "Contact · Theofania", "Book a session or get in touch with Theofania.", f'''    <section class="page-hero">
      <div class="wrap">
        <span class="eyebrow">Contact</span>
        <h1>Book Your Journey</h1>
        <p class="lead">Write to me with the session you're interested in and any questions. I'll get back to you to find a time that suits you.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap contact-grid">
        <div>
          <ul class="contact-list">
            <li><strong>Email</strong><a class="todo" href="mailto:hello@example.com">hello@example.com</a></li>
            <li><strong>Location</strong>Berlin, and online worldwide</li>
            <li><strong>Sessions</strong><a href="qhht.html">QHHT</a> (in person) &middot; <a href="bqh.html">BQH</a> &middot; <a href="readings.html">Readings &amp; Consultations</a></li>
          </ul>
        </div>
        <div class="prose">
          <h2>Online booking</h2>
          <p>Pick a time that suits you in my booking calendar. You'll get a confirmation by email straight away.</p>
          <p><a class="btn" {BOOK}>Book on Calendly</a></p>
        </div>
      </div>
    </section>
''')

page("faq.html", "FAQ · Theofania", "Frequently asked questions about past life regression, QHHT, BQH and readings.", f'''    <section class="page-hero">
      <div class="wrap">
        <span class="eyebrow">FAQ</span>
        <h1>Frequently Asked Questions</h1>
      </div>
    </section>

    <section class="section">
      <div class="wrap prose">
{faq_details(FAQS + FAQS_MORE)}
        <p style="margin-top:48px">Still wondering about something? <a href="contact.html">Get in touch.</a></p>
      </div>
    </section>
''')

page("impressum.html", "Impressum · Theofania", "Impressum", '''    <section class="section">
      <div class="wrap prose">
        <h1>Impressum</h1>
        <p class="todo">German law (§ 5 DDG) requires a business website to name its operator. Fill in your full name, a postal address where you can be reached, your email, and your tax ID if you have one.</p>
      </div>
    </section>
''')

page("privacy.html", "Privacy · Theofania", "Privacy policy", '''    <section class="section">
      <div class="wrap prose">
        <h1>Privacy Policy</h1>
        <p>This website does not use cookies, analytics or tracking. Fonts and images are served from this site itself, so no data is sent to third parties when you visit.</p>
        <p class="todo">Add a full Datenschutzerkl&auml;rung here (who is responsible, the hosting provider, and that bookings are handled by Calendly). Free generators such as the one from e-recht24 can produce it.</p>
      </div>
    </section>
''')

(out / "assets/img/favicon.svg").write_text(LOGO.replace('role="img" aria-label="Theofania" ', 'xmlns="http://www.w3.org/2000/svg" ').replace('stroke-width="3"', 'stroke-width="8"').split('<text')[0] + '</svg>')
print("built")
