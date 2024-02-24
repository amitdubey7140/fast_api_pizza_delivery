from fastapi import APIRouter, status,Depends
from database.database import Session, engine
from schemas.schemas import SignUpModel,LoginModel
from models.models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter(prefix='/auth', tags=['auth'])

session = Session(bind=engine)


@auth_router.get('/')
async def test():
    return {'msg': 'Hello World'}


@auth_router.post('/signup',status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()

    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    db_email = session.query(User).filter(
        User.username == user.username).first()

    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    new_user = User(username=user.username, email=user.email, password=generate_password_hash(
        user.password), is_active=user.is_active, is_staff=user.is_staff)
    session.add(new_user)
    session.commit()
    return {'message':'User created successfully'}


#Login route

@auth_router.post('/login',status_code=status.HTTP_200_OK)
async  def login(user:LoginModel,Authorize:AuthJWT = Depends()):
    db_user = session.query(User).filter(User.username==user.username).first()

    if db_user and check_password_hash(db_user.password,user.password):
        access_token= Authorize.create_access_token(subject=db_user.username)
        refresh_token = Authorize.create_refresh_token(subject=db_user.username)

        response = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

        return jsonable_encoder(response)
    
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Incorrect username or password')