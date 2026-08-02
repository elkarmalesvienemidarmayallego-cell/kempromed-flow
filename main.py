from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>KEMPROMED FLOW</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-black text-cyan-400 min-h-screen flex flex-col justify-center items-center p-6">
        
        <!-- Header Principal -->
        <div class="p-8 border border-cyan-500/30 rounded-2xl bg-gray-950 text-center max-w-3xl w-full shadow-lg shadow-cyan-500/10 mb-8">
            <h1 class="text-4xl font-bold mb-2 tracking-wider text-cyan-300">⚡ KEMPROMED.FLOW</h1>
            <p class="text-gray-400 text-sm mb-4">AETHER Risk Engine & Security Systems</p>
            <div class="inline-block px-4 py-1 bg-cyan-950 border border-cyan-500/50 text-cyan-300 rounded-full text-xs font-semibold animate-pulse">
                • SERVIDOR OPERATIVO EN GOOGLE CLOUD
            </div>
        </div>

        <!-- Menú de Microservicios -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-3xl w-full">
            
            <!-- Card 1 -->
            <a href="#" class="group p-6 border border-cyan-500/20 rounded-xl bg-gray-900/60 hover:bg-cyan-950/40 hover:border-cyan-400 transition-all duration-300 text-center">
                <div class="text-3xl mb-3">🛡️</div>
                <h3 class="text-lg font-bold text-cyan-300 group-hover:text-cyan-200">AETHER Risk</h3>
                <p class="text-gray-400 text-xs mt-2">Motor de evaluación y amenazas en tiempo real.</p>
            </a>

            <!-- Card 2 -->
            <a href="#" class="group p-6 border border-cyan-500/20 rounded-xl bg-gray-900/60 hover:bg-cyan-950/40 hover:border-cyan-400 transition-all duration-300 text-center">
                <div class="text-3xl mb-3">📊</div>
                <h3 class="text-lg font-bold text-cyan-300 group-hover:text-cyan-200">Analytics Hub</h3>
                <p class="text-gray-400 text-xs mt-2">Métricas avanzadas y telemetría de red.</p>
            </a>

            <!-- Card 3 -->
            <a href="/docs" target="_blank" class="group p-6 border border-emerald-500/30 rounded-xl bg-gray-900/60 hover:bg-emerald-950/40 hover:border-emerald-400 transition-all duration-300 text-center">
                <div class="text-3xl mb-3">⚙️</div>
                <h3 class="text-lg font-bold text-emerald-400 group-hover:text-emerald-300">API Docs</h3>
                <p class="text-gray-400 text-xs mt-2">Documentación interactiva de FastAPI (Swagger).</p>
            </a>

        </div>

        <footer class="mt-12 text-gray-600 text-xs">
            KEMPROMED Systems © 2026 — Todos los derechos reservados.
        </footer>

    </body>
    </html>
    """
