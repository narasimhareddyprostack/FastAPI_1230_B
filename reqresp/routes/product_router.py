from fastapi import APIRouter
router=APIRouter(prefix='/products')

products=[
    {'pid':101,'product_name':'Marker Pen','price':30,'category':'Stationary'},
    {'pid':102,'product_name':'Lenovo Mouse','price':400,'category':'Electronics'},
    {'pid':103,'product_name':'ThinkPad','price':108000,'category':'Electronics'},
    {'pid':104,'product_name':'Water Bottle','price':10,'category':'Groceries'},
    {'pid':105,'product_name':'Dell Inspiron','price':150000,'category':'Electronics'},
    {'pid':106,'product_name':'Mac Book Pro','price':183000,'category':'Electronics'},
    {'pid':107,'product_name':'Stappler','price':35,'category':'Stationary'},
    {'pid':108,'product_name':'R Pen','price':10,'category':'Stationary'},
    {'pid':109,'product_name':'Parker Pen','price':200,'category':'Stationary'},
    {'pid':110,'product_name':'Meta Rayban','price':40000,'category':'Electronics'}
]


'''
usage: fetch all stationary products - static routes
Rest API URL: http://127.0.0.1:8000/products/stationary
Method Type:GET
Required Fields:None 
Access Type:public
'''
@router.get("/stationary")
def get_stationary_products():

    return [product 
            for product in products 
            if product['category']=='Stationary'
            ]


'''
usage:get product by id
RestAPI URL: http://127.0.0.1:8000/products/102
Method Type:GET
Required Fields: None
Access Type:Public
'''

@router.get("/{pid}")
def get_product(pid:int):
     new_products=list(filter(lambda p:p['pid']==pid,products))

     if new_products:
          return new_products
     else:
          return {'msg':'Product Not Available'}
     


'''
usage: fetch products by category
Rest API URL: http://127.0.0.1:8000/products/cat/stationary
Method Type:GET

'''

@router.get("/cat/{category}")
def get_products_category(category:str):
     new_products=list(filter(lambda p:p['category']==category,products))
     return new_products