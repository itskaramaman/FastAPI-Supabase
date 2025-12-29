from pydantic import BaseModel

class PostModel(BaseModel):
    title: str
    description: str


class UserAuth(BaseModel):
    email: str
    password: str
