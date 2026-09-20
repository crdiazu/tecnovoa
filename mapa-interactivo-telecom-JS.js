// Lógica de Renderizado y Posicionamiento para el Mapa Interactivo de Telecomunicaciones (Tecnovoa)
function initInteractiveMap() {
    const container = document.getElementById('mapa-tec-main');
    const hotspots = document.querySelectorAll('.mapa-tec-hotspot');
    const tooltip = document.getElementById('mapa-tec-tooltip');
    
    if (!container || !tooltip) return;

    const tooltipTitle = tooltip.querySelector('.mapa-tec-tooltip-title');
    const tooltipDesc = tooltip.querySelector('.mapa-tec-tooltip-desc');

    hotspots.forEach(hotspot => {
        hotspot.addEventListener('mouseenter', function() {
            // Rellenar la información
            tooltipTitle.textContent = this.getAttribute('data-title');
            tooltipDesc.textContent = this.getAttribute('data-desc');
            
            // Renderizado invisible temporal para obtener dimensiones
            tooltip.style.visibility = 'hidden';
            tooltip.style.opacity = '0';
            tooltip.classList.add('mapa-tec-active');
            
            // Calcular posiciones exactas relativas al contenedor
            const containerRect = container.getBoundingClientRect();
            const hotspotRect = this.getBoundingClientRect();
            
            let topPos = hotspotRect.top - containerRect.top;
            let leftPos = hotspotRect.left - containerRect.left;
            
            const tooltipWidth = tooltip.offsetWidth;
            const tooltipHeight = tooltip.offsetHeight;
            
            // Alinear horizontalmente sobre el punto
            let finalLeft = (leftPos + (hotspotRect.width / 2)) - (tooltipWidth / 2);
            
            // Prevenir que se desborde por los lados
            if (finalLeft < 10) finalLeft = 10;
            if (finalLeft + tooltipWidth > containerRect.width - 10) {
                finalLeft = containerRect.width - tooltipWidth - 10;
            }
            
            // Ubicar encima del hotspot (con 15px de separación)
            let finalTop = topPos - tooltipHeight - 15;
            
            // Si choca con el borde superior de la imagen, mostrarlo debajo
            if (finalTop < 10) {
                finalTop = topPos + hotspotRect.height + 15;
            }

            tooltip.style.left = finalLeft + 'px';
            tooltip.style.top = finalTop + 'px'; 
            
            // Transición visible
            tooltip.style.visibility = 'visible';
            tooltip.style.opacity = '1';
        });

        hotspot.addEventListener('mouseleave', function() {
            tooltip.style.opacity = '0';
            tooltip.style.visibility = 'hidden';
            tooltip.classList.remove('mapa-tec-active');
        });
    });
}

// Inicialización segura de JS (resuelve retrasos o diferidos de carga en WordPress)
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initInteractiveMap);
} else {
    initInteractiveMap();
}
