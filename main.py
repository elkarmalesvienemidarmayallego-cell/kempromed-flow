import os
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Dict, Any
import httpx

# 1. Configuración principal de la API
app = FastAPI(
    title="Kempromed Flow API",
    description="Infraestructura B2B / SaaS para Servicios de Salud, Monetización y Soluciones Cripto.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 2. Configuración de Plantillas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
# --- VALIDACIÓN OFICIAL DMCA ---
@app.get("/dmca-validation.html", response_class=HTMLResponse)
async def dmca_validation():
    return "eT15SEdmUjB5dVZFajhzK25mQ2JXdU9jV3BraUdUWkJMWE01bDROcKJXND01"
# 3. Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELOS DE DATOS (Pydantic) ---

class HealthCheckResponse(BaseModel):
    status: str = Field(..., example="ok")
    service: str = Field(..., example="Kempromed Flow Engine")
    environment: str = Field(..., example="production")

class HealthModuleRequest(BaseModel):
    client_id: str = Field(..., example="CANACINTRA-001")
    service_type: str = Field(..., example="telemedicina")

# --- ENDPOINT VISTA DASHBOARD (LANDING PAGE) ---

@app.get("/", response_class=HTMLResponse, tags=["Landing Page"])
async def render_dashboard(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )

# --- ENDPOINTS CORE ---

@app.get("/health", response_model=HealthCheckResponse, tags=["Monitoreo"])
async def health_check():
    """Endpoint ligero para verificar disponibilidad del servidor."""
    return {
        "status": "ok",
        "service": "Kempromed Flow Engine",
        "environment": "production"
    }

# --- MÓDULO CRIPTO ---

@app.get("/api/v1/crypto/price", tags=["Servicios Cripto"])
async def get_crypto_price(symbol: str = "bitcoin", currency: str = "usd") -> Dict[str, Any]:
    """
    Obtiene la cotización en tiempo real de criptomonedas utilizando llamadas asíncronas.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies={currency.lower()}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=5.0)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Error al conectar con la API de mercados cripto."
                )
            data = response.json()
            if not data or symbol.lower() not in data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Símbolo '{symbol}' no encontrado."
                )
            
            return {
                "success": True,
                "asset": symbol.lower(),
                "currency": currency.lower(),
                "price": data[symbol.lower()][currency.lower()]
            }
        except httpx.RequestError:
            raise HTTPException(
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                detail="Tiempo de espera agotado al consultar el mercado."
            )

# --- MÓDULO SALUD & B2B ---

@app.post("/api/v1/health-services/register", tags=["Infraestructura Salud B2B"])
async def register_health_service(payload: HealthModuleRequest):
    """
    Punto de entrada para la integración de módulos de salud empresarial.
    """
    return {
        "success": True,
        "message": f"Servicio '{payload.service_type}' registrado exitosamente para el cliente '{payload.client_id}'.",
        "integration_status": "Active"
    }
import sqlite3
from fastapi import Form

# Inicializar Base de Datos para K-AURA
def init_db():
    conn = sqlite3.connect("kaura.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS perfiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pseudonimo TEXT NOT NULL,
            correo TEXT NOT NULL,
            estado TEXT DEFAULT 'Pendiente',
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

# API: Guardar formulario de K-AURA
@app.post("/api/solicitar-acceso")
async def solicitar_acceso(pseudonimo: str = Form(...), correo: str = Form(...)):
    conn = sqlite3.connect("kaura.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO perfiles (pseudonimo, correo) VALUES (?, ?)", (pseudonimo, correo))
    conn.commit()
    conn.close()
    return {"status": "ok", "message": "Solicitud recibida con éxito"}

# API: Panel de administración para ver postulantes
@app.get("/admin/perfiles")
async def ver_perfiles():
    conn = sqlite3.connect("kaura.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, pseudonimo, correo, estado, fecha FROM perfiles ORDER BY id DESC")
    filas = cursor.fetchall()
    conn.close()
    
    perfiles = [
        {"id": f[0], "pseudonimo": f[1], "correo": f[2], "estado": f[3], "fecha": f[4]}
        for f in filas
    ]
    return {"total_postulantes": len(perfiles), "postulantes": perfiles}
    import os
import stripe
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# Si app ya está definida arriba, solo asegúrate de incluir esta línea y el endpoint:
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@app.get("/checkout")
def cobrar_cien():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'mxn',
                'product_data': {'name': 'Acceso Kempromed Flow'},
                'unit_amount': 10000,  # $100.00 MXN
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://kempromed-flow.onrender.com/?status=success',
        cancel_url='https://kempromed-flow.onrender.com/?status=cancel',
    )
    return RedirectResponse(url=session.url)
