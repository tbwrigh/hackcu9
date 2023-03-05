from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import base64

import pandas as pd

data = pd.read_csv("../data_output.csv")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_root():
    # Return an HTML file as a download response
    return FileResponse("html/home.html")

@app.get("/results")
async def silder_css():
    return FileResponse("html/results.html")

@app.post("/find")
async def calculate_results(gender_identity: int = Form(), sexual_orientation: int = Form(), religion: str = Form(), population: int = Form(), income: int = Form(), age: int = Form(), climate: str = Form()):
    
    scores = {}

    for index, row in data.iterrows():
        print(row)

        score = 0
        score += row["WHScore"] * row["HDI"]
        score += sexual_orientation * row["SOScore"]
        score += gender_identity * (0.02 / row["gii"])
        score += 1 if religion in row["Religion"].lower() else -1
        score -= 2*abs((row["PopulationPercent"]/5.65) - population)
        score -= (max(row["PercentPoverty"], 0.05) * income) / (income+1)
        score -= abs(age - row["Age"]) / 31.2
        score += row["HealthScore"]/50
        score += 1 if (row["Temperature"]-60>0 and climate=="warm")or(row["Temperature"]-60<0 and climate=="cool") else -1
        scores.update({row["Country"]: score})

    ret_values = {}

    for key in scores.keys():
        ret_values.update({scores[key]:f"{key.title()}|{round(scores[key],2)},"})
    
    order = list(reversed(sorted(list(scores.values()))))

    ret_string = ""

    for o in order:
        ret_string += ret_values[o]

    ret_string = ret_string[:-1]

    ret_string_bytes = ret_string.encode('ascii')
    b64_bytes = base64.b64encode(ret_string_bytes)
    b64_str = b64_bytes.decode('ascii')

    return RedirectResponse(f"/results?data={b64_str}", status_code=302)
