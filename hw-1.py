Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> col = ['yellow','orange','red','purple','blue','green','cyan','pink','magenta','pink']
>>> for x in range(4):
...     tao.right(90)
...     for i in range(10):
...         tao.pencolor(col[i])
...         tao.circle(i*10)
... 
...         
