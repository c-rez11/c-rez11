# optimal strategy in the dice game QWIXX
import numpy as np 

# # create white dice
# white_dice1 = np.random.randint(0,6)
# white_dice2 = np.random.randint(0,6)
# sum_white = white_dice1 + white_dice2
# print(white_dice1, white_dice2, sum_white)

# # the red numbers
# red_list = np.arange(2,12)
# print(red_list)

# # probabilities
# p2 = 1/36
# p3 = 2/36
# p4 = 3/36
# p5 = 4/36
# p6 = 5/36
# p7 = 6/36
# p8 = 5/36
# p9 = 4/36
# p10 = 3/36
# p11 = 2/36
# p12 = 1/36


# QWIXX demo but much simpler

# Parameters: 1 die that we will roll 4 times. The numbers we want are 1, 2, and 3.



rolls = 4
rolls_left = rolls-1

# points per roll
points = 5

# list of numbers
simple_list = np.arange(1,7)

# list of target numbers
target_list = np.arange(1,4)

# probability of each roll
p1 = 1/6
p2 = 1/6
p3 = 1/6

# rolls and probability dictionary
dict_prob = {
    1:p1,
    2:p2,
    3:p3
}

max_key = max(dict_prob)
max_prob = dict_prob[max_key]

max_dict = {}
for key in dict_prob:
    if key < max_key:
        new_key = f'max_key{key}'
        max_dict[new_key] = dict_prob[max_key - key]


# other parameters 
selection = 0

# list of pros and cons list
EV_pro1 = 0
EV_pro2 = 0
EV_pro3 = 0
EV_con1 = 0
EV_con2 = 0
EV_con3 = 0

pro_dict = {
    1: EV_pro1,
    2: EV_pro2,
    3: EV_pro3
}

con_dict = {
    1: EV_con1,
    2: EV_con2,
    3: EV_con3
}

# for key in dict_prob:
#     if key>1:
#         sum_prob = sum_prob + dict_prob[key]
# print(sum_prob)

for roll in range(1,rolls+1):
    number_rolled = np.random.randint(1,7)
    starting_prob = 0
    sum_prob1 = 0
    sum_prob2 = 0
    con_prob1 = 0
    con_prob2 = 0

    # list of pros and cons list
    EV_pro1 = 0
    EV_pro2 = 0
    EV_pro3 = 0
    EV_con1 = 0
    EV_con2 = 0
    EV_con3 = 0
    EV_pro_total = 5
    EV_con_total = 0

    if number_rolled not in target_list or number_rolled <= selection:
        print(number_rolled, 'no luck')
    else:
        # for key in dict_prob:
        #     if key > selection:
        #         starting_prob = starting_prob + dict_prob[key]
        # for key in dict_prob:
        #     if key>max(number_rolled,selection):
        #         sum_prob1 = sum_prob1 + dict_prob[key]
        # for key in dict_prob:
        #     if key>max(number_rolled+1,selection):
        #         sum_prob2 = sum_prob2 + dict_prob[key]
        # for key in dict_prob:
        #     if selection < 1:
        #         if key < max(target_list):
        #             con_prob1 = con_prob1 + dict_prob[key]
        #     else:
        #         if key > (selection + 1):
        #             con_prob1 = con_prob1 + dict_prob[key]
        # for key in dict_prob:
        #     if selection < 1:
        #         if key < max(target_list-1):
        #            con_prob2 = con_prob2 + dict_prob[key] 
        #     else:
        #         if key > (selection + 2):
        #             con_prob2 = con_prob2 + dict_prob[key]

        starting_prob = sum(dict_prob[key] for key in dict_prob if key > selection)
        sum_prob1 = sum(dict_prob[key] for key in dict_prob if key > max(number_rolled, selection))
        sum_prob2 = sum(dict_prob[key] for key in dict_prob if key > max(number_rolled + 1, selection))
        con_prob1 = sum(dict_prob[key] for key in dict_prob if (selection < 1 and key < max(target_list)) or
                    (selection >= 1 and key > (selection + 1)))
        con_prob2 = sum(dict_prob[key] for key in dict_prob if (selection < 1 and key < max(target_list - 1)) or
                    (selection >= 1 and key > (selection + 2)))


        con_dict = {
            1: lambda: points*1*(1-((1-(starting_prob))**rolls_left)),
            2: lambda: points*2*(
                # if ends in 3
                    max_prob * (1-((1-(con_prob1))**(rolls_left-1))) +
                # if ends in 2
                    max_dict['max_key1'] * (1-((1-(con_prob2))**(rolls_left-1)))
                ),
            3: lambda: points*3*(max_prob*max_dict['max_key1']*max_dict['max_key2'])   
        }
        for key in con_dict:
            if rolls_left < key:
                con_dict[key] = 0
            else:
                con_dict[key] = con_dict[key]()
            EV_con_total = EV_con_total + con_dict[key]
            
        pro_dict = {
            1: lambda: points*1*(1-((1-(sum_prob1))**rolls_left)),
            2: lambda: points*2*(
                # if ends in 3
                max_prob * (1-((1-(sum_prob2))**(rolls_left-1)))
                ),
            3: lambda: points*3*(max_prob*max_dict['max_key1']*max_dict['max_key2'])  

        }
        for key in pro_dict:
            if rolls_left <= key:
                pro_dict[key] = 0

            else:
                pro_dict[key] = pro_dict[key]()
            EV_pro_total = EV_pro_total + pro_dict[key]
        
        if EV_pro_total > EV_con_total:
            selection = number_rolled
        print(number_rolled, EV_pro_total, EV_con_total, selection)
    rolls_left = rolls_left -1


