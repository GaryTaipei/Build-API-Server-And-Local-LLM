#q: 使用 FastAPI 呼叫 local ollama api http://localhost:11434/api/generate
from fastapi import FastAPI, HTTPException #pip install fastapi
from pydantic import BaseModel #pip install pydantic
import requests #pip install requests
import json
from decouple import config #pip install python-decouple
from urllib.parse import quote_plus
import uvicorn #pip install uvicorn
import ollama #pip install ollama
from RAGQuery import *

headers = {
    "Content-Type": "application/json"
}

class Query(BaseModel):
    prompt: str
    model: str = "llama3.1"

app = FastAPI(debug=True)

@app.post("/chat")
async def update_item(item: Query):
    ollama_api = "http://localhost:11434/api/generate" #ollama default api
    payload = {
            "model": item.model,
            "prompt": item.prompt,
            "stream": False
    }
    response = requests.post(ollama_api,headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        #接收 ollama 回傳的 json 內容時需要再包一層 [] 才能正確解析 response.json()
        return  {"response":[response.json()["response"]]}

    else:
        print("error:", response.status_code, response.text)
        return {"error": response.status_code, "data": response.text}

@app.post("/query")
async def queryOllama(item: Query):
    try:
        response = ollama.chat(model=item.model, messages=[
            {
                'role': 'system',
                'content': 'You are a personal assistant. You help answer questions accurately.',
                'role': 'user',
                'content': item.prompt,
            },
        ])
        return {"response": response['message']['content']}
    except ollama.ResponseError as e:
        return {"error": e.error}

@app.post("/queryvector")
async def queryVector(item: Query):
    rqg = RAGQuery()
    response = rqg.query_vector(item.prompt)
    return {"response": response.response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
