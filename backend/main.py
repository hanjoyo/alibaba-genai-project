from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from query_genai import call_with_stream 

app = FastAPI()

@app.get("/")
async def hello_world(request:Request):
    ip = request.client.host
    print(ip)
    return {"hello":"world", "root_path":request.scope.get("root_path")}

@app.get("/prompt")
async def prompt(query: str):
    response = call_with_stream(query)
    return {"response": response.text}

origins = ['*']

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
