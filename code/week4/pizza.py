def make_pizza(size,  *topping):
    """
    Summarize the information for a pizza
    """
    print("Making pizza " + str(size) +
          "inch, with the following toppings")
    for t in topping:
        print("- " + t)

# make_pizza(8, "mushroom")

def greeting(name):
    print("welcome: " + name)