# Flask-vs-FastAPI
Understanding Flask vs FastAPI Web Framework. A comparison of two different RestAPI frameworks.

#Introduction
Being a Data Scientist does not end with Model Building, but working towards the next step, Model Deployment. Model Deployment is important to show your final results to others (or it could be your clients). This group of people might not understand coding and won’t understand by viewing your codes; they would prefer to view the final application, allowing them to view the results immediately. A common approach is to wrap your codes in a RestAPI and deploy them as a microservice.

In this blog, I will introduce two different frameworks that can quickly set up web servers: Flask and FastAPI. Both Flask and FastAPI are frameworks that are used for building small-scale websites and applications.

Flask Framework
Flask was released in 2010, a micro web framework written in python to support the deployment of web applications with a minimal amount of code. It is designed to be an easy setup, flexible and fast to deploy as a microservice. Flask is built on WSGI (Python Web Server Gateway Interface) whereby the server will tie up a worker for each request.
Below is an example of deploying using Flask (This is an example of using a ‘GET’ method to get user inputs and insert the values into Google Big Query — this example is deployed on Google Cloud Run)

'''
from flask import Flask, request, make_response, jsonify
import pandas as pd
import gcsfs
import os

app = Flask(__name__)

app.config["DEBUG"] = True #If the code is malformed, there will be an error shown when visit app

@app.route("/books", methods=["GET"])
def books_table_update():
    
    Title = request.args.get('title', None)
    Author = request.args.get('author', None)

    input_table = {'book_title':[Title],'book_author':[Author]}
    input_table = pd.DataFrame(input_table)
    input_table["book_title"]= input_table["book_title"].map(str)
    input_table["book_author"]= input_table["book_author"].map(str)
    
    #Push table to Google Big Query

    client = bigquery.Client()
    project_id = 'sue-gcp-learning-env'
    table_id = 'Books.books_title_author'
    pandas_gbq.to_gbq(input_table, table_id, project_id=project_id, if_exists='append')
    
    return "Table books_title_author has been Updated"

'''

#FastAPI Framework

FastAPI is more recent compared to Flask and was released in 2018. It works similarly to Flask which supports the deployment of web applications with a minimal amount of code. However, FastAPI is faster compare to Flask as it is built on ASGI (Asynchronous Server Gateway Interface) whereby it supports concurrency / asynchronous code. This is done by declaring the endpoints with async def syntax.

A good thing to highlight for FastAPI is the documentation. Upon deploying with FastAPI Framework, it will generate documentation and creates an interactive GUI (Swagger UI) which allows developers to test the API endpoints more conveniently.

Below is an example of deploying using FastAPI (This is an example of using a ‘GET’ method to get user inputs and insert the values into Google Big Query — this example is deployed on Google Cloud Run)

'''

import uvicorn
from fastapi import FastAPI
import pandas as pd
import gcsfs
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas_gbq
import os

app = FastAPI()

@app.get("/books_title/{book_title}/author/{author}")
async def books_table_update(books_title: str, author: str ):
    
    Title = books_title
    Author = author

    input_table = {'book_title':[Title],'book_author':[Author]}
    input_table = pd.DataFrame(input_table)
    input_table["book_title"]= input_table["book_title"].map(str)
    input_table["book_author"]= input_table["book_author"].map(str)
    
    #Push table to Google Big Query

    client = bigquery.Client()
    project_id = 'sue-gcp-learning-env'
    table_id = 'Books.books_title_author'
    pandas_gbq.to_gbq(input_table, table_id, project_id=project_id, if_exists='replace')
    
    return "Table books_title_author has been Updated"

'''

Upon finish deploying with Flask, you can run the URL and pass the input in the URL and a message will be returned which works similarly to Flask.

#image

Now, this is the additional function from FastAPI that really makes me excited which is the automated generated docs (Swagger UI). To access the Swagger UI enter the API endpoint /docs and there you go — an interactive GUI to test your API endpoints. Having a Swagger UI makes it easier to explain your program to others as well.

By using Swagger UI, you can easily test your API endpoints and specifying the parameters via the interface. For example, in the image below, you can easily specify the “Book Title” and “Author” in the column provided.

Other than Swagger UI, FastAPI also comes with another documentation — “ReDoc”. The documentation consists of all the endpoints listed which is useful if you are having many endpoints deployed in the same service. To access the documentation page enter the API endpoint /redoc.

Comparison of Flask and FastAPI:

HTTP Methods : 

![HTTP Methods](https://github.com/Mithlesh-Navlakhe/Flask-vs-FastAPI/blob/main/1_eG7Xz7J22Cvyt90RyE6C7g.png)

To specify a “GET” or “POST” method is different in Flask and FastAPI.

Passing Parameter & Data Validation :

![HTTP Methods](https://github.com/Mithlesh-Navlakhe/Flask-vs-FastAPI/blob/main/1_5vpbnDfgLPKzem5yUAGLVw.png)

Flask does not provide validation on the data format which means the user can pass any type of data such as string or integer etc. (Alternatively, a validation script on the input data receive can be built into the script, but this will require additional effort)

FastAPI allows developers to declare additional criteria and validation on the parameter received.

Error Messages Display:

The error messages display in Flask are HTML pages by default where else in FastAPI the error messages displayed are in JSON format.
Asynchronous Tasks:

As mention in the earlier part of this article, Flask is deployed on WSGI (Python Web Server Gateway Interface) which does not support asynchronous tasks where else FastAPI is deployed on ASGI (Asynchronous Server Gateway Interface) which supports asynchronous tasks.

Conclusion:
After looking into both Flask and FastAPI, I would consider adopting FastAPI in the future as it has asynchronous functions and automated generated documents which is very detailed and complete. Additionally, the effort required to deploy using FastAPI is the same as Flask.

If you had been using Flask all the while, you can consider trying out FastAPI and observe the comparison.
