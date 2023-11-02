from fastapi import FastAPI


from routers import router as r_router
from authorization import router as a_router


app = FastAPI()

app.include_router(r_router)
app.include_router(a_router)





if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
