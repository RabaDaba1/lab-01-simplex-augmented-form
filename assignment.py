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
    model.add_constraint(x1 + 2*x2 + x3 >= 10)
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

    p1 = model.create_variable("p1")
    p2 = model.create_variable("p2")
    p3 = model.create_variable("p3")
    p4 = model.create_variable("p4")

    s1 = 0.8*p1 + 2.4*p2 + 0.9*p3 + 0.4*p4
    s2 = 0.6*p1 + 0.6*p2 + 0.3*p3 + 0.3*p4
    
    model.add_constraint(s1 >= 1200)
    model.add_constraint(s2 >= 600)

    model.minimize(9.6*p1 + 14.4*p2 + 10.8*p3 + 7.2*p4)

    return model

def assignment_3():
    model = Model("Assignment 3")

    #TODO:
    # Add:
    # - variables
    # - constraints
    # - objective
    # tip. value at optimum: 21.8181818
    
    steaks = model.create_variable("steaks")
    potatoes = model.create_variable("potatoes")

    carbohydrates = 5*steaks + 15*potatoes
    protein = 20*steaks + 5*potatoes
    fats = 15*steaks + 2*potatoes

    model.add_constraint(carbohydrates >= 50)
    model.add_constraint(protein >= 40)
    model.add_constraint(fats >= 60)

    model.minimize(8*steaks + 4*potatoes)

    return model

def assignment_4():
    model = Model("Assignment 4")

    #TODO:
    # Add:
    # - variables
    # - constraints
    # - objective
    # tip. value at optimum: 4000.0

    cut_1 = model.create_variable("1x105_1x75")
    cut_2 = model.create_variable("1x105_2x35")
    cut_3 = model.create_variable("5x35")
    cut_4 = model.create_variable("1x75_3x35")
    cut_5 = model.create_variable("2x75_1x35")

    cout_105 = cut_1 + cut_2
    cout_75 = cut_1 + cut_4 + 2*cut_5
    cout_35 = 2*cut_2 + 5*cut_3 + 3*cut_4 + cut_5

    model.add_constraint(cout_105 >= 150)
    model.add_constraint(cout_75 >= 200)
    model.add_constraint(cout_35 >= 150)
    
    model.minimize(20*cut_1 + 25*cut_2 + 25*cut_3 + 20*cut_4 + 15*cut_5)
    return model