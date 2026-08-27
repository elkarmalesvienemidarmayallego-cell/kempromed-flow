from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os
import stripe

app = FastAPI(
    title="Kempromed Flow | Motor B2B",
    description="Plataforma Comercial B2B",
    version="3.0.0"
)

# --- TU LÓGICA DE STRIPE Y PAGOS QUEDA INTACTA ABAJO ---
# (Aquí van tus funciones y webhooks que ya tenías programados)


# --- FACHADA CORPORATIVA KEMPROMED FLOW (RUTA RAÍZ) ---
@app.get("/", response_class=HTMLResponse)
def serve_kempromed_flow_landing():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kempromed Flow | Engine 100% Operativo</title>
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    </head>
    <body class="bg-slate-950 text-slate-100 min-h-screen font-sans">
        <div class="max-w-4xl mx-auto p-6 space-y-8">
            <header class="flex justify-between items-center border-b border-slate-800 pb-6">
                <div>
                    <span class="text-xs font-mono text-cyan-400 tracking-widest">KEMPROMED FLOW</span>
                    <h1 class="text-2xl md:text-3xl font-extrabold text-white mt-1">ENGINE 100% OPERATIVO</h1>
                </div>
                <div class="flex items-center gap-2 bg-emerald-950/50 border border-emerald-800 px-3 py-1.5 rounded-full">
                    <span class="w-2.5 h-2.5 bg-emerald-500 rounded-full animate-pulse"></span>
                    <span class="text-xs font-mono text-emerald-400 font-semibold">LIVE</span>
                </div>
            </header>

            <div class="bg-gradient-to-b from-slate-900 to-slate-950 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
                <p class="text-xs font-mono text-slate-400 mb-2">INFRAESTRUCTURA FINTECH B2B</p>
                <div class="bg-slate-950/80 border border-slate-800/80 rounded-xl p-5 my-4">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-xs font-mono text-cyan-400 bg-cyan-950 px-2.5 py-1 rounded">01 — DATA ORACLE</span>
                        <span class="text-xs text-emerald-400 font-mono">+1.92% 24h</span>
                    </div>
                    <div class="text-3xl md:text-4xl font-black font-mono text-white my-2">$62,847.33</div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
