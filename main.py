from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import io
from rembg import remove
from PIL import Image

app = FastAPI(title="Remover Fundo API", description="API gratuita para remover fundos de imagens.")

@app.get("/")
def home():
    return {"status": "ok", "message": "API funcionando corretamente!"}

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        input_image = await file.read()
        output_image = remove(input_image)
        img = Image.open(io.BytesIO(output_image))
        output_path = "output.png"
        img.save(output_path)
        return FileResponse(output_path, media_type="image/png")
    except Exception as e:
        return {"error": str(e)}
