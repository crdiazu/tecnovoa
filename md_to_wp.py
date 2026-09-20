import re
import os
import sys

# Plantillas de salida
HTML_TEMPLATE = """<div class="tecnovoa-wp-component">
    <!-- Mesh Background Light Element -->
    <div class="tn-hero-mesh"></div>

    <!-- Hero Header -->
    <div class="tn-hero">
        <div class="tn-badge">
            <span class="tn-badge-dot"></span>
            <span>{badge}</span>
        </div>
        <h1>{title}</h1>
        <p>{description}</p>
        <div class="tn-button-group">
            <a href="https://wa.me/{whatsapp}" target="_blank" class="btn-grad">
                <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.397.01 12.008.01c3.202.001 6.212 1.246 8.477 3.514 2.266 2.268 3.507 5.28 3.505 8.484-.004 6.657-5.34 11.997-11.953 11.997-2.005-.001-3.973-.502-5.724-1.455L0 24zm6.59-4.846c1.6.95 3.188 1.449 4.825 1.451 5.436 0 9.859-4.407 9.862-9.843.002-2.634-1.024-5.11-2.885-6.974C16.582 1.924 14.12 1.887 12.01 1.887c-5.437 0-9.862 4.41-9.865 9.845-.001 1.696.447 3.351 1.3 4.851l-.95 3.473 3.562-.934zM17.486 14.4c-.3-.15-1.774-.875-2.029-.967-.255-.092-.441-.137-.626.138-.185.276-.717.92-.878 1.103-.162.184-.323.207-.623.057-3.003-1.5-5.064-2.827-6.842-5.856-.161-.276-.161-.476-.011-.626.135-.135.3-.35.45-.525.15-.175.2-.3.3-.5.1-.2.05-.375-.025-.525-.075-.15-.625-1.507-.857-2.063-.226-.543-.453-.469-.623-.477-.16-.008-.344-.01-.529-.01-.185 0-.485.07-.74.36-.254.29-.971.95-.971 2.318c0 1.368.995 2.693 1.135 2.882.14.189 1.957 2.99 4.743 4.19.662.285 1.18.456 1.58.585.666.211 1.272.181 1.751.11.534-.08 1.774-.725 2.029-1.39.255-.666.255-1.238.18-1.353-.075-.115-.275-.19-.575-.34z"/></svg>
                <span>Cotizar por WhatsApp</span>
            </a>
            <a href="https://tecnovoa.cl/contacto/" class="btn-outline">
                <span>Formulario de Contacto</span>
            </a>
        </div>
    </div>

    <!-- Contenido Principal -->
    <div class="tn-content">
        <!-- Intro Section -->
        <div class="tn-intro-section">
            <h2>Tecnología, Experiencia y Conectividad sin límites</h2>
            <p>Proveemos soluciones avanzadas en cada etapa de la infraestructura. Diseñamos e implementamos redes robustas y confiables que garantizan la continuidad de negocio y reducen los costos operativos.</p>
        </div>

        <!-- Grid de Servicios Especializados -->
        <div class="tn-section-header">
            <h2 class="tn-section-title"><span class="tn-title-grad">Servicios Especializados</span> de Red</h2>
            <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">Planificación, tendido, orden, certificación y auditorías técnicas.</p>
        </div>

        <div class="tn-grid">
            <div class="tn-card">
                <div class="tn-card-num">01 / Ingeniería</div>
                <h3>Diseño Profesional</h3>
                <ul>
                    <li>Planificación detallada de infraestructura de red</li>
                    <li>Diseños personalizados bajo normas TIA/EIA</li>
                    <li>Optimización de rutas de cableado para ductos</li>
                    <li>Planos y documentación técnica completa</li>
                </ul>
            </div>
            <div class="tn-card">
                <div class="tn-card-num">02 / Implementación</div>
                <h3>Instalación Profesional</h3>
                <ul>
                    <li>Cableado cobre Categorías 5e, 6, 6A y 7</li>
                    <li>Tendido e inspección de Fibra Óptica</li>
                    <li>Montaje y peinado de Racks y Gabinetes</li>
                    <li>Certificación oficial de cada punto de red</li>
                </ul>
            </div>
            <div class="tn-card">
                <div class="tn-card-num">03 / Continuidad</div>
                <h3>Mantenimiento Técnico</h3>
                <ul>
                    <li>Inspecciones y auditorías periódicas</li>
                    <li>Resolución rápida de incidencias de red</li>
                    <li>Limpieza, peinado y rotulación de racks</li>
                    <li>Actualización y saneamiento de redes</li>
                </ul>
            </div>
            <div class="tn-card">
                <div class="tn-card-num">04 / Consultoría</div>
                <h3>Auditoría y Asesoría</h3>
                <ul>
                    <li>Auditorías exhaustivas de infraestructura</li>
                    <li>Propuestas técnicas de mejora de velocidad</li>
                    <li>Planificación de crecimiento a largo plazo</li>
                    <li>Análisis costo-beneficio de nuevos equipos</li>
                </ul>
            </div>
        </div>

        <!-- Seccion dos columnas (Beneficios y Sectores) -->
        <div class="tn-two-columns">
            <div class="tn-col">
                <h3 class="tn-section-title"><span class="tn-title-grad">Beneficios</span> de Nuestros Servicios</h3>
                <ul class="tn-list-styled">
                    <li>
                        <span class="tn-list-icon">✓</span>
                        <div class="tn-list-text"><strong>Garantía de trabajo certificado:</strong> Certificamos cada nodo para asegurar el cumplimiento de la norma y el óptimo flujo de datos.</div>
                    </li>
                    <li>
                        <span class="tn-list-icon">✓</span>
                        <div class="tn-list-text"><strong>Personal técnico calificado:</strong> Ingenieros en terreno con vasta experiencia y capacitación constante.</div>
                    </li>
                    <li>
                        <span class="tn-list-icon">✓</span>
                        <div class="tn-list-text"><strong>Materiales de primera calidad:</strong> Alianzas estratégicas con marcas líderes (Panduit, Cisco, etc.).</div>
                    </li>
                    <li>
                        <span class="tn-list-icon">✓</span>
                        <div class="tn-list-text"><strong>Soporte continuo y proactivo:</strong> Mantenemos tu negocio operacional 24/7 sin caídas de red.</div>
                    </li>
                </ul>
            </div>

            <div class="tn-col" style="border-left: 1px solid var(--border-hairline); padding-left: 2.5rem;">
                <h3 class="tn-section-title">Sectores que Atendemos</h3>
                <p style="color: var(--text-secondary); margin-bottom: 1.5rem; font-size: 0.95rem;">Creamos soluciones específicas para las necesidades de cada rubro:</p>
                <div class="tn-sector-list">
                    <div class="tn-sector-item">Oficinas Corporativas</div>
                    <div class="tn-sector-item">Centros de Datos</div>
                    <div class="tn-sector-item">Instituciones Educativas</div>
                    <div class="tn-sector-item">Centros Comerciales</div>
                    <div class="tn-sector-item">Industrias y Fábricas</div>
                    <div class="tn-sector-item">Centros de Salud</div>
                </div>
            </div>
        </div>

        <!-- ¿Por qué elegirnos? -->
        <div class="tn-why-box">
            <div class="tn-section-header">
                <h2 class="tn-section-title">¿Por Qué Elegir a Tecnovoa?</h2>
            </div>
            <div class="tn-why-grid">
                <div class="tn-why-card">
                    <h4>
                        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="color: var(--accent-cyan)"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                        10+ Años de Experiencia
                    </h4>
                    <p>Una trayectoria consolidada en el mercado chileno con proyectos exitosos a lo largo del país.</p>
                </div>
                <div class="tn-why-card">
                    <h4>
                        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="color: var(--accent-cyan)"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        Calidad de Fabricante
                    </h4>
                    <p>Empleamos herramientas y certificadores de punta (como analizadores Fluke Networks) y las mejores marcas.</p>
                </div>
                <div class="tn-why-card">
                    <h4>
                        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="color: var(--accent-cyan)"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                        Servicio Ágil e Integral
                    </h4>
                    <p>Desde el diseño inicial hasta el soporte proactivo y preventivo a largo plazo.</p>
                </div>
            </div>
        </div>

        <!-- Enlaces de Interconexión SEO y Socios Tecnológicos -->
        <div class="tn-seo-links">
            <div class="tn-seo-grid">
                <div class="tn-seo-col">
                    <h4>Servicios TI Relacionados (SEO Interno)</h4>
                    <ul class="tn-seo-list">
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/servicios-ti/virtualizacion/">Virtualización</a></li>
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/servicios-cloud/">Servicios Cloud</a></li>
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/servicios-ti/audio-y-video-colaboracion/">Audio & Video Colaboración</a></li>
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/ciberseguridad/">Ciberseguridad Corporativa</a></li>
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/fibra-optica/">Fibra Óptica</a></li>
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/energia/">Energía y Respaldo</a></li>
                    </ul>
                </div>
                <div class="tn-seo-col">
                    <h4>Nuestras Alianzas / Fabricantes</h4>
                    <ul class="tn-seo-list">
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/cisco/" target="_blank">Cisco Systems</a></li>
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/fortinet/" target="_blank">Fortinet Security</a></li>
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/panduit/" target="_blank">Panduit Networks</a></li>
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/apc/" target="_blank">APC by Schneider Electric</a></li>
                        <li class="tn-seo-link-item"><a href="https://tecnovoa.cl/dell/" target="_blank">Dell Technologies</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- CTA Box Final -->
        <div class="tn-cta">
            <h3>¿Listo para optimizar tu infraestructura de red?</h3>
            <p>Agenda hoy un diagnóstico técnico sin costo de tu infraestructura actual con nuestros ingenieros certificados.</p>
            <div class="tn-button-group">
                <a href="https://wa.me/{whatsapp}" target="_blank" class="btn-grad">
                    <span>Contactar por WhatsApp</span>
                </a>
                <a href="https://tecnovoa.cl/contacto/" class="btn-outline">
                    <span>Solicitar Presupuesto</span>
                </a>
            </div>
        </div>

        <!-- Keywords SEO discretas -->
        <div class="tn-seo-tags">
            Keywords: {keywords}
        </div>
    </div>
</div>"""

CSS_TEMPLATE = """.tecnovoa-wp-component {
    --bg-deep: #080b11;
    --bg-surface: #0f131a;
    --bg-surface-raised: #161b24;
    --border-hairline: rgba(255, 255, 255, 0.07);
    --border-active: rgba(42, 115, 255, 0.45);
    --text-primary: #f3f4f6;
    --text-secondary: #9ca3af;
    --text-muted: #6b7280;
    --accent-blue: #2a73ff;
    --accent-cyan: #00c8ff;
    --accent-purple: #5e6ad2;
    --accent-gradient: linear-gradient(135deg, #2a73ff 0%, #5e6ad2 50%, #00c8ff 100%);
    --shadow-soft: 0 12px 40px rgba(0, 0, 0, 0.6);
    --radius-md: 12px;
    --radius-lg: 16px;

    font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-deep);
    color: var(--text-primary);
    line-height: 1.6;
    padding: 0;
    margin: 0 auto;
    max-width: 1200px;
    border-radius: var(--radius-lg);
    overflow: hidden;
    border: 1px solid var(--border-hairline);
    box-shadow: var(--shadow-soft);
}

.tecnovoa-wp-component * {
    box-sizing: border-box;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Hero Header con Gradient Mesh */
.tn-hero {
    position: relative;
    padding: 6rem 2.5rem 5rem;
    text-align: center;
    background: radial-gradient(circle at top, rgba(94, 106, 210, 0.15) 0%, rgba(8, 11, 17, 0) 70%);
    border-bottom: 1px solid var(--border-hairline);
    overflow: hidden;
}

.tn-hero-mesh {
    position: absolute;
    top: -20%;
    left: 30%;
    width: 600px;
    height: 350px;
    background: var(--accent-gradient);
    filter: blur(140px);
    opacity: 0.15;
    pointer-events: none;
    z-index: 0;
}

.tn-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    background: rgba(94, 106, 210, 0.08);
    border: 1px solid rgba(94, 106, 210, 0.25);
    border-radius: 99px;
    font-size: 11px;
    font-weight: 600;
    color: var(--text-primary);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
    z-index: 1;
    position: relative;
}

.tn-badge-dot {
    width: 6px;
    height: 6px;
    background: var(--accent-cyan);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--accent-cyan);
    animation: tn-pulse 2s infinite;
}

@keyframes tn-pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.85); }
}

.tn-hero h1 {
    font-size: clamp(2.2rem, 5vw, 3.5rem);
    font-weight: 800;
    letter-spacing: -0.04em;
    margin: 0 auto 1.2rem;
    color: #ffffff !important;
    max-width: 900px;
    line-height: 1.1;
}

.tn-hero p {
    font-size: 1.15rem;
    color: var(--text-secondary);
    max-width: 800px;
    margin: 0 auto 2.5rem;
    font-weight: 400;
}

/* Container & Layout */
.tn-content {
    padding: 4rem 3rem;
}

.tn-intro-section {
    max-width: 800px;
    margin: 0 auto 4rem;
    text-align: center;
    font-size: 1.15rem;
    color: var(--text-secondary);
    border-bottom: 1px solid var(--border-hairline);
    padding-bottom: 3rem;
}

.tn-intro-section h2 {
    font-size: 1.8rem;
    color: #ffffff !important;
    margin-bottom: 1.5rem;
    font-weight: 700;
    letter-spacing: -0.02em;
}

.tn-section-header {
    margin-bottom: 3rem;
    text-align: center;
}

.tn-title-grad {
    background: var(--accent-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 700;
}

.tn-section-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #ffffff !important;
    letter-spacing: -0.02em;
    margin-bottom: 1rem;
}

/* Grid de Tarjetas (Linear/Raycast style) */
.tn-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-bottom: 5rem;
}

.tn-card {
    background-color: var(--bg-surface);
    border: 1px solid var(--border-hairline);
    border-radius: var(--radius-md);
    padding: 2.2rem;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    --mouse-x: 0px;
    --mouse-y: 0px;
}

.tn-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: var(--accent-gradient);
    opacity: 0;
    z-index: 2;
}

/* Cursor Glow Effect */
.tn-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(300px circle at var(--mouse-x) var(--mouse-y), rgba(0, 200, 255, 0.08), transparent 45%);
    z-index: 1;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.4s;
}

.tn-card:hover {
    background-color: var(--bg-surface-raised);
    border-color: var(--border-active);
    transform: translateY(-3px);
}

.tn-card:hover::before {
    opacity: 1;
}

.tn-card:hover::after {
    opacity: 1;
}

.tn-card-num {
    font-size: 0.8rem;
    font-weight: 700;
    color: var(--accent-cyan);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.5rem;
    z-index: 2;
}

.tn-card h3 {
    font-size: 1.3rem;
    font-weight: 600;
    color: #ffffff !important;
    margin-bottom: 1rem;
    margin-top: 0;
    z-index: 2;
}

.tn-card ul {
    list-style: none;
    padding: 0;
    margin: 0;
    z-index: 2;
}

.tn-card li {
    font-size: 0.9rem;
    color: var(--text-secondary);
    margin-bottom: 0.6rem;
    padding-left: 1.2rem;
    position: relative;
}

.tn-card li::before {
    content: "→";
    position: absolute;
    left: 0;
    color: var(--accent-blue);
}

/* Columnas de Beneficios y Sectores */
.tn-two-columns {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 4rem;
    margin-bottom: 5rem;
    border-top: 1px solid var(--border-hairline);
    padding-top: 4rem;
}

/* Listas Especiales */
.tn-list-styled {
    list-style: none;
    padding: 0;
    margin: 0;
}

.tn-list-styled li {
    position: relative;
    padding-left: 2.2rem;
    margin-bottom: 1.5rem;
    font-size: 1rem;
    color: var(--text-secondary);
    display: flex;
    align-items: flex-start;
}

.tn-list-icon {
    position: absolute;
    left: 0;
    top: 4px;
    color: var(--accent-cyan);
    width: 20px;
    height: 20px;
    background: rgba(0, 200, 255, 0.1);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.75rem;
    font-weight: bold;
}

.tn-list-text strong {
    color: #ffffff;
    font-weight: 600;
    display: block;
    margin-bottom: 0.25rem;
}

/* Sector Items list */
.tn-sector-list {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.tn-sector-item {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border-hairline);
    padding: 0.85rem 1rem;
    border-radius: 8px;
    font-size: 0.9rem;
    color: var(--text-primary);
    text-align: center;
    font-weight: 500;
}

.tn-sector-item:hover {
    border-color: var(--border-active);
    background: rgba(255, 255, 255, 0.04);
    transform: translateY(-1px);
}

/* ¿Por qué elegirnos? */
.tn-why-box {
    background-color: var(--bg-surface);
    border: 1px solid var(--border-hairline);
    border-radius: var(--radius-lg);
    padding: 3.5rem;
    margin-bottom: 5rem;
}

.tn-why-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 3rem;
    margin-top: 2.5rem;
}

.tn-why-card h4 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #ffffff !important;
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 0;
}

.tn-why-card p {
    font-size: 0.92rem;
    color: var(--text-secondary);
    margin: 0;
    line-height: 1.6;
}

/* Enlaces Relacionados para SEO e Interconexión */
.tn-seo-links {
    background: rgba(255, 255, 255, 0.01);
    border: 1px solid var(--border-hairline);
    border-radius: var(--radius-md);
    padding: 2.5rem;
    margin-bottom: 5rem;
}

.tn-seo-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
}

.tn-seo-col h4 {
    color: #ffffff !important;
    font-size: 1.15rem;
    margin-bottom: 1.2rem;
    border-left: 3px solid var(--accent-cyan);
    padding-left: 10px;
    margin-top: 0;
}

.tn-seo-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
}

.tn-seo-link-item a {
    font-size: 0.85rem;
    color: var(--text-secondary);
    background: var(--bg-surface);
    border: 1px solid var(--border-hairline);
    padding: 8px 16px;
    border-radius: 30px;
    display: inline-block;
    text-decoration: none;
}

.tn-seo-link-item a:hover {
    color: #ffffff;
    border-color: var(--accent-blue);
    background: var(--bg-surface-raised);
}

/* CTA Section */
.tn-cta {
    background: radial-gradient(circle at bottom right, rgba(42, 115, 255, 0.08) 0%, rgba(8, 11, 17, 0) 60%), var(--bg-surface);
    border: 1px solid var(--border-hairline);
    border-radius: var(--radius-lg);
    padding: 5rem 2rem;
    text-align: center;
    position: relative;
}

.tn-cta h3 {
    font-size: 2.4rem;
    font-weight: 800;
    color: #ffffff !important;
    letter-spacing: -0.03em;
    margin-bottom: 1rem;
    margin-top: 0;
}

.tn-cta p {
    font-size: 1.15rem;
    color: var(--text-secondary);
    max-width: 600px;
    margin: 0 auto 2.5rem;
}

/* Buttons */
.tn-button-group {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
}

.btn-grad {
    background: var(--accent-gradient);
    color: #ffffff !important;
    font-weight: 700;
    padding: 14px 36px;
    border-radius: 99px;
    text-decoration: none;
    box-shadow: 0 4px 20px rgba(94, 106, 210, 0.3);
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.btn-grad:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 24px rgba(94, 106, 210, 0.55);
}

.btn-outline {
    background: transparent;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-hairline);
    font-weight: 600;
    padding: 14px 36px;
    border-radius: 99px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.btn-outline:hover {
    border-color: var(--text-primary);
    background: rgba(255, 255, 255, 0.03);
    color: #ffffff !important;
}

/* Responsive Breakpoints */
@media (max-width: 860px) {
    .tn-two-columns {
        grid-template-columns: 1fr;
        gap: 3rem;
    }
    .tn-seo-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
}

@media (max-width: 580px) {
    .tn-content { padding: 3rem 1.5rem; }
    .tn-sector-list { grid-template-columns: 1fr; }
    .tn-why-box { padding: 2rem; }
}
"""

JS_TEMPLATE = """// Cursor Glow Effect para Tarjetas de Servicios Tecnovoa (Aesthetic Linear/Vercel)
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.tn-card');
    
    cards.forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });
});
"""

def parse_markdown(file_path):
    if not os.path.exists(file_path):
        print(f"Error: El archivo {file_path} no existe.")
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parsear Frontmatter
    frontmatter = {}
    metadata_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL | re.MULTILINE)
    body = content
    if metadata_match:
        meta_text = metadata_match.group(1)
        body = content[metadata_match.end():]
        for line in meta_text.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                frontmatter[k.strip()] = v.strip().strip('"').strip("'")

    # Si los metadatos SEO no están en el frontmatter, buscarlos en el cuerpo (Yoast SEO Blocks)
    title = frontmatter.get("title")
    description = frontmatter.get("description")
    keywords = frontmatter.get("keywords")
    badge = frontmatter.get("badge", "Infraestructura TI")
    whatsapp = frontmatter.get("whatsapp", "56997051793")

    if not title:
        title_match = re.search(r"<!--\s*SEO Title\s*-->\s*\n(.*?)\n", body, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).split("|")[0].strip()
        else:
            title = "Cableado Estructurado Empresarial"

    if not description:
        desc_match = re.search(r"<!--\s*Meta Description\s*-->\s*\n(.*?)\n", body, re.IGNORECASE)
        if desc_match:
            description = desc_match.group(1).strip()
        else:
            description = "Soluciones completas de infraestructura de red y conectividad certificada."

    if not keywords:
        kw_match = re.search(r"<!--\s*Additional Keywords\s*-->\s*\n(.*?)\n", body, re.IGNORECASE)
        if kw_match:
            keywords = kw_match.group(1).strip()
        else:
            keywords = "cableado estructurado chile, redes de datos, fibra optica"

    # Reemplazos de Markdown a HTML optimizados
    html_body = []
    in_list = False

    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            if in_list:
                html_body.append("</ul>")
                in_list = False
            i += 1
            continue

        if line.startswith("[[") and line.endswith("]]"):
            i += 1
            continue
        if line.startswith("<!--") or line.endswith("-->"):
            i += 1
            continue

        # Encabezados
        if line.startswith("# "):
            html_body.append(f'<h1 class="tn-section-title">{line[2:]}</h1>')
        elif line.startswith("## "):
            html_body.append(f'<h2 class="tn-section-title">{line[3:]}</h2>')
        elif line.startswith("### "):
            html_body.append(f'<h3 class="tn-section-title">{line[4:]}</h3>')
        elif line.startswith("#### "):
            html_body.append(f'<h4>{line[5:]}</h4>')
        # Listas de beneficios o sectores
        elif line.startswith("- ") or line.startswith("* ") or line.startswith("✓ "):
            if not in_list:
                html_body.append('<ul class="tn-list-styled">')
                in_list = True
            val = line[2:]
            
            bold_match = re.match(r"\*\*(.*?)\*\*(.*)", val)
            if bold_match:
                html_body.append(f'<li><span class="tn-list-icon">✓</span><div class="tn-list-text"><strong>{bold_match.group(1)}</strong>{bold_match.group(2)}</div></li>')
            else:
                html_body.append(f'<li><span class="tn-list-icon">✓</span><div class="tn-list-text">{val}</div></li>')
        else:
            if in_list:
                html_body.append("</ul>")
                in_list = False
            
            if line.lower().startswith("keywords:") or line.lower().startswith("focus keyphrase:") or line.lower().startswith("seo title:") or line.lower().startswith("meta description:") or line.lower().startswith("slug:") or line.lower().startswith("breadcrumbs:") or line.lower().startswith("social title:") or line.lower().startswith("social description:") or line.lower().startswith("additional keywords:") or line.lower().startswith("schema markup type:") or line.lower().startswith("canonical url:") or line.lower().startswith("robots:"):
                i += 1
                continue
            
            line = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", line)
            html_body.append(f'<p>{line}</p>')
        
        i += 1

    if in_list:
        html_body.append("</ul>")

    final_content = "\n".join(html_body)

    # Formatear plantillas
    html_out = HTML_TEMPLATE.format(
        title=title,
        description=description,
        keywords=keywords,
        badge=badge,
        whatsapp=whatsapp,
        content=final_content
    )

    return html_out, CSS_TEMPLATE, JS_TEMPLATE

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python md_to_wp.py <archivo.md>")
        sys.exit(1)

    md_file = sys.argv[1]
    parsed_data = parse_markdown(md_file)
    if parsed_data:
        html, css, js = parsed_data
        base_name = md_file.rsplit(".", 1)[0]
        
        # Guardar archivo HTML
        with open(base_name + "-HTML.html", "w", encoding="utf-8") as f:
            f.write(html)
            
        # Guardar archivo CSS
        with open(base_name + "-CSS.css", "w", encoding="utf-8") as f:
            f.write(css)
            
        # Guardar archivo JS
        with open(base_name + "-JS.js", "w", encoding="utf-8") as f:
            f.write(js)
            
        print(f"Éxito: Generados archivos separados (.html, .css, .js) para {base_name}")
