/* ─────────────────────────────────────────────────────────────────
   TECNOVOA — Master Global JavaScript
   Uso: Cargar este archivo JS en WordPress para controlar el tema
   Light/Dark, animaciones IntersectionObserver y scroll suave.
───────────────────────────────────────────────────────────────── */
(function() {
  'use strict';

  /* ── 1. CONTROLADOR DE TEMA (MODO CLARO / OSCURO) ───────────── */
  function initTheme() {
    var toggleBtn = document.getElementById('tv-theme-toggle');
    var targets = [
      document.documentElement,
      document.querySelector('.tv-av-page'),
      document.querySelector('.tv-landing-page')
    ].filter(Boolean);

    function applyTheme(theme) {
      targets.forEach(function(el) {
        el.setAttribute('data-theme', theme);
      });
      if (toggleBtn) {
        var textSpan = toggleBtn.querySelector('.theme-toggle-text');
        if (textSpan) {
          textSpan.textContent = theme === 'light' ? 'Modo Oscuro' : 'Modo Claro';
        }
      }
      try { localStorage.setItem('tecnovoa-theme', theme); } catch(e) {}
    }

    var savedTheme = 'dark';
    try { savedTheme = localStorage.getItem('tecnovoa-theme') || 'dark'; } catch(e) {}
    applyTheme(savedTheme);

    if (toggleBtn && !toggleBtn.dataset.themeBound) {
      toggleBtn.dataset.themeBound = 'true';
      toggleBtn.addEventListener('click', function() {
        var currentTheme = (document.documentElement.getAttribute('data-theme') || 'dark') === 'light' ? 'light' : 'dark';
        var nextTheme = currentTheme === 'light' ? 'dark' : 'light';
        applyTheme(nextTheme);
      });
    }
  }

  /* ── 2. ANIMACIONES EN SCROLL (INTERSECTION OBSERVER) ────────── */
  function initAnimations() {
    var fadeEls = document.querySelectorAll('.fade-in');
    if (!fadeEls.length) return;

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
          if (e.isIntersecting) {
            e.target.classList.add('visible');
            io.unobserve(e.target);
          }
        });
      }, { threshold: 0.05, rootMargin: '0px 0px -20px 0px' });

      fadeEls.forEach(function(el) { io.observe(el); });
    } else {
      fadeEls.forEach(function(el) { el.classList.add('visible'); });
    }
  }

  /* ── 3. NAVEGACIÓN SUAVE DE ANCLAS (#) ────────────────────────── */
  function initSmoothScroll() {
    document.querySelectorAll('.tv-av-page a[href^="#"], .tv-landing-page a[href^="#"]').forEach(function(a) {
      a.addEventListener('click', function(e) {
        var href = a.getAttribute('href');
        if (href && href.length > 1) {
          var target = document.querySelector(href);
          if (target) {
            e.preventDefault();
            window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 40, behavior: 'smooth' });
          }
        }
      });
    });
  }

  /* ── 4. HELPER DE GRID SPAN ─────────────────────────────────── */
  function fixSpan() {
    var span2 = document.querySelector('.tv-span-2');
    if (!span2) return;
    span2.style.gridColumn = window.innerWidth <= 480 ? '' : 'span 2';
  }

  /* ── INICIALIZACIÓN GLOBAL ───────────────────────────────────── */
  function initAll() {
    initTheme();
    initAnimations();
    initSmoothScroll();
    fixSpan();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  window.addEventListener('resize', fixSpan, { passive: true });
})();
