// Lógica Unificada de Interactividad y Mapa con Hotspots para Tecnovoa
function initTecnovoaDashboard() {
    const container = document.getElementById('tn-map-container');
    const menuButtons = document.querySelectorAll('.tn-menu-btn');
    const tabContents = document.querySelectorAll('.tn-tab-content');
    const hotspots = document.querySelectorAll('.tn-hotspot');
    const captionText = document.getElementById('tn-caption-text');
    const tooltip = document.getElementById('tn-tooltip');
    const mainImg = document.getElementById('tn-main-diagram');

    // Añade la clase de página oscura para compatibilidad de estilos sin usar selectores complejos `:has`
    document.body.classList.add('tn-dark-page');

    if (!menuButtons.length || !tabContents.length || !hotspots.length) return;

    // Mapeo de captions amigables para la parte inferior de la imagen
    const captionMap = {
        cabling: "Visualizando: Área de Cuarto de Cableado (Cabling)",
        fiber: "Visualizando: Canalización Subterránea de Fibra Óptica",
        wireless: "Visualizando: Enlaces Inalámbricos y Antenas",
        networking: "Visualizando: Sala de Telecomunicaciones (Switches & Firewall)",
        monitoring: "Visualizando: Monitoreo en Tiempo Real (NOC)"
    };

    // --- 1. RESOLUCIÓN AUTOMÁTICA DE IMAGEN BASE ---
    if (mainImg) {
        const primaryUrl = mainImg.src;
        const candidateUrls = [
            primaryUrl,
            '/wp-content/uploads/2026/07/telecomunicaciones-y-redes.webp',
            '/wp-content/uploads/2026/07/telecomunicaciones-y-redes.png',
            '/wp-content/uploads/2026/07/telecomunicaciones%20y%20redes.png',
            '/wp-content/uploads/telecomunicaciones-y-redes.webp',
            'https://tecnovoa.cl/wp-content/uploads/2026/07/telecomunicaciones-y-redes.webp',
            // Fallback final: foto de datacenter
            'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1200&q=80'
        ];
        
        let attemptIndex = 0;
        function tryNextImage() {
            if (attemptIndex < candidateUrls.length) {
                const nextUrl = candidateUrls[attemptIndex];
                attemptIndex++;
                if (mainImg.src !== window.location.origin + nextUrl && mainImg.src !== nextUrl) {
                    mainImg.src = nextUrl;
                } else {
                    tryNextImage();
                }
            }
        }
        mainImg.addEventListener('error', tryNextImage);
        if (!mainImg.complete || mainImg.naturalWidth === 0) {
            tryNextImage();
        }
    }

    // --- 2. SISTEMA DE CAMBIO DE SOLUCIONES (Tabs + Hotspots) ---
    function switchSolution(targetId) {
        // A. Actualizar botones del menú superior
        menuButtons.forEach(btn => {
            if (btn.getAttribute('data-target') === targetId) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // B. Transición de paneles informativos del lado derecho
        tabContents.forEach(content => {
            if (content.id === targetId) {
                content.style.display = 'flex';
                setTimeout(() => {
                    content.classList.add('active');
                }, 20);
            } else {
                content.classList.remove('active');
                content.style.display = 'none';
            }
        });

        // C. Destacar el punto activo correspondiente en la ilustración
        hotspots.forEach(hotspot => {
            if (hotspot.getAttribute('data-target') === targetId) {
                hotspot.classList.add('active');
            } else {
                hotspot.classList.remove('active');
            }
        });

        // D. Actualizar pie de foto
        if (captionText && captionMap[targetId]) {
            captionText.textContent = captionMap[targetId];
        }
    }

    // Registro de clics en menú superior
    menuButtons.forEach(button => {
        button.addEventListener('click', () => {
            const target = button.getAttribute('data-target');
            switchSolution(target);
        });
    });

    // Registro de clics en hotspots del mapa (cambia el panel)
    hotspots.forEach(hotspot => {
        hotspot.addEventListener('click', () => {
            const target = hotspot.getAttribute('data-target');
            if (target) {
                switchSolution(target);
            }
        });
    });

    // --- 3. COMPORTAMIENTO MOUSE-HOVER DEL TOOLTIP ---
    if (container && tooltip) {
        const tooltipTitle = tooltip.querySelector('.tn-tooltip-title');
        const tooltipDesc = tooltip.querySelector('.tn-tooltip-desc');

        hotspots.forEach(hotspot => {
            hotspot.addEventListener('mouseenter', function() {
                // Llenar datos
                tooltipTitle.textContent = this.getAttribute('data-title');
                tooltipDesc.textContent = this.getAttribute('data-desc');
                
                // Mostrar de forma invisible para medir dimensiones reales
                tooltip.style.visibility = 'hidden';
                tooltip.style.opacity = '0';
                tooltip.classList.add('tn-active');

                // Calcular posiciones relativas al contenedor de la imagen
                const containerRect = container.getBoundingClientRect();
                const hotspotRect = this.getBoundingClientRect();

                let topPos = hotspotRect.top - containerRect.top;
                let leftPos = hotspotRect.left - containerRect.left;

                const tooltipWidth = tooltip.offsetWidth;
                const tooltipHeight = tooltip.offsetHeight;

                // Centrar horizontalmente respecto al punto
                let finalLeft = (leftPos + (hotspotRect.width / 2)) - (tooltipWidth / 2);

                // Evitar desbordes por los laterales
                if (finalLeft < 10) finalLeft = 10;
                if (finalLeft + tooltipWidth > containerRect.width - 10) {
                    finalLeft = containerRect.width - tooltipWidth - 10;
                }

                // Posicionar arriba con 12px de separación
                let finalTop = topPos - tooltipHeight - 12;

                // Si choca arriba, mostrarlo abajo
                if (finalTop < 10) {
                    finalTop = topPos + hotspotRect.height + 12;
                }

                tooltip.style.left = finalLeft + 'px';
                tooltip.style.top = finalTop + 'px';

                // Mostrar con animación
                tooltip.style.visibility = 'visible';
                tooltip.style.opacity = '1';
            });

            hotspot.addEventListener('mouseleave', function() {
                tooltip.style.opacity = '0';
                tooltip.style.visibility = 'hidden';
                tooltip.classList.remove('tn-active');
            });
        });
    }

    // --- 4. CURSOR GLOW TRACK EN TARJETAS DE CASOS DE ÉXITO ---
    const caseCards = document.querySelectorAll('.tn-case-card');
    caseCards.forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });
}

// Inicialización segura
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTecnovoaDashboard);
} else {
    initTecnovoaDashboard();
}
