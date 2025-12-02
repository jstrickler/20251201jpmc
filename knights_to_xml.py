import lxml.etree as et  # xml.ElementTree

FILE_PATH = "DATA/knights.txt"

root = et.Element("knights")
with open(FILE_PATH) as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip().split(':')
        knight = et.SubElement(root, "knight", title=title)
        name_tag = et.SubElement(knight, "name")
        name_tag.text = name
        et.SubElement(knight, "color").text = color
        et.SubElement(knight, "quest").text = quest
        et.SubElement(knight, "comment").text = comment



raw_xml = et.tostring(root, xml_declaration=True, pretty_print=True)  # returns bytes (b-string)
xml_doc = raw_xml.decode()  # decode binary string to Python string
print(xml_doc)
# print(raw_xml)

tree = et.ElementTree(root)
tree.write("knights.xml", pretty_print=True, xml_declaration=True)




