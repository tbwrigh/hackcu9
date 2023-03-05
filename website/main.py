from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, FileResponse

app = FastAPI()

@app.get("/")
async def read_root():
    # Return an HTML file as a download response
    return FileResponse("html/home.html")

@app.post("/find")
async def calculate_results(gender_identity: str = Form(), sexual_orientation: str = Form(), social: str = Form(), wealth: str = Form(), religion: str = Form()):
    
    return RedirectResponse("/")
