from fastapi import FastAPI
import uvicorn

from router import router


if __name__ == '__main__':
    app = FastAPI()
    app.include_router(router)
    uvicorn.run(app, host='127.0.0.1', port=8088)
