from fastapi import FastAPI

from app.models import AdviceRequest, AdviceResponse
from app.services.openai_client import chat_completion

app = FastAPI()


@app.post("/advice", response_model=AdviceResponse)
async def get_advice(body: AdviceRequest) -> AdviceResponse:
    """
    Echoes advice back from the OpenAI chat completion service.

    • Expects `AdviceRequest` with a `conversation` list.
    • Uses the last user message as the prompt.
    • Returns an `AdviceResponse` with the model’s reply.
    """
    # call the synchronous helper – **no await**
    reply = chat_completion(body.conversation[-1].content)
    return AdviceResponse(reply=reply)