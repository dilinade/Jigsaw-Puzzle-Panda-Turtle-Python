
#  FOUR PIECE JIGSAW PUZZLE PANDA

from turtle import *
from math import *

##size_of_pieces = 300 # pixels (excluding any protruding "tabs")
size_of_pieces = 300 # pixels (excluding any protruding "tabs")
half_piece_size = size_of_pieces / 2
max_tab_size = 100 # pixels
box_size = size_of_pieces + (max_tab_size * 2)
half_box_size = box_size / 2
left_border = max_tab_size
gap = max_tab_size
top_bottom_border = max_tab_size
canvas_height = (top_bottom_border + size_of_pieces) * 2
canvas_width = (size_of_pieces * 2 + left_border) * 2
template_centres = [[-(size_of_pieces + half_piece_size), -half_piece_size], # bottom left
                    [-half_piece_size, -half_piece_size], # bottom right
                    [-(size_of_pieces + half_piece_size), half_piece_size], # top left
                    [-half_piece_size, half_piece_size]] # top right
box_centre = [gap + (box_size / 2), 0]




#-----Functions for Drawing the Background---------------------------#

def draw_outline():

    # Determine the position of the box's bottom-left corner
    bottom_left = [box_centre[0] - half_box_size,
                   box_centre[1] - half_box_size]

    # Go to the bottom-left corner and get ready to draw
    penup()
    goto(bottom_left)
    width(5)
    color('black')
    pendown()
    
    # Walk around the box's perimeter
    setheading(0) # point east
    for side in [1, 2, 3, 4]:
        forward(box_size)
        left(90)

    # Reset the pen
    width(1)
    penup()

 

# Draw the individual squares of the jigsaw's template
def draw_template(show_template = False):

    # Only draw if the argument is True
    if show_template:

        # Set up the pen
        width(3)
        color('grey')

        # Draw a box for each centre coordinate
        for centre_x, centre_y in template_centres:
            
            # Determine the position of this square's bottom-left corner
            bottom_left = [centre_x - half_piece_size,
                           centre_y - half_piece_size]

            # Go to the bottom-left corner and get ready to draw
            penup()
            goto(bottom_left)
            pendown()
        
            # Walk around the square's perimeter
            setheading(0) # point east
            for side in [1, 2, 3, 4]:
                forward(size_of_pieces)
                left(90)

        # Reset the pen
        width(1)
        color('black')
        penup()


# As a debugging aid, mark the coordinates of the centres of
# the template squares and the box
def mark_coords(show_coords = False):

    # Only mark the coordinates if the argument is True
    if show_coords:

        # Don't draw lines between the coordinates
        penup()

        # Go to each coordinate, draw a dot and print the coordinate
        color('black')
        for x_coord, y_coord in template_centres + [box_centre]:
            goto(x_coord, y_coord)
            dot(4)
            write(str(x_coord) + ', ' + str(y_coord),
                  font = ('Arial', 12, 'normal'))

    # Reset the pen
    width(1)
    penup()
               

#-----Test data------------------------------------------------------#

# first start developing your "draw_attempt" function.

attempt_00 = []

# Each of the following data sets put just one piece in the box.
# You may find them useful when creating your individual pieces.

attempt_01 = [['Piece A', 'In box']]
attempt_02 = [['Piece B', 'In box']]
attempt_03 = [['Piece C', 'In box']]
attempt_04 = [['Piece D', 'In box']]

# Each of the following data sets put just one piece in a
# location in the template.

attempt_05 = [['Piece A', 'Top left']]
attempt_06 = [['Piece B', 'Bottom right']]
attempt_07 = [['Piece C', 'Top right']]
attempt_08 = [['Piece D', 'Bottom left']]
attempt_09 = [['Piece A', 'Bottom left']]
attempt_10 = [['Piece B', 'Top left']]
attempt_11 = [['Piece C', 'Bottom right']]
attempt_12 = [['Piece D', 'Top right']]

# Each of the following data sets put all four pieces in the
# box, but in different orders.

attempt_13 = [['Piece A', 'In box'], ['Piece B', 'In box'],
              ['Piece C', 'In box'], ['Piece D', 'In box']]
attempt_14 = [['Piece D', 'In box'], ['Piece C', 'In box'],
              ['Piece B', 'In box'], ['Piece A', 'In box']]
attempt_15 = [['Piece C', 'In box'], ['Piece D', 'In box'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]

# Each of the following data sets uses between two and four pieces,
# either in the template or in the box

attempt_16 = [['Piece A', 'Top right'], ['Piece B', 'Bottom left']]
attempt_17 = [['Piece D', 'Bottom right'], ['Piece C', 'In box']]
attempt_18 = [['Piece C', 'Bottom right'], ['Piece A', 'Bottom right']]
attempt_19 = [['Piece B', 'In box'], ['Piece D', 'Top left'],
              ['Piece C', 'In box']]
attempt_20 = [['Piece C', 'Top left'], ['Piece D', 'Top right'],
              ['Piece A', 'Bottom left']]
attempt_21 = [['Piece A', 'In box'], ['Piece D', 'Bottom left'],
              ['Piece C', 'Top right']]
attempt_22 = [['Piece A', 'Bottom left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom right'], ['Piece D', 'In box']]
attempt_23 = [['Piece D', 'Bottom right'], ['Piece C', 'In box'],
              ['Piece B', 'Top right'], ['Piece A', 'Top left']]
attempt_24 = [['Piece C', 'Bottom right'], ['Piece D', 'Top left'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]
attempt_25 = [['Piece D', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece C', 'Bottom right'], ['Piece A', 'Top right']]
attempt_26 = [['Piece C', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece A', 'Bottom right'], ['Piece D', 'Top right']]
attempt_27 = [['Piece C', 'Bottom left'], ['Piece D', 'In box'],
              ['Piece A', 'Top left'], ['Piece B', 'Top right']]

# Each of the following data sets is a complete attempt at solving
# the puzzle using all four pieces (so there are no pieces left in the box)

attempt_28 = [['Piece A', 'Bottom left'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Top right']]
attempt_29 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]
attempt_30 = [['Piece A', 'Bottom left'], ['Piece B', 'Top left'],
              ['Piece C', 'Bottom right'], ['Piece D', 'Top right']]
attempt_31 = [['Piece A', 'Bottom right'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left'], ['Piece D', 'Top left']]
attempt_32 = [['Piece D', 'Top right'], ['Piece A', 'Bottom left'],
              ['Piece B', 'Top left'], ['Piece C', 'Bottom right']]
attempt_33 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]



solution = [['Piece A', 'Top left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left'], ['Piece D', 'Bottom right']] 

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_attempt" function.
#

# Draw the jigsaw pieces as per the provided data set
def draw_attempt(attempt):
  no_of_pieces = len(attempt)
  for pieces in attempt:
    part = pieces[0]
    if(no_of_pieces>0):
      piece_location = pieces[1].replace(" ","_")
      if(part == "Piece A"):
        if(piece_location == "Top_left"):
          partA(-600,0)
        elif(piece_location == "Top_right"):
          partA(-300,0)
        elif(piece_location == "Bottom_left"):
          partA(-600,-300)
        elif(piece_location == "Bottom_right"):
          partA(-300 , -300)
        else:
          partA(250,-150)
      elif(part == "Piece B"):
        if(piece_location == "Top_left"):
          partB(-600,0)
        elif(piece_location == "Top_right"):
          partB(-300,0)
        elif(piece_location == "Bottom_left"):
          partB(-600,-300)
        elif(piece_location == "Bottom_right"):
          partB(-300 , -300)
        else:
          partB(250,-150)
      elif(part == "Piece C"):
        if(piece_location == "Top_left"):
          partC(-600,0)
        elif(piece_location == "Top_right"):
          partC(-300,0)
        elif(piece_location == "Bottom_left"):
          partC(-600,-300)
        elif(piece_location == "Bottom_right"):
          partC(-300 , -300)
        else:
          partC(250,-150)
      elif(part == "Piece D"):
        if(piece_location == "Top_left"):
          partD(-600,0)
        elif(piece_location == "Top_right"):
          partD(-300,0)
        elif(piece_location == "Bottom_left"):
          partD(-600,-300)
        elif(piece_location == "Bottom_right"):
          partD(-300 , -300)
        else:
          partD(250,-150)



    # partB(Top_right[0],Top_right[1])
    # partA(Top_left[0],Top_left[1])
    # partD(Bottom_right[0],Bottom_right[1])
    # partC(Bottom_left[0],Bottom_left[1])
    # partA(In_box[0],In_box[1])
    






#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
# lengths
pieceLength=300
tabLength=40

# outline widths
outlineWidth=4
drawingWidth=2

# headings
east = 0
north = 90
west = 180
south = 270
t = Turtle()
s = Turtle()
writer = Turtle()

t.hideturtle()
s.hideturtle()
writer.hideturtle()
t.speed('fastest')
s.speed('fastest')
writer.speed('fastest')
bgcolor("white")

def negativeTab():
  t.forward(pieceLength/2-tabLength/2)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(pieceLength/2-tabLength/2)

def positiveTab():
  t.forward(pieceLength/2-tabLength/2)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(pieceLength/2-tabLength/2)

def partA(x,y):
  # x and y are the cordinates of the lower left corner
  # begin piece outline
  t.fillcolor("yellow")
  t.begin_fill()
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.width(outlineWidth)
  t.setheading(north)
  t.forward(pieceLength)
  t.right(90)
  t.forward(pieceLength)
  t.right(90)
  positiveTab()
  t.right(90)
  negativeTab()
  t.end_fill()
  # end piece outline

  # neck
  t.penup()
  t.goto(x+pieceLength/2-tabLength,y)
  t.setheading(north)
  t.pendown()
  t.fillcolor("black")
  t.begin_fill()
  t.circle(-pieceLength/2.5,90)
  t.goto(x+pieceLength,y+pieceLength/5)
  t.goto(x+pieceLength,y)
  t.setheading(west)
  t.forward(pieceLength/2-tabLength/2)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.goto(x+pieceLength/2-tabLength,y)
  t.end_fill()

  
  # ear
  t.width(drawingWidth)
  t.fillcolor("black")
  t.begin_fill()
  t.penup()
  t.goto(x+pieceLength-(pieceLength/3),y+pieceLength/2+tabLength/2)
  t.pendown()
  t.setheading(east)
  t.circle(pieceLength/5)
  t.end_fill()
  #inner ear
  t.fillcolor("grey")
  t.begin_fill()
  t.penup()
  t.goto(x+pieceLength-(pieceLength/3),y+pieceLength/2+tabLength)
  t.pendown()
  t.setheading(east)
  t.circle(pieceLength/5-tabLength/2)
  t.end_fill()

  # face
  t.width(drawingWidth)
  t.fillcolor("white")
  t.begin_fill()
  t.penup()
  t.goto(x+pieceLength,y+(pieceLength/5))
  t.pendown()
  t.setheading(west)
  t.circle(-(pieceLength/2.6),180)
  t.right(90)
  t.goto(x+pieceLength,y+pieceLength/2+tabLength/2)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.goto(x+pieceLength,y+(pieceLength/5))
  t.end_fill()

  #eye

  t.penup()
  t.goto(x+pieceLength-(1.3*tabLength),y+205)
  t.pendown()
  t.fillcolor("black")
  t.shape("circle")
  t.shapesize(4,3,3)
  t.settiltangle(-120)
  t.stamp()
  t.resizemode('auto')

  t.penup()
  t.goto(x+(pieceLength-tabLength)+tabLength/6-15,y+190)
  t.pendown()
  
  t.fillcolor("white")
  t.shape("circle")
  t.shapesize(1,1,1)
  t.settiltangle(-120)
  t.stamp()
  t.resizemode('auto')

  s.penup()
  s.goto(x+(pieceLength-tabLength)+tabLength/5-15,y+187)
  s.pendown()
  s.dot(10,"black")
  s.resizemode('auto')

  s.penup()
  s.goto(x+(pieceLength-tabLength)+tabLength/5-15,y+187)
  s.pendown()
  s.dot(3,"white")

 

  # nose
  t.penup()
  t.goto(x+pieceLength+tabLength/5,y+pieceLength/2)
  t.pendown()
  t.fillcolor("black")
  t.shape("circle")
  t.shapesize(3,1.75,2)
  t.settiltangle(180)
  t.stamp()
  t.resizemode('auto')

  # mouth
  t.penup()
  t.goto(x+pieceLength,y+pieceLength/2-tabLength*1.4)
  t.setheading(west)
  t.pendown()
  t.circle(-tabLength,45)

  #nose dots
  s.penup()
  s.goto(x+pieceLength-tabLength/5,y+pieceLength/2+tabLength/8)
  s.pendown()
  s.dot(10,"white")

  s.penup()
  s.goto(x+pieceLength+tabLength/8,y+pieceLength/2+tabLength/5)
  s.pendown()
  s.dot(7,"white")

  # bamboo  
  t.penup()
  t.fillcolor("DarkGreen")
  t.goto(x+pieceLength/2-tabLength,y)
  t.begin_fill()
  t.pendown()
  t.setheading(north)
  t.left(45)
  t.forward(120)
  t.right(90)
  t.forward(tabLength/2)
  t.right(90)
  t.forward(125)
  t.goto(x+pieceLength/2-tabLength/2,y)
  t.goto(x+pieceLength/2-tabLength,y)
  t.end_fill()
  #
  t.penup()
  t.goto(x+pieceLength/2-tabLength,y)
  t.setx(t.xcor()-40)
  t.sety(t.ycor()+40)
  t.pendown()
  t.setheading(north)
  t.right(45)
  t.forward(tabLength/2)
  

  

def partB(x,y):
  # x and y are the cordinates of the lower left corner

  # begin piece outline
  t.penup()
  t.fillcolor("yellow")
  t.begin_fill()
  t.goto(x,y)
  t.width(outlineWidth)
  t.setheading(north)
  t.pendown()
  negativeTab()
  t.right(90)
  t.forward(pieceLength)
  t.right(90)
  t.forward(pieceLength)
  t.right(90)
  negativeTab()
  t.end_fill()
  # end piece outline

  # neck
  t.penup()
  t.goto(x+300-(pieceLength/2-tabLength),y)
  t.setheading(south)
  t.pendown()
  t.fillcolor("black")
  t.begin_fill()
  t.circle(-pieceLength/2.5,-90)
  t.goto(x,y+pieceLength/5)
  t.goto(x,y)
  t.setheading(east)
  t.forward(pieceLength/2-tabLength/2)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.goto(x+300-(pieceLength/2-tabLength),y)
  t.end_fill()

  # ear
  t.width(drawingWidth)
  t.fillcolor("black")
  t.begin_fill()
  t.penup()
  t.goto(x+pieceLength/3,y+pieceLength/2+tabLength/2)
  t.pendown()
  t.setheading(east)
  t.circle(pieceLength/5)
  t.end_fill()
  # inner ear
  t.fillcolor("grey")
  t.begin_fill()
  t.penup()
  t.goto(x+pieceLength/3,y+pieceLength/2+tabLength)
    # t.goto(x+pieceLength-(pieceLength/3),y+pieceLength/2+tabLength)
  t.pendown()
  t.setheading(east)
  t.circle(pieceLength/5-tabLength/2)
  t.end_fill()

  # face
  t.width(drawingWidth)
  t.fillcolor("white")
  t.penup()
  t.goto(x,y+(pieceLength/5))
  t.pendown()
  t.setheading(east)
  t.begin_fill()
  t.circle((pieceLength/2.6),180)
  t.left(90)
  t.goto(x,y+pieceLength/2+tabLength/2)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.goto(x,y+(pieceLength/5))
  t.end_fill()

  #eye

  t.penup()
  t.goto(x+tabLength*1.3,y+205)
  t.pendown()
  t.fillcolor("black")
  t.shape("circle")
  t.shapesize(4,3,3)
  t.settiltangle(120)
  t.stamp()
  t.resizemode('auto')

  t.penup()
  t.goto(x+300-(pieceLength-tabLength+tabLength/6)+15,y+190)
  t.pendown()
  t.fillcolor("white")
  t.shape("circle")
  t.shapesize(1,1,1)
  t.settiltangle(120)
  t.stamp()
  t.resizemode('auto')

  s.penup()
  s.goto(x+300-(pieceLength-tabLength+tabLength/5)+15,y+187)
  s.pendown()
  s.dot(10,"black")
  s.resizemode('auto')

  s.penup()
  s.goto(x+300-(pieceLength-tabLength+tabLength/5)+15,y+187)
  s.pendown()
  s.dot(3,"white")

  # mouth
  t.penup()
  t.goto(x+tabLength/3,y+pieceLength/2-19)
  t.pendown()
  t.circle(-tabLength*4,12)

  t.penup()
  t.goto(x,y+pieceLength/2-tabLength*1.4)
  t.setheading(east)
  t.pendown()
  t.circle(tabLength,45)

def partC(x,y):
  # x and y are the cordinates of the lower left corner

  # begin piece outline
  t.penup()
  t.fillcolor("yellow")
  t.begin_fill()
  t.goto(x,y)
  t.pendown()
  t.width(outlineWidth)
  t.setheading(north)
  t.forward(pieceLength)
  t.right(90)
  positiveTab()
  t.right(90)
  negativeTab()
  t.right(90)
  t.forward(pieceLength)
  t.end_fill()
  # end piece outline

  # neck
  t.penup()
  t.goto(x+pieceLength/2-tabLength,y+pieceLength)
  t.setheading(south)
  t.pendown()
  t.fillcolor("black")
  t.begin_fill()
  t.circle(pieceLength/2.5,60)
  t.goto(x+pieceLength,y+pieceLength)
  t.setheading(west)
  t.forward(pieceLength/2-tabLength/2)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.goto(x+pieceLength/2-tabLength,y+pieceLength)
  t.end_fill()

  # torso
  t.penup()
  t.goto(x+pieceLength,y+pieceLength/5)
  t.setheading(west)
  t.fillcolor("black")
  t.begin_fill()
  t.pendown()
  t.width(drawingWidth)
  t.circle(-pieceLength/2,128) # MAGIC NUMBER
  t.goto(x+pieceLength,y+pieceLength)
  t.setheading(south)
  t.forward(pieceLength/2-tabLength/2)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.goto(x+pieceLength,y+pieceLength/5)
  t.end_fill()

  t.penup()
  t.goto(x+pieceLength,y+pieceLength/4.2)
  t.setheading(west)
  t.fillcolor("white")
  t.begin_fill()
  t.pendown()
  t.width(drawingWidth)
  t.circle(-pieceLength/2.70,180)
  t.goto(x+pieceLength,y+pieceLength)
  t.setheading(south)
  t.forward(pieceLength/2-tabLength/2)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.goto(x+pieceLength,y+pieceLength/5)
  t.end_fill()

  # bamboo
  head = t.heading()
  t.penup()
  t.goto(x+pieceLength/2-tabLength,y+pieceLength)
  t.fillcolor("DarkGreen")
  t.begin_fill()
  t.pendown()
  t.setheading(south)
  t.left(45)
  t.forward(190)
  t.left(90); pos=t.position()
  t.forward(tabLength/2)
  t.left(90)
  t.forward(180)
  t.end_fill()
  #
  t.penup()
  t.goto(pos)
  t.setx(t.xcor()-20)
  t.sety(t.ycor()+20)
  t.pendown()
  t.setheading(north)
  t.right(45)
  t.forward(tabLength/2)
  t.setheading(head)
  

  #torso1
  t.penup()
  t.goto(x+180,y+110)
  t.pendown()
  t.fillcolor("black")
  t.shape("circle")
  t.shapesize(9,7,2)
  t.settiltangle(-45)
  t.stamp()
  t.resizemode('auto')

  t.penup()
  t.goto(x+180,y+95)
  t.pendown()
  t.fillcolor("grey")
  t.shape("circle")
  t.shapesize(7,5,2)
  t.stamp()
  t.resizemode('auto')

  t.penup()
  t.goto(x+200,y+70)
  t.pendown()
  t.fillcolor("pink")
  t.shape("circle")
  t.shapesize(3,2,2)
  t.settiltangle(45)
  t.stamp()
  t.resizemode('auto')

  t.penup()
  t.goto(x+145,y+130)
  t.pendown()
  t.stamp()
  
  t.penup()
  t.goto(x+175,y+130)
  t.pendown()
  t.stamp()

  t.penup()
  t.goto(x+142,y+100)
  t.pendown()
  t.stamp()

  #hand

  t.penup()
  t.goto(x+130,y+240)
  t.pendown()
  t.fillcolor("black")
  t.begin_fill()
  t.circle(1.25*tabLength)
  t.end_fill()

  #white dots

  s.penup()
  s.goto(x+210,y+255)
  s.pendown()
  s.dot(10,"white")

  s.penup()
  s.goto(x+205,y+235)
  s.pendown()
  s.dot(10,"white")

  s.penup()
  s.goto(x+200,y+215)
  s.pendown()
  s.dot(10,"white")







def partD(x,y):
  # x and y are the cordinates of the lower left corner

  # begin piece outline
  
  t.penup()
  t.fillcolor("yellow")
  t.begin_fill()
  t.goto(x,y)
  t.pendown()
  t.width(outlineWidth)
  t.setheading(north)
  positiveTab()
  t.right(90)
  positiveTab()
  t.right(90)
  t.forward(pieceLength)
  t.right(90)
  t.forward(pieceLength)
  t.end_fill()
  # end piece outline

  # neck
  t.penup()
  t.goto(x+300-(pieceLength/2-tabLength),y+pieceLength)
  t.setheading(south)
  t.pendown()
  t.fillcolor("black")
  t.begin_fill()
  t.circle(-pieceLength/2.5,60)
  t.goto(x,y+pieceLength)
  t.setheading(east)
  t.forward(pieceLength/2-tabLength/2)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(tabLength)
  t.right(90)
  t.forward(tabLength)
  t.goto(x+300-(pieceLength/2-tabLength),y+pieceLength)
  t.end_fill()


  # torso
  t.penup()
  t.goto(x,y+pieceLength/5)
  t.setheading(east)
  t.fillcolor("black")
  t.begin_fill()
  t.pendown()
  t.width(drawingWidth)
  t.circle(pieceLength/2,128) # MAGIC NUMBER
  t.goto(x,y+pieceLength)
  t.setheading(south)
  t.forward(pieceLength/2-tabLength/2)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.goto(x,y+pieceLength/5)
  t.end_fill()

  t.penup()
  t.goto(x,y+pieceLength/4.2)
  t.setheading(east)
  t.fillcolor("white")
  t.begin_fill()
  t.pendown()
  t.width(drawingWidth)
  t.circle(pieceLength/2.70,180)
  t.goto(x,y+pieceLength)
  t.setheading(south)
  t.forward(pieceLength/2-tabLength/2)
  t.right(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.left(90)
  t.forward(tabLength)
  t.right(90)
  t.goto(x,y+pieceLength/5)
  t.end_fill()

  #torso middle
  t.penup()
  t.goto(x+120,y+110)
  t.pendown()
  t.fillcolor("black")
  t.shape("circle")
  t.shapesize(9,7,2)
  t.settiltangle(-135)
  t.stamp()
  t.resizemode('auto')

  t.penup()
  t.goto(x+120,y+95)
  t.pendown()
  t.fillcolor("grey")
  t.shape("circle")
  t.shapesize(7,5,2)
  t.stamp()
  t.resizemode('auto')

  t.penup()
  t.goto(x+100,y+70)
  t.pendown()
  t.fillcolor("pink")
  t.shape("circle")
  t.shapesize(3,2,2)
  t.settiltangle(135)
  t.stamp()
  t.resizemode('auto')

  t.penup()
  t.goto(x+155,y+130)
  t.pendown()
  t.stamp()
  
  t.penup()
  t.goto(x+125,y+130)
  t.pendown()
  t.stamp()

  t.penup()
  t.goto(x+158,y+100)
  t.pendown()
  t.stamp()

  #hand 

  t.penup()
  t.goto(x+70,y+240)
  t.pendown()
  t.fillcolor("black")
  t.begin_fill()
  t.circle(1.25*tabLength)  
  t.end_fill()

  #white dots

  s.penup()
  s.goto(x+90,y+255)
  s.pendown()
  s.dot(10,"white")

  s.penup()
  s.goto(x+95,y+235)
  s.pendown()
  s.dot(10,"white")

  s.penup()
  s.goto(x+100,y+215)
  s.pendown()
  s.dot(10,"white")





# Set up the drawing canvas
setup(canvas_width, canvas_height)

bgcolor('light grey')


title('Four Piece Jigsaw Puzzle - Panda')


speed('fastest')


tracer(True)

# Draw the box that holds unused jigsaw puzzle pieces
draw_outline()


draw_template(True)

# Mark the centres of the places where jigsaw puzzle pieces must
# be drawn
# ***** If you don't want to display the coordinates change the
# ***** argument below to False
mark_coords(True)


writer.penup()
writer.goto(350,300)
writer.pendown()
writer.pencolor("red")

#Use this for testing
# for i in range(34):
#   writer.write("Drawing Attempt  " + str(i),font=("Arial",18,"normal"))
#   draw_attempt(globals()["attempt_%02d"%(i)])
#   t.clear()
#   s.clear()
#   writer.clear()
writer.write("Drawing Solution ",font=("Arial",18,"normal"))
draw_attempt(solution)


# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#

