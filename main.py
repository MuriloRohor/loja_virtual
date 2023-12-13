from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)