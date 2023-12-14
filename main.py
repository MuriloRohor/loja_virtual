from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routes.RootRouter import router as rootRouter


app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(rootRouter)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)