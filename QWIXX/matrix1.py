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

m_start = np.array([
            [p1,p2,p3,0,0,0],
            [p1,p2,p3,0,0,0],
            [p1,p2,p3,0,0,0],
            [p1,p2,p3,0,0,0],
            [p1,p2,p3,0,0,0],
            [p1,p2,p3,0,0,0]
])
sum_start = np.sum(m_start)
EV_start = (sum_start)/max(roll_list)*points


m_next = np.array([
            [0,p2,p3,0,0,0],
            [0,0,p3,0,0,0],
            [0,0,0,0,0,0],
            [p1,p2,p3,0,0,0],
            [p1,p2,p3,0,0,0],
            [p1,p2,p3,0,0,0]
])
sum_next = np.sum(m_next)
EV_next = (sum_next)/max(roll_list)*points

row_sum_dict = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

for key in row_sum_dict:
    row_sum_dict[key] = np.sum(m_next[(key-1),:])




# game function
for roll in range(1,2):
#for roll in range(1,rolls+1):
    number_rolled = 1
    #number_rolled = np.random.randint(1,7)
    if number_rolled not in target_list:
        print(number_rolled, 'no luck')
    else:
        loop_dict = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
        for key in loop_dict:
            if key < max(target_list):
                loop_dict[key] = row_sum_dict[key]

        pro_dict = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
        loop_rolls_left = rolls_left
        

        for key in pro_dict:
            discount = 1
            if key == 1:
                pro_dict[key] = points * (1-((1-loop_dict[key])**loop_rolls_left))
            else:
                inner_dict = {}
                for n in range(1,rolls_left+1):
                    inner_dict[n] = 0
                for n in inner_dict:
                    if rolls_left == 1:
                        inner_dict[n] = 0
                    if key == max(prob_dict):
                        inner_dict[n] = 0
                    else:
                        inner_dict[n] = n * prob_dict[key] * prob_dict[key+1] * ((1-prob_dict[key]) + (1-prob_dict[key+1])) ** (n - 1)
                        
                        
                
                print('inner dict',inner_dict)
                sum_inner_dict = sum(inner_dict.values())
                pro_dict[key] = points * sum_inner_dict

            

            if (loop_rolls_left-1) > 0:
                loop_rolls_left = loop_rolls_left - 1
            else:
                loop_rolls_left = 0
        

        sum_pro_dict = 0
        for key in pro_dict:
            sum_pro_dict = sum_pro_dict + pro_dict[key]
        
        pro_EV = points + sum_pro_dict
    
        con_EV = EV_start + EV_next*(rolls_left-1)
        
        selection = 0
        if pro_EV > con_EV:
            selection = number_rolled
        print(number_rolled, pro_EV, con_EV, selection)
        print('row_sum_dict')
        print(row_sum_dict)
        print('')
        print('loop_dict')
        print(loop_dict)
        print('')
        print('pro_dict')
        print(pro_dict)


rolls_left = rolls_left - 1
