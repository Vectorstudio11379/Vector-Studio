// Contact form: sends the project brief to the studio inbox via FormSubmit
// (https://formsubmit.co), since the site is static and has no server of its own.
// Without JavaScript the form still posts to FormSubmit's normal endpoint.
(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;

  var success = document.getElementById('contact-success');
  var error = document.getElementById('contact-error');
  var button = form.querySelector('button[type="submit"]');
  var label = button ? button.querySelector('.btn-primary-text-3') : null;
  var endpoint = form.getAttribute('data-ajax-action');
  var sending = false;

  // Arrived back from a no-JavaScript submission (FormSubmit redirects to ?sent=1).
  if (/[?&]sent=1\b/.test(window.location.search) && success) {
    form.style.display = 'none';
    success.style.display = 'block';
  }

  function setSending(on) {
    sending = on;
    if (!button) return;
    button.disabled = on;
    button.style.opacity = on ? '0.6' : '';
    button.style.cursor = on ? 'wait' : 'pointer';
    if (label) label.textContent = on ? 'Sending…' : 'Submit Discovery Brief →';
  }

  form.addEventListener('submit', function (event) {
    if (!endpoint || !window.fetch) return; // fall back to a normal form post
    event.preventDefault();
    if (sending) return;
    if (error) error.style.display = 'none';

    var data = {};
    new FormData(form).forEach(function (value, key) { data[key] = value; });
    // Readable labels for the selects, so the email doesn't show raw codes.
    form.querySelectorAll('select').forEach(function (select) {
      var option = select.options[select.selectedIndex];
      if (option) data[select.name] = option.text;
    });

    setSending(true);
    fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(data)
    })
      .then(function (res) {
        return res.json().catch(function () { return {}; }).then(function (body) {
          if (!res.ok || String(body.success) !== 'true') throw new Error(body.message || 'HTTP ' + res.status);
        });
      })
      .then(function () {
        form.reset();
        form.style.display = 'none';
        if (success) success.style.display = 'block';
      })
      .catch(function (err) {
        if (window.console) console.warn('Contact form failed:', err);
        if (error) error.style.display = 'block';
      })
      .then(function () { setSending(false); });
  });
})();
