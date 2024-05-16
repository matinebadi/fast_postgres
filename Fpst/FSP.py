from fastapi import FastAPI
from post import add
from post import update
from post import deleted
from post import showed_all
from post import showed
app = FastAPI()

data_dict=dict()

@app.post("/items/")
async def creat_item(name:str,item_id:int):
    add(name, item_id)
    return {"message":"inserted"}
@app.get("/items/")
async def read_items():    
    return {f"all data":showed_all()}   
 

@app.delete("/items/{last_id1}/") #path
async def delete_item(last_id1:int):
        deleted(last_id1)

        return ("massage : deleted :( ")

@app.put("/items/{item_id}/{name}") #path
async def update_item(item_id: int, name: str,last_id:int):
        update(name, item_id,last_id)
        return {"item_id":item_id , "name":name}

@app.get("/items/{litem_id}")
async def read_items_one(litem_id:int):    
    return {f"response":showed(litem_id)}   