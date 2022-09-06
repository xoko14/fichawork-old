import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api.routes import setup_routes

os.system("cd client && npm run build");

app = FastAPI()
setup_routes(app)
app.mount('', StaticFiles(directory="client/dist/", html=True), name="static")
