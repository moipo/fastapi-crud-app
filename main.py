from fastapi import FastAPI

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

@app.post("/")
def addItem(task:str):
    last_id = len(db)
    db[last_id+1] = {"task" : task}