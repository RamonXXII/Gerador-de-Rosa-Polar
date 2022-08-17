


Point = (float,float)
Circle = (Point,float)

def svgCircle( x,y,r, str): 
    return "<circle cx= '{X}' cy='{Y}f' r='{R}' style = '{style}' />\n". format(X= x, Y=y, R=r, style= str)

def loop (num,deno): 
    return (deno % num == 0)


# começo do svg
def svgBegin(l, a):
    return "<svg width='{w}' height='{h}' xmlns='http://www.w3.org/2000/svg'>\n".format(w = l, h = a)

# fim do svg
def svgEnd():
    return "</svg>"

def plus2(x):
    return x+2