# turtle is a package
from turtle import color, forward, right

# outer loop: 100 iterations
for steps in range(1, 101):
    # a nested loop: 3 iterations
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps) # length of the line: 1, 2, 3, ..., 100
        right(30) # change the direction by 30 degrees

input("press enter to exit")

# analyze the iterations

# 1. iteration of the outer loop
# steps = 1
## 1. iteration of the inner loop
## c = 'blue'
## 2. iteration of the inner loop
## c = 'red'
## 3. iteration of the inner loop
## c = 'green'

# 2. iteration of the outer loop
# steps = 2
## 1. iteration of the inner loop
## c = 'blue'
## 2. iteration of the inner loop
## c = 'red'
## 3. iteration of the inner loop
## c = 'green'
