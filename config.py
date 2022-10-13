import os


class Config:
    CSRF_ENABLE = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
