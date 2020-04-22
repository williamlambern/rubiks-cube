from tkinter import Tk, Canvas, Frame, Entry, Button, BOTH
from cube import *
import random

class Window:

    def __init__(self,master):
        #GUI INIT
        self.master = master
        self.master.geometry("400x450")
        self.canvas = Canvas(self.master)
        
        self.e1 = Entry(self.canvas)
        self.canvas.create_window(100,20,window=self.e1)

        self.button = Button(self.master, text = "Move", command = lambda : self.prepare_execute_moves())
        button_window = self.canvas.create_window(235, 20,window=self.button)

        self.scrambleit = Button(self.master, text = "Scramble", command = lambda : self.scramble())
        solveit_window = self.canvas.create_window(293, 20,window=self.scrambleit)
          
        #CUBE INIT
        self.cube = Cube()

        self.drawCube()

    def drawCube(self):
        colours = {'w': 'white', 'y' : 'yellow', 'r' : 'red', 'o' : 'orange', 'b' : 'blue', 'g' : 'green'}
        self.master.title("Rubik's Cube by William Lambern")
        canvas = self.canvas
        canvas.delete('polygon')
        c = self.cube
        colours[c.sorted['-1-11'].colour[2]]
        #right side
        x = 200
        y = 400
        canvas.create_polygon(x,y,x+50,y-25,x+50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-1-11'].colour[2]])
        x = 250
        y = 375
        canvas.create_polygon(x,y,x+50,y-25,x+50,y-75,x,y-50,outline="black", fill=colours[c.sorted['0-11'].colour[2]])
        x = 300
        y = 350
        canvas.create_polygon(x,y,x+50,y-25,x+50,y-75,x,y-50,outline="black", fill=colours[c.sorted['1-11'].colour[2]])
        
        x = 200
        y = 350
        canvas.create_polygon(x,y,x+50,y-25,x+50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-101'].colour[2]])
        x = 250
        y = 325
        canvas.create_polygon(x,y,x+50,y-25,x+50,y-75,x,y-50,outline="black", fill=colours[c.sorted['001'].colour[2]])
        x = 300
        y = 300
        canvas.create_polygon(x,y,x+50,y-25,x+50,y-75,x,y-50,outline="black", fill=colours[c.sorted['101'].colour[2]])

        x = 200
        y = 300
        canvas.create_polygon(x,y,x+50,y-25,x+50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-111'].colour[2]])
        x = 250
        y = 275
        canvas.create_polygon(x,y,x+50,y-25,x+50,y-75,x,y-50,outline="black", fill=colours[c.sorted['011'].colour[2]])
        x = 300
        y = 250
        canvas.create_polygon(x,y,x+50,y-25,x+50,y-75,x,y-50,outline="black", fill=colours[c.sorted['111'].colour[2]])

        #left side
        x = 200
        y = 400
        canvas.create_polygon(x,y,x-50,y-25,x-50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-1-11'].colour[0]])
        x = 150
        y = 375
        canvas.create_polygon(x,y,x-50,y-25,x-50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-1-10'].colour[0]])
        x = 100
        y = 350
        canvas.create_polygon(x,y,x-50,y-25,x-50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-1-1-1'].colour[0]])
        
        x = 200
        y = 350
        canvas.create_polygon(x,y,x-50,y-25,x-50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-101'].colour[0]])
        x = 150
        y = 325
        canvas.create_polygon(x,y,x-50,y-25,x-50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-100'].colour[0]])
        x = 100
        y = 300
        canvas.create_polygon(x,y,x-50,y-25,x-50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-10-1'].colour[0]])
        
        x = 200
        y = 300
        canvas.create_polygon(x,y,x-50,y-25,x-50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-111'].colour[0]])
        x = 150
        y = 275
        canvas.create_polygon(x,y,x-50,y-25,x-50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-110'].colour[0]])
        x = 100
        y = 250
        canvas.create_polygon(x,y,x-50,y-25,x-50,y-75,x,y-50,outline="black", fill=colours[c.sorted['-11-1'].colour[0]])

        #top side
        x = 200
        y = 250
        canvas.create_polygon(x,y,x-50,y-25,x,y-50,x+50,y-25,outline="black", fill=colours[c.sorted['-111'].colour[1]])
        x = 250
        y = 225
        canvas.create_polygon(x,y,x-50,y-25,x,y-50,x+50,y-25,outline="black", fill=colours[c.sorted['011'].colour[1]])
        x = 300
        y = 200
        canvas.create_polygon(x,y,x-50,y-25,x,y-50,x+50,y-25,outline="black", fill=colours[c.sorted['111'].colour[1]])

        x = 150
        y = 225
        canvas.create_polygon(x,y,x-50,y-25,x,y-50,x+50,y-25,outline="black", fill=colours[c.sorted['-110'].colour[1]])
        x = 200
        y = 200
        canvas.create_polygon(x,y,x-50,y-25,x,y-50,x+50,y-25,outline="black", fill=colours[c.sorted['010'].colour[1]])
        x = 250
        y = 175
        canvas.create_polygon(x,y,x-50,y-25,x,y-50,x+50,y-25,outline="black", fill=colours[c.sorted['110'].colour[1]])

        x = 100
        y = 200
        canvas.create_polygon(x,y,x-50,y-25,x,y-50,x+50,y-25,outline="black", fill=colours[c.sorted['-11-1'].colour[1]])
        x = 150
        y = 175
        canvas.create_polygon(x,y,x-50,y-25,x,y-50,x+50,y-25,outline="black", fill=colours[c.sorted['01-1'].colour[1]])
        x = 200
        y = 150
        canvas.create_polygon(x,y,x-50,y-25,x,y-50,x+50,y-25,outline="black", fill=colours[c.sorted['11-1'].colour[1]])
        
        
        canvas.pack(fill=BOTH, expand=1)

    def prepare_execute_moves(self):
        
        self.moves = self.e1.get().split(' ')
        self.execute_moves(self.moves)

    def execute_moves(self, moves):
        if len(moves) > 0:
            self.cube.rotate(moves[0])
            self.drawCube()
            self.moves.pop(0)
            self.master.after(250, lambda : self.execute_moves(self.moves))

    def scramble(self): #function here as we wan't to render after every move
        options = ['f', 'r' , 'u' , 'l' , 'd' , 'b', "f'", "r'", "u'", "l'", "d'", "b'"]
        moves = []
        for i in range(5):
            moves.append(random.choice(options))
        self.moves = moves
        self.execute_moves(moves)
