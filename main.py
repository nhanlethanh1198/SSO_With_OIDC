from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {
        "message": "This is a project for Single Sign On using OpenID Connect"
    }