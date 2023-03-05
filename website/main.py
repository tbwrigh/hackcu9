from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_root():
    # Return an HTML file as a download response
    return FileResponse("html/home.html")

@app.get("/slider_design.css")
async def silder_css():
    return FileResponse("html/style.css")

@app.post("/find")
async def calculate_results(gender_identity: str = Form(), sexual_orientation: str = Form(), social: str = Form(), wealth: str = Form(), religion: str = Form()):
    
    return RedirectResponse("/")
