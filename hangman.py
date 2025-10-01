from random import choice
import turtle as t

tpen = t.Turtle()
tpen.speed(0)
tpen.pensize(2)
tpen.hideturtle()
tpen.penup()
count = 1
correct = 0
guesses = []

def draw_gallows():
    tpen.goto(-200,0)
    tpen.pendown()
    tpen.fd(400)
    tpen.lt(90)
    tpen.fd(20)
    tpen.lt(90)
    tpen.fd(400)
    tpen.lt(90)
    tpen.fd(20)
    tpen.home()
    tpen.penup()
    tpen.fd(100)
    tpen.lt(90)
    tpen.fd(20)
    tpen.pendown()
    tpen.fd(250)
    tpen.lt(90)
    tpen.fd(100)
    tpen.lt(90)
    tpen.fd(30)

def draw_blanks(word):
    num_blanks = len(word)
    blank_length = 400//num_blanks
    tpen.penup()
    tpen.home()
    tpen.goto(-200,-100)
    for i in range(len(word)):
        tpen.pendown()
        tpen.fd(blank_length-20)
        tpen.penup()
        tpen.fd(20)
    tpen.goto(-360,-195)
    tpen.write('Used Letters: ', False, 'left', ('Arial', 18, 'normal'))

def draw_head():
    tpen.penup()
    tpen.goto(0, 200)
    tpen.pendown()
    tpen.circle(20)
    tpen.penup()

def draw_body():
    tpen.penup()
    tpen.home()
    tpen.goto(0, 200)
    tpen.pendown()
    tpen.rt(90)
    tpen.fd(100)
    tpen.penup()

def draw_l_arm():
    tpen.penup()
    tpen.home()
    tpen.goto(0, 180)
    tpen.pendown()
    tpen.rt(45)
    tpen.fd(50)
    tpen.penup()

def draw_r_arm():
    tpen.penup()
    tpen.home()
    tpen.goto(0, 180)
    tpen.pendown()
    tpen.rt(135)
    tpen.fd(50)
    tpen.penup()

def draw_l_leg():
    tpen.penup()
    tpen.home()
    tpen.goto(0, 100)
    tpen.pendown()
    tpen.rt(45)
    tpen.fd(50)
    tpen.penup()

def draw_r_leg():
    tpen.penup()
    tpen.home()
    tpen.goto(0, 100)
    tpen.pendown()
    tpen.rt(135)
    tpen.fd(50)
    tpen.penup()

def show_intro():
    tpen.penup()
    tpen.goto(-200,350)
    tpen.write('Welcome to the Hangman Game',False, 'left',('Arial',20,'bold'))
    tpen.goto(-125, 320)
    tpen.write(f'Can you save yourself from the noose?',False, 'left',('Arial',12,'normal'))
    tpen.goto(-130, 290)
    tpen.write(f'You only have 6 guesses, use them wisely!',False, 'left',('Arial',12,'normal'))

def get_word():
    with open('word_list.txt','r+') as file:
        word_list = file.read()
        words = word_list.split()
    word = choice(words)
    return word

def get_guess() -> str:
    global guesses
    guess = ''
    while not guess.isalpha() and guess not in guesses:
        guess = t.textinput(' Enter Your Guess: ','Any letter from A - Z')
    guess = guess.lower()
    guesses.append(guess)
    return guess

def check_guess(word,guess):
    global correct
    tpen.penup()
    tpen.home()
    tpen.goto(-200, -100)
    length = len(word)
    blank_length = 400 // length
    for i in range(length):
        if guess not in word:
            draw_parts(word)
            tpen.goto(-280 + (count * 50), -200)
            tpen.write(guess.upper(), False, 'center', ('Arial', 24, 'bold'))
            return False
        else:

            for j in range(length):
                if guess == word[j]:
                    correct += 1
                    tpen.goto(-200+(j * blank_length + (blank_length//3)), -100)
                    tpen.write(guess.upper(), False, 'center', ('Arial', 24, 'bold'))
            if correct == length:
                tpen.goto(-350, -300)
                tpen.color('green')
                tpen.write('YOU ARE A WINNER !!!', False, 'left', ('Arial', 48, 'bold'))
                end_game = t.textinput('YOU WIN !!!', 'Press OK to Exit')
                exit()
            return True
    return None

def draw_parts(word):
    global count
    match count:
        case 1:
            draw_head()
        case 2:
            draw_body()
        case 3:
            draw_l_arm()
        case 4:
            draw_r_arm()
        case 5:
            draw_l_leg()
        case 6:
            draw_r_leg()
    count += 1
    if count >= 7:
        tpen.penup()
        tpen.home()
        tpen.goto(-10,215)
        tpen.write('X   X')
        tpen.goto(-200,-300)
        tpen.color('red')
        tpen.write('YOU LOSE !!!', False, 'left', ('Arial', 48, 'bold'))
        tpen.goto(-200 - (len(word)*10),-350)
        tpen.write(f'The word you missed is {word.upper()}', False, 'left', ('Arial', 24, 'bold'))
        end_game = t.textinput('YOU LOSE !!!', 'Press OK to Exit')
        exit()


def main_menu():
    print('*' * 32)
    print('*     1) Start a New Game      *')
    print('*     2) Continue the Game     *')
    print('*     3) Exit the Game         *')
    print('*' * 32)
    option = input('Enter your choice from the menu above: ')
    match option:
        case '1':
            print('New Game')
        case '2':
            print('Continue')
        case '3':
            print('Quit')
            exit()

def main() -> None:
    running = True
    draw_gallows()
    show_intro()
    word = get_word()
    draw_blanks(word)
    #main_menu()
    while running:
        guess = get_guess()
        check_guess(word,guess)
    t.mainloop()


if __name__ == '__main__':
    main()

