
class UserObject():
    _username: str
    _password: str
    _first_name: str
    _last_name: str

    def __init__(self, username: str, password: str, first: str, last: str):
        self._username = username
        self._password = password
        self._first_name = first
        self._last_name = last

    def get_username(self) -> str:
        return self._username

    def get_password(self) -> str:
        return self._password

    def get_first(self) -> str:
        return self._first_name

    def get_last(self) -> str:
        return self._last_name

    def set_username(self, username: str):
        self._username = username

    def set_password(self, password: str):
        self._password = password

    def set_first(self, first: str):
        self._first_name = first

    def set_last(self, last: str):
        self._last_name = last

    def __str__(self) -> str:
        return "username: {}\npassword: {}\nname: {} {}".format(
            self._username, self._password, self._first_name, self._last_name
        )
