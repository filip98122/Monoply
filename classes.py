from personalfunc import *
#BUTTON AND WHAT GOES WITH IT

class Button:
    def __init__(s,type,permanantargs,selfargs,plus):
        s.type=type
        s.permanantargs=permanantargs
        s.permanantargs[0]=s.permanantargs[0]-textures[s.type].get_width()//2
        s.permanantargs[1]=s.permanantargs[1]-textures[s.type].get_height()//2
        
        s.permanantargs[0]=s.permanantargs[0]+plus[0]
        s.permanantargs[1]=s.permanantargs[1]+plus[1]
        s.selfargs=selfargs
    def doit(s,functionhash,args):
        returnedargs,s.selfargs=functionhash[s.type](args,s.permanantargs,s.type,s.selfargs)
        return returnedargs
lbuttons=[
    Button("intostartmenu",[WIDTH//2,HEIGHT//1.5],["playmenu"],[0,0]),
    Button("intostartmenu",[WIDTH//2,HEIGHT//1.25],["game"],[0,0]),
    Button("numofplayers",[WIDTH//2,HEIGHT//4],[0],[textures["numofplayers"].get_width()//2,textures["numofplayers"].get_height()//2]),
    
    [
    Button("playerconfig",[WIDTH//2,HEIGHT//1.5],[0],[0,0])
    
    
    ]

    
]
functionhash={"intostartmenu":startbutton,"numofplayers":doublenumofplayers,"playerconfig":playerconfig}