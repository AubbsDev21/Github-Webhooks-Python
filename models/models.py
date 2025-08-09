from typing import Optional, List, Dict
from pydantic import BaseModel, Field

class GitHubComment(BaseModel):
    """
    Represents a GitHub comment.
    """
    id: int 
    body: str 
    user: Dict[str, str] 


class GitHubIssue(BaseModel):
    """
    Represents a GitHub issue or pull request.
    """
    url: str 


class GitHubPayload(BaseModel):
    """
    Represents the structure of a GitHub webhook payload for issue_comment events.
    """
    action: str 
    issue: Optional[GitHubIssue] 
    comment: GitHubComment 
    repository: Dict[str, str] 


class CommentValidationResult(BaseModel):
    """
    Represents the result of validating a GitHub comment.
    """
    comment_id: int = Field(..., description="The ID of the comment")
    comment_body: str = Field(..., description="The body of the comment")
    status: bool = Field(..., description="True if the comment contains the required text, False otherwise")