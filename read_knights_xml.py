import lxml.etree as et

tree = et.parse("knights.xml")

for tag in tree.findall('.//name'):   # search starting at root tag
    print(tag.text)
print()

for knight_tag in tree.getroot():
    print(knight_tag.findtext('name'))