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

    // 7. Sticky Right-Side Rail (.aside-navbar) Handlers & Scroll-Spy
    const asideNav = document.querySelector('.aside-navbar');
    if (asideNav) {
      const openBtn = asideNav.querySelector('.js-open-aside-menu');
      const closeBtn = asideNav.querySelector('.js-close-aside-menu');
      let overlay = asideNav.querySelector('.w-nav-overlay');
      if (!overlay) {
        overlay = document.createElement('div');
        overlay.className = 'w-nav-overlay';
        asideNav.appendChild(overlay);
      }

      function openAsideMenu(e) {
        if (e) e.preventDefault();
        document.body.classList.remove('aside-menu-is-closed');
        document.body.classList.add('aside-menu-is-opened');
        asideNav.classList.remove('short-mode');
        asideNav.classList.add('full-mode');
      }

      function closeAsideMenu(e) {
        if (e) e.preventDefault();
        document.body.classList.remove('aside-menu-is-opened');
        document.body.classList.add('aside-menu-is-closed');
        setTimeout(() => {
          asideNav.classList.remove('full-mode');
          asideNav.classList.add('short-mode');
        }, 750);
      }

      if (openBtn) {
        openBtn.addEventListener('click', openAsideMenu);
      }
      if (closeBtn) {
        closeBtn.addEventListener('click', closeAsideMenu);
      }
      overlay.addEventListener('click', closeAsideMenu);

      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && asideNav.classList.contains('full-mode')) {
          closeAsideMenu();
        }
      });

      const asideItems = asideNav.querySelectorAll('.aside-nav-item');
      asideItems.forEach(item => {
        item.addEventListener('click', function(e) {
          const href = this.getAttribute('href');
          if (href && href.startsWith('#')) {
            const target = document.querySelector(href);
            if (target) {
              e.preventDefault();
              if (asideNav.classList.contains('full-mode')) {
                closeAsideMenu();
              }
              target.scrollIntoView({ behavior: 'smooth' });
            }
          }
        });
      });

      // Scroll-Spy for aside navigation rail
      const sectionIds = ['intro', 'unlimited-solutions', 'solutions', 'cases', 'ecosystem', 'our-token', 'faq', 'site-footer'];
      function updateAsideScrollSpy() {
        const scrollMid = window.scrollY + window.innerHeight * 0.35;
        let activeId = 'intro';

        for (const id of sectionIds) {
          const el = document.getElementById(id);
          if (el) {
            const top = el.getBoundingClientRect().top + window.scrollY;
            if (scrollMid >= top) {
              activeId = id;
            }
          }
        }

        asideItems.forEach(item => {
          const href = item.getAttribute('href');
          if (href === `#${activeId}`) {
            item.classList.add('w--current');
          } else {
            item.classList.remove('w--current');
          }
        });
      }

      window.addEventListener('scroll', updateAsideScrollSpy, { passive: true });
      updateAsideScrollSpy();
    }

    // 8. Page loader
    // The homepage loader must stay up until the 3D robot is in the scene: the
    // robot script adds body.loaded at that moment, which also starts the hero
    // text animations. Dismissing earlier shows a blank hero, then the robot
    // and text pop in. This only steps in if loading genuinely stalls (slow
    // network, WebGL unavailable, a CDN failing), so nobody is ever stuck.
    (function initPageLoader() {
      const body = document.body;
      const loader = document.querySelector('.page-loader');

      if (!loader) {
        body.classList.add('page-ready', 'loaded');
        return;
      }

      const AFTER_WINDOW_LOAD_MS = 4000; // robot still missing after every asset finished
      const HARD_CAP_MS = 15000;         // absolute worst case on a very slow connection
      let finished = false;

      function hideLoader() {
        if (finished) return;
        finished = true;
        body.classList.add('page-ready', 'loaded');
        body.classList.add('vs-loader-done');
        // Remove from layout after the CSS fade (see .vs-loader-done in vector-nav.css).
        setTimeout(() => { loader.style.display = 'none'; }, 700);
      }

      if (body.classList.contains('loaded')) {
        hideLoader();
        return;
      }

      new MutationObserver((_, observer) => {
        if (body.classList.contains('loaded')) {
          observer.disconnect();
          hideLoader();
        }
      }).observe(body, { attributes: true, attributeFilter: ['class'] });

      const fallback = () => setTimeout(hideLoader, AFTER_WINDOW_LOAD_MS);
      if (document.readyState === 'complete') fallback();
      else window.addEventListener('load', fallback, { once: true });
      setTimeout(hideLoader, HARD_CAP_MS);
    })();

    // 9. Brand Logo Subpath Resolution for Nested Subpages
    const isSub = window.location.pathname.includes('/projects/');
    const brandLogos = document.querySelectorAll('.vs-brand-logo-img');
    if (isSub && brandLogos.length > 0) {
      brandLogos.forEach(img => {
        const src = img.getAttribute('src');
        if (src && !src.startsWith('http') && !src.startsWith('../') && !src.startsWith('/')) {
          img.setAttribute('src', `../${src}`);
        }
      });
    }

    // 10. Media that can't load: collapse its wrapper instead of leaving a
    // blank box. A <video> reports networkState NETWORK_NO_SOURCE (3) once
    // every <source> has failed; the last source's error event fires then.
    (function initMediaFallback() {
      const WRAPPER = '.landing-hero-asset-wrapper, .hero-assets-container, .w-embed';

      function collapseIfDead(video) {
        if (video.networkState !== HTMLMediaElement.NETWORK_NO_SOURCE) return;
        const wrapper = video.closest(WRAPPER) || video;
        wrapper.classList.add('vs-media-missing');
      }

      document.querySelectorAll('video').forEach(video => {
        // The robot's hidden eye/touch videos are WebGL textures, not visible media.
        if (video.closest('.eye-video, .touch-video')) return;
        const sources = video.querySelectorAll('source');
        const last = sources[sources.length - 1];
        if (last) last.addEventListener('error', () => collapseIfDead(video));
        video.addEventListener('error', () => collapseIfDead(video));
        collapseIfDead(video); // may already have failed before this ran
      });
    })();
  }

  if (window.__vectorNavInitialized) return;
  window.__vectorNavInitialized = true;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initVectorNav);
  } else {
    initVectorNav();
  }
})();
