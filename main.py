from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# Enlace oficial de agendamiento de Kempromed Calendario
CALENDAR_URL = "https://calendar.app.google/MmtT61gVi86QjgoPA"

@app.get("/citas", response_class=HTMLResponse)
async def citas_page(request: Request):
    """
    Ruta para la Plataforma de Citas de KemProMed.
    Despliega la interfaz de agendamiento sin posibilidad de error 404.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>KemProMed | Agendamiento de Citas</title>
        <style>
            :root {{
                --bg-color: #0b0f19;
                --card-bg: #111827;
                --primary: #0284c7;
                --text-main: #f8fafc;
                --text-muted: #94a3b8;
            }}
            body {{
                margin: 0;
                padding: 0;
                font-family: system-ui, -apple-system, sans-serif;
                background-color: var(--bg-color);
                color: var(--text-main);
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
            }}
            header {{
                width: 100%;
                padding: 20px;
                text-align: center;
                background-color: var(--card-bg);
                border-bottom: 1px solid #1f2937;
            }}
            h1 {{
                margin: 0;
                font-size: 1.5rem;
                color: var(--text-main);
            }}
            p {{
                color: var(--text-muted);
                font-size: 0.9rem;
                margin-top: 5px;
            }}
            .container {{
                width: 100%;
                max-width: 900px;
                flex: 1;
                padding: 20px;
                box-sizing: border-box;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            iframe {{
                width: 100%;
                height: 700px;
                border: none;
                border-radius: 12px;
                background-color: #ffffff;
            }}
            .btn-fallback {{
                display: inline-block;
                margin-top: 15px;
                padding: 12px 24px;
                background-color: var(--primary);
                color: white;
                text-decoration: none;
                font-weight: 600;
                border-radius: 8px;
                transition: background 0.2s;
            }}
            .btn-fallback:hover {{
                background-color: #0369a1;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Plataforma de Citas KemProMed</h1>
            <p>Consulta de disponibilidad y agendamiento de servicios B2B</p>
        </header>

        <div class="container">
            <!-- Calendario de Google Incrustado -->
            <iframe src="{CALENDAR_URL}" loading="lazy"></iframe>

            <!-- Botón de respaldo por si el navegador bloquea iframes -->
            <a href="{CALENDAR_URL}" target="_blank" class="btn-fallback">
                Abrir Agendador en Pantalla Completa
            </a>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Opcional: Redirección directa sin interfaz
@app.get("/citas/directo")
async def citas_directo():
    return RedirectResponse(url=CALENDAR_URL)
