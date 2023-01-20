'''
PROTOTYPE app : a prototype off azure function app.
run this prototype app from root directory with: $ python main
'''

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from model.model import predict_pipeline
from model.model import classes


class TextInput(BaseModel):
    text: str


app = FastAPI()

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

# @app.get('/predict')
# async def predict_language(text: str):
#     if text == '':
#         return {'error': 'text query parameter can not be empty'}
#     predicted_result = predict_pipeline(input.text)
#     return {"Predicted Result: ", predicted_result}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)