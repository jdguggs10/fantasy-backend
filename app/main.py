from fastapi import FastAPI
from app.models import AdviceRequest, AdviceResponse
from app.services.openai_client import chat_completion

app = FastAPI()

@app.post("/advice", response_model=AdviceResponse)
async def get_advice(body: AdviceRequest):
    # placeholder until stats are wired in
    reply = await chat_completion(body.conversation[-1].content)
    return AdviceResponse(reply=reply)
