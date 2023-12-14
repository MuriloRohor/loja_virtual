from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routes.RootRouter import router as rootRouter
from routes.UsuarioRouter import router as usuarioRouter 

from util.security import atualizar_cookie_autenticacao

from repositories.UsuarioRepo import UsuarioRepo

UsuarioRepo.criar_tabela()
UsuarioRepo.criar_administrador_padrao()
UsuarioRepo.criar_usuario_padrao()

app = FastAPI()

app.middleware("http")(atualizar_cookie_autenticacao)

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(rootRouter)
app.include_router(usuarioRouter)


if __name__ == "__main__":
    uvicorn.run(app="main:app",host="localhost", reload=True, port=8000)