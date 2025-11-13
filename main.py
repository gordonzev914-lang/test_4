import uvicorn
import json
from fastapi import FastAPI, HTTPException
from utlls import caesar
from utlls import basec1
from utlls import basec2


app = FastAPI()



@app("/test")
def testing(test):
    func1=basec1(test)
    return {"maseg":func1}



@app("/test")
def testing(name):
    func=basec2(name)
    return {"maseg":func}






@app("/caesar")
def decrpting_caesar(text: str, offset: int):
    the_encrypter=caesar(text,offset)
    return the_encrypter 











if __name__ == "__main__": 
    uvicorn.run(app, host="localhost", port=8000)