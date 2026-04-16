from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Change this to your needs
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Mounting the route for the vulnerability scanner
@app.get('/vulnerabilities')
async def get_vulnerabilities():
    return {'message': 'List of vulnerabilities will be here.'}

# You can add more routes and functionality here as needed.
