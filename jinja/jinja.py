import jinja2

env = jinja2.Environment()
template = env.from_string("Hi {{ their_name }}, my name is {{ my_name }}.")
print(template.render(their_name="John", my_name="Mary"))

#fruits
template = env.from_string("""
My favorite fruits are:
{% for fruit in fruits %}
- {{ fruit }}
{% endfor %}
""")
# - at the end of the {% for fruit in fruits -%} line. What happens?
#space bettween the statements and fruits
print(template.render(fruits=["apples", "oranges","mangoes"]))

#books
template = env.from_string("The title of the book I'm reading is ,{{ book_title }}.")
print(template.render(book_title="Breaking Boundaries"))
