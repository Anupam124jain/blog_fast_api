from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordHash():
    def __init__(self, password):
        self.hashed_password = pwd_context.hash(password)
        self.pwd_context = pwd_context
