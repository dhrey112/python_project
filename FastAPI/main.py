from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()


@app.get('/blog') # Endpoint or Path Decorator
# Path Operation function
def index(limit=10, published:bool=True, sort: Optional[str] = None):
    # Only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/about')
def about():
    return {'data': "About us"}


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blog'}


@app.get('/blog/{id}')
def shows(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    return {'data':{'1', '2', '3'}}




class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title as {blog.title}"}



if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=9900)
