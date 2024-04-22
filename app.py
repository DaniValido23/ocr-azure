from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from script import extract_image
from jinja2 import Template
import os

app = FastAPI()

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    with open(os.path.join("images", file.filename), "wb") as buffer:
        buffer.write(file.file.read())
    
    response = extract_image(str(file.filename))

    template = Template(open("result.html").read())
    html_content = template.render(response=response)

    return HTMLResponse(content=html_content, status_code=200)


@app.get("/", response_class=HTMLResponse)
async def home():
    return FileResponse("index.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
