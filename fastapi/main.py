
#installation steps
#virtualenv envname
#activate environment .\envname\Scripts\activate
#pip install 'fastapi[all]'
#pip freeze requirements.txt
#pip freeze > requirements.txt
#create main.py
#uvicorn main:app --reload


from fastapi import FastAPI 
from pydantic import BaseModel

import requests
app = FastAPI()

# on the terminal type: curl http://127.0.0.1:8000
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.get('/home')
def index():
    return {'key' : 'Hello world'}

# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:8000 / square / 10
# this returns 100 (square of 10)
@app.get('/sqaure/{num}')
def get_city(num: int):
    return {'key': num**2}
