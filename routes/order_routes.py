from fastapi import APIRouter

order_router = APIRouter(prefix='/order')

@order_router.get('/')
async def test():
    return {'msg':'Hello World'}