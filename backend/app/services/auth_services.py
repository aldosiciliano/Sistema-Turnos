from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt, JWTError
from app.db.sessions import get_session
from datetime import datetime,timedelta
from app.models import Usuario, Rol
from passlib.context import CryptContext
from app.schemas import usuario_schemas
from sqlalchemy.future import select
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 60

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return password_context.hash(password)

def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)
   
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def register_user(usuario: usuario_schemas.UsuarioCreate, db: AsyncSession):
    result = await db.execute(select(Usuario).where(Usuario.email == usuario.email))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Email ya registrado")
    hashed_password = get_password_hash(usuario.password)
    nuevo_usuario = Usuario(email=usuario.email, password_hash=hashed_password, rol=usuario.rol)
    db.add(nuevo_usuario)
    await db.commit()
    await db.refresh(nuevo_usuario)
    return nuevo_usuario

async def login_user(form_data: OAuth2PasswordRequestForm, db: AsyncSession):
    result = await db.execute(select(Usuario).where(Usuario.email == form_data.username))
    usuario = result.scalar_one_or_none()
    if not usuario or not verify_password(form_data.password, usuario.password_hash):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    access_token = create_access_token(data={"sub": usuario.email, "rol": usuario.rol.value})
    return {"access_token": access_token, "token_type": "bearer"}    
