from UserObject import UserObject
from UserParser import UserParser

class UserController:
    user: UserObject

    def __init__(self, keyword: str):
        parser = UserParser()
        user = parser.parse_single(keyword)

    def get_username(self) -> str:
        return self.user.get_username()

    def get_password(self) -> str:
        return self.user.get_password()

    def get_first(self) -> str:
        return self.user.get_first()

    def get_last(self) -> str:
        return self.user.get_last()

    def set_username(self, username: str):
        self.user.set_usernmae(username)

    def set_password(self, password: str):
        self.user.set_password(password)

    def set_first(self, first: str):
        self.user.set_first(first)

    def set_last(self, last: str):
        self.user.set_last(last)

    def __str__(self) -> str:
        return "username: {}\npassword: {}\nname: {} {}".format(
            self.user.get_username(), self.user.get_password(),
            self.user.get_first(), self.user.get_last()
        )
