from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
# from services.ocr.boot_ocr import OCR
import uvicorn
from services.yolo_service.yolo.conf.detect import YOLO_img_to_base64_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"status": "success", "message": "Hello World"}


@app.post("/yolo")
async def image(images: UploadFile):
    return YOLO_img_to_base64_response.predict(await images.read())


# @app.post("/ocr")
# async def image(images: UploadFile):
#     return OCR(await images.read()).start()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)  # or python3 -m main
