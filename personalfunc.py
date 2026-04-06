from functions import *
# STATE RELEVANT

def escclicked(state,esc,keys):
    if not esc:
        if keys[pygame.K_ESCAPE]:
            if state=="mainmenu":
                state="break"
            if state=="playmenu":
                state="mainmenu"
                esc=True
            if state=="game":
                state="mainmenu"
                esc=True
    return state,esc
# STATE RELEVANT

def background(state):
    if state=="mainmenu":
        window.blit(textures["mainmenu"],(0,-HEIGHT//4))
    if state=="playmenu":
        window.fill((144,213,255))
    if state=="game":
        window.fill((144,213,255))
        window.blit(textures["board"],textures["board"].get_rect(center=(WIDTH//2,HEIGHT//2)))

#BUTTON FUNCTIONS BELOW
#BUTTON FUNCTIONS BELOW
#BUTTON FUNCTIONS BELOW
#BUTTON FUNCTIONS BELOW

def startbutton(args:list,permanants,type,selfargs):
    state=args[2]
    window.blit(textures[type],textures[type].get_rect(center=(permanants[0],permanants[1])))
    if button_colision(textures[type].get_width(),textures[type].get_height(),permanants[0],permanants[1],args[0],args[1]):
        state=selfargs[0]
    return [state],selfargs



def playerconfig(args,permanants,type,selfargs):
    returned,index=doublenumofplayers(args,permanants,type,selfargs)
    selfargs[0]=index[0]
    return returned,selfargs

def doublenumofplayers(args,permanants,type,selfargs):
    if type=="numofplayers":
        mod=4
    else:
        mod=5
    state=args[2]
    window.blit( textures [f'{type}{selfargs[0]+1}'],textures[f'{type}{selfargs[0]+1}'].get_rect(center=(permanants[0],permanants[1])))
    window.blit( textures ["less"],textures["less"].get_rect(center=(permanants[0]-textures[f'{type}{selfargs[0]+1}'].get_width()*0.5-textures["less"].get_width()//1.5,permanants[1])))
    window.blit( textures ["more"],textures["more"].get_rect(center=(permanants[0]+textures[f'{type}{selfargs[0]+1}'].get_width()*0.5+textures["more"].get_width()//1.5,permanants[1])))
    window.blit( textures [type],textures[type].get_rect(center=(permanants[0],permanants[1]-textures[f'{type}{selfargs[0]+1}'].get_height()))) 
    
    if button_colision(textures["less"].get_width(),
                       textures["less"].get_height(),
                       permanants[0]
                       -textures[f'{type}{selfargs[0]+1}'].get_width()*0.5
                       -textures["less"].get_width()//1.5
                       ,permanants[1],args[0],args[1]):
        
        
                selfargs[0]-=1
                
        
    selfargs[0]+=mod
    selfargs[0]%=mod
    if button_colision(textures["more"].get_width(),
                       textures["more"].get_height(),
                       permanants[0]
                       +textures[f'{type}{selfargs[0]+1}'].get_width()*0.5
                       +textures["more"].get_width()//1.5,
                       permanants[1],args[0],args[1]):
    
        
    
        selfargs[0]+=1
        
        
    
    selfargs[0]+=mod
    selfargs[0]%=mod
    return [],selfargs