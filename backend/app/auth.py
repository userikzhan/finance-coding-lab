from datetime import datetime, timedelta
from jose import jwt, JWTError

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from app.schemas import UserCreate, UserLogin

SECRET_KEY = "SUPER_SECRET_KEY"
ALGORITHM = "HS256"

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

fake_db = {}

# -------------------------
# CREATE JWT TOKEN
# -------------------------

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=12)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# -------------------------
# REGISTER
# -------------------------

@router.post("/register")
def register(user: UserCreate):

    if user.email in fake_db:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    fake_db[user.email] = user.password

    return {
        "message": "User created"
    }


# -------------------------
# LOGIN
# -------------------------

@router.post("/login")
def login(user: UserLogin):

    if fake_db.get(user.email) != user.password:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# -------------------------
# GET CURRENT USER
# -------------------------

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials"
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

        return email

    except JWTError:
        raise credentials_exception


# -------------------------
# PROTECTED ROUTE
# -------------------------

@router.get("/me")
def get_me(
    current_user: str = Depends(get_current_user)
):

    return {
        "email": current_user
    }
