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
usage:fetch all products
RestAPI URL: http://127.0.0.1:8000/products/
Method Type:GET
Required Fields:None
Access Type:Public

'''
@router.get("/")
def get_products():
    return products 

'''
usage:fetch all stationary products -- static routes
RestAPI URL: http://127.0.0.1:8000/products/Stationary
Method Type:GET
Required Fields:None
AccessType:Pubic
'''
@router.get("/stationary")
def get_stationary_products():
     stationary_products=list(filter(lambda p:p['category']=='Stationary',products))
     return stationary_products

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
usage: fetch all stationary products below 500
RestAPI URL: http://127.0.0.1:8000/products/stationary/filter?price=500
Method Type:GET
Required Fields: None
Access Type:Public
'''
@router.get("/stationary/filter")
def get_all_products(price:int):

     new_products=list(filter(lambda p:p['price']>price and p['category']=="Stationary",products))
     if new_products:
          return new_products
     else:
          return {'msg':'Products not available'}

