from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import os

# FastAPI 인스턴스 생성
app = FastAPI(
    title="k3s Web Server Example",
    description="A simple web server running on k3s.",
    version="1.0.0"
)

# 데이터 모델 정의 (예제용)
class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the k3s Web Server!"}

@app.get("/items", response_model=list[Item], tags=["Items"])
async def read_items(q: str | None = None):
    items_db = [
        Item(name="Item One", price=19.5, description="The item one"),
        Item(name="Item Two", price=9.5, description="The item two")
    ]
    filtered_db = items_db
    if q:
        search_str = f"%{q}%"
        filtered_db = [item for item in filtered_db if search_str.lower() in item.name.lower()]
    
    return filtered_db

@app.get("/users/{username}", response_model=User, tags=["User"])
async def read_user(username: str):
    # 실제 사용자는 DB 에서 가져오는 것이지만 여기서는 예시로 반환합니다.
    user_db = {
        "ali": User(name="ali", email="ali@k3s.com"),
        "ahmet": User(name="ahmet", email="ahmet@k3s.com")
    }
    
    # 사용자 이름을 기반으로 DB 에서 사용자 찾기
    if username not in user_db:
        raise HTTPException(status_code=404, detail=f"User {username} not found")
    
    return user_db[username]

class User(BaseModel):
    name: str
    email: str | None = None
