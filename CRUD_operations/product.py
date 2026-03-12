from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# Create a Product CRUD API.

# Product fields:
# name
# price
# quantity

# APIs required:
# POST /products
# GET /products
# GET /products/{id}
# PUT /products/{id}
# DELETE /products/{id}
app = FastAPI()

class Product(BaseModel):
    name : str
    price : float
    quantity : int

products = []

@app.get('/')
def home():
    return {"message" : "CRUD prectice"}

@app.post('/api/products')
def create_product(product:Product):
    products.append(product)
    return {"message":"Product Created",
            "products" : product}

@app.get('/api/products')
def get_products():
    return products

@app.get('/api/products/{product_id}')
def get_product_by_id(product_id : int):
    if product_id >= len(products):
        raise HTTPException(status_code=404,detail="Product Not Found")
    return products[product_id]

@app.put('/api/products/{product_id}')
def update_product(product_id : int,product: Product):
    if product_id >= len(products):
        raise HTTPException(status_code=404,detail="Product Not Found")
    products[product_id] = product
    return {"message" : "Updated Sucessfully",
            "products" : products}

@app.delete('/api/products/{product_id}')
def delete_products(product_id : int):
    if product_id >= len(products):
        raise HTTPException(status_code=404,detail="Product Not Found")
    deleted_product =  products.pop(product_id)
    return {"message" : "Deleted Successfully",
            "deleted_product" : deleted_product,
            "products" : products}