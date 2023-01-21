from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home_view():
    return {"message": "HelloWorld"}

@app.post('/')
def home_detail_view():
    return {"message": "HelloWorld"}