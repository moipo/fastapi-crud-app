from pydantic import BaseModel
import schemas

class Item(BaseModel):
    task:str 
    some_another_required_param: str