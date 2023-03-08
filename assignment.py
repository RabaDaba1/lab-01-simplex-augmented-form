from saport.simplex.model import Model

#TODO:
# Model assignments from assignment.pdf
# tip 1. you may use an external solver to check if your models reach correct optima
# tip 2. external solver available on-line: https://online-optimizer.appspot.com/?model=builtin:default.mod 

def assignment_1():
    model = Model("Assignment 1")

    #TODO:
    # Add:
    # - variables
    # - constraints
    # - objective
    # tip. value at optimum: 80.0

    x1 = model.create_variable("x1")
    x2 = model.create_variable("x2")
    x3 = model.create_variable("x3")

    model.add_constraint(x1 + x2 + x3 <= 30)
    model.add_constraint(x1 + 2 * x2 + x3 >= 10)
    model.add_constraint(2 * x2 + x3)

    model.maximize(2 * x1 + x2 + 3 * x3)

    return model

def assignment_2():
    model = Model("Assignment 2")

    #TODO:
    # Add:
    # - variables
    # - constraints
    # - objective
    # tip. value at optimum: 10800.0
    return model

def assignment_3():
    model = Model("Assignment 3")

    #TODO:
    # Add:
    # - variables
    # - constraints
    # - objective
    # tip. value at optimum: 21.8181818
    return model

def assignment_4():
    model = Model("Assignment 4")

    #TODO:
    # Add:
    # - variables
    # - constraints
    # - objective
    # tip. value at optimum: 4000.0
    return model