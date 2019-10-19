import sys
import getopt
import turtle

def print_help():
      print('HELP - this script draws regulars polygons.')
      print('-h help')
      print('-n <number> -> number of sides, default is 4')
      print('-r <number> -> length of each side, default is 50')
      print('-m <number> -> move center, default is 0')
      print('-t <number> -> turn at start, default is 0')

def draw_figure(length, number, move, turn):
      angle=((int(number)-2)*180)/int(number)
      draw_angle=180-int(angle)
      print(draw_angle)

      x.right(int(turn))
      for i in range(1,int(number)+1):
            x.forward(int(length))
            x.right(int(draw_angle))


def move_start_point(move):
      x.up()
      x.forward(int(move))
      x.down()

try:
    opts, args = getopt.getopt(sys.argv[1:], 't:m:r:n:h', ['turn=','move=', 'length=', 'number', 'help'])
except getopt.GetoptError:
    print_help()
    sys.exit(1)

var_n=4
var_length=50
var_move=0
var_turn=0


x=turtle.Turtle()

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print_help()
        sys.exit(2)

    elif opt in ('-n', '--number'):
        var_n=arg
        
    elif opt in ('-r', '--length'):
        var_length=arg

    elif opt in ('-t', '--turn'):
        var_turn=arg
        
    elif opt in ('-m', '--move'):
        var_move=arg
        
    else:
        
        print_help()
        sys.exit(2)
move_start_point(var_move)
draw_figure(var_length, var_n, var_move, var_turn)
#x.circle(50)

input("Press Enter to continue...")
