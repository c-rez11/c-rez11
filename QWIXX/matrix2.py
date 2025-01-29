# attempt two with the matrix

# Solving QWIXX using a matrix Markov chain
import numpy as np

# probabilities of each roll
p1 = 1/6
p2 = 1/6
p3 = 1/6
p4 = 1/6
p5 = 1/6
p6 = 1/6

prob_dict = {
    1: p1,
    2: p2,
    3: p3,
    4: p4,
    5: p5,
    6: p6
}

roll_list = np.arange(1,7)
target_list = np.arange(1,4)
rolls = 4
rolls_left = rolls-1
points = 5

# transition matrix
m_transition = np.array([
            [p1,p2,p3,p4,p5,p6],
            [p1,p2,p3,p4,p5,p6],
            [p1,p2,p3,p4,p5,p6],
            [p1,p2,p3,p4,p5,p6],
            [p1,p2,p3,p4,p5,p6],
            [p1,p2,p3,p4,p5,p6]
])

# initial payoff before a die has been chosen
m_payoff1 = np.array([
            [points,points,points,0,0,0],
            [points,points,points,0,0,0],
            [points,points,points,0,0,0],
            [points,points,points,0,0,0],
            [points,points,points,0,0,0],
            [points,points,points,0,0,0]
])

# payoff after you've selected at least one die in your previous rolls
m_payoff2 = np.array([
            [0,points,points,0,0,0],
            [0,0,points,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]
])

matrix_multipy = m_transition * m_payoff2
print(matrix_multipy)

