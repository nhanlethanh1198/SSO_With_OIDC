from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    'http://localhost:3000',
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def index():
    return {
        "message": "This is a project for Single Sign On using OpenID Connect"
    }