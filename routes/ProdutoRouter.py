from fastapi import (
 APIRouter,
 Depends,
 HTTPException,
 Request,
 status,
)
from fastapi.templating import Jinja2Templates
from models.Usuario import Usuario
from repositories.ProdutoRepo import ProdutoRepo
from util.security import obter_usuario_logado

router = APIRouter(prefix="/produto")

templates = Jinja2Templates(directory="templates")



@router.get("/")
async def get_index(
    request: Request,
    usuario: Usuario = Depends(obter_usuario_logado),
):
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if not usuario.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
    produtos = ProdutoRepo.obter_todos()
    return templates.TemplateResponse(
        "produto/index.html",
        {"request": request, "usuario": usuario, "produtos": produtos},
    )
