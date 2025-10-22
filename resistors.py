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

def draw_result(voltage, current, resistance):
    pen.penup()
    pen.home()
    pen.goto(-50, -250)
    pen.write(f'An input voltage of {voltage} volts', False, 'center', ('Arial', 18, 'bold'))
    pen.goto(-50, -280)
    pen.write(f'across a resistance of {resistance} ohms', False, 'center', ('Arial', 18, 'bold'))
    pen.goto(-50, -310)
    pen.write(f'will produce a current of {round(current,4)} amps', False, 'center', ('Arial', 18, 'bold'))


def calculate_current():
    circuit_type = ''
    while circuit_type not in ['1', '2']:
        circuit_type = input('Enter the circuit type- 1:Series 2:Parallel ')
    voltage = ''
    while not voltage.isnumeric():
        voltage = input('Enter the voltage applied to the circuit in volts: ')
    voltage = int(voltage)
    resistance = 0
    match circuit_type:
        case '1':
            resistance = series_resistors()
            current = voltage / resistance
            draw_result(voltage, current, resistance)
            x = input('Press enter to continue...')
            return

        case '2':
            resistance = parallel_resistors()
            current = voltage / round(resistance,2)
            draw_result(voltage, current, round(resistance,2))
            x = input('Press enter to continue...')
            return


def draw_resistor(colors, r_value):
    pen.goto(-200,-80)
    pen.pendown()
    pen.fillcolor('#e1b29b')
    pen.begin_fill()
    pen.fd(400)
    pen.lt(90)
    pen.fd(200)
    pen.lt(90)
    pen.fd(400)
    pen.lt(90)
    pen.fd(200)
    pen.end_fill()
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
    pen.goto(-50,-150)
    pen.write(f'Resistance Value is {r_value:,}{chr(0x03a9)}',False,'center',('Arial',18,'bold'))

def draw_resistors(resistors, circuit_type):
    match circuit_type:
        case 'series':
            r_total = 0
            for r in range(len(resistors)):
                r_total += int(resistors[r])
            colors: list[list] = [[ 0 for _ in range(3)] for _ in range(len(resistors))]
            pen.penup()
            pen.home()
            pen.goto((-140 * len(resistors)/2) - 40, 20)
            pen.pendown()
            pen.lt(90)
            pen.fd(60)
            pen.bk(20)
            pen.write(chr(0x2b9d), False,'center',('Arial',18,'bold'))
            pen.penup()
            pen.fd(40)
            pen.write("+V", False,'center',('Arial',18,'bold'))
            pen.penup()
            pen.home()
            pen.goto((140 * len(resistors))/2, 20)
            pen.pendown()
            pen.rt(90)
            pen.fd(40)
            pen.penup()
            pen.fd(20)
            pen.write(chr(0x23da), False,'center',('Arial',18,'bold'))
            pen.fd(40)
            pen.write("GND", False,'center',('Arial',18,'bold'))
            pen.penup()
            for i in range(len(resistors)):
                digits = [int(digit) for digit in (resistors[i])]
                if len(digits) < 2:
                    digits.append(0)
                count = 0
                value = int(resistors[i])
                if 10 < value < 100:
                    count = 1
                elif value < 10:
                    count = 0
                else:
                    count = len(digits) -2
                colors[i][2] = count
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
                pen.fillcolor('#e1b29b')
                pen.begin_fill()
                pen.fd(100)
                pen.lt(90)
                pen.fd(40)
                pen.lt(90)
                pen.fd(100)
                pen.lt(90)
                pen.fd(40)
                pen.end_fill()
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
                    current_pos = pen.pos()
                pen.penup()
                pen.home()
                pen.goto(-140*len(resistors)/2+i*140,-30)
                pen.write(f'R{i+1}:{resistors[i]}{chr(0x03a9)}', False, 'left',('Arial',14,'bold'))
            pen.penup()
            pen.home()
            pen.goto(-140*(len(resistors)/2) + len(resistors)*140,20)
            pen.pendown()
            pen.bk(40)
            pen.penup()
            pen.goto(-50,-150)
            pen.write(f'Total Resistance is {r_total:,}{chr(0x03a9)}',False,'center',('Arial',18,'bold'))

        case 'parallel':
            r_total = 0
            for r in range(len(resistors)):
                r_total += 1 / int(resistors[r])
            r_total = round(1 / r_total, 2)
            colors: list[list] = [[0 for _ in range(3)] for _ in range(len(resistors))]
            for i in range(len(resistors)):
                digits = [int(digit) for digit in (resistors[i])]
                count = 0
                value = int(resistors[i])
                count = len(digits)-2
                colors[i][2] = count
                colors[i][0] = digits[0]
                colors[i][1] = digits[1]
                pen.penup()
                pen.home()
                pen.goto(-70 * len(resistors) + i * 140, 0)
                pen.pendown()
                pen.rt(90)
                pen.fillcolor('#e1b29b')
                pen.begin_fill()
                pen.fd(100)
                pen.lt(90)
                pen.fd(40)
                pen.lt(90)
                pen.fd(100)
                pen.lt(90)
                pen.fd(40)
                pen.end_fill()
                pen.bk(20)
                pen.rt(90)
                pen.fd(40)
                pen.penup()
                pen.bk(140)
                pen.pendown()
                pen.bk(40)
                pen.penup()
                pen.home()
                pen.goto(-140 * len(resistors) / 2 + i * 140, 0)
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
                pen.goto(-70 * len(resistors) + 20, 40)
                pen.pendown()
                pen.fd(140 * i)
                pen.penup()
                pen.penup()
                pen.home()
                pen.goto(-70 * len(resistors) + 20, -140)
                pen.pendown()
                pen.fd(140 * i)
                pen.penup()
                pen.goto(-150 * (len(resistors) / 2) + i * 140, 150)
                pen.write(f'R{i + 1}:{resistors[i]}{chr(0x03a9)}', False, 'left', ('Arial', 14, 'bold'))
            pen.penup()
            pen.home()
            pen.goto(-50 , -140)
            pen.rt(90)
            pen.pendown()
            pen.fd(20)
            pen.penup()
            pen.fd(30)
            pen.write(f'{chr(0x23da)}', False, 'center', ('Arial', 24, 'normal'))
            pen.penup()
            pen.home()
            pen.goto(-50 , 40)
            pen.lt(90)
            pen.pendown()
            pen.fd(40)
            pen.penup()
            pen.bk(20)
            pen.write(f'{chr(0x2b9d)}', False, 'center', ('Arial', 24, 'normal'))
            pen.penup()
            pen.goto(-50, -220)
            pen.write(f'Resistance Value is {r_total:,}{chr(0x03a9)}', False, 'center', ('Arial', 18, 'bold'))


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


def series_resistors() -> int:
    circuit_type = 'series'
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
    draw_resistors(resistors, circuit_type)
    x = input('Press enter to continue...')
    return resistance


def parallel_resistors() -> float:
    circuit_type = 'parallel'
    for _ in range(20):
        print('')
    print('*' * 40)
    print('*    Calculate Parallel Resistance     *')
    print('*' * 40)
    for _ in range(3):
        print('')
    num_resistors = ''
    while not num_resistors.isnumeric() or int(num_resistors) > 6 or int(num_resistors) < 2:
        num_resistors = input('Please enter the number of resistors in the circuit(2-6): ')
    num_resistors = int(num_resistors)
    resistance = []
    resistors = []
    r_total = 0
    for x in range(num_resistors):
        resistors.append(input(f'Enter the value of resistor R{x+1} in ohms: '))
    for y in range(num_resistors):
        resistance.append(1/float(resistors[y]))
    for z in range(num_resistors):
        r_total += float(resistance[z])
    r_total = 1/r_total
    print(f'The total resistance of this circuit is {round(r_total, 1)} ohms')
    draw_resistors(resistors, circuit_type)
    x = input('Press enter to continue...')
    return r_total


def menu():
    # pen.clear()
    # pen.hideturtle()
    # pen.goto(-50,250)
    # pen.write((40*'*'), False, 'center', ('Arial', 24, 'bold'))
    # pen.goto(-50,200)
    # pen.write('Resistor ID and Utility', False, 'center', ('Arial', 36, 'bold'))
    # pen.goto(-50,150)
    # pen.write((40*'*'), False, 'center', ('Arial', 24, 'bold'))
    # pen.goto(-50,130)
    # pen.write('Please Select an Option Below', False, 'center', ('Arial', 24, 'bold'))
    # pen.goto(-50,100)
    # pen.write((40*'*'), False, 'center', ('Arial', 24, 'bold'))
    # pen.goto(-50,75)
    # pen.write('1: Identify with Color Code', False, 'center', ('Arial', 24, 'bold'))
    # pen.goto(-50,25)
    # pen.write('2: Find Resistance in Series', False, 'center', ('Arial', 24, 'bold'))
    # pen.goto(-50,-25)
    # pen.write('3: Find Resistance in Parallel', False, 'center', ('Arial', 24, 'bold'))
    # pen.goto(-50,-75)
    # pen.write('4: Calculate Current' , False, 'center', ('Arial', 24, 'bold'))
    # pen.goto(-50,-125)
    # pen.write('5: Exit Resistors' , False, 'center', ('Arial', 24, 'bold'))

    print('*',36*' ','*')
    print('*    1) Identify with Color Code       *')
    print('*',36*' ','*')
    print('*    2) Find Resistance in Series      *')
    print('*',36*' ','*')
    print('*    3) Find Resistance in Parallel    *')
    print('*',36*' ','*')
    print('*    4) Calculate Current              *')
    print('*',36*' ','*')
    print('*    5) Exit Resistors                 *')
    print(40*'*')
    option = ''
    while not option.isnumeric() or option not in ['1','2','3','4','5']:
        option = input('Enter Your Choice: ')
    option = int(option)
    match option:
        case 1:
            pen.clear()
            id_resistor()
        case 2:
            pen.clear()
            series_resistors()
            menu()
        case 3:
            pen.clear()
            parallel_resistors()
            menu()
        case 4:
            pen.clear()
            calculate_current()
            menu()
        case 5:
            exit()


def main() -> None:
    menu()
    t.done()


if __name__ == '__main__':
    main()
