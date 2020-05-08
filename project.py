# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:06:52 2020

@author: shubh
"""


from IPython.display import clear_output

def display_board(board):
    
    '''
    Creating board
    
    '''
    
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
test_board = [' ']*10
display_board(test_board)

def player_input():
    
    '''
    Output = (player1,player2)
    
    '''
    marker=''
    #ask player 1 for X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player1 one should choose X or O:').upper()
    
    
    if marker == 'X':
        return ('X','O') #(player1,player2) values
        
    else:
        return('O','X')

def place_marker(board,marker,position):
    '''
    Assigning X and O to the 1-9 pos 
    
    '''
    board[position] = marker
    
def win_check(board,mark):
    '''
    To check which marker/player won the game
    
    '''
    return ((board[7] == board[8] == board[9] == mark) or  #for top row
    (board[4] == board[5] == board[6] == mark) or #for middle row
    (board[1] == board[2] == board[3] == mark) or #for bottom row
    (board[7] == board[4] == board[1] == mark) or #for 1st column
    (board[8] == board[5] == board[2] == mark) or #for 2nd column
    (board[9] == board[6] == board[3] == mark) or #for 3rd column
    (board[7] == board[5] == board[3] == mark) or #for diagonal1
    (board[9] == board[5] == board[1] == mark))  #for diagonal2


import random

def first_move():
    
    '''
    who plays first?
    
    '''
    flip = random.randint(0,1)
    if flip == 0:
        return 'player2'
    else:
        return 'player1'
              
        
def board_check(board,position):
    
    '''
    position to mark is empty or not
    
    '''
    
    return board[position] == ' '


def full_board_check(board):
    '''
    Board is full or not 
    
    '''
    for i in range(1,10):
        if board_check(board, i):
            return False
    return True   # board is full in this case


def player_choice(board):
    
    '''
    mark the position
    
    '''
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not board_check(board,position):
        position = int(input('Choose a position (1-9:)'))
        
    return position

def replay():
    
    choice = input('Do u want to play again? enter Yes or NO')
    
    return choice == 'Yes'


#while loop to keep the game running
print('Welcome to the game ')

while True:
    
    #play game 
    
    #set everything(board, who first,marker,X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = first_move()
    print(turn + 'will go first')
    
    play_game = input('Ready to play? y or n')
    
    if play_game == 'y':
        game_on = True
        
    else:
        game_on = False
    
    
    ##gameplay
    while game_on:
        
        
        if turn == 'player1':
            
            #show board
            display_board(the_board)
            # choose posn
            position = player_choice(the_board)
            # place marker
            place_marker(the_board,player1_marker,position)
            # check if won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player1 has won...eeewww')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie ;-;')
                    break
                else:
                    turn = 'player2'
                    
        else:
            
            
             #show board
            display_board(the_board)
            # choose posn
            position = player_choice(the_board)
            # place marker
            place_marker(the_board,player2_marker,position)
            # check if won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('player2 has won...eeewww')
                
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie ;-;')
                    game_on = False
                else:
                    turn = 'player1'
            
           
    
    if not replay():
        break
#break out of the loop on replay()        
    
    
    
    