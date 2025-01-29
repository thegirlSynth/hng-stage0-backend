from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_methods=["GET"],  # Allows only GET requests
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def get_info():
    return {
        "email": "cynthianuchepro@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-4] + "Z",
        "github_url": "https://github.com/thegirlSynth/hng-stage0-backend",
    }
