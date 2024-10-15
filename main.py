'''
coucou
'''

# imports
from plotly.graph_objects import Scatter, Figure

def syr_plot(lsyr):
    '''
    coucou
    '''
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    liste = []
    liste.append(n)
    while n > 1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        liste.append(n)
    return liste

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    # votre code ici

    n = len(l)
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici

    n = 0
    i=0
    while i<len(l):
        if l[i]<l[0]:
            return n
        n+=1
        i+=1

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    # votre code ici

    n = 0
    i=0
    while i<len(l):
        if n<l[i]:
            n=l[i]
        i+=1
    return n

def main():
    '''
    coucou
    '''
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(f"temp de vol : {temps_de_vol(lsyr)}")
    print(f"temp de vol en altitude : {temps_de_vol_en_altitude(lsyr)}")
    print(f"altitude max : {altitude_maximale(lsyr)}")

if __name__ == "__main__":
    main()
