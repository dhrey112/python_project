import xml.dom.minidom

domtree = xml.dom.minidom.parse("group.xml")
group = domtree.documentElement


persons = group.getElementsByTagName("person")

for person in persons:
    print("---- Person ----")
    if person.hasAttribute("id"):
        print("ID: %s" % person.getAttribute("id"))

    name = person.getElementsByTagName("name")[0]
    age = person.getElementsByTagName("age")[0]
    weight = person.getElementsByTagName("weight")[0]
    height = person.getElementsByTagName("height")[0]



