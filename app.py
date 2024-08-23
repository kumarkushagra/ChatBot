from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import model

app = FastAPI()
# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class UserMessage(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("templates/index.html") as f:
        return HTMLResponse(content=f.read())

@app.post("/chat")
async def chat(request: UserMessage):
    user_message = request.message
    response = model.generate_response(user_message)
    return {"response": response}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8000)
