from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from services.yolo.boot_yolo import YOLO
from services.ocr.boot_ocr import OCR
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


@app.post("/yolo")
async def image(images: UploadFile):
    YOLO(await images.read()).get_image()


@app.post("/ocr")
async def image(images: UploadFile):
    return OCR(await images.read()).start()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)  # or python3 -m main
