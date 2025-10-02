import turtle as t

color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
screen = t.Screen()
screen.setup(1000, 800, 0, 0)
pen = t.Turtle()
pen.speed(0)
pen.home()
pen.penup()
pen.hideturtle()
pen.color('black')
pen.pensize(2)


def draw_resistor(colors, r_value):
    pen.goto(-200,-80)
    pen.pendown()
    pen.fd(400)
    pen.lt(90)
    pen.fd(200)
    pen.lt(90)
    pen.fd(400)
    pen.lt(90)
    pen.fd(200)
    pen.penup()
    pen.goto(200,20)
    pen.pensize(4)
    pen.pendown()
    pen.lt(90)
    pen.fd(200)
    pen.penup()
    pen.goto(-200, 20)
    pen.pensize(4)
    pen.pendown()
    pen.lt(180)
    pen.fd(200)
    pen.penup()
    pen.pensize(2)
    pen.home()
    pen.goto(-190,-80)
    pen.pendown()
    pen.fd(10)
    pen.lt(90)
    for i in range(3):
        pen.fillcolor(colors[i])
        pen.begin_fill()
        pen.fd(200)
        pen.rt(90)
        pen.fd(60)
        pen.rt(90)
        pen.fd(200)
        pen.end_fill()
        pen.lt(90)
        pen.fd(20)
        pen.lt(90)
    pen.penup()
    pen.home()
    pen.goto(0,-150)
    pen.write(f'Resistance Value is {r_value:,}{chr(0x03a9)}',False,'center',('Arial',24,'bold'))

def small_resistors(num, resistors, r_total):
    colors: list[list] = [[ 0 for _ in range(3)] for _ in range(len(resistors))]

    for i in range(len(resistors)):
        digits = [int(digit) for digit in (resistors[i])]
        count = 0
        value = int(resistors[i])
        while value > 9:
            value = value / 10
            count += 1
        colors[i][2] = count-1
        colors[i][0] = digits[0]
        colors[i][1] = digits[1]
        pen.home()
        pen.goto(-140*len(resistors)/2+i*140,20)
        pen.pendown()
        pen.bk(40)
        pen.penup()
        pen.home()
        pen.goto(-140*len(resistors)/2+i*140,0)
        pen.pendown()
        pen.fd(100)
        pen.lt(90)
        pen.fd(40)
        pen.lt(90)
        pen.fd(100)
        pen.lt(90)
        pen.fd(40)
        pen.penup()
        pen.home()
        pen.goto(-140*len(resistors)/2+i*140,0)
        pen.lt(90)
        for j in range(3):
            pen.fillcolor(color_list[int(colors[i][j])])
            pen.begin_fill()
            pen.fd(40)
            pen.rt(90)
            pen.fd(10)
            pen.rt(90)
            pen.fd(40)
            pen.end_fill()
            pen.lt(90)
            pen.fd(10)
            pen.lt(90)
        pen.penup()
        pen.home()
        pen.goto(-140*len(resistors)/2+i*140,-30)
        pen.write(f'R{i+1}:{resistors[i]}{chr(0x03a9)}', False, 'left',('Arial',14,'bold'))
    pen.penup()
    pen.home()
    pen.goto(-140*len(resistors)/2 + len(resistors) * 130,20)
    pen.pendown()
    pen.fd(40)
    pen.penup()
    pen.goto(0,-150)
    pen.write(f'Resistance Value is {r_total:,}{chr(0x03a9)}',False,'center',('Arial',24,'bold'))

def draw_resistors(num,resistors,r_total):# Each resistor is around 140 pixels in length
    for i in range(num):
        pen.penup()
        pen.home()
        pen.goto((-150 * num/2) + (i * 100),50)
        pen.pendown()
        pen.fd(20)
        pen.rt(45)
        pen.fd(10)
        for _ in range(3):
            pen.lt(90)
            pen.fd(20)
            pen.rt(90)
            pen.fd(20)
        pen.lt(90)
        pen.fd(10)
        pen.rt(45)
        pen.fd(20)
        pen.penup()
        pen.goto((-135 * num/2) + (i * 100),0)
        pen.write(f'{resistors[i]} k{chr(0x03a9)}',False,"left",('Arial', 18, 'bold'))
    pen.penup()
    pen.goto(-200,-100)
    pen.pendown()
    pen.write(f'Total Resistance: {r_total} k{chr(0x03a9)}',False, 'left', ('Arial', 24, 'bold'))


def id_resistor() :
    colors = []
    color_bands = []
    for n in range(1, 4):
        color = ''
        while color not in color_list:
            color = input(f'Enter the color for band {n}: ')
        colors.append(color)
        color_bands.append(color_list.index(color))
    band1,band2,band3 = color_bands[0],color_bands[1],color_bands[2]
    r_value = (band1*10 + band2) * 10 ** band3
    draw_resistor(colors, r_value) #draw_resistor(colors,r_value)
    x = input('Press enter to continue...')
    menu()


def series_resistors():
    for _ in range(20):
        print('')
    print('*' * 40)
    print('*      Calculate Series Resistance     *')
    print('*' * 40)
    for _ in range(3):
        print('')
    num_resistors = ''
    while not num_resistors.isnumeric() or int(num_resistors) > 6 or int(num_resistors) < 2:
        num_resistors = input('Please enter the number of resistors in the circuit(2-6): ')
    num_resistors = int(num_resistors)
    resistance = 0
    resistors = []
    for x in range(num_resistors):
        resistors.append(input(f'Enter the value of resistor R{x+1} in ohms: '))
    for z in range(num_resistors):
        resistance += float(resistors[z])
    print()
    print(f'The total resistance of this circuit is {resistance} ohms')
    small_resistors(num_resistors,resistors,resistance)
    x = input('Press enter to continue...')
    menu()


def parallel_resistors():
    for _ in range(20):
        print('')
    print('*' * 40)
    print('*    Calculate Parallel Resistance     *')
    print('*' * 40)
    for _ in range(3):
        print('')
    num_resistors = ''
    while not num_resistors.isnumeric() or int(num_resistors) > 10 or int(num_resistors) < 2:
        num_resistors = input('Please enter the number of resistors in the circuit(2-10): ')
    num_resistors = int(num_resistors)
    resistance = []
    resistors = []
    r_total = 0
    for x in range(num_resistors):
        resistors.append(input(f'Enter the value of resistor{x+1} in k-ohms: '))
    for y in range(num_resistors):
        resistance.append(1/float(resistors[y]))
    for z in range(num_resistors):
        r_total += float(resistance[z])
    r_total = 1/r_total
    print(f'The total resistance of this circuit is {round(r_total, 1)}K ohms')
    draw_resistors(num_resistors, resistors, resistance)
    x = input('Press enter to continue...')
    menu()


def menu():
    pen.clear()
    pen.hideturtle()
    print(40*'*')
    print('*       Resistor ID and utility        *')
    print(40*'*')
    print('*    Please Select an Option Below     *')
    print(40*'*')
    print('*',36*' ','*')
    print('*    1) Identify with Color Code       *')
    print('*',36*' ','*')
    print('*    2) Find Resistance in Series      *')
    print('*',36*' ','*')
    print('*    3) Find Resistance in Parallel    *')
    print('*',36*' ','*')
    print('*    4)           EXIT                 *')
    print(40*'*')
    option = ''
    while not option.isnumeric() or option not in ['1','2','3','4']:
        option = input('Enter Your Choice: ')
    option = int(option)
    match option:
        case 1:
            id_resistor()
        case 2:
            series_resistors()
        case 3:
            parallel_resistors()
        case 4:
            exit()


def main() -> None:
    menu()
    t.done()


if __name__ == '__main__':
    main()
