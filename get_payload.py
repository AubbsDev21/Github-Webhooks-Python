from fastapi import FastAPI
from logic.get_payload import GetPayload
from models.get_payload_model import GithubRawPayload


app = FastAPI()
instance = GetPayload()

def event():

    @app.post("/get_payload")
    async def handler(payload: GithubRawPayload):
       result = instance.payload_validation(payload)

       print("Message: " + result)

if __name__ == "__main__":
    event()