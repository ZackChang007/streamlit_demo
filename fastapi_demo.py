# https://levelup.gitconnected.com/fastapi-fundamentals-getting-faster-with-fastapi-866545b841ca

from fastapi import FastAPI
app = FastAPI()


"""
The “@app.get(‘/’)” decorator gives FastAPI two pieces of information. 
1. It’s a GET operation. 
    POST : Create data.
    GET : Retrieve/Read data.
    PUT : Update the data.
    DELETE : Delete data.
2. The path parameter is “/”. 
A decorator is always defined on top of a function, which takes the function and does something with it. 
Here, the function base will be called by FastAPI whenever it receives a request to the URL “/” using a GET operation.
"""


@app.get('/')
def base():
    return "hello world"


@app.get('/add')
def base(x: int, y: int):
    return f"x={x} and y={y} and x+y={x+y}"


@app.get('/multiply')
def base(x: int = 4, y: int = 6):
    return f"x={x} and y={y} and x*y={x*y}"


"""
命令行命令：
uvicorn fastapi_demo:app --reload
"""
