from fastapi import FastAPI, Request
import json
from logic.get_payload import GetPayload
from models.get_payload_model import GithubRawPayload


app = FastAPI()
instance = GetPayload()

def event():

    @app.post("/get_payload")
    async def handler(payload: GithubRawPayload):
       result = instance.payload_validation(payload)

       print("Message: " + result)

    @app.put("/parse_data")
    async def handler(request: Request):
        payload = await request.json()
        instance = GetPayload(json.dumps(payload))
        new_payload = instance.payload_parser()
        return new_payload 

if __name__ == "__main__":
    event()