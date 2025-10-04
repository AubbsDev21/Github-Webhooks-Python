from pydantic import ValidationError
import json
from models.get_payload_model import GithubRawPayload
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
          hook = payload["hook"]
          hook_id = hook["id"]
          update_time = hook["updated_at"]
          create_time = hook["created_at"]

          repo = payload["repository"]
          owner = repo["owner"]
          full_name = repo["full_name"]
          owner_login = owner["login"]
          owner_type = owner["type"]
          comment_url = repo["comments_url"]
          issue_comments_url = repo["issue_comment_url"]
          created_at = repo["created_at"]
          updated_at = repo["updated_at"]
          language = repo["language"]
          
          data = {
              "hook": {
                  "id": hook_id,
                  "update_time": update_time,
                  "create_time": create_time
              },
              "repository": {
                  "full_name": full_name,
                  "owner": {
                      "login": owner_login,
                      "type": owner_type
                  },
                  "comments_url": comment_url,
                  "issue_comments_url": issue_comments_url,
                  "created_at": created_at,
                  "updated_at": updated_at,
                  "language": language
              }
          }

          parse_paylaod = json.dumps(data, indent=2)
          return parse_paylaod
        
        except TypeError as err:
            logging.error(f"Type Error: {err}")
            raise
          
        