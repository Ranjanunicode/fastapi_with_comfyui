from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import io
import comfyuiservice

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; restrict to specific domains as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process/")
async def process_input(
    prompt: str = Form(...),
    user_image: UploadFile = File(...),
    garment_image: UploadFile = File(...),
    model_image_id: str = Form(...)
):
    image = comfyuiservice.fetch_image_from_comfy(prompt, user_image, garment_image, model_image_id)
    image_stream = io.BytesIO(image)
    return StreamingResponse(image_stream, media_type="image/png")

@app.get("/hello")
def read_hello():
    return {"message": "Hello World!"}