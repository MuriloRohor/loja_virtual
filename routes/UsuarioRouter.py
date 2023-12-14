from fastapi import (
 APIRouter,
 Depends,
 HTTPException,
 Path,
 Request,
 status,
)

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models.Usuario import Usuario
from repositories.UsuarioRepo import UsuarioRepo
from util.security import obter_usuario_logado

router = APIRouter(prefix="/usuario")

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_index(
    request: Request,
    usuario: Usuario = Depends(obter_usuario_logado),
):
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if not usuario.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    usuarios = UsuarioRepo.obter_todos()
    return templates.TemplateResponse(
        "usuario/index.html",
        {"request": request, "usuario": usuario, "usuarios": usuarios},
    )
    

@router.get("/excluir/{id_usuario:int}", response_class=HTMLResponse)
async def get_excluir(
    request: Request,
    id_usuario: int = Path(),
    usuario: Usuario = Depends(obter_usuario_logado),
):
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if not usuario.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
    usuario_excluir = UsuarioRepo.obter_por_id(id_usuario)
    return templates.TemplateResponse(
        "usuario/excluir.html",
        {"request": request, "usuario": usuario, "usuario_excluir": usuario_excluir})
