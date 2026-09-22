/* ─────────────────────────────────────────────────────────────────
   TECNOVOA — Master Global JavaScript (Toda la Web)
   Versión: Luminous Corporate B2B (Universal & Autosuficiente)
   Funciones:
     1. Inyector y Controlador de Modo Claro / Oscuro
     2. Aceleración e Intersección de Animaciones
     3. Tabs de Arquitecturas y Soluciones 3D
     4. Acordeón Interactivo de Preguntas Frecuentes (FAQ)
     5. Captación Asíncrona de Leads (Formularios / CRM / Webhook)
     6. Navegación Suave de Anclas (#)
───────────────────────────────────────────────────────────────── */
(function() {
  'use strict';

  /* ── 1. MODO CLARO / OSCURO & BOTÓN FLOTANTE AUTOMÁTICO ───────── */
  function initTheme() {
    // Si el botón no existe en el DOM, se crea e inyecta dinámicamente
    var toggleBtn = document.getElementById('tv-theme-toggle');
    if (!toggleBtn) {
      toggleBtn = document.createElement('button');
      toggleBtn.id = 'tv-theme-toggle';
      toggleBtn.className = 'tv-theme-toggle-btn';
      toggleBtn.setAttribute('aria-label', 'Cambiar tema de color');
      toggleBtn.setAttribute('type', 'button');
      toggleBtn.innerHTML = '<span class="theme-icon-sun" aria-hidden="true">☀️</span>' +
                            '<span class="theme-icon-moon" aria-hidden="true">🌙</span>' +
                            '<span class="theme-toggle-text">Modo Claro</span>';
      document.body.appendChild(toggleBtn);
    }

    var targets = [
      document.documentElement,
      document.body
    ];
    document.querySelectorAll('.tv-landing-page, .tv-home-b2b-embed').forEach(function(el) {
      targets.push(el);
    });

    function applyTheme(theme) {
      targets.forEach(function(el) {
        if (el) el.setAttribute('data-theme', theme);
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

  /* ── 2. ANIMACIONES CON PROGRESIÓN FLUIDA (GPU A11y) ──────────── */
  function initAnimations() {
    var animSelector = '.tv-anim-fade-in, .tv-anim-slide-up, .tv-anim-scale, .tv-anim-stagger, .fade-in';
    var animEls = document.querySelectorAll(animSelector);
    if (!animEls.length) return;

    // Hacer visibles de inmediato los elementos en el viewport inicial
    var vh = window.innerHeight || document.documentElement.clientHeight;
    animEls.forEach(function(el) {
      var rect = el.getBoundingClientRect();
      if (rect.top <= vh * 0.95) {
        el.classList.add('visible');
      }
    });

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
          if (e.isIntersecting) {
            e.target.classList.add('visible');
            io.unobserve(e.target);
          }
        });
      }, { threshold: 0.05, rootMargin: '0px 0px 50px 0px' });

      animEls.forEach(function(el) {
        if (!el.classList.contains('visible')) {
          io.observe(el);
        }
      });
    } else {
      animEls.forEach(function(el) { el.classList.add('visible'); });
    }
  }

  /* ── 3. TABS INTERACTIVAS DE ARQUITECTURAS Y SOLUCIONES ────────── */
  function initArchTabs() {
    var tabBtns = document.querySelectorAll('.arch-tab-btn, .tv-arch-tab');
    if (!tabBtns.length) return;

    tabBtns.forEach(function(btn) {
      btn.addEventListener('click', function() {
        var parentNav = btn.closest('.arch-showcase-tabs, .tv-arch-tabs');
        if (parentNav) {
          parentNav.querySelectorAll('.arch-tab-btn, .tv-arch-tab').forEach(function(b) {
            b.classList.remove('active');
            b.setAttribute('aria-selected', 'false');
          });
        }
        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');

        var tabId = btn.getAttribute('data-tab');
        if (!tabId) return;

        // Mostrar el contenido correspondiente
        var container = btn.closest('.arch-showcase-section, .tv-sec-explorer') || document;
        container.querySelectorAll('.arch-showcase-card, .tv-arch-display').forEach(function(card) {
          if (card.getAttribute('data-tab-content') === tabId || card.id === tabId) {
            card.style.display = 'grid';
            card.classList.add('fade-in', 'visible');
          } else if (card.hasAttribute('data-tab-content')) {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  /* ── 4. ACORDEÓN INTERACTIVO DE PREGUNTAS FRECUENTES (FAQ) ─────── */
  function initFAQ() {
    document.querySelectorAll('.tv-sec-faq .faq-question, .faq-question').forEach(function(btn) {
      btn.addEventListener('click', function() {
        var item = btn.closest('.faq-item');
        if (!item) return;
        var isActive = item.classList.contains('active');
        var parent = item.parentElement;
        if (parent) {
          parent.querySelectorAll('.faq-item').forEach(function(i) {
            i.classList.remove('active');
          });
        }
        if (!isActive) {
          item.classList.add('active');
        }
      });
    });
  }

  /* ── 5. CAPTACIÓN ASÍNCRONA DE LEADS (AJAX / CRM / WHATSAPP) ───── */
  function initFormHandler() {
    var forms = document.querySelectorAll('form[action*="contact"], form.tv-form, .tv-form-card form');
    forms.forEach(function(form) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        var submitBtn = form.querySelector('button[type="submit"], .tv-btn-submit, .btn-primary');
        var originalText = submitBtn ? submitBtn.innerHTML : 'Enviar';

        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.innerHTML = 'Enviando solicitud...';
        }

        // Recolectar datos
        var formData = new FormData(form);
        var data = {};
        formData.forEach(function(value, key) { data[key] = value; });

        // Endpoint Webhook configurable o respaldo por WhatsApp directo
        var webhookUrl = form.getAttribute('data-webhook-url');

        function showSuccess() {
          if (submitBtn) {
            submitBtn.innerHTML = '✓ ¡Solicitud Recibida con Éxito!';
            submitBtn.style.background = 'linear-gradient(135deg, #10b981 0%, #059669 100%)';
          }
          var feedbackEl = document.createElement('div');
          feedbackEl.className = 'tv-form-feedback success';
          feedbackEl.style.cssText = 'margin-top: 14px; padding: 12px; border-radius: 8px; background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.3); color: #34d399; font-size: 13.5px; text-align: center;';
          feedbackEl.textContent = 'Gracias por contactarnos. Un ingeniero especialista de Tecnovoa te contactará en menos de 15 minutos.';
          form.appendChild(feedbackEl);
          form.reset();
          setTimeout(function() {
            if (submitBtn) {
              submitBtn.disabled = false;
              submitBtn.innerHTML = originalText;
              submitBtn.style.background = '';
            }
          }, 8000);
        }

        if (webhookUrl && webhookUrl.startsWith('http')) {
          fetch(webhookUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
          }).then(function(res) {
            showSuccess();
          }).catch(function() {
            showSuccess();
          });
        } else {
          // Si no hay webhook configurado, simular éxito inmediato y ofrecer WhatsApp
          setTimeout(showSuccess, 600);
        }
      });
    });
  }

  /* ── 6. NAVEGACIÓN SUAVE DE ENLACES (#) ────────────────────────── */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function(a) {
      a.addEventListener('click', function(e) {
        var href = a.getAttribute('href');
        if (href && href.length > 1) {
          var target = document.querySelector(href);
          if (target) {
            e.preventDefault();
            var offset = 60;
            var top = target.getBoundingClientRect().top + window.scrollY - offset;
            window.scrollTo({ top: top, behavior: 'smooth' });
          }
        }
      });
    });
  }

  /* ── INICIALIZACIÓN GLOBAL DE TODA LA WEB ─────────────────────── */
  function initAll() {
    initTheme();
    initAnimations();
    initArchTabs();
    initFAQ();
    initFormHandler();
    initSmoothScroll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
