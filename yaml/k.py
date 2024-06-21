import yaml
import json

# Define the data structure in Python
my_books = [
    {
        "author": "J. K. Rowling",
        "pages": [
            {"number": 1, "text": "There once was a boy..."},
            {"number": 2, "text": "He went to magic school..."}
        ]
    },
    {
        "author": "Edgar Allan Poe",
        "pages": [
            {"number": 2, "text": "He went to magic school..."}
        ]
    },
    {
        "author": "Edgar Allan Poe",
        "pages": [
            {"number": 1, "text": "Book things pages words"}
        ]
    }
]

# Convert a single book to YAML
print(yaml.dump(my_books[0]))

# Convert the entire list of books to YAML
print(yaml.dump(my_books))

# Convert the entire list of books to JSON
print(json.dumps(my_books, indent=2))  # indent for pretty printing
