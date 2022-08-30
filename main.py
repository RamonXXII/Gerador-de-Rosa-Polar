import math
from ntpath import join
import sys


def svgBegin(l, a):
    return "<svg width='{w}' height='{h}' xmlns='http://www.w3.org/2000/svg'>\n".format(w = l, h = a)

# circulo svg
def svgCircle(x,style):
    return "<circle cx='{X}' cy='{Y}' r='{R}' style = '{S}' />\n".format (X=x[0], Y=x[1], R=x[2], S=style)

# fim do svg
def svgEnd():
    return "</svg>"

def svgStyle(x):
    return "fill:rgb({R},{G},{B}); mix-blend-mode: screen;".format(R=x[0], G=x[1], B=x[2])

def rosa_polar(n,d,quality):
    
    tam_loop = d/n if (d%n == 0) else d
    # quality = 100 * max(n,d) +30

    list =  []
    theta = 0.0
    # for better visualization:
    Height = 750
    Widht = 350
    Tam = 200

    for i in range(0,int(quality*2*math.pi*tam_loop),1):
        theta +=0.01
        
        # converting polar coordnates to cartesian coordinates
        r = math.cos(n/d*theta)
        x = Height + Tam *(r)*(math.cos(theta))
        y = Widht + Tam *(r)*(math.sin(theta))

        # this is a list of points in cartesian coordinates (x, y) + radius
        list.append((x , y, 2))
    return list

def oscar_butterfly(n,d,quality):
    tam_loop = d/n if (d%n==0) else (n/d if (n%d==0) else max(n,d))

    list =[]
    theta =0.0
    # for better visualization:
    Height = 750
    Widht = 350
    Tam = 200

    for i in range(0,int(quality*2*math.pi*tam_loop),1):
        theta+=0.01

        r = pow(math.cos(n*theta), 2) + math.sin(d*theta) +0.3
        x = Height - Tam * math.cos(theta) * r
        y = Widht  - Tam * math.sin(theta) * r

        list.append((x, y, 2))
    return list

def limason(a,b,quality):
    tam_loop = b/a if (b%a == 0) else b

    list = []
    theta = 0.0
    # for centralization: 
    Height = 750
    Widht = 350

    for i in range(0,int(quality* 2*math.pi*tam_loop),1):
        theta+=0.01

        r = math.cos(theta)
        x = Height -(a+ b*(math.cos(theta))* r)
        y = Widht  -(a+ b*(math.sin(theta))) * r

        list.append((x, y, 2))
    return list 

def quality(case):
    case = case.lower()
    if(case == "high"):
        return 1000
    # recommended == 100
    else:
        return 100

def switch_color(case):
    case = case.lower()
    if (case == "red"):
        return (255,0,0)
    elif (case == "blue"):
        return (0,0,255)
    elif (case == "green"):
        return (0,255,0)
    elif (case == "gold"):
        return (255,215,0)
    elif (case == "black"):
        return (0,0,0)
    elif (case == "pink"):
        return (255,77,255)
    elif (case == "purple"):
        return (160,32,240)
    
def coloracao(n, d, quality, cores,str):
    if(str=="borbo"):
        tam_loop = d/n if (d%n==0) else (n/d if (n%d==0) else max(n,d))
    else:
         tam_loop = d/n if ( d%n==0 ) else d
         #quality = 100* max(n,d) +30
    
    list =[]
    cor = switch_color (cores)
    for i in range(0,int(quality*2*math.pi*tam_loop),1):
        list.append(cor)
    return list

def svgElements(func, elements, style):
    return ' '.join(map(func,elements,style))

def svgAll(str,n,d,quality,str_cor):
    str = str.lower()
    if(str == "rose"):
        fig = rosa_polar(n,d,quality)
    elif(str == "butterfly"):
        fig = oscar_butterfly(n,d,quality)
    elif(str == "limason"):
        fig = limason(n,d,quality)
    else:
        print("entrada incorreta!")
        return
    palette = coloracao (n, d, quality,str_cor, str)
    return svgElements(svgCircle,fig,map(svgStyle,palette))

# main 
def main():
    str = (sys.argv[1])
    n = float (sys.argv[2]) 
    d = float (sys.argv[3]) 
    quality = float (sys.argv[4]) 
    cor = sys.argv[5]

    quality = 100

    print ( (svgBegin (1500, 700)) + (svgAll (str,n,d,quality,cor)) + svgEnd())

# improvisa uma main() em python
if __name__ == "__main__":
    main()