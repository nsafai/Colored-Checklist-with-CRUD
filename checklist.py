# https://www.makeschool.com/academy/track/captain-rainbow-s-color-checklist/captain-rainbow-s-color-checklist/putting-it-together

checklist = list()

def create(item):
    checklist.append(item)
    list_all_items()

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    checklist[index] = "DONE: " + checklist[index]

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

running = True
# print("running is {}".format(running))
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)

def test():
    # Add your testing code here
    create("purple sox")
    create("red cloak")

    select("C")
    list_all_items()
    select("R")
    list_all_items()

    list_all_items()
    mark_completed(1)
    list_all_items()

    update(0, "purple socks")
    destroy(1)

    list_all_items()
