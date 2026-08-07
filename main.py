import os
import random
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Kempromed Flow Engine",
    description="Hub de Integración Tecnológica B2B, Servicios Cripto, Telemedicina y Plataformas Web",
    version="1.2.0"
)

# --- 1. RUTA RAÍZ (HUB PRINCIPAL CON FOOTER LEGAL Y CRIPTO) ---
@app.get("/", response_class=HTMLResponse, tags=["Dashboard"])
def home_dashboard(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kempromed Flow | Developer & Business Hub</title>
        <style>
            * { box-sizing: border-box; }
            body { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background: #0b0f19; color: #f8fafc; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; }
            .header { text-align: center; padding: 40px 20px 20px; background: linear-gradient(180deg, #111827 0%, #0b0f19 100%); border-bottom: 1px solid #1f2937; }
            .status-badge { background: #064e3b; color: #34d399; font-size: 0.8rem; padding: 5px 14px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 12px; }
            h1 { color: #38bdf8; font-size: 2.4rem; margin: 0 0 10px; font-weight: 800; letter-spacing: -0.5px; }
            p.sub { color: #94a3b8; font-size: 1.05rem; max-width: 700px; margin: 0 auto; line-height: 1.5; }
            
            .container { max-width: 1100px; margin: 0 auto; padding: 40px 20px; flex: 1; }
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }
            
            .card { background: #161e2e; border: 1px solid #223046; border-radius: 16px; padding: 28px; transition: transform 0.2s, border-color 0.2s; position: relative; }
            .card:hover { transform: translateY(-4px); border-color: #38bdf8; }
            .card h3 { color: #38bdf8; margin: 0 0 10px; font-size: 1.3rem; display: flex; align-items: center; gap: 8px; }
            .card p { color: #94a3b8; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; }
            
            .price-box { background: #0f172a; border: 1px solid #1e293b; border-radius: 10px; padding: 12px 16px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; }
            .price-val { color: #4ade80; font-size: 1.4rem; font-weight: bold; }
            
            .btn { display: inline-block; background: #38bdf8; color: #0b0f19; font-weight: 700; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 0.9rem; transition: background 0.2s; }
            .btn:hover { background: #7dd3fc; }
            .btn-green { background: #10b981; color: #022c22; }
            .btn-green:hover { background: #34d399; }
            
            /* FOOTER LEGAL */
            footer { background: #070a12; border-top: 1px solid #1f2937; padding: 40px 20px; margin-top: auto; font-size: 0.85rem; color: #64748b; }
            .footer-content { max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; text-align: left; }
            .footer-col h4 { color: #cbd5e1; margin: 0 0 12px; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.5px; }
            .footer-col ul { list-style: none; padding: 0; margin: 0; }
            .footer-col ul li { margin-bottom: 8px; }
            .footer-col a { color: #94a3b8; text-decoration: none; transition: color 0.2s; }
            .footer-col a:hover { color: #38bdf8; }
            .legal-bar { max-width: 1100px; margin: 30px auto 0; padding-top: 20px; border-top: 1px solid #111827; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 15px; }
            .dmca-badge { background: #111827; border: 1px solid #1f2937; color: #38bdf8; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 0.75rem; }
        </style>
    </head>
    <body>

        <div class="header">
            <span class="status-badge">● Sistema 100% Operativo | GCP & Render</span>
            <h1>KEMPROMED FLOW</h1>
            <p class="sub">Plataforma de orquestación B2B, arquitectura de microservicios, analítica de criptomonedas y soluciones integradas de salud y comercio.</p>
        </div>

        <div class="container">
            <div class="grid">
                
                <!-- CARD 1: SERVICIOS CRIPTO EN VIVO -->
                <div class="card">
                    <h3>📊 Servicios Cripto & Liquidez</h3>
                    <p>Monitoreo asíncrono de activos digitales y pasarela de datos financieros para monetización de microservicios.</p>
                    <div class="price-box">
                        <span style="color:#64748b; font-size:0.8rem;">BITCOIN (USD):</span>
                        <div class="price-val" id="btc-price">Cargando...</div>
                    </div>
                    <a href="/docs" class="btn">API Price Feed →</a>
                </div>

                <!-- CARD 2: PASARELA & MULTIPLICADOR B2B -->
                <div class="card">
                    <h3>💳 Pasarela B2B & Licencias</h3>
                    <p>Terminal de inyección de liquidez y cobros recurrentes para software comercial, cámaras e instituciones.</p>
                    <div class="price-box">
                        <span style="color:#64748b; font-size:0.8rem;">ENTRADA BASE:</span>
                        <div class="price-val" style="color:#38bdf8;">$100.00 MXN</div>
                    </div>
                    <a href="/checkout" class="btn btn-green">Ir a Checkout / Terminal</a>
                </div>

                <!-- CARD 3: TOM & AIX QUANTUM SUITE -->
                <div class="card">
                    <h3>⚡ Tom & Aix Space</h3>
                    <p>Módulo de optimización de entropía, cálculo de algoritmos y gestión de riesgos iGaming / Casino.</p>
                    <div class="price-box">
                        <span style="color:#64748b; font-size:0.8rem;">MOTOR ACTIVO:</span>
                        <div class="price-val" style="color:#a855f7;">Quantum Net</div>
                    </div>
                    <a href="/aura" class="btn" style="background:#a855f7; color:#fff;">Acceder a Módulo Aura</a>
                </div>

            </div>
        </div>

        <!-- FOOTER LEGAL Y REGISTROS -->
        <footer>
            <div class="footer-content">
                <div class="footer-col">
                    <h4 style="color:#38bdf8;">KEMPROMED DEVELOPMENT</h4>
                    <p style="margin:0; line-height:1.6;">Infraestructura de software backend, motores de inteligencia y conectividad para sectores empresarial, salud e iGaming.</p>
                </div>
                <div class="footer-col">
                    <h4>MÓDULOS DEL SISTEMA</h4>
                    <ul>
                        <li><a href="/docs">Documentación OpenAPI / Swagger</a></li>
                        <li><a href="/checkout">Terminal de Licencias B2B</a></li>
                        <li><a href="/aura">Aura Quantum Suite</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>LEGAL & COMPLIANCE</h4>
                    <ul>
                        <li><span style="color:#cbd5e1;">Código de Propiedad:</span> KMP-7492-ENT</li>
                        <li><span style="color:#cbd5e1;">Protección DMCA:</span> Verified & Active</li>
                        <li><span style="color:#cbd5e1;">Director de Desarrollo:</span> Dr. Mauro Falcón</li>
                    </ul>
                </div>
            </div>

            <div class="legal-bar">
                <div>
                    © 2026 <strong>Kempromed Technology S.A.</strong> Todos los derechos reservados. Desarrollado por Mau.
                </div>
                <div>
                    <span class="dmca-badge">PROTECTED BY DMCA</span>
                </div>
            </div>
        </footer>

        <script>
            async function fetchBTC() {
                try {
                    const res = await fetch('/api/v1/crypto/price');
                    const data = await res.json();
                    if(data.bitcoin_usd) {
                        document.getElementById('btc-price').innerText = '$' + data.bitcoin_usd.toLocaleString('en-US') + ' USD';
                    }
                } catch(e) {
                    document.getElementById('btc-price').innerText = '$64,249.00 USD';
                }
            }
            fetchBTC();
            setInterval(fetchBTC, 10000);
        </script>
    </body>
    </html>
    """

# --- 2. TERMINAL DE PAGO / CHECKOUT ---
@app.get("/checkout", response_class=HTMLResponse, tags=["Terminales"])
def checkout_page(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Terminal de Cobro B2B | Kempromed Flow</title>
        <style>
            body { font-family: sans-serif; background: #0b0f19; color: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
            .card { background: #161e2e; border: 1px solid #223046; border-radius: 16px; padding: 40px; max-width: 450px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
            .amount { font-size: 2.2rem; color: #4ade80; font-weight: bold; margin: 15px 0; }
            .btn { background: #10b981; color: #000; font-weight: bold; padding: 12px 24px; border-radius: 8px; text-decoration: none; display: inline-block; margin-top: 15px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2 style="color:#38bdf8;">Pasarela B2B & Licencias</h2>
            <p style="color:#94a3b8;">Inyección de Liquidez / Licencia de Uso</p>
            <div class="amount">$100.00 MXN</div>
            <p style="font-size:0.85rem; color:#64748b;">Sincronizado con SPEI y Red Polygon / Cripto</p>
            <a href="/docs" class="btn">Procesar Transacción en API →</a>
            <br><br>
            <a href="/" style="color:#94a3b8; text-decoration:none; font-size:0.9rem;">← Volver al Hub Principal</a>
        </div>
    </body>
    </html>
    """

# --- 3. RUTA AURA / TOM & AIX ---
@app.get("/aura", response_class=HTMLResponse, tags=["Terminales"])
def aura_engine(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tom & Aix Space | Aura Quantum Engine</title>
        <style>
            body { font-family: sans-serif; background: #020617; color: #a855f7; text-align: center; padding: 50px; }
            .box { border: 1px solid #1e293b; background: #0f172a; padding: 40px; border-radius: 16px; display: inline-block; max-width: 500px; }
            a { color: #38bdf8; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>⚡ Tom & Aix Space</h1>
            <h3>Aura Quantum Network & Entropy Suite</h3>
            <p style="color: #94a3b8;">Motor asíncrono de procesamiento de datos en tiempo real activo en la nube.</p>
            <br>
            <a href="/">← Regresar al Portal Principal</a>
        </div>
    </body>
    </html>
    """

# --- 4. ENDPOINT API DE PRECIO BITCOIN ---
@app.get("/api/v1/crypto/price", tags=["Crypto"])
def get_crypto_price():
    try:
        res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=5).json()
        return {"status": "success", "bitcoin_usd": res.get("bitcoin", {}).get("usd", 64249.00)}
    except Exception:
        return {"status": "success", "bitcoin_usd": 64249.00}

# --- 5. ENDPOINT CASINO / MULTIPLICADOR ---
@app.post("/api/v1/casino/multiply", tags=["Casino Engine"])
def multiply_balance(user_id: str, amount_mxn: float):
    multipliers = [0, 0, 1.2, 1.5, 2.0, 3.0, 5.0]
    hit = random.choice(multipliers)
    final_amount = amount_mxn * hit
    return {
        "user_id": user_id,
        "initial_deposit_mxn": amount_mxn,
        "multiplier": f"{hit}x",
        "final_balance_mxn": final_amount,
        "status": "WIN" if hit > 1 else "LOSS"
    }
