# Description: This file contains the functions to decay the temperature of the Boltzmann distribution.
# Usage: please import this file in the main file and use the function decay_temperature(episode, current_reward, temp, MODE, decay_rate) to decay the temperature.
# the parameters you need to pass are: (feel free to change the values)
# this file is mainly referred to https://github.com/aakash94/RED/blob/master/Balancer.ipynb

TEMP    = 5 # initial temperature
TEMP_DECAY    = 0.999 # decay rate
MODE_E = 'EXPONENTIAL'
MODE_L = 'LINEAR'
MODE_R = 'RBTD'
def linear_decay( episode, decay_till=1024 , start_val = 10, end_val = 0.01):
    t = (((end_val - start_val)/decay_till)*episode) + start_val
    return max(t, end_val)

REWARD_THRESHOLD = 0
def reward_based_t_decay(current_reward, temp=TEMP, highest_t=10, stop_red=0.1, lowest_t=0.01, target_reward=500, target_increment=1):
        
    global REWARD_THRESHOLD
    
    
#     if eps < lowest_ep:
#         return eps
    
#     if eps < stop_red :
#         eps *= decay_rate
#         return rps
    
    steps_to_move_in = target_reward
    #steps_to_move_in = steps_to_move
    quanta = (highest_t - lowest_t)/steps_to_move_in   
    
    
    #REWARD_THRESHOLD = min(REWARD_THRESHOLD, 200)
    
    if current_reward > REWARD_THRESHOLD :
        REWARD_THRESHOLD += target_increment
        temp -= quanta
        
    return max(temp, lowest_t)

REWARD_THRESHOLD = 0
def reward_based_t_decay1(current_reward, temp=TEMP, highest_t=1.0, lowest_t=0.01, target_reward=200, target_increment=1, steps_to_move=256):
    
    steps_to_move_in = target_increment
    # steps_to_move_in = steps_to_move
    
    quanta = (highest_t - lowest_t)/steps_to_move_in
        
    return max(temp, lowest_t)

def exponential_decay (temp=TEMP, decay_rate=TEMP_DECAY):
    # need to decide decay_rate.
    temp *= decay_rate
    return  temp


def decay_temperature(episode, current_reward=0, temp=TEMP, MODE=MODE_L, decay_rate=TEMP_DECAY):
    
    if MODE == MODE_L:
        temp = linear_decay(episode)
    
    elif MODE == MODE_E:
        temp = exponential_decay(temp, decay_rate)
    
    elif MODE == MODE_R:
        temp = reward_based_t_decay(current_reward=current_reward, temp=temp)
    
    return temp



