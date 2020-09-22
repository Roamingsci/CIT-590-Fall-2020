'''
Name: Yingjie Guo
PennID: 47716260
Statement of work: I worked alone.
'''
import random


def print_instructions():
    print(
        '''
Welcome to play the game 'Pig'!

As a player, you will fight against an intelligent computer AI!
Try to win! Do roll the die each turn!
In the game you will roll a die for several times, until you stop or get a six.
By adding up all the numbers you roll in the turn, you get your score for this turn. 
Remember, six is not a good number for you, it means the end of your term and erasing everything you have in this turn.
The first player gets a total score of 50 or over wins!
        
Ok, I know what you want to say, the first person to roll always have some advantage.(That's why the computer always begins first:)
Let me give you one more turn. Even if the computer reaches first, you still get a turn to reach a tie.
        
Well, for the tie, try to win in the extra turns! 

Now, let the game BEGIN!!!
        '''
          )


def computer_move(computer_score,human_score):
    '''
    The computer rolls some times. If the score gap between the human and computer is too large,
    the computer will try to roll more times to catch up or take advantage. However, if computer is in advantage,
    it will only roll once to lower the play risk.
    current computer score:parameter computer_score
    current human score:parameter human_score
    return: computer total score
    '''
    computer_turn_score = 0
    print("The computer gets:", end='')
    gap = human_score - computer_score

    if computer_score >= human_score:
        while True:
            roll_result = roll()
            print(roll_result, end=' ')
            computer_turn_score += roll_result
            if roll_result == 6:
                computer_turn_score = 0
                break
            if computer_turn_score >= 15:  # if computer in advance, try to reach 15 for each turn.
                break

    else:
        while computer_turn_score < gap + 5: # if computer is left behind, try to win 10 more in one turn.
            roll_result = roll()
            print(roll_result, end=' ')
            if roll_result == 6:
                computer_turn_score = 0 # if the roll result is 6, the turn ends and turn score =0.
                break
            else:
                computer_turn_score += roll_result

    computer_score += computer_turn_score
    print()
    return computer_score


def human_move(computer_score,human_score):
    '''
    Human turn to roll the die. Continually ask player if want to roll again.
    If roll result is 6, set this turn's score to 0.
    current computer score:parameter computer_score
    current human score:parameter human_score
    return: human total score
    '''
    human_turn_score = 0
    roll_again = first_roll()

    while roll_again:
        roll_result = roll()
        print("You get a {} for this roll.".format(roll_result))
        if roll_result != 6:
            human_turn_score += roll_result
            roll_again = ask_yes_or_no()
        else:
            print("You get a six! What a pity!") # if the roll result is 6, the turn ends and turn score =0.
            human_turn_score = 0
            break

    human_score += human_turn_score
    return human_score


def is_game_over(computer_score,human_score):
    '''
    Check if any one of the players reaches or exceeds a total of 50 points.
    Check for a tie?
    current computer score:param computer_score
    current human score:param human_score
    return: whether game is over or not. type: bool
    '''
    result = False
    a = (computer_score >= 50) and (human_score >= 50) # a tie
    b = (computer_score < 50) and (human_score < 50) # game still playing
    if (a or b) == False:
        result = True
    return result


def roll():
    '''
    roll the die
    return: the roll result
    '''
    return random.randint(1,6)


def tie_round():
    '''
    When there's a tie, play one more turn for each player.
    When the tie round score is different, the winner is determined.
    return the computer and player score in a list.
    '''
    tie_human_score = 0
    tie_computer_score = 0
    tie =True
    while tie:
        if tie_computer_score == tie_human_score:  # if there is a tie in the extra rounds, get another round!
            show_current_status(tie_computer_score,tie_human_score)
            print('Extra Round!')
            tie_computer_score = computer_move(tie_computer_score, tie_human_score)
            tie_human_score = human_move(tie_computer_score,tie_human_score)
        else:
            break
    return [tie_computer_score,tie_human_score]

def first_roll():
    '''
    This function ensures that player get at least on roll at the beginning of each turn.
    '''
    prompt = input("Do you want to roll?")
    roll_again = True

    while bool(prompt) == False or prompt[0] not in ['y', 'Y']:  # Check if the input is valid, and there must be a first roll.
        prompt = input("You must roll at least once, type y/Y to begin!")

    return roll_again


def ask_yes_or_no():
    '''
    Ask the user if wants to roll again.
    If the user responds with a string whose first character is 'y' or 'Y', the function returns True.
    If the user responds with a string whose first character is 'n' or 'N', the function returns False.
    Any other response will cause the question to be repeated until the user provides an acceptable response.
    return result as bool
    '''
    prompt = input("Do you want to roll again?")
    roll_again = True

    while bool(prompt) == False or prompt[0] not in ['y','Y','n','N']:  # Check if the input is valid
        prompt = input("Do you want to roll again?")
    else:
        if prompt[0] == 'y' or prompt[0] == 'Y':
            roll_again = True
        elif prompt[0] == 'n' or prompt[0] == 'N':
            roll_again = False

    return roll_again

def ask_play_again_or_not():
    '''
    Ask the user if wants to play again.
    If the user responds with a string whose first character is 'y' or 'Y', the function returns True.
    If the user responds with a string whose first character is 'n' or 'N', the function returns False.
    Any other response will cause the question to be repeated until the user provides an acceptable response.
    return result as bool
    '''
    prompt = input("Do you want to play again?")
    play_again = True


    while bool(prompt) == False or prompt[0] not in ['y', 'Y', 'n', 'N']: # Check if the input is valid, avoid empty input.
        prompt = input("Do you want to play again?")
    else:
        if prompt[0] == 'y' or prompt[0] == 'Y':
            play_again = True
        elif prompt[0] == 'n' or prompt[0] == 'N':
            play_again = False

    return play_again


def show_current_status(computer_score,human_score):
    '''
    Show the current scores for computer and player.
    current computer score:param computer_score
    current human score:param human_score
    '''
    print()
    print("Your opponent's current score is: ", computer_score)
    print("Your current score is: ", human_score)
    print()


def show_final_results(computer_score,human_score):
    '''
    Show the final game results for computer and player according to the rule.
    current computer score:param computer_score
    current human score:param human_score
    '''
    print()
    print("Finally, the computer gets {} and you get {}.".format(computer_score,human_score))

    if computer_score > human_score:
        print("You lost to the computer...")
        print("The computer wins you by {}.".format(computer_score - human_score))
    else:
        print("Congratulations! You win the computer!")
        print("You win the computer by {}.".format(human_score - computer_score))


def main():
    play_again = True
    while play_again:
        computer_score = 0
        human_score = 0
        result=[]
        print_instructions()
        play = True

        while play:
            print()
            show_current_status(computer_score,human_score) # show current score
            computer_score = computer_move(computer_score,human_score) # computer move
            human_score = human_move(computer_score,human_score) # human move
            play = not(is_game_over(computer_score,human_score)) # check if game is set
            if (computer_score < 50) and (human_score < 50) == True:
                continue
            elif (computer_score >= 50) and (human_score >= 50): # a tie
                print('\nA tie!\n')
                result = tie_round()
                break

        if result != []:
            show_final_results(result[0],result[1]) # show the result for the tie.
        else:
            show_final_results(computer_score,human_score) # show result for ordinary ending.
        print()

        print('Thank you for playing!\n')
        play_again = ask_play_again_or_not()


if __name__ == '__main__':
    main()