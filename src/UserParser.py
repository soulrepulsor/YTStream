import json
from typing import Dict
from UserObject import UserObject

class UserParser():

    def __init__(self):
        pass


    def parse_single(self, username: str) -> UserObject:
        password = "password"
        first = "first"
        last = "last"

        usernames = json.load(open('User/user.json', 'r'))

        if username in usernames:
            user_dict = usernames.get(username)
            return UserObject(
                username, user_dict.get(password),
                user_dict.get(first), user_dict.get(last))

        # print(json.dumps(parsed, indent=4, sort_keys=True))
        return None


if __name__ == "__main__":
    test = UserParser()
    print(str(test.parse_single('user1')))
