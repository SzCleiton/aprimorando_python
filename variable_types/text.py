# declare
name_complete = "Cleiton Souza"

name_complete_asp = """Cleiton
Souza"""

name_complete_qbr = "Cleiton \
Souza"

name = "Cleiton"
sbName = "Souza"

# format
print("Name Complete:", name_complete)
print("Name Complete:" + name_complete)
print("Name Complete: " + "Cleiton " + sbName)
print("Name Complete:" + "Cleiton", "Souza")
print("Name Complete:", name_complete_asp)
print("Name Complete:", name_complete_qbr)

print("Name Complete: %s" % name_complete)
print("Name Complete: %s %s" % (name, sbName))
print(f"Name Complete: {name} {sbName}")
print("Name Complete: {} {}".format(name, sbName))