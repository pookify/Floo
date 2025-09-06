import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")

""" 
Outer Ring Squares
"""
#region

# Turtle for squares 
sq = turtle.Turtle()
sq.speed(0)
sq.pensize(1)

# base pattern settings
num_squares = 120 
side_length = 10 
radii = [
    230, 
    220, 
    210, 
    200, 
    190, 
    180,
    170
]
fill_colors = [
    "#00610E", 
    "#17730D",
    "#3D860B", 
    "#34A203", 
    "#6EC007", 
    "#C1D11F", 
    "#C1D11F",
]

outline_color = "white" 

# Draw squares in a circle
for layer in range(0, 7):
    radius = radii[layer]
    fill_color = fill_colors[layer]
    for i in range(num_squares):
        angle = (360 / num_squares) * i             # angle for each square
        
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        sq.penup()
        sq.goto(x, y)
        sq.setheading(angle + 89)                   # rotate so square touches neighbor
        sq.pendown()
        sq.pencolor(outline_color)
        sq.fillcolor(fill_color)
        sq.begin_fill()
        for j in range(4):
            sq.forward(side_length)
            sq.right(90)
        sq.end_fill()
        
        sq.penup()

sq.hideturtle()
#endregion

"""
Outer Ring of Flowers
"""
#region

# function to draw one spirograph with yellow center
def draw_spirograph(t, x, y, spiro_count, circle_radius, spiro_size, fill_color, pen_color):
    t.pencolor(pen_color)
    t.fillcolor(fill_color)

    # draw spirograph (outer circles)
    for i in range(spiro_count):
        angle = (360 / spiro_count) * i
        cx = x + spiro_size * math.cos(math.radians(angle))
        cy = y + spiro_size * math.sin(math.radians(angle))

        t.penup()
        t.goto(cx, cy - circle_radius)
        t.pendown()

        t.begin_fill()
        t.circle(circle_radius)
        t.end_fill()

    # draw yellow center circle
    t.penup()
    t.goto(x, y - circle_radius//2)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(circle_radius//2)
    t.end_fill()


# function to make a circle of spirographs
def circle_of_spirographs(t, center_x, center_y, big_radius, num_spiro, 
                          spiro_count, circle_radius, spiro_size, fill_color, pen_color):
    for i in range(num_spiro):
        angle = (360 / num_spiro) * i
        x = center_x + big_radius * math.cos(math.radians(angle))
        y = center_y + big_radius * math.sin(math.radians(angle))
        draw_spirograph(t, x, y, spiro_count, circle_radius, spiro_size, fill_color, pen_color)

flower_ring_t = turtle.Turtle()
flower_ring_t.speed(0)

circle_of_spirographs(
    flower_ring_t,                                  # turtle object
    0, 0,                                           # center
    230, 24,                                        # big radius, number of spirographs
    10, 10, 7,                                      # spiro_count, circle_radius, spiro_size
    "#FF6F91", "#FF3E75"                        # fill and pen colors
)

flower_ring_t.hideturtle()
#endregion

"""
Lotus Outward Spiral - Removed
"""
#region

# lotus_spiral_t = turtle.Turtle()
# lotus_spiral_t.speed(0)

# for step in range(10, 20):
#     for c in ("DeepSkyBlue", "DeepPink3", "DarkViolet"):
#         lotus_spiral_t.right(0)
#         lotus_spiral_t.up()
#         lotus_spiral_t.goto(0,0)
#         lotus_spiral_t.forward(step*8)
#         lotus_spiral_t.down()
#         lotus_spiral_t.width(2)
#         lotus_spiral_t.begin_fill()
#         lotus_spiral_t.color("lime")
#         lotus_spiral_t.circle(4)
#         lotus_spiral_t.end_fill()
#         lotus_spiral_t.color("yellow")
#         lotus_spiral_t.stamp()
#         lotus_spiral_t.right(75)
#         for i in range(3):
#             lotus_spiral_t.left(35)
#             lotus_spiral_t.width(2)
#             lotus_spiral_t.color(c)
#             lotus_spiral_t.circle(step, 100)
#             lotus_spiral_t.left(85)
#             lotus_spiral_t.circle(step, 100)
# lotus_spiral_t.hideturtle()
#endregion


""" 
Outer Red Ring - Removed
"""
#region

# outer_circle_t = turtle.Turtle()
# outer_circle_t.speed(0)

# outer_circle_t.pensize(5) 
# outer_circle_t.fillcolor("pink")
# outer_circle_t.begin_fill()
# outer_circle_t.pencolor("red") 
# outer_circle_t.penup()
# outer_circle_t.goto(0, -200)                        # start at bottom of circle so it’s centered
# outer_circle_t.pendown()
# outer_circle_t.circle(200)
# outer_circle_t.end_fill()
# outer_circle_t.hideturtle()
#endregion

""" 
Main Petals Spiral 
"""
#region

def draw_filled_petal(t, radius, color, angle):
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.circle(radius, angle)
    t.left(2 * angle)
    t.circle(radius, angle)
    t.left(360 - 2 * angle)
    t.end_fill()

def draw_petals(t, radius, petals, color, offset = 0, angle = 60):
    t.pencolor(0, 0, 0)
    for i in range(petals):
        t.penup()
        t.goto(0, 0)
        t.setheading((360/petals * i) + offset)
        t.forward(radius)
        t.pendown()
        draw_filled_petal(t, radius, color, angle)
        
def pookalam_pattern(size):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    
    draw_petals(t, size + 70, 12, '#FF0000', 19, 50)
    draw_petals(t, size + 60, 12, '#FF3300', 3, 50)
    draw_petals(t, size + 50, 12, '#FF6600', 19, 50)
    draw_petals(t, size + 40, 12, '#FF8000', 3, 50)
    draw_petals(t, size + 35, 12, '#FFA500', 19, 50)
    draw_petals(t, size + 28, 12, '#FFCC00', 3, 50)
    draw_petals(t, size + 22, 12, '#FFFF00', 19, 50)
    
    t.hideturtle()

size = 50
pookalam_pattern(size)
#endregion

""" 
Center Circle inside Petals - Removed
"""
#region

# inner_circle_t = turtle.Turtle()
# inner_circle_t.speed(0)

# inner_circle_t.pencolor("black") 
# inner_circle_t.fillcolor("yellow") 
# inner_circle_t.pensize(3)
# inner_circle_t.penup()
# inner_circle_t.goto(0, -77)                         # start at bottom of circle so it’s centered
# inner_circle_t.pendown()
# inner_circle_t.begin_fill()
# inner_circle_t.circle(77)
# inner_circle_t.end_fill()
# inner_circle_t.hideturtle()
#endregion

"""
Lotus Bud Petal Spiral at the Centre
"""
#region

petal_circ_t = turtle.Turtle()
petal_circ_t.speed(0)

petal_circ_t.pencolor("white")
petal_circ_t.pensize(0.5)

num_circles = 10
fill_colors = [
    "#FF3E75", 
    "#FF6F91",
    "#FF91AF",
    "#FF5F75",
    "#FF8F91",
    "#FF9FEF"
]
big_radii = [
    50,
    40,
    30
]
small_radii = [
    45,
    40,
    35
]
for layer in range(0, 3):
    
    petal_circ_t.pencolor(fill_colors[layer + 3])
    petal_circ_t.fillcolor(fill_colors[layer])
    
    big_radius = big_radii[layer]
    small_radius = small_radii[layer]
    
    for i in range(num_circles):
        angle = (360 / num_circles) * i             # angle for each circle
        # Calculate x,y position using polar coordinates
        x = big_radius * math.cos(math.radians(angle))
        y = big_radius * math.sin(math.radians(angle))

        petal_circ_t.penup()
        petal_circ_t.goto(x, y - small_radius)      # start at bottom of circle so it is centered
        petal_circ_t.pendown()
        petal_circ_t.begin_fill()
        petal_circ_t.circle(small_radius)
        petal_circ_t.end_fill()

petal_circ_t.hideturtle()
#endregion

"""
Spirograph base at the Centre - Hidden
"""
#region

sq = turtle.Turtle()
sq.speed(0)

nums_squares = [
    40, 
    35, 
    30,
    25
]
side_lengths = [
    37,
    34,
    30,
    26
]
colors = [
    "#1FA247",
    "#0B6623",
    "#34C759",
    "#C8FACC"
]
for layer in range(0, 4):
    sq.pencolor(colors[layer])
    sq.fillcolor(colors[layer])
    
    num = nums_squares[layer]
    side = side_lengths[layer]
    
    for i in range(num):
        sq.begin_fill()
        for _ in range(4):
            sq.forward(side)
            sq.right(90)
        sq.end_fill()
        
        sq.right(360 / num)

sq.hideturtle()
#endregion

"""
Central Lotus - Test
"""
#region

sq_t = turtle.Turtle()
sq_t.speed(0)

sq_t.pencolor("black")
sq_t.pensize(2)

fill_colors = [
    "#C2185B",
    "#FF3E75",
    "#FF6F91",
    "#FF91AF",
    "#FFB6C1",
    "#FFB6C1",
    "#FFB6C1"
]
nums_squares = [
    12, 12, 12, 12, 9, 9, 9
]
square_sizes = [
    57, 50, 43, 36, 29, 22, 15
]

# Function to draw one filled square
def draw_square(size):
    sq_t.begin_fill()
    for _ in range(4):
        sq_t.forward(size)
        sq_t.right(90)
    sq_t.end_fill()

# Draw the square spirograph
for i in range(len(nums_squares)):
    num = nums_squares[i]
    square_size = square_sizes[i]
    angle = (360 / num)
    sq_t.fillcolor(fill_colors[i])
    
    for _ in range(num):
        draw_square(square_size)
        sq_t.right(angle)                               # rotate before drawing next square

sq_t.hideturtle()
#endregion

"""
Vilakku - Removed
"""
#region

""" 
Center Spirograph - Removed
"""
#region

# sq_t = turtle.Turtle()
# sq_t.speed(0) 
# sq_t.pencolor("blue") 
# sq_t.pensize(5)

# def draw_square(size):
#     for _ in range(4):
#         sq_t.forward(size)
#         sq_t.right(90)

# # Spirograph settings 
# num_squares = 6 
# square_size = 57 
# angle = 360 / num_squares                           # rotation angle between squares

# # Draw spirograph
# for _ in range(num_squares):
#     draw_square(square_size)
#     sq_t.right(angle)                               # rotate before next square

# sq_t.hideturtle()
#endregion

""" 
Vilakku Base - Removed
"""
#region

# vilakku_circle_t = turtle.Turtle()
# vilakku_circle_t.speed(0)
# vilakku_circle_t.pencolor("black") 
# vilakku_circle_t.fillcolor("yellow") 
# vilakku_circle_t.pensize(3)
# vilakku_circle_t.penup()
# vilakku_circle_t.goto(0, -50)                       # start at bottom of circle so it’s centered
# vilakku_circle_t.pendown()
# vilakku_circle_t.begin_fill()
# vilakku_circle_t.circle(50)
# vilakku_circle_t.end_fill()
# vilakku_circle_t.hideturtle()
#endregion

""" 
Vilakku Flame - Removed
"""
#region

# petal = turtle.Turtle()
# petal.speed(0)

# petal.pencolor("darkred") 
# petal.fillcolor("orange") 

# # Move to starting point (adjust to position)
# petal.penup()
# petal.goto(20, -17) 
# petal.setheading(63)                                # center-bottom of petal
# petal.pendown()

# # Draw flame-like petal
# petal.begin_fill()

# # First arc (left side of flame)
# petal.circle(45, 55)                                # radius=100, arc=60 degrees
# petal.left(120)                                     # sharp turn at tip

# # Second arc (right side of flame)
# petal.circle(45, 55)
# petal.end_fill()
# petal.hideturtle()
#endregion

""" 
Vilakku - Removed
"""
#region

# semi = turtle.Turtle()
# semi.speed(0)

# semi.pencolor("white") 
# semi.fillcolor("blue") 
# semi.penup()
# semi.goto(-25, -7)                                  # left edge of semicircle
# semi.setheading(-90)                                # face right (so arc goes upward)
# semi.pendown()
# semi.begin_fill()
# semi.circle(25, 180)                                # radius=100, extent=180 → semicircle
# semi.goto(-25, -7)                                  # close the shape
# semi.end_fill()

# semi.hideturtle()
#endregion

""" 
Vilakku Circles Halo - Removed
"""
#region

# # Create a new turtle for the circle of circles
# coc_t = turtle.Turtle()
# coc_t.speed(0) 

# coc_t.pencolor("orange")
# coc_t.fillcolor("yellow")
# coc_t.pensize(2)

# # Settings 
# big_radius = 40                                     # radius of the circles' ring
# small_radius = 3                                    # radius of each small circle
# num_circles = 12 

# # Draw the circle of circles
# for i in range(num_circles):
#     angle = (360 / num_circles) * i                 # angle for each circle
#     # Calculate x,y position using polar coordinates
#     x = big_radius * math.cos(math.radians(angle))
#     y = big_radius * math.sin(math.radians(angle))
#     coc_t.penup()
#     coc_t.goto(x, y - small_radius)                 # start at bottom of circle so it’s centered
#     coc_t.pendown()
#     coc_t.begin_fill()
#     coc_t.circle(small_radius)
#     coc_t.end_fill()

# coc_t.hideturtle()
#endregion

#endregion

# Keep window open
turtle.done()

"""
temp
"""
#region


#endregion
