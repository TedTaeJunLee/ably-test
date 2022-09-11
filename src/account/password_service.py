import bcrypt


class PasswordService:
    @classmethod
    def make_hashed_password(cls, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
