from functions import *
# STATE RELEVANT

def escclicked(state,esc,keys):
    if esc>0:
        esc-=1
    else:
        if keys[pygame.K_ESCAPE]:
            if state=="mainmenu":
                state="break"
            if state=="playmenu":
                state="mainmenu"
                esc=120
    return state,esc
# STATE RELEVANT

def background(state):
    if state=="mainmenu":
        window.blit(textures["mainmenu"],(0,-HEIGHT//4))
    if state=="playmenu":
        window.fill((144,213,255))

#BUTTON FUNCTIONS BELOW
#BUTTON FUNCTIONS BELOW
#BUTTON FUNCTIONS BELOW
#BUTTON FUNCTIONS BELOW

def startbutton(args:list,permanants,type,selfargs):
    state=args[2]
    window.blit(textures[type],(permanants[0],permanants[1]))
    if button_colision(textures[type].get_width(),textures[type].get_height(),permanants[0],permanants[1],args[0],args[1]):
        state="playmenu"
    return [state],selfargs

def doublenumofplayers(args,permanants,type,selfargs):
    state=args[2]
    
    window.blit(textures[f'{selfargs[0]}'],textures[f'{selfargs[0]}'].get_rect(center=(permanants[0],permanants[1])))
    window.blit(textures["less"],textures["less"].get_rect(center=(textures[f'{selfargs[0]}'].get_width()*1.5+permanants[0],permanants[1])))
    #if button_colision(textures[type].get_width(),textures[type].get_height(),permanants[0],permanants[1],args[0],args[1]):
    #    state="playmenu"
    return [state],selfargs