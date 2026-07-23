from fastapi import APIRouter
from models.product import Product
router=APIRouter(prefix='/products')

'''
usage: fetch all products
RestAPI URL: http://127.0.0.1:8000/products
Method Type:GET
Required Fields: None 
Access Type:Public
'''
@router.get('/')
def get_proudcts():
    return {"msg":"Fetching all products"}


'''
usage: search product
RestAPI URL: http://127.0.0.1:8000/products/search?category=books&price=200
Method Type:GET
Required Fields:None
Access Type:Public
'''
@router.get("/search")
def search_products(category:str,price:int):
    return {"msg":'Searching products',
            "category":category,
            "price":price
            }



'''
usage: create products
RestAPI URL: http://127.0.0.1:8000/products/
Method Type:POST
Required Fields: pid,pname,price,category 
Access Type:Public
'''

@router.post("/")
def create_new_product(product:Product):
    return {'msg':'New Product Created successfully',
            'product':product
            } 

'''
usage: fetch product by id
RestAPI URL: http://127.0.0.1:8000/products/101
Method Type:GET
Required Fields: None 
Access Type:Public
'''
@router.get("/{pid}")
def get_product(pid:int):
    return {'msg':'fetching product id','product_id':pid}



