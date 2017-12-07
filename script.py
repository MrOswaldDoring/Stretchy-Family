

#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9451269
#    Student name: Oswald Doring
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  MY STRETCHY FAMILY
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_portrait".
#  You are required to complete this function so that when the
#  program is run it produces a portrait of a stick figure family in
#  the style of the car window stickers that have become popular in
#  recent years, using data stored in a list to determine the
#  locations and heights of the figures.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  only your final solution, whether or not you complete both
#  parts.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for drawing the background.  You should not change any
# of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to import any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

window_height = 550 # pixels
window_width = 900 # pixels
grass_height = 200 # pixels
grass_offset = -100 # pixels
location_width = 150 # pixels
num_locations = 5

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background and the locations where the individuals in the
# portrait are required to stand.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up.
#


# Draw the grass as a big green rectangle
def draw_grass():
    
    penup()
    goto(-window_width / 2, grass_offset) # start at the bottom-left
    setheading(90) # face north
    fillcolor('pale green')
    begin_fill()
    forward(grass_height)
    right(90) # face east
    forward(window_width)
    right(90) # face south
    forward(grass_height)
    right(90) # face west
    forward(window_width)
    end_fill()


# Draw the locations where the individuals must stand
def draw_locations(locations_on = True):

    # Only draw the locations if the argument is True
    if locations_on:

        # Define a small gap at each end of each location
        gap_size = 5 # pixels
        location_width_less_gaps = location_width - (gap_size * 2) # pixels

        # Start at the far left, facing east
        penup()
        goto(-num_locations * location_width / 2, 0)
        setheading(0) 
  
        # Draw each location as a thick line with a gap at each end
        color('dark khaki')
        for location in range(num_locations):
            penup()
            forward(gap_size)
            pendown()
            width(5) # draw a thick line
            forward(location_width_less_gaps)
            width(1)
            penup()
            forward(gap_size)


# Draw the numeric labels on the locations
def draw_labels(labels_on = True):

    # Only draw the labels if the argument is True
    if labels_on:
    
        font_size = 16 # size of characters for the labels

        # Start in the middle of the left-hand location, facing east
        penup()
        goto(-((num_locations - 1) * location_width) / 2,
             -font_size * 2)
        setheading(0) 

        # Walk to the right, print the labels as we go
        color('dark khaki')
        for label in range(num_locations):
            write(label, font = ('Arial', font_size, 'bold'))
            forward(location_width)


# As a debugging aid, mark certain absolute coordinates on the canvas
def mark_coords(marks_on = True):

    # Only mark the coordinates if the argument is True
    if marks_on:

        # Mark the "home" coordinate
        home()
        width(1)
        color('black')
        dot(3)
        write('0, 0', font = ('Arial', 10, 'normal'))

        # Mark the centre point of each individual's location
        max_x = (num_locations - 1) * location_width / 2
        penup()
        for x_coord in range(-max_x, max_x + location_width, location_width):
            for y_coord in [0, 400]:
                goto(x_coord, y_coord)
                dot(3)
                write(str(x_coord) + ', ' + str(y_coord),
                      font = ('Arial', 10, 'normal'))
                
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the positions for
# the people in the portrait:
#
# 1. The name of the individual, from 'Person A' to 'Person D' or 'Pet'
# 2. The place where that person/pet must stand, from location 0 to 4
# 3. How much to stretch the person/pet vertically, from 0.5 to 1.5
#    times their normal height
# 4. A mystery value, either '*' or '-', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily include all people and sometimes
# they require the same person to be drawn more than once.  You
# can assume, however, that they never put more than one person in
# the same location.
#
# You may add additional data sets but you may not change any of the
# given data sets below.
#

# The following data set doesn't require drawing any people at
# all.  You may find it useful as a dummy argument when you
# first start developing your "draw_portrait" function.

portrait_00 = []

# The following data sets each draw just one of the individuals
# at their default height.

portrait_01 = [['Person A', 2, 1.0, '-']]

portrait_02 = [['Person B', 3, 1.0, '-']]

portrait_03 = [['Person C', 1, 1.0, '-']]

portrait_04 = [['Person D', 0, 1.0, '-']]

portrait_05 = [['Pet', 4, 1.0, '-']]

# The following data sets each draw just one of the individuals
# but multiple times and at different sizes.

portrait_06 = [['Person A', 3, 1.0, '-'],
               ['Person A', 1, 0.75, '-'],
               ['Person A', 2, 0.5, '-'],
               ['Person A', 4, 1.4, '-']]

portrait_07 = [['Person B', 0, 0.5, '-'],
               ['Person B', 2, 1.0, '-'],
               ['Person B', 3, 1.5, '-']]

portrait_08 = [['Person C', 0, 0.5, '-'],
               ['Person C', 1, 0.75, '-'],
               ['Person C', 2, 1.0, '-'],
               ['Person C', 3, 1.25, '-'],
               ['Person C', 4, 1.5, '-']]

portrait_09 = [['Person D', 3, 1.25, '-'],
               ['Person D', 1, 0.8, '-'],
               ['Person D', 0, 1.0, '-']]

portrait_10 = [['Pet', 1, 1.3, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Pet', 3, 0.7, '-']]

# The following data sets each draw a family portrait with all
# individuals at their default sizes.  These data sets create
# "natural" looking portraits.  Notably, the first two both
# show the full family.

portrait_11 = [['Person A', 0, 1.0, '-'],
               ['Person B', 1, 1.0, '-'],
               ['Person C', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Pet', 4, 1.0, '-']]

portrait_12 = [['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*'],
               ['Person C', 1, 1.0, '-'],
               ['Person D', 4, 1.0, '-'],
               ['Pet', 0, 1.0, '-']]

portrait_13 = [['Person B', 1, 1.0, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Person C', 3, 1.0, '*']]

portrait_14 = [['Person C', 0, 1.0, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Person B', 4, 1.0, '-']]

portrait_15 = [['Person D', 4, 1.0, '*'],
               ['Person A', 3, 1.0, '-'],
               ['Person B', 2, 1.0, '-']]

portrait_16 = [['Person D', 1, 1.0, '-'],
               ['Person C', 0, 1.0, '-'],
               ['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*']]

# The following data sets draw all five individuals at their
# minimum and maximum heights.

portrait_17 = [['Person A', 0, 0.5, '-'],
               ['Person B', 1, 0.5, '-'],
               ['Person C', 2, 0.5, '*'],
               ['Person D', 3, 0.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_18 = [['Person A', 4, 1.5, '-'],
               ['Person B', 3, 1.5, '*'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 1, 1.5, '-'],
               ['Pet', 0, 1.5, '-']]

# The following data sets each draw a family portrait with
# various individuals at varying sizes.

portrait_19 = [['Person A', 0, 0.5, '*'],
               ['Person B', 1, 0.8, '-'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_20 = [['Person B', 1, 0.8, '*'],
               ['Pet', 2, 1.4, '-'],
               ['Person C', 3, 0.7, '-']]

portrait_21 = [['Person C', 0, 1.5, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '*'],
               ['Person B', 4, 1.5, '-']]

portrait_22 = [['Person D', 4, 1.2, '-'],
               ['Person A', 3, 1.0, '*'],
               ['Person B', 2, 0.8, '-']]

portrait_23 = [['Person D', 1, 1.1, '-'],
               ['Person C', 2, 0.9, '-'],
               ['Person A', 0, 1.1, '*'],
               ['Person B', 3, 0.9, '-']]

# ***** If you want to create your own data sets you can add them here
# ***** (but your code must still work with all the data sets above plus
# ***** any other data sets in this style).

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_portrait" function.
#


def fish(pos, stretch):
    color('gold')
    goto( -300.0 + pos * 150, 15.0 * stretch )
    begin_fill()
    goto( -300.0 + pos * 150, 0.0 * stretch )
    goto( -293.0 + pos * 150, 10.0 * stretch )
    goto( -289.0 + pos * 150, 14.0 * stretch )
    goto( -284.0 + pos * 150, 19.0 * stretch )
    goto( -276.0 + pos * 150, 18.0 * stretch )
    goto( -272.0 + pos * 150, 14.0 * stretch )
    goto( -268.0 + pos * 150, 8.0 * stretch )
    goto( -269.0 + pos * 150, 3.0 * stretch )
    goto( -278.0 + pos * 150, 0.0 * stretch )
    goto( -290.0 + pos * 150, 2.0 * stretch )
    goto( -293.0 + pos * 150, 7.0 * stretch )
    goto( -300.0 + pos * 150, 15.0 * stretch )
    end_fill()

    goto( -274.0 + pos * 150, 11.0 * stretch )
    color('red')
    dot(3)

    goto( -286.0 + pos * 150, 4.0 * stretch )
    begin_fill()
    goto( -286.0 + pos * 150, 11.0 * stretch )
    goto( -280.0 + pos * 150, 9.0 * stretch )
    goto( -285.0 + pos * 150, 5.0 * stretch )
    end_fill()

    
def joe(pos, stretch):

    color('dark blue')
    goto( -298 + pos * 150, 1.0 )
    pd()
    goto( -300.0 + pos * 150, 16.0 * stretch )
    goto( -312.0 + pos * 150, 0.0 * stretch )
    goto( -300.0 + pos * 150, 14.0 * stretch )
    goto( -301.0 + pos * 150, 31.0 * stretch )
    goto( -288.0 + pos * 150, 32.0 * stretch )
    goto( -311.0 + pos * 150, 31.0 * stretch )
    goto( -300.0 + pos * 150, 31.0 * stretch )
    goto( -300.0 + pos * 150, 42.0 * stretch )
    goto( -289.0 + pos * 150, 47.0 * stretch )
    goto( -289.0 + pos * 150, 59.0 * stretch )
    goto( -301.0 + pos * 150, 68.0 * stretch )
    goto( -312.0 + pos * 150, 57.0 * stretch )
    goto( -309.0 + pos * 150, 44.0 * stretch )
    goto( -301.0 + pos * 150, 42.0 * stretch )
    pu()

def jerome(pos, stretch):

    goto( -302.0 + pos * 150, 114.0 * stretch)#body shape
    color('brown')
    begin_fill()
    goto( -277.0 + pos * 150 , 10.0 * stretch)
    goto( -241.0 + pos * 150, 11.0 * stretch)
    goto( -247.0 + pos * 150, 23.0 * stretch)
    goto( -262.0 + pos * 150, 29.0 * stretch)
    goto( -273.0 + pos * 150, 24.0 * stretch)
    goto( -291.0 + pos * 150, 113.0 * stretch)
    goto( -282.0 + pos * 150, 121.0 * stretch)
    goto( -283.0 + pos * 150, 131.0 * stretch)
    goto( -263.0 + pos * 150, 169.0 * stretch)
    goto( -263.0 + pos * 150, 180.0 * stretch)
    goto( -284.0 + pos * 150, 254.0 * stretch)
    goto( -298.0 + pos * 150, 260.0 * stretch)
    goto( -297.0 + pos * 150, 270.0 * stretch)
    goto( -276.0 + pos * 150, 276.0 * stretch)
    goto( -261.0 + pos * 150, 296.0 * stretch)
    goto( -255.0 + pos * 150, 323.0 * stretch)
    goto( -276.0 + pos * 150, 354.0 * stretch)
    goto( -309.0 + pos * 150, 362.0 * stretch)
    goto( -342.0 + pos * 150, 341.0 * stretch)
    goto( -346.0 + pos * 150, 297.0 * stretch)
    goto( -329.0 + pos * 150, 279.0 * stretch)
    goto( -304.0 + pos * 150, 268.0 * stretch)
    goto( -306.0 + pos * 150, 262.0 * stretch)
    goto( -320.0 + pos * 150, 253.0 * stretch)
    goto( -342.0 + pos * 150, 180.0 * stretch)
    goto( -322.0 + pos * 150, 130.0 * stretch)
    goto( -320.0 + pos * 150, 120.0 * stretch)
    goto( -311.0 + pos * 150, 110.0 * stretch)
    goto( -319.0 + pos * 150, 23.0 * stretch)
    goto( -335.0 + pos * 150, 28.0 * stretch)
    goto( -350.0 + pos * 150, 9.0 * stretch)
    goto( -313.0 + pos * 150, 13.0 * stretch)
    goto( -306.0 + pos * 150, 79.0 * stretch)
    goto( -302.0 + pos * 150, 113.0 * stretch)
    end_fill()

    goto( -319.0 + pos * 150, 228.0 * stretch)#arm cutouts
    color('white')
    begin_fill()
    goto( -311.0 + pos * 150, 135.0 * stretch)
    goto( -316.0 + pos * 150, 134.0 * stretch)
    goto( -334.0 + pos * 150, 173.0 * stretch)
    goto( -319.0 + pos * 150, 228.0 * stretch)
    end_fill()
    goto( -285.0 + pos * 150, 228.0 * stretch)
    begin_fill()
    goto( -293.0 + pos * 150, 134.0 * stretch)
    goto( -288.0 + pos * 150, 136.0 * stretch)
    goto( -271.0 + pos * 150, 174.0 * stretch)
    goto( -284.0 + pos * 150, 228.0 * stretch)
    end_fill()

    goto( -344.0 + pos * 150, 334.0 * stretch)#hair
    color('red')
    begin_fill()
    goto( -349.0 + pos * 150, 348.0 * stretch)
    goto( -337.0 + pos * 150, 340.0 * stretch)
    end_fill()
    goto( -324.0 + pos * 150, 354.0 * stretch)
    begin_fill()
    goto( -325.0 + pos * 150, 370.0 * stretch)
    goto( -320.0 + pos * 150, 357.0 * stretch)
    end_fill()
    goto( -292.0 + pos * 150, 359.0 * stretch)
    begin_fill()
    goto( -282.0 + pos * 150, 370.0 * stretch)
    goto( -280.0 + pos * 150, 355.0 * stretch)
    end_fill()
    goto( -263.0 + pos * 150, 334.0 * stretch)
    begin_fill()
    goto( -250.0 + pos * 150, 336.0 * stretch)
    goto( -259.0 + pos * 150, 326.0 * stretch)
    end_fill()

    goto( -324.0 + pos * 150, 334.0 * stretch) #eyes
    color('white')
    pd()
    goto( -325.0 + pos * 150, 320.0 * stretch)
    pu()
    goto( -289.0 + pos * 150, 334.0 * stretch)
    pd()
    goto( -291.0 + pos * 150, 321.0 * stretch)
    pu()

    goto( -311.0 + pos * 150, 311.0 * stretch)#nose
    pd()
    goto( -312.0 + pos * 150, 305.0 * stretch)
    pu()
    goto( -304.0 + pos * 150, 311.0 * stretch)
    pd()
    goto( -304.0 + pos * 150, 305.0 * stretch)
    pu()

    goto( -299.0 + pos * 150, 286.0 * stretch) #mouth
    pd()
    goto( -281.0 + pos * 150, 303.0 * stretch)
    pu() 

    goto( -298.0 + pos * 150, 261.0 * stretch)#bowtie
    begin_fill()
    goto( -287.0 + pos * 150, 265.0 * stretch)
    goto( -288.0 + pos * 150, 244.0 * stretch)
    goto( -299.0 + pos * 150, 260.0 * stretch)
    end_fill()
    goto( -299.0 + pos * 150, 260.0 * stretch)
    begin_fill()
    goto( -311.0 + pos * 150, 267.0 * stretch)
    goto( -311.0 + pos * 150, 244.0 * stretch)
    goto( -300.0 + pos * 150, 259.0 * stretch)
    end_fill()    

def mary(pos, stretch):
    
    color('black')
    goto( -313.0 + pos * 150, 56.0 * stretch)#body
    begin_fill()
    goto( -283.0 + pos * 150, 61.0 * stretch)
    goto( -252.0 + pos * 150, 25.0 * stretch)
    goto( -246.0 + pos * 150, 24.0 * stretch)
    goto( -234.0 + pos * 150, 34.0 * stretch)
    goto( -234.0 + pos * 150, 40.0 * stretch)
    goto( -243.0 + pos * 150, 42.0 * stretch)
    goto( -253.0 + pos * 150, 34.0 * stretch)
    goto( -277.0 + pos * 150, 62.0 * stretch)
    goto( -269.0 + pos * 150, 66.0 * stretch)
    goto( -288.0 + pos * 150, 113.0 * stretch)
    goto( -266.0 + pos * 150, 130.0 * stretch)
    goto( -244.0 + pos * 150, 131.0 * stretch)
    goto( -243.0 + pos * 150, 135.0 * stretch)
    goto( -262.0 + pos * 150, 135.0 * stretch)
    goto( -245.0 + pos * 150, 148.0 * stretch)
    goto( -248.0 + pos * 150, 152.0 * stretch)
    goto( -262.0 + pos * 150, 138.0 * stretch)
    goto( -260.0 + pos * 150, 156.0 * stretch)
    goto( -265.0 + pos * 150, 155.0 * stretch)
    goto( -269.0 + pos * 150, 135.0 * stretch)
    goto( -288.0 + pos * 150, 122.0 * stretch)
    goto( -302.0 + pos * 150, 148.0 * stretch)
    goto( -320.0 + pos * 150, 150.0 * stretch)
    goto( -323.0 + pos * 150, 159.0 * stretch)
    goto( -304.0 + pos * 150, 168.0 * stretch)
    goto( -300.0 + pos * 150, 185.0 * stretch)
    goto( -307.0 + pos * 150, 212.0 * stretch)
    goto( -353.0 + pos * 150, 207.0 * stretch)
    goto( -358.0 + pos * 150, 190.0 * stretch)
    goto( -349.0 + pos * 150, 167.0 * stretch)
    goto( -339.0 + pos * 150, 160.0 * stretch)
    goto( -330.0 + pos * 150, 160.0 * stretch) 
    goto( -327.0 + pos * 150, 147.0 * stretch)
    goto( -343.0 + pos * 150, 144.0 * stretch)
    goto( -347.0 + pos * 150, 111.0 * stretch)
    goto( -370.0 + pos * 150, 117.0 * stretch)
    goto( -379.0 + pos * 150, 134.0 * stretch)
    goto( -382.0 + pos * 150, 132.0 * stretch)
    goto( -373.0 + pos * 150, 118.0 * stretch)
    goto( -394.0 + pos * 150, 126.0 * stretch)
    goto( -396.0 + pos * 150, 123.0 * stretch)
    goto( -379.0 + pos * 150, 117.0 * stretch)
    goto( -395.0 + pos * 150, 113.0 * stretch)
    goto( -393.0 + pos * 150, 107.0 * stretch)
    goto( -373.0 + pos * 150, 112.0 * stretch)
    goto( -348.0 + pos * 150, 104.0 * stretch)
    goto( -353.0 + pos * 150, 57.0 * stretch)
    goto( -346.0 + pos * 150, 50.0 * stretch)
    goto( -316.0 + pos * 150, 56.0 * stretch)
    goto( -319.0 + pos * 150, 14.0 * stretch)
    goto( -333.0 + pos * 150, 12.0 * stretch)
    goto( -337.0 + pos * 150, 5.0 * stretch)
    goto( -331.0 + pos * 150, 0.0 * stretch)
    goto( -314.0 + pos * 150, 5.0 * stretch)
    goto( -312.0 + pos * 150, 56.0 * stretch)
    end_fill()

    goto( -353.0 + pos * 150, 173.0 * stretch)#hair
    color('purple')
    begin_fill()
    goto( -371.0 + pos * 150, 168.0 * stretch)
    goto( -368.0 + pos * 150, 207.0 * stretch)
    goto( -341.0 + pos * 150, 223.0 * stretch)
    goto( -315.0 + pos * 150, 225.0 * stretch)
    goto( -295.0 + pos * 150, 208.0 * stretch)
    goto( -283.0 + pos * 150, 178.0 * stretch)
    goto( -304.0 + pos * 150, 174.0 * stretch)
    goto( -306.0 + pos * 150, 211.0 * stretch)
    goto( -355.0 + pos * 150, 206.0 * stretch)
    goto( -356.0 + pos * 150, 173.0 * stretch)
    goto( -353.0 + pos * 150, 177.0 * stretch)
    end_fill()

    goto( -336.0 + pos * 150, 204.0 * stretch)#eyes
    pd()
    goto( -335.0 + pos * 150, 190.0 * stretch)
    pu()
    goto( -324.0 + pos * 150, 205.0 * stretch)
    pd()
    goto( -323.0 + pos * 150, 193.0 * stretch)
    pu()

    goto( -329.0 + pos * 150, 182.0 * stretch)#nose
    pd()
    goto( -330.0 + pos * 150, 178.0 * stretch)
    goto( -328.0 + pos * 150, 174.0 * stretch)
    pu()

    goto( -348.0 + pos * 150, 174.0 * stretch) #mouth
    pd()
    goto( -339.0 + pos * 150, 168.0 * stretch)
    goto( -329.0 + pos * 150, 166.0 * stretch)
    goto( -317.0 + pos * 150, 166.0 * stretch)
    goto( -308.0 + pos * 150, 180.0 * stretch)
    pu()

    goto( -322.0 + pos * 150, 125.0 * stretch) #shirt buttons
    color('blue')
    dot(8)
    goto( -317.0 + pos * 150, 105.0 * stretch)
    dot(8)
    goto( -313.0 + pos * 150, 71.0 * stretch)
    dot(8)

def dave(pos, stretch):

    color('brown')
    speed('slowest')
    goto( -281.0 + pos * 150, 10 * stretch) #right shoe
    begin_fill()
    goto( -275.0 + pos * 150, 6.0 * stretch)
    goto( -276.0 + pos * 150, 0.0 * stretch)
    goto( -292.0 + pos * 150, 0.0 * stretch)
    goto( -298.0 + pos * 150, 6.0 * stretch)
    goto( -295.0 + pos * 150, 13.0 * stretch)
    goto( -281.0 + pos * 150, 10.0 * stretch)

    width(3)
    goto( -275.0 + pos * 150, 13.0 * stretch)
    goto( -283.0 + pos * 150, 71.0 * stretch)
    goto( -281.0 + pos * 150, 95.0 * stretch)
    goto( -273.0 + pos * 150, 92.0 * stretch)

    goto( -269.0 + pos * 150, 96.0 * stretch)
    goto( -261.0 + pos * 150, 85.0 * stretch)#right arm
    goto( -259.0 + pos * 150, 79.0 * stretch)
    goto( -254.0 + pos * 150, 79.0 * stretch)
    goto( -252.0 + pos * 150, 86.0 * stretch)
    goto( -256.0 + pos * 150, 88.0 * stretch)
    goto( -260.0 + pos * 150, 88.0 * stretch)
    goto( -266.0 + pos * 150, 98.0 * stretch)

    goto( -264.0 + pos * 150, 101.0 * stretch)
    goto( -262.0 + pos * 150, 103.0 * stretch)
    goto( -280.0 + pos * 150, 116.0 * stretch)
    goto( -291.0 + pos * 150, 119.0 * stretch)
    goto( -295.0 + pos * 150, 110.0 * stretch)
    goto( -296.0 + pos * 150, 122.0 * stretch)
    goto( -287.0 + pos * 150, 125.0 * stretch)
    goto( -277.0 + pos * 150, 138.0 * stretch)
    goto( -279.0 + pos * 150, 154.0 * stretch)
    goto( -274.0 + pos * 150, 154.0 * stretch)
    goto( -273.0 + pos * 150, 157.0 * stretch)
    goto( -289.0 + pos * 150, 167.0 * stretch)
    goto( -299.0 + pos * 150, 173.0 * stretch)
    goto( -299.0 + pos * 150, 169.0 * stretch)
    goto( -308.0 + pos * 150, 172.0 * stretch)
    goto( -320.0 + pos * 150, 165.0 * stretch)
    goto( -317.0 + pos * 150, 161.0 * stretch)
    goto( -322.0 + pos * 150, 145.0 * stretch)
    goto( -318.0 + pos * 150, 132.0 * stretch)
    goto( -308.0 + pos * 150, 124.0 * stretch)
    goto( -301.0 + pos * 150, 124.0 * stretch)
    goto( -300.0 + pos * 150, 114.0 * stretch)
    goto( -311.0 + pos * 150, 118.0 * stretch)
    goto( -322.0 + pos * 150, 117.0 * stretch)

    goto( -334.0 + pos * 150, 104.0 * stretch)
    goto( -330.0 + pos * 150, 98.0 * stretch)
    goto( -342.0 + pos * 150, 90.0 * stretch)
    goto( -348.0 + pos * 150, 86.0 * stretch)
    goto( -345.0 + pos * 150, 80.0 * stretch)
    goto( -339.0 + pos * 150, 81.0 * stretch) #left arm
    goto( -338.0 + pos * 150, 85.0 * stretch)
    goto( -328.0 + pos * 150, 95.0 * stretch)
    goto( -325.0 + pos * 150, 80.0 * stretch)
    goto( -321.0 + pos * 150, 94.0 * stretch)


    goto( -323.0 + pos * 150, 77.0 * stretch)
    goto( -321.0 + pos * 150, 69.0 * stretch)

    goto( -327.0 + pos * 150, 14.0 * stretch)
    goto( -325.0 + pos * 150, 12.0 * stretch)
    goto( -307.0 + pos * 150, 12.0 * stretch) #left shoe
    goto( -307.0 + pos * 150, 7.0 * stretch)
    goto( -312.0 + pos * 150, 0.0 * stretch)
    goto( -325.0 + pos * 150, 0.0 * stretch)
    goto( -329.0 + pos * 150, 6.0 * stretch)
    goto( -323.0 + pos * 150, 11.0 * stretch)

    goto( -308.0 + pos * 150, 14.0 * stretch)
    goto( -305.0 + pos * 150, 14.0 * stretch)
    goto( -300.0 + pos * 150, 36.0 * stretch)
    goto( -299.0 + pos * 150, 13.0 * stretch)
    goto( -295.0 + pos * 150, 11.0 * stretch)
    goto( -281.0 + pos * 150, 10.0 * stretch)
    end_fill()
   

   
    goto( -318.0 + pos * 150, 159.0 * stretch)
    color('black')
    
    pd()
    goto( -308.0 + pos * 150, 159.0 * stretch)
    goto( -308.0 + pos * 150, 156.0 * stretch) #hairline
    goto( -299.0 + pos * 150, 158.0 * stretch)
    goto( -295.0 + pos * 150, 155.0 * stretch)
    goto( -289.0 + pos * 150, 157.0 * stretch)
    goto( -280.0 + pos * 150, 152.0 * stretch)
    pu()
    
    goto( -305.0 + pos * 150, 148.0 * stretch) #eyes
    dot(6)
    goto( -296.0 + pos * 150, 148.0 * stretch)
    dot(6)

    goto( -300.0 + pos * 150, 145.0 * stretch)
    pd()
    goto( -300.0 + pos * 150, 140.0 * stretch)#nose
    pu()

    goto( -307.0 + pos * 150, 136.0 * stretch)
    pd()
    goto( -302.0 + pos * 150, 134.0 * stretch)
    goto( -298.0 + pos * 150, 134.0 * stretch)#mouth
    goto( -294.0 + pos * 150, 136.0 * stretch)
    goto( -289.0 + pos * 150, 139.0 * stretch)
    pu()

    goto( -319.0 + pos * 150, 70.0 * stretch)
    pd()
    goto( -308.0 + pos * 150, 71.0 * stretch)#pant line
    goto( -293.0 + pos * 150, 72.0 * stretch)
    goto( -284.0 + pos * 150, 72.0 * stretch)
    pu()

def crown(pos, stretch, xOffset, yOffset):
    color('gold')
    goto( -305.0 + pos * 150 + xOffset, (0.0 + yOffset) * stretch )
    begin_fill()
    goto( -313.0 + pos * 150 + xOffset, (44.0 + yOffset) * stretch )
    goto( -296.0 + pos * 150 + xOffset, (33.0 + yOffset) * stretch )
    goto( -289.0 + pos * 150 + xOffset, (62.0 + yOffset)  * stretch )
    goto( -272.0 + pos * 150 + xOffset, (39.0 + yOffset) * stretch )
    goto( -257.0 + pos * 150 + xOffset, (79.0 + yOffset) * stretch )
    goto( -240.0 + pos * 150 + xOffset, (38.0 + yOffset) * stretch )
    goto( -220.0 + pos * 150 + xOffset, (61.0 + yOffset) * stretch )
    goto( -217.0 + pos * 150 + xOffset, (32.0 + yOffset) * stretch )
    goto( -198.0 + pos * 150 + xOffset, (44.0 + yOffset) * stretch )
    goto( -206.0 + pos * 150 + xOffset, (2.0 + yOffset) * stretch )
    goto( -305.0 + pos * 150 + xOffset, (0.0 + yOffset) * stretch )
    end_fill()

    

### Draw the stick figures as per the provided data set
def draw_portrait(portrait_number):
    for cell in portrait_number:
        name = cell[0]
        pos = cell[1]
        stretch = cell[2]
        hat = cell[3]
        if name == 'Person A':
            dave(pos, stretch)
            if hat == '*':
                crown(pos, stretch, -40, 173)
        elif name == 'Person B':
            mary(pos, stretch)
            if hat == '*':
                crown(pos, stretch, -75, 215)
        elif name == 'Person C':
            jerome(pos, stretch)
            if hat == '*':
                crown(pos, stretch, -40, 355)
        elif name == 'Person D':
            joe(pos, stretch)
            if hat == '*':
                crown(pos, stretch, -40, 65)
        elif name == 'Pet':
            fish(pos, stretch)


#--------------------------------------------------------------------#


#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your stick figures.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing window with a blue background representing
# the sky, and with the "home" coordinate set to the middle of the
# area where the stick figures will stand
setup(window_width, window_height)
setworldcoordinates(-window_width / 2, grass_offset,
                    window_width / 2, window_height + grass_offset)
bgcolor('sky blue')

# Draw the grass (with animation turned off to make it faster)
tracer(False)
draw_grass()

# Give the window a title
# ***** Replace this title with one that describes your choice
# ***** of individuals
title('My Stretchy Squad (Close friends and their pet fish)')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Draw the locations to stand, their labels and selected coordinates
# ***** If you don't want to display these background elements,
# ***** to make your portrait look nicer, change the corresponding
# ***** argument(s) below to False
draw_locations(True)
draw_labels(True)
mark_coords(True)

# Call the student's function to display the stick figures
# ***** If you want to turn off animation while drawing your
# ***** stick figures, to make your program draw faster, change
# ***** the following argument to False
tracer(False)
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_portrait(portrait_12)


# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#

