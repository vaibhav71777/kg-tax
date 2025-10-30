from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Project KG Prototype")

# --- Allow frontend to talk to backend ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------- Models ----------
class TaxInput(BaseModel):
    income: float
    age: int
    regime: str  # "old" or "new"

# --------- Core Logic ----------
def calculate_tax(data: TaxInput):
    income = data.income
    regime = data.regime.lower()
    tax = 0

    if regime == "new":
        # New regime (FY 2023–24 slabs)
        slabs = [(0, 3, 0), (3, 6, 5), (6, 9, 10), (9, 12, 15), (12, 15, 20), (15, 1e9, 30)]
    else:
        # Old regime
        slabs = [(0, 2.5, 0), (2.5, 5, 5), (5, 10, 20), (10, 1e9, 30)]

    remaining = income / 100000  # convert ₹ to lakhs for easier slabs
    prev_limit = 0
    for lower, upper, rate in slabs:
        if remaining > lower:
            taxable = min(remaining, upper) - lower
            tax += taxable * rate * 1000  # convert back to ₹
        else:
            break

    return round(tax, 2)

def recommend_deductions(data: TaxInput):
    recs = []
    if data.regime.lower() == "old":
        if data.income > 500000:
            recs += ["Invest in ELSS (u/s 80C)", "Health Insurance (80D)", "NPS (80CCD)"]
        else:
            recs += ["Utilize 80C fully (₹1.5 L)", "Consider term insurance"]
    else:
        recs += ["Switch to old regime if deductions > ₹2 L", "No major deductions in new regime"]
    return recs

# --------- Endpoints ----------
@app.post("/calculate")
def calculate(data: TaxInput):
    tax = calculate_tax(data)
    recs = recommend_deductions(data)
    return {"tax": tax, "recommendations": recs, "regime": data.regime}

@app.get("/")
def root():
    return {"message": "Project KG API running!"}
