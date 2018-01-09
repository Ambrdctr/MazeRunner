def ecrire(ch, screen):
    size = screen.get_size()
    if size[0] <= size[1]:
        taille_case = size[0] // 12
    else:
        taille_case = size[1] // 12

    x=0
    y=taille_case*6
    xp=taille_case*13
    yp=taille_case*8