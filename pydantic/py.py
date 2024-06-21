from pydantic import BaseModel

class Page(BaseModel):
    number: int
    text: str

class Book(BaseModel):
    author: str
    title: str
    pages: list[Page]
     
my_books = [
		Book(
		    author="J. K. Rowling",
		    title="Harry Potter and the Philosopher's stone",
		    pages=[
		        Page(
		            number=1,
		            text="There once was a boy...",
		        ),
		        Page(
		            number=2,
		            text="He went to magic school...",
		        )
		    ]
		),
		Book(
		    author="Roger Zelazny",
		    title="Lord of Light",
		    pages=[
		        Page(
		            number=1,
		            text="It is said that fifty-three years ago...",
		        )
		    ]
		),
		Book(author="Toni Simone",
		    title="Breaking Boundaries",
		    pages=[
		        Page(
		            number=1,
		            text="Standing in my local coffee shop I'm sorrounded by farmiliar faces...",
		        )
		    ]),
]
print(my_books[0].author)
print(my_books[0].pages[0].text)
for book in my_books:
    print(book.title)