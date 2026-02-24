from classes import *
state="mainmenu"
esc=0
while state!="break":
    #Start what needs to be used
    
    window.fill((144,213,255))
    background(state)
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            state="break"
    state,esc=escclicked(state,esc,keys)
    # STATE RELEVANT
    if state=="mainmenu" or state=="break":
        args=lbuttons[0].doit(functionhash,[mousePos,mouseState,state])
        state=args[0]
    # End what needs to be used
    pygame.display.update()
    clock.tick(60)