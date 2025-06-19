from pydantic import BaseModel, Field


class Author(BaseModel):
    author_id: int
    name: str
    surname: str
    age: int
    email: str

class Post(BaseModel):
    post_id: int
    content: str
    author: Author
    published_data: str
    last_update_data: str

class Blog(BaseModel):
    blog_id: int
    description: str
    author: Author
    posts: list[Post]

author = Author(
    author_id=12, name="Eduard", surname="Nikitin", age=20, email="maste@gmail.com"
)

posts = [
    Post(post_id=11, content="first post", author=author, published_data="18.06.2025", last_update_data="19.06.2025")
]

blog = Blog(
    blog_id = 130, description="New Blog", author=author, posts = posts
)

print(blog.model_dump_json())
