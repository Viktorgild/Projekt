import re

text = """
Visit my website at https://www.example.com
or you can check out https://www.someotherexample.com
"""

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

matches = pattern.finditer(text)

urls = [match.group() for match in matches]

print(urls)


text = "Позвоните мне по номеру 555-123-4567 или 555-987-6543"

pattern = re.compile(r"\d{3}-\d{3}-\d{4}")

phone_numbers = pattern.findall(text)
print(phone_numbers)


text = "Цвет неба - синий."

new_text = re.sub(r"синий", "blue", text)

print(new_text)
