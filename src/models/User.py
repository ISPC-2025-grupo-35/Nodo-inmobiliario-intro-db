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

    def __str__(self):
        return f"User(id={self.user_id}, name={self.name}, surname={self.surname}, email={self.email}, role={self.role}, date={self._register_date}, enabled={self.enabled})"

        

    