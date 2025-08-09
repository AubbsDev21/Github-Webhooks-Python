import logging
from pydantic import ValidationError
from models.models import CommentValidationResult, GitHubPayload  # Import models
import json

# Configure logging (set up once at the module level)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class CommentValidator:
    """
    Validates GitHub comments based on a required text.
    """

    def __init__(self, required_text: str, payload: dict):
        self.required_text = required_text
        self.paylaod = payload

    def validate_comment(self, payload: dict) -> str:  # Return JSON string
        """
        Validates a GitHub comment in a webhook payload.

        Args:
            payload: The GitHub webhook payload (dict).

        Returns:
            A JSON string representing the CommentValidationResult.
        """
        try:
            github_payload = GitHubPayload.model_validate(payload)
            comment_status = self.required_text in github_payload.comment.body
            result = CommentValidationResult(
                comment_id=github_payload.comment.id,
                comment_body=github_payload.comment.body,
                status=comment_status,
            )
            json_result = result.model_dump_json()  # Serialize to JSON
            logging.info(f"Comment validation successful. Result: {json_result}")
            return json_result
        except ValidationError as e:
            error_result = CommentValidationResult(comment_id=-1, comment_body=str(e), status=False)
            json_error_result = error_result.json()
            logging.error(f"Validation Error: {json_error_result}, Payload: {payload}")
            return json_error_result



