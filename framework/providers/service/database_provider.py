class DatabaseProvider:
    
    def __init__(self, connect_str) -> None:
        self.connect_str = connect_str

    def connect(self):
        self.connection = True

    def get_user(self, username):
        self.connection.execute(f"SELECT * from users where username='{username}'")