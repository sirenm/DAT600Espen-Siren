from pulp import *

RevenueX = 200
RevenueY = 300

MTX = 0.25
MTY = 1/3
CTX = 1/3
CTY = 0.5

MTCost = 100
CCost = 20

TotalMachineTime = 40
TotalCraftsmanTime = 35

ConstraintX = 10

x = LpVariable("x")
y = LpVariable("y")

prob = LpProblem("UnitsOfXandY", LpMaximize)

prob += RevenueX * x + RevenueY * y, "Revenue"

prob += MTX*x + MTY * y <= TotalMachineTime

prob += CTX*x + CTY * y <= TotalCraftsmanTime

prob += x >= 10

answer = prob.solve()

print("Value for X: " + str(value(x)))
print("Value for Y: " + str(value(y)))

