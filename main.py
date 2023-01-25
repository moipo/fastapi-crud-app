from fastapi import FastAPI, Body, Depends
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

#uses engine configuration from database.py
Base.metadata.create_all(engine)


app = FastAPI()

db = {
    "1" : "item_1",
    "2" : "item_2",
    "3" : "item_3",
}

@app.get("/")
def getItems():
    return db

@app.get("/{id}")
def getItem(id:int):
    return db[id] 

#Option 1
# @app.post("/")
# def addItem(task:str):
#     last_id = len(db)
#     db[last_id+1] = {"task" : task}


# Option 2
@app.post("/")
def addItem(task:schemas.Item):
    last_id = len(db)
    db[last_id+1] = {"task" : task}
    return db
    

# Option 3
@app.post("/")
def addItem(body = Body()):
    last_id = len(db)
    db[last_id+1] = {"task" : body['task']}
    return db 



    
