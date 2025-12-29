from pydantic import BaseModel

class CreatePost(BaseModel):
    title: str
    description: str


class UserAuth(BaseModel):
    email: str
    password: str
