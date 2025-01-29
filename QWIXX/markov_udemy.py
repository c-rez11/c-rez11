# Using the Markov course on Udemy, trying to create a simple algorithm
import numpy as np

S = ['start','1','2','3','4','5','6','1_used','2_used','3_used','4_used','5_used','6_used','end'] # define the state space

A = ['new','old'] # define the action space

payoff = 5

# define transition probabiliites
P = {
    'start': {
        'new': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},
        'old': {'start': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 1},},
    '1': {
        'new': {'start': 0, '1': 0, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 1/6, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '2': {
        'new': {'start': 0, '1': 0, '2': 0, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 2/6, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '3': {
        'new': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '4': {
        'new': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '5': {
        'new': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '6': {
        'new': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '1_used': {
        'new': {'start': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 1},
        'old': {'start': 0, '1': 0, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 1/6, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '2_used': {
        'new': {'start': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 1},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '3_used': {
        'new': {'start': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 1},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '4_used': {
        'new': {'start': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 1},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '5_used': {
        'new': {'start': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 1},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    '6_used': {
        'new': {'start': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 1},
        'old': {'start': 0, '1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 0},},
    'end': {
        'new': {'start': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 1},
        'old': {'start': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '1_used': 0, '2_used': 0, '3_used': 0, '4_used': 0, '5_used': 0, '6_used': 0, 'end': 1},},   
    
}

# define the reward
R = {
    'start': {
        'new': payoff,
        'old': 0,},
    '1': {
        'new': payoff,
        'old': 0,},
    '2': {
        'new': payoff,
        'old': 0,},
    '3': {
        'new': payoff,
        'old': 0,},
    '4': {
        'new': payoff,
        'old': 0,},
    '5': {
        'new': payoff,
        'old': 0,},
    '6': {
        'new': payoff,
        'old': 0,},
    '1_used': {
        'new': payoff,
        'old': 0,},
    '2_used': {
        'new': payoff,
        'old': 0,},
    '3_used': {
        'new': payoff,
        'old': 0,},
    '4_used': {
        'new': payoff,
        'old': 0,},
    '5_used': {
        'new': payoff,
        'old': 0,},
    '6_used': {
        'new': payoff,
        'old': 0,},
    'end': {
        'new': payoff,
        'old': 0,}
}

gamma = 1 # define the discount factor

# compute the value function
V = {s: 0 for s in S}
print(V)
for _ in range(100): # iterate for a fixed number of times
    for s in S:
        for a in A:
            value = 0
            for s_prime in S: 
                transition_prob = P[s][a][s_prime]
                reward = R[s][a]
                next_state_value = V[s_prime]
                value = value + transition_prob * (reward + gamma * next_state_value)
                # Bellman equation
                V[s] = max(V[s], value)
print(V)