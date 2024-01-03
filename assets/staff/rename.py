import os
for name in os.listdir("."):
    names = name.split(" - ")
    if len(names) > 1:
        names[1] = names[1].lower().replace(" ", "-")
        names[1] = names[1].replace(".", "2.")
        os.rename(name, names[1])
