/* ─────────────────────────────────────────────────────────────────
   TECNOVOA — Master Global JavaScript
   Versión: Modular & Extensible (Control de Tema, Animaciones, FAQ)
───────────────────────────────────────────────────────────────── */
(function() {
  'use strict';

  /* ── 1. CONTROLADOR DE TEMA (MODO CLARO / OSCURO) ───────────── */
  function initTheme() {
    var toggleBtn = document.getElementById('tv-theme-toggle');
    var targets = [
      document.documentElement,
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

  /* ── 2. OBSERVER DE ANIMACIONES MODULARES ───────────────────── */
  function initAnimations() {
    var animSelector = '.tv-anim-fade-in, .tv-anim-slide-up, .tv-anim-scale, .tv-anim-stagger, .fade-in';
    var animEls = document.querySelectorAll(animSelector);
    if (!animEls.length) return;

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
          if (e.isIntersecting) {
            e.target.classList.add('visible');
            io.unobserve(e.target);
          }
        });
      }, { threshold: 0.05, rootMargin: '0px 0px -20px 0px' });

      animEls.forEach(function(el) { io.observe(el); });
    } else {
      animEls.forEach(function(el) { el.classList.add('visible'); });
    }
  }

  /* ── 3. ACORDEÓN DE PREGUNTAS FRECUENTES (FAQ) ──────────────── */
  function initFAQ() {
    document.querySelectorAll('.tv-sec-faq .faq-question').forEach(function(btn) {
      btn.addEventListener('click', function() {
        var item = btn.closest('.faq-item');
        if (!item) return;
        var isActive = item.classList.contains('active');
        // Cerrar otros del mismo acordeón
        var parent = item.parentElement;
        if (parent) {
          parent.querySelectorAll('.faq-item').forEach(function(i) { i.classList.remove('active'); });
        }
        if (!isActive) {
          item.classList.add('active');
        }
      });
    });
  }

  /* ── 4. NAVEGACIÓN SUAVE DE ANCLAS (#) ────────────────────────── */
  function initSmoothScroll() {
    document.querySelectorAll('.tv-landing-page a[href^="#"]').forEach(function(a) {
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

  /* ── INICIALIZACIÓN GLOBAL ───────────────────────────────────── */
  function initAll() {
    initTheme();
    initAnimations();
    initFAQ();
    initSmoothScroll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
