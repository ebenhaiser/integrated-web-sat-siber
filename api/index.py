import asyncio
import time

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="BSecure Threat Analysis API",
    version="1.0.0"
)


class ThreatRequest(BaseModel):
    threat: str
    severity: str
    source: str


async def analyze_model_1(threat: str):
    start = time.perf_counter()

    print("[MODEL-1] START")
    await asyncio.sleep(2)
    duration = time.perf_counter() - start
    print(f"[MODEL-1] END - {duration:.2f}s")

    return {
        "model": "NVIDIA-NIM-1",
        "result": "HIGH",
        "duration": round(duration, 2)
    }


async def analyze_model_2(threat: str):
    start = time.perf_counter()

    print("[MODEL-2] START")
    await asyncio.sleep(2)
    duration = time.perf_counter() - start
    print(f"[MODEL-2] END - {duration:.2f}s")

    return {
        "model": "NVIDIA-NIM-2",
        "result": "HIGH",
        "duration": round(duration, 2)
    }


@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "BSecure Threat Analysis API"
    }


@app.post("/analyze")
async def analyze_threat(request: ThreatRequest):
    start = time.perf_counter()

    print("[ANALYSIS] START")

    model_1, model_2 = await asyncio.gather(
        analyze_model_1(request.threat),
        analyze_model_2(request.threat)
    )

    total_duration = time.perf_counter() - start

    print(f"[ANALYSIS] END - {total_duration:.2f}s")

    return {
        "status": "success",
        "threat": request.threat,
        "severity": request.severity,
        "source": request.source,
        "analysis": [
            model_1,
            model_2
        ],
        "execution_time": round(total_duration, 2)
    }