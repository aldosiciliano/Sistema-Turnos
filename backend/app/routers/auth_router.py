from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from app.db.sessions import get_session
from app.schemas import usuario_schemas
from app.services import register_user, login_user



router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/register")
async def register(
    usuario: usuario_schemas.UsuarioCreate,
    db: AsyncSession = Depends(get_session)
):
    return await register_user(usuario, db)

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_session)
):
    return await login_user(form_data, db)
    
    
