def dicotomie(TirantEau, Fpoids, Farchimede):
    epsilon = 0.1

    while abs(Fpoids-Farchimede) > epsilon :
        milieu = (abs(Fpoids) + abs(Farchimede)) / 2

        if abs(Fpoids) > abs(Farchimede):
            abs(Fpoids) - milieu
