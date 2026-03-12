from fastapi import APIRouter, HTTPException
from app.schema import Product

router = APIRouter()

products = []

@router.post('/api/products')
def create_product(product:Product):
    products.append(product)
    return {"message":"Product Created",
            "products" : product}

@router.get('/api/products')
def get_products():
    return products

@router.get('/api/products/{product_id}')
def get_product_by_id(product_id : int):
    if product_id >= len(products):
        raise HTTPException(status_code=404,detail="Product Not Found")
    return products[product_id]

@router.put('/api/products/{product_id}')
def update_product(product_id : int,product: Product):
    if product_id >= len(products):
        raise HTTPException(status_code=404,detail="Product Not Found")
    products[product_id] = product
    return {"message" : "Updated Sucessfully",
            "products" : products}

@router.delete('/api/products/{product_id}')
def delete_products(product_id : int):
    if product_id >= len(products):
        raise HTTPException(status_code=404,detail="Product Not Found")
    deleted_product =  products.pop(product_id)
    return {"message" : "Deleted Successfully",
            "deleted_product" : deleted_product,
            "products" : products}