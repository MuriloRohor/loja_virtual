from io import BytesIO
from fastapi import (
 APIRouter,
 Depends,
 File,
 Form,
 HTTPException,
 Request,
 UploadFile,
 status,
)
from fastapi.templating import Jinja2Templates
from models.Produto import Produto
from models.Usuario import Usuario
from repositories.ProdutoRepo import ProdutoRepo
from util.imagem import transformar_em_quadrada
from util.mensagem import redirecionar_com_mensagem
from util.security import obter_usuario_logado

from PIL import Image

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
    
@router.get("/inserir")
async def get_inserir(
    request: Request,
    usuario: Usuario = Depends(obter_usuario_logado),
):
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if not usuario.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
 
    return templates.TemplateResponse(
        "produto/inserir.html",
        {"request": request, "usuario": usuario},
    )
    
    
@router.post("/inserir")
async def post_inserir(
    nome: str = Form(...),
    arquivoImagem: UploadFile = File(),
    usuario: Usuario = Depends(obter_usuario_logado),
):
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if not usuario.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
    produto = Produto(nome=nome)
    produto = ProdutoRepo.inserir(produto)
    if arquivoImagem.filename:
        conteudo_arquivo = await arquivoImagem.read()
        imagem = Image.open(BytesIO(conteudo_arquivo))
        imagem_quadrada = transformar_em_quadrada(imagem)
        imagem_quadrada.save(f"static/img/produtos/{produto.id:04d}.jpg","JPEG")
    response = redirecionar_com_mensagem("/produto", "Produto inserido com sucesso!")
    return response

