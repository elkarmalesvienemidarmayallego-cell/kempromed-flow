from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

# Enlace de destino directo para libros / contenido
LINK_LIBROS = "https://www.meta.ai/share/a/d45a7a41-6243-4cf5-9229-70bfd34bb035?utm_campaign=wa_artifact_share"

@app.get("/citas")
def redirect_citas_to_books():
    """
    Redirige el tráfico de /citas directamente al enlace compartido.
    """
    return RedirectResponse(url=LINK_LIBROS, status_code=302)

@app.get("/api/v1/payment/terminal")
def get_payment_terminal():
    return {
        "status": "operational",
        "merchant": "KemProMed Ecosistema B2B",
        "channels": {
            "spei_directo": {
                "banco": "Banco Azteca",
                "clabe": "127180016456259755",
                "beneficiario": "KemProMed",
                "moneda": "MXN"
            },
            "stripe_card": {
                "status": "active",
                "moneda": "MXN / USD"
            },
            "trust_wallet_crypto": {
                "network": "Polygon Mainnet",
                "accepted_tokens": ["USDT", "POL", "MATIC"]
            }
        }
    }
