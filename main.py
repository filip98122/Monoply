from classes import *
state="mainmenu"
esc=False
clickedl=False
holdingl=False
clickedr=False
holdingr=False
hold=False
while state!="break":
    window.fill((144,213,255))
    background(state)
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            state="break"
    #Start what needs to be used
    
    if esc and not keys[pygame.K_ESCAPE]:
        esc=False
    
    if clickedl:
        clickedl=False
    if mouseState[0]:
        if not holdingl:
            clickedl=True
        holdingl=True
    else:
        holdingl=False
    if clickedr:
        clickedr=False
    if mouseState[1]:
        if not holdingr:
            clickedr=True
        holdingr=True
    else:
        holdingr=False

    state,esc=escclicked(state,esc,keys)
    # STATE RELEVANT
    if state=="mainmenu" or state=="break":
        args=lbuttons[0].doit(functionhash,[mousePos,[clickedl],state])
        state=args[0]
    elif state=="playmenu":
        args=lbuttons[2].doit(functionhash,[mousePos,[clickedl],state])
        args=lbuttons[1].doit(functionhash,[mousePos,[clickedl],state])
        state=args[0]
        for i in range(lbuttons[2].selfargs[0]+1):
            lbuttons[3][i].doit(functionhash,[mousePos,[clickedl],state])
            # +1 jer je lb[2].slargs[0] indeksiran od 0
    elif state=="game":
        if keys[pygame.K_SPACE]:
            if not hold:
                p.pos+=1
                hold=False
        else:
            hold=False
        p.draw()
    # End what needs to be used
    pygame.display.update()
    clock.tick(60)
