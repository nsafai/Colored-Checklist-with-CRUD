
checklist = list()

# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

def create(item):
    checklist.append(item)

def read(index):
    item = checklist[index]
    return item

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def test():
    # Add your testing code here
    create("purple sox")
    create("red cloak")

    print(checklist)

    update(0, "purple socks")
    destroy(1)

    print(checklist)

test()
