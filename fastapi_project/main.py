from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "hello-world"}

@app.post('/create/')
def create():
    return {"msg" : "Вы успешно создали что то!"}