from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# URL de Kempromed Calendario
CALENDAR_URL = "https://calendar.app.google/MmtT61gVi86QjgoPA"

@app.get("/citas")
async def gestionar_citas():
    """
    Ruta oficial de citas B2B Kempromed sin errores de despliegue.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>KemProMed | Citas & Agenda B2B</title>
        <meta http-equiv="refresh" content="0;url=https://calendar.app.google/MmtT61gVi86QjgoPA">
        <style>
            body {
                margin: 0;
                padding: 20px;
                font-family: system-ui, -apple-system, sans-serif;
                background-color: #0b0f19;
                color: #f8fafc;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 90vh;
                text-align: center;
            }
            .card {
                background-color: #111827;
                border: 1px solid #1f2937;
                padding: 30px;
                border-radius: 16px;
                max-width: 480px;
                width: 100%;
                box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
            }
            .spinner {
                border: 4px solid rgba(255, 255, 255, 0.1);
                width: 40px;
                height: 40px;
                border-radius: 50%;
                border-left-color: #0284c7;
                animation: spin 1s linear infinite;
                margin: 20px auto;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            .btn-agenda {
                display: inline-block;
                margin-top: 15px;
                padding: 14px 28px;
                background-color: #0284c7;
                color: #ffffff;
                text-decoration: none;
                font-weight: 700;
                border-radius: 10px;
                font-size: 1rem;
            }
            p.info {
                color: #94a3b8;
                font-size: 0.9rem;
                margin-top: 15px;
            }
        </style>
        <script>
            window.location.href = "https://calendar.app.google/MmtT61gVi86QjgoPA";
        </script>
    </head>
    <body>
        <div class="card">
            <h2>Conectando con Kempromed Calendario</h2>
            <div class="spinner"></div>
            <p class="info">Redirigiendo a la plataforma oficial de citas...</p>
            <a href="https://calendar.app.google/MmtT61gVi86QjgoPA" class="btn-agenda">
                Abrir Calendario Manualmente
            </a>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/citas/directo")
async def citas_directo():
    return RedirectResponse(url=CALENDAR_URL, status_code=307)
