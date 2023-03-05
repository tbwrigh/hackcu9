from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, FileResponse

app = FastAPI()

@app.get("/")
async def read_root():
    # Return an HTML file as a download response
    return FileResponse("html/home.html")
