import json

# Data stucture:
# The shopping list is modeled as a dictionary keyed by product name.
# The value is another dictionary, with the following keys: "isle" and "quantity"
# Example:
#   shopping_list = { "Apple": { "isle": 1, "quantity": 5}, "Pineapple": { "isle": 3, "quantity": 15 } }
#


def add_product(shopping_list, name, quantity, isle):
    shopping_list[name] = {"quantity":quantity, "isle":isle}


def remove_product(shopping_list, name):
    if name in shopping_list:
        del shopping_list[name]
    else:
        print("Sorry, no such product on list!  :( ")


def modify_product(shopping_list, name, quantity, isle=0):
    "If the parameter isle is not specified or 0, the isle will not be modified."
    if name in shopping_list.keys():
        # Modify an existing product
        shopping_list[name]["quantity"] = quantity
        if isle != 0:
            shopping_list[name]["isle"] = isle
    else:
        add_product(shopping_list, name, quantity, isle)

def load_data(filename):
    with open(filename) as input_file:
        return json.load(input_file)


def save_data(shopping_list, filename):
    with open(filename, "w") as output_file:
        json.dump(shopping_list, output_file, indent=4)


if __name__ == '__main__':
    # Create a prompt loop with the main menu
    shopping_list = load_data("shopping_list.json")
    while True:
        match(int(input("Enter 1 to Add, 2 to Remove, 3 to Modify, 4 to List, 5 to Save and Exit: "))):
            case 1:
                name = input("Please enter name of product: ")
                quantity = int(input("Enter quantity needed: "))
                isle = int(input("Enter isle where product is located: "))
                add_product(shopping_list, name, quantity, isle)
            case 2:
                name = input("Please enter name of product: ")
                remove_product(shopping_list, name)
            case 3:
                name = input("Please enter name of product: ")
                quantity = int(input("Enter quantity needed: "))
                # ask if isle has changed here?
                isle = int(input("Enter isle where product is located, or enter 0 if not changed: "))
                modify_product(shopping_list, name, quantity, isle)
            case 4:
                print(shopping_list)
            case 5:
                save_data(shopping_list, "shopping_list.json")
                print ("Thank you and goodbye!")
                break
        print ("\n") # newline

