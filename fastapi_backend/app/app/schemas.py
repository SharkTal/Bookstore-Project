from datetime import date
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import conint
from pydantic import constr


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    # This must be here instead of 'Genre' class to avoid
    # recursion error when genre and book show eachother
    # On a second thought i might not need books here at all
    # books: List['Book'] = []
    pass


class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    # https://pydantic-docs.helpmanual.io/usage/types/#constrained-types
    username: constr(min_length=5, max_length=20)  # type: ignore[valid-type]
    email: Optional[EmailStr] = None  # Maybe hide email somewhere


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = False
    register_date: date

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    # https://pydantic-docs.helpmanual.io/usage/types/#constrained-types
    rating: conint(gt=-1, lt=6)  # type: ignore[valid-type]
    comment: str


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
    user: User
    edited: bool

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    description: Optional[str] = None  # Make required
    language: Optional[str] = None
    price: float = 0
    publication_date: date
    isbn: Optional[str] = None


class BookCreate(BookBase):
    # Default values to make testing faster
    image: str = "iVBORw0KGgoAAAANSUhEUgAAABEAAAAXCAYAAADtNKTnAAAABHNCSVQICAgIfAhkiAAAAdBJREFUOI3tlE1uE0EQhb/+m/GMrShGSiwHwo8IG07AIhyCyyAOwFm4ABdAYssCRYhEASwSZYMSE1Bij7vnp1n0EI899iobFvSqq+b1q/eqq0c86z313HLJ2xL8QySiRIedx7w4of+8CNGHIedvuovgrUv6L8cYBeQpV693yK4WlAiKkxj/t8XbOXpJoxi4ee6iQz6p91417HxPKMr6wJZF6iaFR911CBGi6rRDUc2/3kD9rw75WGAGHmKL2fa4s/qUqND38hooKUYx3PlN/9U5RjcbW8W4bxIPIHLMTqOUdOhhHZcxbqQQDZ0N54L8OAEPCI964G6AYsOhN+pg3MFdgs8i7PtNpu82WXQ+SnH5NXEEcneGlAllBexmaFUL+ZKGXJYwfZssKwEmKe401BeDjKgbmqofzZAC8Ir8KGb5nSySeI07rEHaYu5XIAvMw/raZgl21J7PVqY86lKWgCgxexaRZJhhqO2/dslti2PF2P9IsRfBknySoR5nGAN4ifuUUq14822SKsJ9Dv0Wgwm9/WkYMpdgD1WbYSUJguKgG25AWaK9EgFUxz3cpI1eQwL+rIf92Uwo8o+rrawloYyZHURzjixltsYKgPj/e2ytP0Bvq196uVzkAAAAAElFTkSuQmCC"
    file: str = "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JtIbvhWDGbKUb0Whs8xwTNUs7kyhz7zgKkpiFcKdL0uxLO/vxnU35/yyYcOxZct+DZZ+/wTTOC1Zy+cHWl7NSgplbmRzdHJlYW0KZW5kb2JqCjUgMCBvYmoKPDwvVHlwZSAvRm9udAovU3VidHlwZSAvVHlwZTAKL0Jhc2VGb250IC9JbnRlci1SZWd1bGFyCi9FbmNvZGluZyAvSWRlbnRpdHktSAovRGVzY2VuZGFudEZvbnRzIFsxNSAwIFJdCi9Ub1VuaWNvZGUgMTYgMCBSPj4KZW5kb2JqCnhyZWYKMCAxNwowMDAwMDAwMDAwIDY1NTM1IGYgCjAwMDAwMDAwMTUgMDAwMDAgbiAKMDAwMDAwMjM0MSAwMDAwMCBuIAowMDAwMDAwMjk3IDAwMDAwIG4gCjAwMDAwMDU4NzIgMDAwMDAgbiAKMDAwMDAxMDg4MiAwMDAwMCBuIAowMDAwMDAwMzM0IDAwMDAwIG4gCjAwMDAwMDI1NTkgMDAwMDAgbiAKMDAwMDAwMjYxNCAwMDAwMCBuIAowMDAwMDAyNjYxIDAwMDAwIG4gCjAwMDAwMDQ4MjEgMDAwMDAgbiAKMDAwMDAwNTA1NyAwMDAwMCBuIAowMDAwMDA1NTAyIDAwMDAwIG4gCjAwMDAwMDYwMTIgMDAwMDAgbiAKMDAwMDAwOTQyNCAwMDAwMCBuIAowMDAwMDA5NjYwIDAwMDAwIG4gCjAwMDAwMTA0MTAgMDAwMDAgbiAKdHJhaWxlcgo8PC9TaXplIDE3Ci9Sb290IDggMCBSCi9JbmZvIDEgMCBSPj4Kc3RhcnR4cmVmCjExMDIwCiUlRU9G"


class Book(BookBase):
    id: int
    avg_rating: Optional[float]
    authors: List["Author"]
    genres: List[Genre]

    class Config:
        orm_mode = True


class BookUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    language: Optional[str]
    price: Optional[float]
    publication_date: Optional[date]
    isbn: Optional[str]
    image: Optional[str]
    file: Optional[str]


# https://github.com/samuelcolvin/pydantic/issues/1333
# Need this so classes can refrence each other
Genre.update_forward_refs()


class ShoppingCart(BaseModel):
    book_ids: List[int]


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    # books: List[Book] = []

    class Config:
        orm_mode = True


Book.update_forward_refs()


class OrderBase(BaseModel):
    order_date: date
    total_price: float
    order_id: Optional[str]
    completed: Optional[bool]


class Order(OrderBase):
    id: int
    client: Optional[User]
    ordered_books: List[Book]

    class Config:
        orm_mode = True


class Wishlist(BaseModel):
    id: int
    books: List[Book]

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: str
