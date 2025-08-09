import json
from models.get_payload_model import GithubRawPayload
from pydantic import ValidationError
import logging


logger = logging.getLogger(__name__)
class GetPayload:
    def __init__(self, payload: dict):
        self.payload = payload
        logger.info(f"Github Payload '{self.payload}'")

    def payload_validation(self) -> dict:

        try:
            json_load = json.loads(self.payload)
            valid_payload = GithubRawPayload.model_validate(json_load)

            logger.info(f"The payload was vaildated: '{valid_payload.hook.id}', Updated at: '{valid_payload.hook.updated_at}'")

            return valid_payload


        except ValidationError as e:
            logging.error(f"Validation Error: {e}")
            raise  

    def payload_parser(self) -> dict:
          data = {}
        try:
          payload = json.loads(self.payload)
          # Navigating nested structures
          #engineering_employees = data["departments"][0]["employees"]
          hook_id = payload["hook"]["id"]
          update_time = payload["hook"]["updated_at"]
          create_time = payload["hook"]["created_at"]

          full_name = payload["repository"]["full_name"]
          owner_login = payload["repository"]["owner"]["login"]
          owner_type = payload["repository"]["owner"]["type"]
          comment_url = payload["repository"]["comments_url"]
          
        