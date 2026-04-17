import os
from dotenv import load_dotenv


load_dotenv()
my_user: str | None = os.getenv("MY_USER")
my_password: str | None = os.getenv("MY_PASSWORD")
