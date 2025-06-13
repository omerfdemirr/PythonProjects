import xml.etree.ElementTree as et

xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<catalog>
    <book id="bk101">
        <author>Ömer Demir</author>
        <title>XML Developer</title>
        <price>44.95</price>
        <description>Comment...</description>
    </book>
    <book id="bk102">
        <author>Doğan</author>
        <title>Rust Developer</title>
        <price>44.95</price>
        <description>Comment...</description>
    </book>
    <book id="bk103">
        <author>Enes</author>
        <title>Python Developer</title>
        <price>44.95</price>
        <description>Comment...</description>
    </book>
</catalog>"""

root = et.fromstring(xml_data)

for book in root.findall("book"):
    book_id = book.get("id")
    author = book.find("author").text
    title = book.find("title").text
    price = book.find("price").text
    description = book.find("description").text
    print(f"Book Id : {book_id}")
    print(f"Author : {author}")
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Description: {description}")
    print('-' * 40)