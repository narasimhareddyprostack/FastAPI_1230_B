from pydantic import BaseModel
class Product(BaseModel):
    pid:int
    pname:str
    price:float
    category:str 

    