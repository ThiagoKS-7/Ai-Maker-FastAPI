from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from services.yolo.boot import get_image
import uvicorn

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"status": "success", "message": "Hello World"}


@app.get("/yolo")
async def image(images: UploadFile):
    get_image(await images.read())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)  # or python3 -m main
