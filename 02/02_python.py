import sys
import getopt
import turtle

def print_help():
      print('HELP - this script draws regulars polygons.')
      print('-h help')
      print('-n <number> -> number of sides, default is 4')
      print('-r <number> -> length of each side, default is 50')
      print('-m <number> -> move center, default is 0')

def draw_figure(length, number, move):
      angle=((int(number)-2)*180)/int(number)
      draw_angle=180-int(angle)
      print(draw_angle)
      x=turtle.Turtle()
      for i in range(1,int(number)+1):
            x.forward(int(length))
            x.right(int(draw_angle))
      input("Press Enter to continue...")

try:
    opts, args = getopt.getopt(sys.argv[1:], 'm:r:n:h', ['move=', 'length=', 'number', 'help'])
except getopt.GetoptError:
    print_help()
    sys.exit(1)

var_n=4
var_length=50
var_move=0

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print_help()
        sys.exit(2)

    elif opt in ('-n', '--number'):
        var_n=arg
        
    elif opt in ('-r', '--length'):
        var_length=arg
        
    elif opt in ('-m', '--move'):
        print('p')
        
    else:
        
        print_help()
        sys.exit(2)

draw_figure(var_length, var_n, var_move)
