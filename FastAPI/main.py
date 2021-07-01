from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'greeting':"Hello, world!"}}


@app.get('/about')
def abou():
    return {'data': "About us"}