class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password  # This should be a hashed password in production

    def to_dict(self):
        """Convert user object to dictionary format."""
        return {
            "ID": self.id,
            "Username": self.username,
            "Password": self.password
        }
