from fastapi import FastAPI
import logic.check_comment as check_comment
from models.models import GitHubPayload 
app = FastAPI()
def event():
    
    required_text = "important keyword"
    @app.post("/check_payload")
    async def handler(payload: GitHubPayload):
        check_comment.CommentValidator(required_text)
        result = check_comment.CommentValidator(payload)

        print(result)

    # Example GitHub webhook payload (replace with real payload)
    example_payload = {
        "action": "created",
        "issue": {"url": "https://api.github.com/repos/octocat/Hello-World/issues/1347"},
        "comment": {
            "id": 1,
            "body": "This is an important keyword comment.",
            "user": {"login": "octocat"}
        },
        "repository": {"name": "Hello-World"}
    }

    print("Result of valid payload:")
    

    example_payload_invalid = {
        "action": "created",
        "comment": {
            "id": 2,
            "body": "This comment is irrelevant.",
            "user": {"login": "octocat"}
        }
    }




if __name__ == "__main__":
    event()