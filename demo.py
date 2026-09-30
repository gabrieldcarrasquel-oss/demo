import sympy as sp
import matplotlib.pyplot as mp
import numpy as np

class differential_eqn_solver: 
    def __init__(self,eqn,h,x_0,y_0,n):
        self.eqn = eqn
        self.h = h
        self.x_0=x_0
        self.y_0 = y_0
        self.n = n
    def calculate_eulers(self):
        tbl = {
        'x_n':[],
        "y_n":[],
        "dy/dx":[]
        }
        for i in range(0,self.n):
            if i == 0:
                derivative = self.eqn.subs({x:self.x_0, y:self.y_0})
                xn = self.x_0
                yn = self.y_0
                dydx = self.eqn.subs({x:xn, y:yn})
                tbl['x_n'].append(xn)
                tbl['y_n'].append(yn)
                tbl["dy/dx"].append(dydx)
            else:
                xn = tbl['x_n'][i-1]
                yn = tbl['y_n'][i-1]
                derivative = self.eqn.subs({x:xn, y:yn})
                xnp1 = xn + self.h
                ynp1 = yn + self.h * derivative
                dydxnp1 = self.eqn.subs({x:xnp1, y:ynp1})
                tbl['x_n'].append(xnp1)
                tbl['y_n'].append(ynp1)
                tbl['dy/dx'].append(dydxnp1)
        return tbl
    def show_table(self):
        tbl = self.calculate_eulers()
        formated_table = " x_0" + " "*7 + "y_0" +  " "*6 + "dy/dx"
        formated_table += "\n"+"_"*len(" x_n" + " "*7 + "y_n" +  " "*7 + "dy/dx") +"\n"
        val_matrix = [tbl['x_n'],tbl['y_n'],tbl["dy/dx"]]
        for j in range(0,self.n):
            formated_table+= f"\n{val_matrix[0][j]:4.3f}" + " "*5 + f"{val_matrix[1][j]:<1.3f}" + " "*5 +f"{val_matrix[2][j]:<1.3f}"
        return(formated_table)
x = sp.symbols("x")
y = sp.symbols("y")

errors = []

while True:
    try:
        eqn = sp.sympify(input("Enter differential equation in terms of x and y:"))         
        h = float(input("Enter step: "))
        x_0 = float(input("Enter x_0: "))
        y_0 = float(input('Enter y_0: '))
        n = int(input("Enter number of iterations: "))
        setup = differential_eqn_solver(eqn,h,x_0,y_0,n)
        print(setup.show_table())
        break
    except Exception as e:
        print("Error:", e)
