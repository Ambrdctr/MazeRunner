def convertirSecondes(temps):

    heure = 0
    minute = 0
    seconde = 0
    reste = temps

    while reste != 0:
        if reste >= 3600:
            heure += 1
            reste -= 3600
        if reste >= 60:
            minute += 1
            reste -= 60
        else:
            seconde += reste
            reste -= reste

    if heure >= 1:
        chH = str(heure) + ":"
    else:
        chH = ""

    if minute >= 1:
        chM = str(minute) + "'"
    else:
        chM = ""

    if seconde >= 1:
        chS = str(seconde) + '"'
    else:
        chS = ""

    return chH + chM + chS
