from typing import TypedDict


class Credentials(TypedDict):
    user: str
    password: str
    client_id: str
    client_secret: str
