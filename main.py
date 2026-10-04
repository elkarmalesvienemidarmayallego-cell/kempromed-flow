import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="KemProMed Ecosystem Hub", version="2.0.0")

@app.get("/", response_class=HTMLResponse)
async def serve_hub_landing():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>KemProMed // Central Hub & Service Directory</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #060911; color: #f1f5f9; min-height: 100vh; display: flex; flex-direction: column; justify-content: space-between; }
            
            /* HEADER / NAV */
            header { background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(10px); border-bottom: 1px solid #1e293b; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
            .logo-title { font-size: 1.5rem; font-weight: 800; letter-spacing: 2px; color: #38bdf8; display: flex; align-items: center; gap: 10px; }
            .status-badge { background: rgba(34, 197, 94, 0.1); border: 1px solid #22c55e; color: #22c55e; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; }

            /* HERO SECTION */
            .hero { text-align: center; max-width: 900px; margin: 60px auto 40px auto; padding: 0 20px; }
            .hero h1 { font-size: 2.8rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 15px; background: linear-gradient(135deg, #f8fafc 0%, #94a3b8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            .hero p { color: #94a3b8; font-size: 1.2rem; line-height: 1.6; }

            /* GRID DE BIFURCACIÓN DE SERVICIOS */
            .services-grid { max-width: 1100px; margin: 0 auto 60px auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; padding: 0 20px; }
            
            .card { background: #0f172a; border: 1px solid #1e293b; border-radius: 14px; padding: 35px 25px; transition: all 0.3s ease; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden; }
            .card:hover { transform: translateY(-6px); border-color: #38bdf8; box-shadow: 0 10px 30px -10px rgba(56, 189, 248, 0.2); }
            
            .card-tag { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #38bdf8; margin-bottom: 12px; }
            .card h3 { font-size: 1.4rem; color: #f8fafc; margin-bottom: 12px; }
            .card p { color: #94a3b8; font-size: 0.95rem; line-height: 1.5; margin-bottom: 25px; }

            /* BOTONES DE REDIRECCIÓN */
            .btn { display: inline-block; text-align: center; background: #2563eb; color: #ffffff; text-decoration: none; padding: 12px 24px; border-radius: 8px; font-weight: 700; font-size: 0.95rem; transition: background 0.2s ease; }
            .btn:hover { background: #1d4ed8; }
            .btn-outline { background: transparent; border: 1px solid #334155; color: #f8fafc; }
            .btn-outline:hover { background: #1e293b; border-color: #475569; }

            /* FOOTER OFICIAL */
            footer { background: #04070e; border-top: 1px solid #1e293b; padding: 40px 20px 20px 20px; font-size: 0.9rem; }
            .footer-container { max-width: 1100px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 30px; }
            .footer-col h4 { color: #f8fafc; margin-bottom: 12px; font-size: 1rem; letter-spacing: 1px; }
            .footer-col p { color: #94a3b8; margin-bottom: 6px; line-height: 1.5; }
            .copyright { max-width: 1100px; margin: 30px auto 0 auto; padding-top: 20px; border-top: 1px solid #0f172a; text-align: center; color: #64748b; font-size: 0.8rem; }
        </style>
    </head>
    <body>

        <!-- NAVEGACIÓN Y CABECERA -->
        <header>
            <div class="logo-title">
                <span>KEMPROMED</span>
            </div>
            <div class="status-badge">
                ● INFRAESTRUCTURA ACTIVA
            </div>
        </header>

        <!-- SECCIÓN PRINCIPAL DE PRESENTACIÓN -->
        <div class="hero">
            <h1>Ecosistema de Tecnologías Autónomas</h1>
            <p>Portal central de acceso a las plataformas de ingeniería, monitoreo en blockchain y gestión de servicios de KemProMed.</p>
        </div>

        <!-- BIFURCACIÓN DE SERVICIOS Y MOTORES -->
        <div class="services-grid">

            <!-- MODULO 1: Q-ENGINE / K-AURA -->
            <div class="card">
                <div>
                    <div class="card-tag">FINTECH & BLOCKCHAIN</div>
                    <h3>Q-Engine Krypto</h3>
                    <p>Motor determinista de monitoreo de liquidez y gestión de riesgo en la red Polygon. Control estricto de Stop Loss (80%) y Take Profit (100%).</p>
                </div>
                <a href="https://k-aura-ser.onrender.com" target="_blank" class="btn">Acceder al Control Panel →</a>
            </div>

            <!-- MODULO 2: ASISTENTE DE IA INDUSTRIAL -->
            <div class="card">
                <div>
                    <div class="card-tag">INTELIGENCIA ARTIFICIAL</div>
                    <h3>KemProMed Flow</h3>
                    <p>Asistente virtual industrial potenciado por la API de Gemini. Análisis de gemelos digitales, cálculo de entropía y optimización en tiempo real.</p>
                </div>
                <a href="https://kempromed.ai.studio" target="_blank" class="btn btn-outline">Ingresar a Flow AI →</a>
            </div>

            <!-- MODULO 3: PLATAFORMA DE CITAS Y SERVICIOS -->
            <div class="card">
                <div>
                    <div class="card-tag">GESTIÓN & SAAS</div>
                    <h3>Plataforma de Citas</h3>
                    <p>Módulo de agendamiento de servicios, consulta de disponibilidad y cobros automatizados con integración directa a Stripe.</p>
                </div>
                <a href="/citas" class="btn btn-outline">Gestionar Citas →</a>
            </div>

        </div>

        <!-- FOOTER INSTITUCIONAL -->
        <footer>
            <div class="footer-container">
                <div class="footer-col" style="max-width: 380px;">
                    <h4>KEMPROMED</h4>
                    <p>Desarrollo de arquitectura tecnológica SaaS, motores de gestión de riesgo en blockchain e integración de inteligencia artificial para el sector industrial y comercial.</p>
                </div>
                <div class="footer-col">
                    <h4>INFORMES Y ATENCIÓN</h4>
                    <p>🇲🇽 México: +52 653 155 2063</p>
                    <p>🇺🇸 USA / Int: +1 661 750 8599</p>
                    <p>✉️ Correo: direccion@kempromed.com</p>
                </div>
            </div>
            <div class="copyright">
                © 2026 KemProMed. Todos los derechos reservados.
            </div>
        </footer>

    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
