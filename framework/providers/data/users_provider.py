import os


class UserProvider:
    
    @staticmethod
    def fake_user():
        return {
            'login': 'some_name',
            'id': 777777777777777777777777777
        }

    @staticmethod
    def existing_user():
        return {
            'login': 'se1t4r',
            'id': 102989181
        }
    
    @staticmethod
    def existing_user_from_env():
        return {
            'login': os.environ.get("EXISTING_GITHUB_USER_LOGIN"),
            'id': int(os.environ.get("EXISTING_GITHUB_USER_ID"))
        }