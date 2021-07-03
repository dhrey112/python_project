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

#####################################################################
#                   MANIPULATING XML FILES                          #
#####################################################################
persons[0].getElementsByTagName("name")[0].childNodes[0].nodeValue = "New Name"
persons[0].setAttribute("id", "10")

#####################################################################
#                   CREATING NEW ELEMENTS                           #
#####################################################################
new_person = domtree.createElement("person")
new_person.setAttribute("id", "6")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Paul Smith"))
age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("45"))
weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("78"))
height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("178"))

new_person.appendChild(name)
new_person.appendChild(age)
new_person.appendChild(weight)
new_person.appendChild(height)
group.appendChild(new_person)


domtree.writexml(open("group.xml", "w"))