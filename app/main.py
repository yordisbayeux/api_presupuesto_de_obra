from fastapi import FastAPI
from .routers import auth, obras, presupuestos, capitulos, partidas

app = FastAPI(title="API Presupuestos Obras")

app.include_router(auth.router)
app.include_router(obras.router)
app.include_router(presupuestos.router)
app.include_router(capitulos.router)
app.include_router(partidas.router)