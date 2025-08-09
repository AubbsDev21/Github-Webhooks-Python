from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


class HookConfig(BaseModel):
    content_type: str
    insecure_ssl: str # Often a string "0" or "1" for GitHub webhooks
    url: HttpUrl

class LastResponse(BaseModel):
    code: Optional[int]
    status: str
    message: Optional[str]

class Hook(BaseModel):
    type: str
    id: int
    name: str
    active: bool
    events: List[str]
    config: HookConfig
    updated_at: datetime
    created_at: datetime
    url: HttpUrl
    test_url: HttpUrl
    ping_url: HttpUrl
    deliveries_url: HttpUrl
    last_response: LastResponse

class Owner(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: HttpUrl
    gravatar_id: str
    url: HttpUrl
    html_url: HttpUrl
    followers_url: HttpUrl
    following_url: str # This is a template URL, not a direct HttpUrl
    gists_url: str    # This is a template URL
    starred_url: str  # This is a template URL
    subscriptions_url: HttpUrl
    organizations_url: HttpUrl
    repos_url: HttpUrl
    events_url: str   # This is a template URL
    received_events_url: HttpUrl
    type: str
    user_view_type: str = Field(alias="user_view_type") # Field added for "user_view_type"
    site_admin: bool

class Repository(BaseModel):
    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    owner: Owner
    html_url: HttpUrl
    description: Optional[str] # Can be null
    fork: bool
    url: HttpUrl
    forks_url: HttpUrl
    keys_url: str # Template URL
    collaborators_url: str # Template URL
    teams_url: HttpUrl
    hooks_url: HttpUrl
    issue_events_url: str # Template URL
    events_url: HttpUrl
    assignees_url: str # Template URL
    branches_url: str # Template URL
    tags_url: str # Template URL
    blobs_url: str # Template URL
    git_tags_url: str # Template URL
    git_refs_url: str # Template URL
    trees_url: str # Template URL
    statuses_url: str # Template URL
    languages_url: HttpUrl
    stargazers_url: HttpUrl
    contributors_url: HttpUrl
    subscribers_url: HttpUrl
    subscription_url: HttpUrl
    commits_url: str # Template URL
    git_commits_url: str # Template URL
    comments_url: str # Template URL
    issue_comment_url: str # Template URL
    contents_url: str # Template URL
    compare_url: str # Template URL
    merges_url: HttpUrl
    archive_url: str # Template URL
    downloads_url: HttpUrl
    issues_url: str # Template URL
    pulls_url: str # Template URL
    milestones_url: str # Template URL
    notifications_url: str # Template URL
    labels_url: str # Template URL
    releases_url: str # Template URL
    deployments_url: HttpUrl
    created_at: datetime
    updated_at: datetime
    pushed_at: datetime
    git_url: str # Can be git://
    ssh_url: str # Can be git@
    clone_url: HttpUrl
    svn_url: HttpUrl
    homepage: Optional[str] # Can be null
    size: int
    stargazers_count: int
    watchers_count: int
    language: Optional[str] # Can be null
    has_issues: bool
    has_projects: bool
    has_downloads: bool
    has_wiki: bool
    has_pages: bool
    has_discussions: bool
    forks_count: int
    mirror_url: Optional[str] # Can be null
    archived: bool
    disabled: bool
    open_issues_count: int
    license: Any # Can be null or an object, use Any for simplicity if you don't need to parse it
    allow_forking: bool
    is_template: bool
    web_commit_signoff_required: bool
    topics: List[str]
    visibility: str
    forks: int
    open_issues: int
    watchers: int
    default_branch: str

class Sender(Owner): # Sender shares many fields with Owner
    pass


class GithubRawPayload(BaseModel):
    zen: str
    hook_id: int
    hook: Hook
    repository: Repository # Added this fie
    sender: Sender

class Hook(BaseModel):
    id: int
    updated_at: str
    created_at: str

class Owner(BaseModel):
    login: str
    type: str

class Repository(BaseModel):
    full_name: str
    owner: Owner
    comments_url: str
    issue_comment_url: str
    created_at: str
    updated_at: str
    language: str

class Webhook(BaseModel):
    hook: Hook
    repository: Repository

class ParsedPayload(BaseModel):
    webhook: Webhook