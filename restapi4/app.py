from fastapi import FastAPI,Header
from routers.product_router import router as product_router
app=FastAPI()

'''
usage: Application Root request
RestAPI URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None 
Access Type:Public
'''
@app.get("/")
def root_request():
    return {'msg':'Application Root Request'}



'''
usage: Application Root request
RestAPI URL: http://127.0.0.1:8000/headers
Method Type:GET
Required Fields: username,token 
Access Type:Public
'''
@app.get("/headers")
def get_headers(username:str=Header(...),token:str=Header(...)):
    return {'username':username,'token':token}

app.include_router(product_router)


