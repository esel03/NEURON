from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from fastapi import status
from fastapi.responses import JSONResponse

from yandexGPTdemo import GENERATE
import asyncio
import requests
import json
import jwt

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



SECRET_KEY = 'django-insecure-fa6x_kpu4wa1&x(*j2vy*&meyp-oyx1-zr*p!t=h#d7dq2%1ql'
url_take_marketing_specific = "http://127.0.0.1:8000/api/two_table/take_marketing_specific/"
headers= {
    "Content-Type": "application/json",
    "Accept-Charset": "UTF-8"
    # "Authorization": "4506"
}

url_update_under_table_advertisement = "http://127.0.0.1:8000/api/two_table/update_under_table_advertisement/"



class Api(BaseModel):
    token: str
    adv_id: str
    type_services: Union[str, None] = None
    economic_works: Union[str, None] = None
    title: Union[str, None] = None
    text_in: Union[str, None] = None
    skill_level: Union[str, None] = None
    details: Union[str, None] = None
    founding_date: Union[str, None] = None
    text_out: Union[str, None] = None

    



@app.post("/api/generate/", status_code=status.HTTP_200_OK)
async def proba(item: Api):
    auth = jwt.decode(item.token, key=SECRET_KEY, algorithms=["HS256"])
    prompt_take_marketing_specific = {
            "token": item.token,
            "adv_id": item.adv_id,
        }
    result_take_marketing_specific = requests.post(url_take_marketing_specific, headers=headers, json=prompt_take_marketing_specific)
    json_text = json.loads(result_take_marketing_specific.text)
    
    exp_dict = json_text
    exp_dict.pop('token')
    exp_dict.pop('adv_id')
    
    result_generate = GENERATE(**exp_dict)
    prompt_update_under_table_advertisement = {
            "token": item.token,
            "adv_id": item.adv_id,
            "text_out": result_generate,
    }

    result_update_under_table_advertisement = requests.post(url_update_under_table_advertisement, headers=headers, json=prompt_update_under_table_advertisement)
    print(type(result_update_under_table_advertisement))
    print(str(result_update_under_table_advertisement))
    if str(result_update_under_table_advertisement) == '<Response [200]>':
        return JSONResponse(content={"token": item.token, "adv_id": item.adv_id}, status_code=200)
    else:
        return JSONResponse(content={"message": "Bad Request"}, status_code=404)


#@app.post("/api/")


#from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
#from databases import Database

# Подключение к базе данных SQLite
'''
DATABASE_URL = "sqlite:///./test.db"

database = Database(DATABASE_URL)
metadata = MetaData()

# Определение схемы таблицы

notes = Table(
    "notes",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("content", String(200)),
    )

# Создание экземпляра FastAPI
app = FastAPI()



@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Определение операций CRUD

@app.get("/notes/{note_id}")
async def read_note(note_id: int):
    query = notes.select().where(notes.c.id == note_id)
    return await database.fetch_one(query)

@app.post("/notes/")
async def create_note(title: str, content: str):
    query = notes.insert().values(title=title, content=content)
    return await database.execute(query)

@app.put("/notes/{note_id}")
async def update_note(note_id: int, title: str, content: str):
    query = notes.update().where(notes.c.id == note_id).values(title=title, content=content)
    return await database.execute(query)

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    query = notes.delete().where(notes.c.id == note_id)
    return await database.execute(query)
'''
'''
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjoiYmFmYmQzMWQtMjhmYS00OThiLTgzY2UtMzdkZTg5MjVmMTc2IiwiaWF0IjoxNzI4NDIxMjA2LCJuYmYiOjE3Mjg0MjA5MDYsImV4cCI6MTczMTAxMzIwNn0.KpYhFIohHIlj1Y6_tdD60Rw5UzKplXCu9y7vEyyDnos",
  "adv_id": "494fce4c-487d-4818-98ad-d4ab45239798",
  "type_services": "string",
  "economic_works": "string",
  "title": "string",
  "text_in": "string",
  "skill_level": "string",
  "details": "string",
  "founding_date": "string",
  "text_out": "string"
}
'''




