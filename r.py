import os

os.environ.setdefault("MY_PASSWORD", "12345")
print(os.environ.get("MY_PASSWORD"))