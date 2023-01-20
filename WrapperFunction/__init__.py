import logging
import azure.functions as func
from pydantic import BaseModel

from FastAPIApp import app
from model.model import predict_pipeline
from model.model import classes


class TextInput(BaseModel):
    text: str


@app.get('/')
async def test_route():
    return {
        "About this NLP model" : 
        "This Language-Predict ML model recoginze the following languages.",
        "languages": classes
    }

@app.post('/predict')
async def predictLanguage(input: TextInput):
    predicted_result = predict_pipeline(input.text)
    return {
        "Input text: ": input.text,
        "Language Predicted Result: ": predicted_result
    }


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)