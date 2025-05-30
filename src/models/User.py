from datetime import date
from typing import List
from .User_role import RoleEnum
import uuid

class User:
    def __init__(
        self,
        name: str,
        surname: str,
        email: str,
        password: str,
        role: RoleEnum
    ):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.surname = surname
        self.email = email
        self._password = password
        self.role = role
        self._register_date = date.today()
        self.enabled = True
        

    