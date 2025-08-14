from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Product Detection Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProductURL(BaseModel):
    url: str

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "product-detection-service", "features": ["image_recognition", "product_analysis"]}

@app.post("/detect/url")
async def detect_from_url(request: ProductURL):
    return {
        "is_product_page": True,
        "confidence": 0.95,
        "product_name": "Detected Product",
        "price": "$99.99",
        "service": "product-detection-service"
    }

@app.post("/detect/image")
async def detect_from_image(file: UploadFile = File(...)):
    return {"detected_products": [], "confidence": 0.0, "service": "product-detection-service"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3010)
