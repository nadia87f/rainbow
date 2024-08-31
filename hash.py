import turtle
t=turtle.Turtle()
t.shape('turtle')
t.pencolor('light green')
t.speed(1)
screen=turtle.Screen()
screen.title('suherfe.blug.ir')
t.width(3)
List=['crimson','indigo','darkslategray','steelblue','lightcoral','cadetblue','hotpink','darkred']
for i in range(8):
    t.right(45)
    t.color(List[i])
    
    for j in range(8):
        
        t.forward(100)
        
        t.right(45)
t.hideturtle()      
