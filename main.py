from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routes.RootRouter import router as rootRouter
from routes.UsuarioRouter import router as usuarioRouter
from routes.ProdutoRouter import router as produtoRouter

from util.security import atualizar_cookie_autenticacao
from util.excecoes import configurar_paginas_de_erro

from repositories.UsuarioRepo import UsuarioRepo
from repositories.ProdutoRepo import ProdutoRepo

UsuarioRepo.criar_tabela()
UsuarioRepo.criar_administrador_padrao()
UsuarioRepo.criar_usuario_padrao()
ProdutoRepo.criar_tabela()



app = FastAPI()

app.middleware("http")(atualizar_cookie_autenticacao)
configurar_paginas_de_erro(app)

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(rootRouter)
app.include_router(usuarioRouter)
app.include_router(produtoRouter)


if __name__ == "__main__":
    uvicorn.run(app="main:app",host="localhost", reload=True, port=8000)