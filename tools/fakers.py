import time
from random import randint

def get_random_email() -> str:
    return f"{time.time()}@example.com"

def get_random_password() -> str:
    return f"{''.join([str(randint(0, 9)) for i in range(10)])}"

def get_random_name() -> str:
    return f"{''.join([chr(randint(97, 122)) for i in range(5)])}"

