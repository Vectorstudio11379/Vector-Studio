"""Build the Vector Studioz legal pages: privacy-policy.html, tos.html, cookies.html.

Reuses the shared head, header and footer from about.html so the pages match
the rest of the site, then drops in the legal content defined below.
After building, run tools/seo_normalize.py to refresh the share tags.

Run from the repo root:  python tools/build_legal_pages.py
"""
import html
import json
import re

UPDATED = '7 November 2026'
EMAIL = 'contact@vectorstudioz.com'
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

# ---------------------------------------------------------------- content

PRIVACY = {
    'file': 'privacy-policy.html',
    'title': 'Privacy Policy | Vector Studioz',
    'description': 'How Vector Studioz collects, uses and protects personal data when you visit our website, contact us or work with us on a project.',
    'h1': 'Privacy Policy',
    'lede': 'This policy explains what personal data Vector Studioz collects when you visit vectorstudioz.uk, get in touch or work with us, why we collect it, and the choices and rights you have.',
    'sections': [
        ('who-we-are', 'Who we are', f'''
<p>Vector Studioz (“<strong>Vector Studioz</strong>”, “<strong>we</strong>”, “<strong>us</strong>”) is a digital studio that designs and builds websites, WebGL 3D experiences, mobile apps, custom software and AI automation for clients worldwide.</p>
<p>For the personal data described in this policy, Vector Studioz is the <strong>controller</strong>. You can reach us about anything in this policy at {MAIL}.</p>
<p>When we build or run a product for a client and handle that client’s customer data on their behalf, we act as the client’s <strong>processor</strong>. In that case the client’s own privacy notice applies, and our handling of the data is governed by our contract with them.</p>
'''),
        ('data-we-collect', 'Personal data we collect', '''
<h3>Information you give us</h3>
<ul>
<li><strong>Contact and enquiry details</strong>: your name, email address, company, phone number (if you share it) and the content of your message when you email us, submit a project brief or use the contact form.</li>
<li><strong>Project information</strong>: requirements, budgets, timelines, brand assets, content and account access you share with us so we can quote for or deliver a project.</li>
<li><strong>Business and billing details</strong>: billing contact, company details and payment records needed to invoice you and keep our accounts.</li>
<li><strong>Job applications</strong>: your CV, portfolio, links and any other information you send when applying to work with us.</li>
</ul>
<h3>Information collected automatically</h3>
<ul>
<li><strong>Technical data</strong>: when you load our website, our hosting and security providers receive standard request data such as your IP address, browser type, device type, pages requested, referring page and the date and time of the request. This is used to deliver the site, keep it secure and diagnose faults.</li>
<li><strong>Browser storage</strong>: the site stores a small number of preference and security values in your browser. These are explained in our <a href="cookies.html">Cookie Policy</a>.</li>
</ul>
<p>We do not currently use advertising cookies, cross-site tracking or third-party analytics on vectorstudioz.uk. If we introduce analytics in future, we will update this policy and, where the law requires it, ask for your consent first.</p>
<p>We do not knowingly collect special category data (such as health or religious information). Please do not send it to us.</p>
'''),
        ('how-we-use', 'How we use your data and our legal bases', '''
<p>Under UK and EU data protection law (the UK GDPR, the Data Protection Act 2018 and the EU GDPR) we must have a legal basis for each use of personal data.</p>
<div class="legal-table-wrap"><table class="legal-table">
<thead><tr><th>Purpose</th><th>Data used</th><th>Legal basis</th></tr></thead>
<tbody>
<tr><td>Replying to enquiries and preparing proposals or quotes</td><td>Contact and enquiry details, project information</td><td>Steps at your request before entering a contract; legitimate interests in responding to business enquiries</td></tr>
<tr><td>Delivering, supporting and managing projects</td><td>Contact details, project information</td><td>Performance of our contract with you or your organisation</td></tr>
<tr><td>Invoicing, accounting and tax records</td><td>Business and billing details</td><td>Legal obligation; performance of contract</td></tr>
<tr><td>Running, securing and improving the website</td><td>Technical data, browser storage</td><td>Legitimate interests in operating a secure, working website</td></tr>
<tr><td>Assessing job applications</td><td>Application information</td><td>Steps at your request before entering a contract; legitimate interests in recruiting</td></tr>
<tr><td>Occasional updates about our services to existing clients</td><td>Contact details</td><td>Legitimate interests (you can opt out at any time)</td></tr>
<tr><td>Establishing or defending legal claims</td><td>Any relevant records</td><td>Legitimate interests; legal obligation</td></tr>
</tbody></table></div>
<p>We do not sell your personal data and we do not use it for automated decision-making that has legal or similarly significant effects on you.</p>
'''),
        ('sharing', 'Who we share data with', '''
<p>We share personal data only where needed for the purposes above, with:</p>
<ul>
<li><strong>Service providers</strong> who host and secure our website, store files, provide email and productivity tools, and handle payments and accounting. They act on our instructions and are bound by confidentiality and data protection terms.</li>
<li><strong>Content delivery networks</strong> that serve fonts, scripts, images and video to your browser (for example Google Fonts, jsDelivr, unpkg, Amazon Web Services and the Webflow content network). These providers receive your IP address so they can deliver the file you requested.</li>
<li><strong>Professional advisers</strong> such as accountants, lawyers and insurers, where reasonably necessary.</li>
<li><strong>Authorities</strong> where we are required to by law, or to protect our rights, our clients or others.</li>
<li><strong>A successor business</strong> if Vector Studioz is reorganised, merged or sold, subject to this policy.</li>
</ul>
'''),
        ('transfers', 'International transfers', '''
<p>We work with clients and providers in several countries, so your data may be processed outside the UK or the European Economic Area. Where that happens we rely on an adequacy decision or put appropriate safeguards in place, such as the UK International Data Transfer Agreement or the EU Standard Contractual Clauses. You can ask us for details of the safeguards that apply.</p>
'''),
        ('retention', 'How long we keep data', '''
<ul>
<li><strong>Enquiries that do not become projects</strong>: up to 24 months after our last contact, so we have context if you get back in touch.</li>
<li><strong>Client and project records</strong>: for the length of the engagement and up to 6 years afterwards, to meet accounting, tax and legal requirements.</li>
<li><strong>Job applications</strong>: up to 12 months after the role is filled, unless you ask us to delete them sooner or agree to us keeping them longer.</li>
<li><strong>Server and security logs</strong>: kept by our providers for short periods, typically no longer than 90 days.</li>
</ul>
<p>When data is no longer needed we delete it or anonymise it.</p>
'''),
        ('security', 'How we protect data', '''
<p>We use appropriate technical and organisational measures to protect personal data, including encrypted connections (HTTPS), access controls and two-factor authentication on the tools we use, least-privilege access to client systems, and removing project access when an engagement ends. No method of transmission or storage is completely secure, so we cannot guarantee absolute security, but we will notify you and the relevant regulator of a personal data breach where the law requires it.</p>
'''),
        ('your-rights', 'Your rights', f'''
<p>Depending on where you live, you have the right to:</p>
<ul>
<li>access the personal data we hold about you and receive a copy;</li>
<li>have inaccurate data corrected;</li>
<li>have your data deleted in certain circumstances;</li>
<li>restrict or object to our processing, including objecting at any time to direct marketing;</li>
<li>receive data you provided to us in a portable format;</li>
<li>withdraw consent where we rely on consent, without affecting processing that already happened.</li>
</ul>
<p>To use any of these rights, email {MAIL}. We will respond within one month and may need to confirm your identity first. There is normally no fee.</p>
<p>If you are unhappy with how we handle your data, please tell us so we can try to put it right. You also have the right to complain to a data protection authority. In the UK this is the Information Commissioner’s Office (<a href="https://ico.org.uk/make-a-complaint/" rel="noopener" target="_blank">ico.org.uk</a>); in the EU it is the supervisory authority in your country.</p>
'''),
        ('children', 'Children', '''
<p>Our website and services are intended for businesses and adults. We do not knowingly collect personal data from children under 16. If you believe a child has sent us personal data, contact us and we will delete it.</p>
'''),
        ('third-party-sites', 'Links to other websites', '''
<p>Our site links to client websites, project case studies and other third-party sites. We are not responsible for how those sites handle personal data, so please read their privacy notices.</p>
'''),
        ('changes', 'Changes to this policy', f'''
<p>We may update this policy as our services, tools or legal requirements change. The “Last updated” date at the top shows when it last changed. If a change materially affects how we use your data, we will make that clear on this page and, where appropriate, contact you directly.</p>
<p>Questions about this policy? Email {MAIL}.</p>
'''),
    ],
}

TERMS = {
    'file': 'tos.html',
    'title': 'Terms of Service | Vector Studioz',
    'description': 'The terms that apply when you use the Vector Studioz website or engage Vector Studioz for web design, development, 3D, app, software or AI automation work.',
    'h1': 'Terms of Service',
    'lede': 'These terms govern your use of vectorstudioz.uk and set out the standard terms on which Vector Studioz provides design, development and engineering services.',
    'sections': [
        ('about', 'About these terms', f'''
<p>These terms are between you and Vector Studioz (“<strong>we</strong>”, “<strong>us</strong>”). By using this website you accept the website terms in sections 2 to 4. If you engage us for a project, sections 5 to 14 also apply, together with the proposal, statement of work or quote we agree with you (the “<strong>Proposal</strong>”).</p>
<p>If anything in a signed Proposal conflicts with these terms, the Proposal wins for that project.</p>
<p>Questions about these terms can be sent to {MAIL}.</p>
'''),
        ('website-use', 'Using our website', '''
<p>You may browse the site and share links to it. You must not:</p>
<ul>
<li>use the site in a way that breaks the law or infringes anyone’s rights;</li>
<li>attempt to gain unauthorised access to the site, its servers or any connected systems, or interfere with its operation;</li>
<li>scrape, copy or republish substantial parts of the site, or use it to build a competing product, without our written permission;</li>
<li>introduce malware or send unsolicited marketing through our contact channels.</li>
</ul>
<p>We may change, suspend or withdraw any part of the site at any time. We aim to keep it available and accurate, but it is provided “as is” and we do not promise that it will always be uninterrupted, error-free or up to date.</p>
'''),
        ('site-content', 'Website content and intellectual property', '''
<p>The site’s design, text, graphics, 3D assets, animations, code and our name and logo belong to Vector Studioz or our licensors and are protected by intellectual property laws. Client names, logos and project images shown in our portfolio belong to their respective owners and appear with their permission or as a factual record of our work.</p>
<p>Content on the site is general information about our services. It is not professional advice for your specific situation.</p>
'''),
        ('third-party-links', 'Third-party links', '''
<p>We link to client websites and other third-party sites. We do not control them and are not responsible for their content, availability or privacy practices.</p>
'''),
        ('proposals', 'Proposals and starting a project', '''
<ul>
<li>A Proposal sets out the scope, deliverables, timeline, fees and payment schedule for a project. Unless it says otherwise, a Proposal is valid for 30 days.</li>
<li>A project starts when you accept the Proposal in writing (email is fine) and pay any initial deposit.</li>
<li>Promotional offers shown on the site, such as a discount on a first project sprint, are “up to” amounts applied at our discretion. They apply only to new clients, cannot be combined with other offers and must be confirmed in the Proposal.</li>
</ul>
'''),
        ('responsibilities', 'Your responsibilities', '''
<p>To keep a project on schedule you agree to:</p>
<ul>
<li>provide content, brand assets, feedback, approvals and system access when reasonably requested;</li>
<li>nominate a contact person who can make decisions;</li>
<li>make sure anything you give us (text, images, data, trademarks) is yours to use, or properly licensed, and does not break any law;</li>
<li>keep your own accounts, hosting, domains and third-party subscriptions in good standing unless the Proposal says we will manage them.</li>
</ul>
<p>Delays in feedback or materials may move the timeline, and work that is on hold for more than 30 days may need to be rescheduled.</p>
'''),
        ('changes-to-scope', 'Changes to scope', '''
<p>The Proposal defines what is included. Requests outside it, including extra pages, features, integrations or revision rounds beyond those agreed, are change requests. We will confirm the cost and timing impact in writing before starting any change request.</p>
'''),
        ('fees', 'Fees and payment', '''
<ul>
<li>Fees, currency and the payment schedule are set out in the Proposal. Unless agreed otherwise, we invoice a deposit up front and the balance in stages or on completion.</li>
<li>Invoices are due within 14 days of the invoice date.</li>
<li>If an invoice is overdue we may pause work until it is paid. Under UK law we may also charge statutory interest and compensation on late payments.</li>
<li>Fees exclude third-party costs such as hosting, domains, premium plugins, fonts, stock media and API usage, unless the Proposal includes them.</li>
<li>Deposits cover time reserved and work started, and are non-refundable once work has begun.</li>
</ul>
'''),
        ('ip', 'Ownership of the work', '''
<ul>
<li><strong>Your deliverables</strong>: once you have paid all fees for a project in full, we assign to you the intellectual property in the final deliverables we created specifically for you.</li>
<li><strong>Our tools and know-how</strong>: we keep ownership of our pre-existing materials, frameworks, components, code libraries and general know-how. Where these are built into your deliverables, we grant you a perpetual, non-exclusive, royalty-free licence to use them as part of those deliverables.</li>
<li><strong>Third-party materials</strong>: open-source software, fonts, stock media and other third-party materials remain subject to their own licences, which we will tell you about where relevant.</li>
<li><strong>Portfolio</strong>: unless you ask us not to in writing, we may show the finished work, your name and logo in our portfolio and marketing. We will never publish your confidential information.</li>
</ul>
'''),
        ('confidentiality', 'Confidentiality and data protection', '''
<p>Each of us will keep the other’s confidential information private and use it only for the project, except where disclosure is required by law. Where we process personal data on your behalf, we do so as your processor, only on your documented instructions and with appropriate security, and we will sign a data processing agreement on request. Our <a href="privacy-policy.html">Privacy Policy</a> explains how we handle our own data.</p>
'''),
        ('warranties', 'Acceptance, warranty and support', '''
<ul>
<li>We will carry out our services with reasonable skill and care and in line with good industry practice.</li>
<li>When we deliver a milestone or the final project, you have 10 working days to report any ways it does not match the agreed scope. If you do not report issues in that time, or you put the work into live use, it is treated as accepted.</li>
<li>For 30 days after final delivery we will fix, free of charge, any defects in our work that stop it meeting the agreed scope. This does not cover issues caused by changes made by others, third-party services, hosting environments or new browser or operating system releases.</li>
<li>Ongoing maintenance, hosting and support after that period are available under a separate retainer.</li>
</ul>
<p>We do not guarantee specific business results such as search rankings, traffic, conversion rates or revenue.</p>
'''),
        ('liability', 'Limitation of liability', '''
<p>Nothing in these terms limits liability that cannot be limited by law, including liability for death or personal injury caused by negligence, or for fraud.</p>
<p>Subject to that:</p>
<ul>
<li>we are not liable for loss of profits, revenue, business, goodwill, data or anticipated savings, or for any indirect or consequential loss;</li>
<li>our total liability arising from or in connection with a project is limited to the total fees you have paid us for that project in the 12 months before the claim arose;</li>
<li>we are not liable for any loss arising from your use of this website, which is provided free of charge for general information.</li>
</ul>
<p>If you are a consumer rather than a business, you also have legal rights that these terms do not affect.</p>
'''),
        ('termination', 'Ending a project', '''
<ul>
<li>Either of us may end a project by written notice if the other materially breaches these terms or the Proposal and does not fix the breach within 14 days of being asked to.</li>
<li>You may end a project for convenience with 14 days’ written notice.</li>
<li>If a project ends early, you pay for work done up to the end date and any non-cancellable third-party costs, and we hand over the work completed to that point once those amounts are paid.</li>
</ul>
'''),
        ('general', 'General', '''
<ul>
<li><strong>Events outside our control</strong>: neither of us is responsible for delays caused by events beyond reasonable control.</li>
<li><strong>Subcontractors</strong>: we may use trusted subcontractors, and we remain responsible for their work.</li>
<li><strong>Independence</strong>: we work as an independent contractor. Nothing in these terms creates a partnership or employment relationship.</li>
<li><strong>Whole agreement</strong>: these terms and the Proposal are the whole agreement for a project and replace earlier discussions about it.</li>
<li><strong>Changes</strong>: we may update these terms from time to time. The version in force when you accept a Proposal applies to that project.</li>
<li><strong>Severability</strong>: if any part of these terms is found unenforceable, the rest stays in force.</li>
<li><strong>Governing law</strong>: these terms are governed by the law of England and Wales, and the courts of England and Wales have exclusive jurisdiction, unless the Proposal names a different law. If you are a consumer, you may also have the right to bring proceedings where you live.</li>
</ul>
'''),
        ('contact', 'Contact', f'''
<p>For anything about these terms or a project, email {MAIL} or use our <a href="contact-us.html">contact page</a>.</p>
'''),
    ],
}

COOKIES = {
    'file': 'cookies.html',
    'title': 'Cookie Policy | Vector Studioz',
    'description': 'Which cookies and browser storage the Vector Studioz website uses, why, and how to control them. We do not use advertising or tracking cookies.',
    'h1': 'Cookie Policy',
    'lede': 'This policy explains the cookies and similar technologies used on vectorstudioz.uk, what they do and how you can control them.',
    'sections': [
        ('summary', 'The short version', '''
<div class="legal-callout"><p><strong>We do not use advertising cookies, cross-site tracking or third-party analytics.</strong> The site only uses storage that is needed for it to work securely and to remember a few simple preferences.</p></div>
'''),
        ('what-are-cookies', 'What cookies and similar technologies are', '''
<p>Cookies are small text files a website places in your browser. Similar technologies, such as local storage, let a site keep small pieces of information on your device. They can be <strong>first-party</strong> (set by the site you are visiting) or <strong>third-party</strong> (set by another service), and either last only for your visit (<strong>session</strong>) or for a set period (<strong>persistent</strong>).</p>
<p>In this policy “cookies” covers all of these.</p>
'''),
        ('cookies-we-use', 'Cookies we use', '''
<h3>Strictly necessary</h3>
<p>These keep the site secure and working. Under UK and EU law they do not need consent.</p>
<div class="legal-table-wrap"><table class="legal-table">
<thead><tr><th>Name</th><th>Provider</th><th>Purpose</th><th>Duration</th></tr></thead>
<tbody>
<tr><td><code>__cf_bm</code>, <code>cf_clearance</code></td><td>Cloudflare (our security and delivery network)</td><td>Tells genuine visitors apart from bots and protects the site from attacks. Only set when Cloudflare’s security checks need them.</td><td>30 minutes to 1 year</td></tr>
</tbody></table></div>
<h3>Preferences</h3>
<p>These remember choices you make, such as dismissing a banner or your cookie preferences. They are stored only in your browser and never sent to us.</p>
<div class="legal-table-wrap"><table class="legal-table">
<thead><tr><th>Name</th><th>Type</th><th>Purpose</th><th>Duration</th></tr></thead>
<tbody>
<tr><td><code>consentMode</code>, <code>userCookieSetting</code></td><td>Local storage (first-party)</td><td>Remembers your cookie preferences so we do not ask again.</td><td>Until you clear your browser storage</td></tr>
<tr><td>Interface preferences</td><td>Local or session storage (first-party)</td><td>Remembers small interface choices, such as a closed announcement banner.</td><td>Session, or until you clear your browser storage</td></tr>
</tbody></table></div>
<h3>Analytics and advertising</h3>
<p>We do not use any. If that changes, we will update this policy and ask for your consent before setting them.</p>
'''),
        ('third-parties', 'Content from third-party providers', '''
<p>To load quickly, the site fetches fonts, scripts, 3D models, images and video from content delivery networks, including Google Fonts, jsDelivr, unpkg, Amazon Web Services and the Webflow content network. These requests send your IP address and browser details to the provider so it can deliver the file, but they do not set tracking cookies on our behalf. Each provider handles that data under its own privacy policy.</p>
'''),
        ('control', 'How to control cookies', '''
<p>You can block or delete cookies and site data in your browser settings. Blocking strictly necessary cookies may stop parts of the site from working, for example if a security check cannot complete. Guidance for common browsers:</p>
<ul>
<li><a href="https://support.google.com/chrome/answer/95647" rel="noopener" target="_blank">Google Chrome</a></li>
<li><a href="https://support.apple.com/guide/safari/manage-cookies-sfri11471/mac" rel="noopener" target="_blank">Safari</a></li>
<li><a href="https://support.mozilla.org/kb/clear-cookies-and-site-data-firefox" rel="noopener" target="_blank">Mozilla Firefox</a></li>
<li><a href="https://support.microsoft.com/microsoft-edge/delete-cookies-in-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09" rel="noopener" target="_blank">Microsoft Edge</a></li>
</ul>
'''),
        ('changes', 'Changes and contact', f'''
<p>We will update this policy if the cookies we use change. The “Last updated” date at the top shows when it last changed. For more on how we handle personal data, see our <a href="privacy-policy.html">Privacy Policy</a>. Questions? Email {MAIL}.</p>
'''),
    ],
}

PAGES = [PRIVACY, TERMS, COOKIES]

# ---------------------------------------------------------------- template

def shell():
    src = open('about.html', encoding='utf-8').read()
    head_end = src.index('<main class="main-content">') + len('<main class="main-content">')
    foot_start = src.index('</main>')
    vnav = re.search(r'<script src="vector-nav\.js\?v=[^"]+"></script>', src).group(0)
    footer = src[foot_start:src.index('</footer>') + len('</footer>')]
    top = src[:head_end]
    # Our own stylesheet, after vector-nav.css.
    top = re.sub(r'(<link href="vector-nav\.css\?v=[^"]+" rel="stylesheet"/>)',
                 r'\1\n<link href="legal.css?v=1.0.1" rel="stylesheet"/>', top, count=1)
    return top, footer, vnav


def label_tables(markup):
    """Copy each table's column headings onto its cells (data-label) for the stacked mobile layout."""
    def one(m):
        table = m.group(0)
        heads = [re.sub(r'<[^>]+>', '', h) for h in re.findall(r'<th>(.*?)</th>', table)]
        def row(r):
            cells = iter(heads)
            return re.sub(r'<td>', lambda _: f'<td data-label="{html.escape(next(cells, ""))}">', r.group(0))
        return re.sub(r'<tr>.*?</tr>', row, table, flags=re.S)
    return re.sub(r'<table class="legal-table">.*?</table>', one, markup, flags=re.S)


def build(page, top, footer, vnav):
    t = top
    t = re.sub(r'<title>[^<]*</title>', f'<title>{html.escape(page["title"], quote=False)}</title>', t, count=1)
    t = re.sub(r'<meta content="[^"]*" name="description"/>',
               f'<meta content="{html.escape(page["description"])}" name="description"/>', t, count=1)
    url = f'https://vectorstudioz.uk/{page["file"]}'
    t = re.sub(r'<link rel="canonical" href="[^"]*"/>', f'<link rel="canonical" href="{url}"/>', t, count=1)
    t = re.sub(r'data-wf-page="[^"]*"', 'data-wf-page="legal"', t, count=1)

    toc = '\n'.join(f'<li><a href="#{sid}">{html.escape(title)}</a></li>' for sid, title, _ in page['sections'])
    body = '\n'.join(
        f'<section id="{sid}"><h2><span class="legal-num">{i:02d}</span>{html.escape(title)}</h2>{content.strip()}</section>'
        for i, (sid, title, content) in enumerate(page['sections'], 1))
    body = label_tables(body)
    related = '\n'.join(f'<a href="{p["file"]}">{p["h1"]}</a>' for p in PAGES if p is not page)
    jsonld = (
        '<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage",'
        f'"@id":"{url}#webpage","url":"{url}","name":{json.dumps(page["title"])},'
        '"inLanguage":"en","dateModified":"2026-11-07",'
        '"isPartOf":{"@id":"https://vectorstudioz.uk/#website"},"publisher":{"@id":"https://vectorstudioz.uk/#organization"}}</script>')

    main = f'''
<article class="legal-page">
<header class="legal-hero">
<div class="legal-eyebrow">Legal</div>
<h1>{page["h1"]}</h1>
<p class="legal-lede">{page["lede"]}</p>
<div class="legal-meta"><span>Last updated: {UPDATED}</span><span>Vector Studioz</span></div>
</header>
<div class="legal-layout">
<nav aria-label="On this page" class="legal-toc">
<p class="legal-toc-title">On this page</p>
<ol>
{toc}
</ol>
</nav>
<div class="legal-body">
{body}
<section id="related"><h2><span class="legal-num">Related</span>Other policies</h2><div class="legal-related">{related}</div></section>
</div>
</div>
</article>
'''
    toc_js = '''<script>
(function () {
  var links = document.querySelectorAll('.legal-toc a');
  if (!('IntersectionObserver' in window) || !links.length) return;
  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting || !byId[e.target.id]) return;
      links.forEach(function (a) { a.classList.remove('is-active'); });
      byId[e.target.id].classList.add('is-active');
    });
  }, { rootMargin: '-20% 0px -70% 0px' });
  document.querySelectorAll('.legal-body section[id]').forEach(function (s) { io.observe(s); });
})();
</script>'''
    out = (t + main + footer + '\n'
           + '<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>\n'
           + vnav + '\n' + toc_js + '\n' + jsonld + '\n</body>\n</html>\n')
    open(page['file'], 'w', encoding='utf-8', newline='\n').write(out)
    print('built', page['file'])


if __name__ == '__main__':
    top, footer, vnav = shell()
    for p in PAGES:
        build(p, top, footer, vnav)
