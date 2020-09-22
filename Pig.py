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
    computer_turn_score = 0
    print("The computer gets:", end='')
    gap = human_score - computer_score

    if computer_score >= human_score:
        computer_turn_score = roll()
        print(computer_turn_score)
        if computer_turn_score == 6:
            computer_turn_score = 0
    else:
        while computer_turn_score < gap + 3:
            roll_result = roll()
            print(roll_result, end=' ')
            if roll_result == 6:
                computer_turn_score = 0
                break
            else:
                computer_turn_score += roll_result

    computer_score += computer_turn_score
    print()
    return computer_score


def human_move(computer_score,human_score):

    human_turn_score = 0
    roll_again = ask_yes_or_no()

    while roll_again:
        roll_result = roll()
        print("You get a {} for this roll.".format(roll_result))
        if roll_result != 6:
            human_turn_score += roll_result
            roll_again = ask_yes_or_no()
        else:
            print("You get a six! What a pity!")
            human_turn_score = 0
            break

    human_score += human_turn_score
    return human_score


def is_game_over(computer_score,human_score):
    result = False
    a = (computer_score >= 50) and (human_score >= 50)
    b = (computer_score < 50) and (human_score < 50)
    if (a or b) == False:
        result = True
    return result


def roll():
    return random.randint(1,6)


def tie_round():
    tie_human_score = 0
    tie_computer_score = 0
    tie =True
    while tie:
        if tie_computer_score == tie_human_score:
            show_current_status(tie_computer_score,tie_human_score)
            print('Extra Round!')
            tie_computer_score = computer_move(tie_computer_score, tie_human_score)
            tie_human_score = human_move(tie_computer_score,tie_human_score)
        else:
            break
    return [tie_computer_score,tie_human_score]


def ask_yes_or_no():
    prompt = input("Do you want to roll?")
    roll_again = True

    while bool(prompt) == False or prompt[0] not in ['y','Y','n','N']:
        prompt = input("Do you want to roll?")
    else:
        if prompt[0] == 'y' or prompt[0] == 'Y':
            roll_again = True
        elif prompt[0] == 'n' or prompt[0] == 'N':
            roll_again = False
    return roll_again

def ask_play_again_or_not():
    prompt = input("Do you want to play again?")
    play_again = True

    while bool(prompt) == False or prompt[0] not in ['y', 'Y', 'n', 'N']:
        prompt = input("Do you want to play again?")
    else:
        if prompt[0] == 'y' or prompt[0] == 'Y':
            play_again = True
        elif prompt[0] == 'n' or prompt[0] == 'N':
            play_again = False
    return play_again


def show_current_status(computer_score,human_score):
    print()
    print("Your opponent's current score is: ", computer_score)
    print("Your current score is: ", human_score)
    print()


def show_final_results(computer_score,human_score):
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
            show_current_status(computer_score,human_score)
            computer_score = computer_move(computer_score,human_score)
            human_score = human_move(computer_score,human_score)
            play = not(is_game_over(computer_score,human_score))
            if (computer_score < 50) and (human_score < 50) == True:
                continue
            elif (computer_score >= 50) and (human_score >= 50):
                print('\nA tie!\n')
                result = tie_round()
                break

        if result != []:
            show_final_results(result[0],result[1])
        else:
            show_final_results(computer_score,human_score)
        print()

        print('Thank you for playing!\n')
        play_again = ask_play_again_or_not()


if __name__ == '__main__':
    main()