# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
from indiv_assign_1 import linear_congruence 

throw_10 =0
throw_00=0
throw_11=0
throw_01=0

def computer_decision():
    if player_number == 0 and throw_10 > throw_00:
       comp_dec = 1
    elif player_number == 0 and throw_10 < throw_00:
       comp_dec = 0
    elif player_number == 0:
       comp_dec = random.randint(0,1)    
    if player_number == 1 and throw_11 > throw_01:
       comp_dec = 1
    elif player_number == 1 and throw_11 < throw_01:
       comp_dec = 0
    elif player_number == 1:
       comp_dec = random.randint(0,1)       
    return(comp_dec)   
    
 
#variables definition session

#""" Reset the variables"""
x_moves=""
x_levels=""
result_computer = 0
result_player = 0
seed = random.randint(0,100)
check_sum = (2**31)
x_level = 0
x_moves = 0    
print("Welcome to Human Behaviour Predictor by Daniel López")



#Code to create the level selection
while True:    
    try :
        x_level = int(input("""Choose the type of game (1:Easy; 2:Dificult):"""))
        if x_level == 2:
            break
        elif x_level == 1:
            break
        else:
            print("""C'mon... your not that good...""")
    except:
        print("""The level chosen should be 1 or 2""")
              

""" Code to create the number of moves to be played """

#x_moves= int(input("Enter the number of moves:"))
while True:
    try:
        x_moves= int(input("""Enter the number of moves:"""))
        if x_moves > 0:
            break
        else: print(""" Come on... let's play for a bit!!!""")
    except:
        print("""Ooops!! Thats not a number""")
    

print("""---""")

""" Choose your move number"""
for i in range (1,x_moves+1):
    while True:
        try:
            player_number=int(input("""Choose your move number (0 or 1):"""))
            if player_number == 1:
                break
            elif player_number == 0:
                break
            else:
                print("""Don't be cheeky... Use binary numbers 1 or 0""")
        except:
            print(""" Difficulties reading?? Only numbers!! """)
        
    #"""cpu_throw first play is random and always random if easy"""
    if x_level== 1:
        computer_number = linear_congruence (seed)
        if seed < check_sum:
            computer_number=0
        else:
            computer_number = 1   
    #elif i == 1:
    #    computer_number = linear_congruence (seed)
    #   seed=linear_congruence 
    else:
    #""" if difficult use algorythm throw 00, 01,10,11 """
         computer_number = computer_decision()
         
    #""" first compare results from x_choose and cpu_throw"""
    if player_number == computer_number:
        #result_computer_org = 1
        result_computer= result_computer+1
        result= """computer wins"""
    elif player_number != computer_number:
        #result_player_org= 1
        result_player=result_player+1
        result= """player wins"""
    
    print("""player=""" , player_number ,"","""machine=""",computer_number, "" ,"-", result)
    print("""PLAYER:""" , "*"*int(result_player))
    print("""COMPUTER:""" , "*"*int(result_computer))
    print("""---""")
    
"""end loop"""

if x_level == 1:
    print("""easy game is over, final score: Player""" , result_player , "-" , result_computer , """ computer""")
    if result_player > result_computer:
        print("""  - you won """)
    elif result_player < result_computer:
        print( """ computer - you won """)
    else: 
        print( "it was a tie")
        print("play against the computer and see if you are able to beat it")
else:
    print("""difficult game is over, final score: Player""" , result_player , "-" , result_computer , """ computer""")
    if result_player > result_computer:
        print("""  - you won """)
    elif result_player < result_computer:
        print( """ computer - you won """)
    else: 
        print( "it was a tie")
        print("play against the computer and see if you are able to beat it")

#repeat while True






