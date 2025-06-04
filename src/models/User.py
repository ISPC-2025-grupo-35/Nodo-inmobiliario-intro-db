from datetime import date
from typing import List
from .Role_enum import RoleEnum
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
        return f"User(id={self.user_id}, name={self.name}, surname={self.surname}, email={self.email}, role={self.role}, date={self.__register_date}, enabled={self.enabled})"

    def __repr__(self):
        return f"User(id={self.user_id}, name={self.name}, surname={self.surname}, email={self.email}, role={self.role}, date={self.__register_date}, enabled={self.enabled})"

    @property
    def user_id(self):
        return self.__user_id
    
    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    @property
    def register_date(self):
        return self.__register_date

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value