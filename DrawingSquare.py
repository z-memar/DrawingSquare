
class Square():
    """Represents a square
    """

    def __init__(self, size, hChar, vChar, cornerChar):
        ''' Initializes a square
        Pass in the size, the character to used for the horizontal edge, vertical edge, and corners.
        '''
        self.size = size
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar
#Get has return but the set will set the new value to the attribuite.
    def GetSize(self):
        ''' Returns the size of an edge of the Square '''
        return self.size

    def SetSize(self,size):
        ''' Returns the size of an edge of the Square '''
        self.size = size

    def SetHorizontalChar(self, y):
        ''' Set a new horizontal character '''
        self.hchar = y
        
    def SetVerticalChar(self, x):
        ''' Set a new vertical character '''
        self.vChar = x

    def SetCornerChar(self, c):
        ''' Set a new corner character '''
        self.cornerChar = c


    def GetArea(self, size):
        area = (self.size)*(self.size)
        return area


    def Show(self):
        for row in range(0, self.size):
            if row == 0 or row == self.size - 1:
                print(self.cornerChar, (self.vChar) * ((self.size) -2), self.cornerChar)
            else:
                print(self.hChar, (' ') * ((self.size) -2), self.hChar)
                

# Test code
# Create a square of size 5
print("oSquare1")
oSquare1 = Square(5, '-', '|', '*')  # pass in size, horizonal, vertical, and edge characters
oSquare1.Show()

#print('Size is:', oSquare1.GetSize(), " area is:", oSquare1.GetArea(size))

# Create another square of size 10
print("oSquare2")
oSquare2 = Square(10, 'O', '|', '*')
oSquare2.Show()
#print('Size is:', oSquare2.GetSize(), " area is:", oSquare2.GetArea(size))

# Tell the first square to modify its data

oSquare1.SetSize(7)
oSquare1.SetHorizontalChar('^')

oSquare1.SetVerticalChar('?')
oSquare1.SetCornerChar('$')
oSquare1.Show()
print('Size is:', oSquare1.GetSize(), " area is:", oSquare1.GetArea(oSquare1.GetSize()))
print()

# Add code here to ask the user questions, and create and show a new Square based on the answers
while True:
   
    size = input("Please input the size of your square or type Quit to break the program")
    if size == 'Quit':
        print("bye")
        break
    size = int(size)    
    hCar = input("Please input the shape for your square's horizantal?")
    vCar = input("Please input the shape of your square's vertical?")
    cornerCar = input("Please input the shape of your square's corner?")
    oSquare3 = Square (size, hCar, vCar, cornerCar)
    oSquare3.Show()


