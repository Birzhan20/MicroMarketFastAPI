from fastapi import APIRouter

from .schemas import Product, ProductCreate
from . import crud

router = APIRouter(tags=["Products"])


@router.get("/")
async def get_products(session):
    return await crud.get_products(session=session)


@router.post("/")
async def create_product(session, product_in: ProductCreate):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}")
async def get_products(product_id: int, session):
    return await crud.get_product(session=session, product_id=product_id)
