/**
 * Vector Studioz — Global Navigation & URL Sanitation Script
 */
(function() {
  'use strict';

  function initVectorNav() {
    // 1. Mobile Menu Toggle & Body Mount
    const toggleBtn = document.querySelector('.vs-mobile-toggle');
    const drawer = document.querySelector('.vs-mobile-drawer');

    if (toggleBtn && drawer) {
      // Liberate drawer from navbar containing block (created by backdrop-filter)
      if (drawer.parentElement !== document.body) {
        document.body.appendChild(drawer);
      }

      function closeDrawer() {
        drawer.classList.remove('is-open');
        toggleBtn.classList.remove('is-active');
        document.body.style.overflow = '';
      }

      function openDrawer() {
        drawer.classList.add('is-open');
        toggleBtn.classList.add('is-active');
        document.body.style.overflow = 'hidden';
      }

      toggleBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        const isOpen = drawer.classList.contains('is-open');
        if (isOpen) {
          closeDrawer();
        } else {
          openDrawer();
        }
      });

      // Close on escape
      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && drawer.classList.contains('is-open')) {
          closeDrawer();
        }
      });

      // Auto-close drawer when clicking on any navigation link inside it
      const drawerLinks = drawer.querySelectorAll('a');
      drawerLinks.forEach(link => {
        link.addEventListener('click', function() {
          closeDrawer();
        });
      });
    }

    // 2. Mobile Accordion Toggle
    const accordionBtns = document.querySelectorAll('.vs-mobile-header-btn');
    accordionBtns.forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.stopPropagation();
        const subitems = this.nextElementSibling;
        const isExpanded = this.classList.contains('is-expanded');
        if (subitems) {
          if (isExpanded) {
            this.classList.remove('is-expanded');
            subitems.classList.remove('is-open');
          } else {
            this.classList.add('is-expanded');
            subitems.classList.add('is-open');
          }
        }
      });
    });

    // 3. Highlight Active Page
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const allLinks = document.querySelectorAll('.vs-nav-link, .vs-dropdown-item, .vs-mobile-sublink, .vs-mobile-single-link');

    allLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      const targetPage = href.split('/').pop().split('#')[0].split('?')[0];

      if (targetPage && (targetPage === currentPath || (currentPath === '' && targetPage === 'index.html') || (currentPath === 'index.html' && targetPage === 'index.html'))) {
        link.classList.add('active');
        // If inside a dropdown, also highlight parent
        const parentNavItem = link.closest('.vs-nav-item');
        if (parentNavItem) {
          const parentLink = parentNavItem.querySelector('.vs-nav-link');
          if (parentLink) parentLink.classList.add('active');
        }
      }
    });

    // 4. Scroll State Detection
    const navbar = document.querySelector('.vs-navbar');
    if (navbar) {
      window.addEventListener('scroll', function() {
        if (window.scrollY > 20) {
          navbar.classList.add('vs-scrolled');
        } else {
          navbar.classList.remove('vs-scrolled');
        }
      }, { passive: true });
    }

    // 5. Automatic Sanitation of Legacy Extensionless Links Across the Whole Page
    const pageLinks = document.querySelectorAll('a[href]');
    const isSubpage = window.location.pathname.includes('/projects/');
    const relPrefix = isSubpage ? '../' : '';

    const knownHtmlPages = [
      'about', 'careers', 'case-studies', 'contact-us', 'contact',
      'blog', 'brand-kit', 'verify', 'videos', 'privacy-policy', 'tos',
      'cookies', 'eligibility-policy', 'ai-agents', 'ai-crypto-alerts',
      'ai-trading-assistant', 'ai-web3-news', 'crypto-ai-hub',
      'crypto-compliance-assistant', 'smart-contract-auditor',
      'smart-contract-generator', 'web3-ai-grant', 'web3-chatbot',
      'projects', 'web-design', 'web-development', 'webgl-3d',
      'software-engineering', 'ai-automation', 'mobile-development'
    ];

    pageLinks.forEach(a => {
      let href = a.getAttribute('href');
      if (!href) return;

      // Map /pricing or pricing.html -> contact-us.html
      if (href === '/pricing' || href === 'pricing' || href === '/pricing.html' || href === 'pricing.html') {
        a.setAttribute('href', `${relPrefix}contact-us.html`);
        return;
      }

      // Map /contact -> contact-us.html
      if (href === '/contact' || href === 'contact') {
        a.setAttribute('href', `${relPrefix}contact-us.html`);
        return;
      }

      // Check if href matches a known page without .html (e.g. /about, /careers)
      for (const page of knownHtmlPages) {
        if (href === `/${page}` || href === page) {
          const mapped = page === 'contact' ? 'contact-us' : page;
          a.setAttribute('href', `${relPrefix}${mapped}.html`);
          break;
        }
      }
    });

    // 6. Universal Header CTA Text Alignment (SUBMIT PROJECT BRIEF ↓)
    const headerCtaTexts = document.querySelectorAll('.vs-navbar .btn-primary-text, .vs-mobile-cta-wrapper .btn-primary-text');
    headerCtaTexts.forEach(el => {
      if (el.textContent.includes('Start a Project') || el.textContent.includes('Start A Project')) {
        el.innerHTML = 'SUBMIT PROJECT BRIEF &darr;';
      }
    });
  }

  if (window.__vectorNavInitialized) return;
  window.__vectorNavInitialized = true;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initVectorNav);
  } else {
    initVectorNav();
  }
})();
