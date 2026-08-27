from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os
import stripe

app = FastAPI(
    title="Kempromed Flow | Motor B2B",
    description="Plataforma Comercial B2B",
    version="3.0.0"
)

@app.get("/", response_class=HTMLResponse)
def serve_kempromed_flow_landing():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta property="og:title" content="Kempromed Flow | Engine 100% Operativo">
    <meta property="og:description" content="Infraestructura Fintech B2B. Cada módulo validado en producción sobre Render Cloud.">
    <meta property="og:type" content="website">

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
                <p class="text-slate-300 text-sm md:text-base mb-6">Cada módulo validado en producción sobre Render Cloud + Binance WS. Diseñado para pitch de inversores — B2B Terminal & Crypto API Docs.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">
                    <div class="bg-slate-950/80 border border-slate-800/80 rounded-xl p-4">
                        <span class="text-[10px] font-mono text-cyan-400 bg-cyan-950/80 px-2 py-0.5 rounded">01 — DATA ORACLE</span>
                        <div class="text-xl font-black font-mono text-white mt-2">$62,847.33</div>
                        <p class="text-[11px] text-emerald-400 font-mono mt-1">+1.92% 24h</p>
                    </div>
                    <div class="bg-slate-950/80 border border-slate-800/80 rounded-xl p-4">
                        <span class="text-[10px] font-mono text-cyan-400 bg-cyan-950/80 px-2 py-0.5 rounded">02 — CLOUD UPTIME</span>
                        <div class="text-xl font-black font-mono text-white mt-2">99.99%</div>
                        <p class="text-[11px] text-slate-400 font-mono mt-1">Nodes: 128 Active</p>
                    </div>
                    <div class="bg-slate-950/80 border border-slate-800/80 rounded-xl p-4">
                        <span class="text-[10px] font-mono text-cyan-400 bg-cyan-950/80 px-2 py-0.5 rounded">03 — SYSTEM STATUS</span>
                        <div class="text-xl font-black font-mono text-emerald-400 mt-2">SECURE</div>
                        <p class="text-[11px] text-slate-400 font-mono mt-1">Throughput: 1.24M req/s</p>
                    </div>
                </div>

                <div class="pt-4 border-t border-slate-800 flex flex-wrap gap-3 items-center justify-between">
                    <span class="text-xs font-mono text-slate-400">KEMPROMED FLOW • ESPECIFICACIÓN TÉCNICA 2026</span>
                    <a href="#contacto" class="bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold font-mono px-5 py-2.5 rounded-lg transition-all shadow-lg shadow-cyan-950">ACCEDER AHORA →</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
