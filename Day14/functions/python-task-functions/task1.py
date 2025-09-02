# 📝 Task 1: Grocery List Manager
def add_groceries(grocery_list, *items):
    """
    Add multiple grocery items into the grocery list.
    
    Parameters:
    grocery_list: The existing list of groceries.
    items: Any number of grocery items (strings).
    
    Example:
        groceries = []
        add_groceries(groceries, "Tomato", "Bread", "Milk")
    """
    for item in items:
        grocery_list.append(item)
    print(grocery_list)
grocery_list = []


add_groceries(grocery_list, "Tomato", "Bread", "Mik")
