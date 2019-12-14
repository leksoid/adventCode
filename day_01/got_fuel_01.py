# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. 
# To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?

from math import floor

sampleInput = [83326,84939,135378,105431,119144,124375,138528,88896,98948,85072,112576,144497,112824,98892,81551,139462,73213,93261,130376,118425,132905,54627,134676,140435,131410,128441,96755,94866,89490,122118,106596,77531,84941,57494,97518,136224,69247,147209,92814,63436,79819,109335,85698,110103,79072,52282,73957,68668,105394,149663,91954,66479,55778,126377,75471,75662,71910,113031,133917,76043,65086,117882,134854,60690,67495,62434,67758,95329,123078,128541,108213,93543,147937,148262,56212,148586,73733,110763,149243,133232,95817,68261,123872,93764,147297,51555,110576,89485,109570,88052,132786,70585,105973,85898,149990,114463,147536,67786,139193,112322]


def fuel_required_for_module(mass):
    return int(floor(mass / 3)) - 2

def compute_total_fuel_required(modules):
    total = 0
    for each in modules:
        fuel = fuel_required_for_module(each)
        total += fuel
    return total