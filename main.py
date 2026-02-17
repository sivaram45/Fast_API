from fastapi import FastAPI,HTTPException


app = FastAPI()


items=[ ]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items")
def get_items(limit: int = 3) -> list:
    return items[:limit]

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="item not found")
    
@app.put("/items/{item_id}")
def update_item(item_id: int, new_item: str):
    if item_id < len(items):
        items[item_id] = new_item
        return items
@app.delete("/items/{item_id}")
def del_item(item_id: int):
    if item_id < len(items):
        del items[item_id]
        return items
    else:
        raise HTTPException(status_code=404, detail="item not found")




    