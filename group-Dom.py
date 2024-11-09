# author : Percy Ratheko
# working with xml data using DOM

import xml.dom.minidom

try:
    domtree = xml.dom.minidom.parse("group.xml")
except FileNotFoundError:
    print("Error : group.xml not found ")
    exit()

group = domtree.documentElement

persons = group.getElementsByTagName("person")


for person in persons:

    print("------------Person------------")

    if person.hasAttribute("id"):
        print("ID: %s" % person.getAttribute("id"))



    name_tags = person.getElementsByTagName("name")
    age_tags = person.getElementsByTagName("age")
    weight_tags = person.getElementsByTagName("weight")
    height_tags = person.getElementsByTagName("height")

    if name_tags:
        name = name_tags[0].childNodes[0].data
        print("Name: %s" % name)
    else:
        print("Name not found.")

    if age_tags:
        age = age_tags[0].childNodes[0].data
        print("Age: %s" % age)
    else:
        print("Age not found.")

    if weight_tags:
        weight = weight_tags[0].childNodes[0].data
        print("Weight: %s" % weight)
    else:
        print("Weight not found.")

    if height_tags:
        height = height_tags[0].childNodes[0].data
        print("Height: %s" % height)
    else:
        print("Height not found.")


print()
print("LETS PLAY AROUND WITH IT")
print()
persons = group.getElementsByTagName("person")
persons[0].getElementsByTagName("name")[0].childNodes[0].nodeValue = "New Navida"
persons[0].getElementsByTagName("age")[0].childNodes[0].nodeValue = "22"

# Now we writting to our files

domtree.writexml(open("group.xml","w"))

# to ccreate a new xml element , using dom : we use the domtree object

newperson = domtree.createElement("person")
newperson.setAttribute("id", "5")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Saint Peter"))

age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("36"))

weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("70"))

height = domtree.createElement( "height" )
height.appendChild(domtree.createTextNode( "178" ))

#defining the hierarchical structure

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)
try:
    domtree.writexml(open("group.xml","w"))
except FileNotFoundError:
    print("file not found ")
    exit()















