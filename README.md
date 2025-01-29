# HNG Stage 0 Backend Task

This is a FastAPI-based public API for the HNG Stage 0 Backend task.

## API Endpoint
- **URL**: `https://hng-stage0-backend-one.vercel.app/`
- **Method**: `GET`
- **Response Format**: JSON
  ```json
  {
    "email": "cynthianuchepro@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/thegirlSynth/hng-stage0-backend"
  }

## Setup Instructions
  ### 1. Clone the repository:

    git clone https://github.com/thegirlSynth/hng-stage0-backend.git

  ### 2. Install dependencies:

    pip install fastapi uvicorn


  ### 3. Run the app locally:

    uvicorn main:app --reload

  ### 4. Test the app locally. On a separate terminal run:

    curl http://127.0.0.1:8000/


## API Documentation
### Endpoint: `GET /`
  * **Response:** Returns a JSON object with:
    * `email`: My registered email.
    * `current_datetime`: Current UTC datetime in ISO 8601 format.
    * `github_url`: The GitHub URL of this project.

## Hire a Python Developer
Looking to hire a Python Developer? Check out [HNG Python Developers](https://hng.tech/hire/python-developers)
