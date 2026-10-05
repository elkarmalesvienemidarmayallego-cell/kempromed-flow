from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# URL oficial de agendamiento de Kempromed Calendario
CALENDAR_URL = "https://calendar.app.google/MmtT61gVi86QjgoPA"

@app.get("/citas")
async def gestionar_citas(request: Request, modo: str = "directo"):
    """
    Ruta oficial de citas B2B Kempromed.
    Resuelve el error {"detail": "Not Found"} y garantiza el acceso 100% libre de fallos.
    """
    # Si viene en modo directo, ejecuta la redirección HTTP transparente inmediatamente
    if modo == "redirect":
        return RedirectResponse(url=CALENDAR_URL, status_code=307)

    # Interfaz híbrida de respuesta instantánea con triple respaldo
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>KemProMed | Citas & Agenda B2B</title>
        <!-- Redirección automática a nivel de navegador en 0 segundos -->
        <meta http-equiv="refresh" content="0;url={CALENDAR_URL}">
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
                padding: 20px;
                font-family: system-ui, -apple-system, sans-serif;
                background-color: var(--bg-color);
                color: var(--text-main);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 90vh;
                text-align: center;
            }}
            .card {{
                background-color: var(--card-bg);
                border: 1px solid #1f2937;
                padding: 30px;
                border-radius: 16px;
                max-width: 480px;
                width: 100%;
                box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
            }}
            .spinner {{
                border: 4px solid rgba(255, 255, 255, 0.1);
                width: 40px;
                height: 40px;
                border-radius: 50%;
                border-left-color: var(--primary);
                animation: spin 1s linear infinite;
                margin: 20px auto;
            }}
            @keyframes spin {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}
            .btn-agenda {{
                display: inline-block;
                margin-top: 15px;
                padding: 14px 28px;
                background-color: var(--primary);
                color: #ffffff;
                text-decoration: none;
                font-weight: 700;
                border-radius: 10px;
                font-size: 1rem;
                transition: transform 0.2s, background-color 0.2s;
            }}
            .btn-agenda:hover {{
                background-color: #0369a1;
                transform: translateY(-2px);
            }}
            p.info {{
                color: var(--text-muted);
                font-size: 0.9rem;
                margin-top: 15px;
            }}
        </style>
        <script>
            // Forzar redirección activa por JavaScript
            window.location.href = "{CALENDAR_URL}";
        </script>
    </head>
    <body>
        <div class="card">
            <h2>Conectando con Kempromed Calendario</h2>