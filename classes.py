from personalfunc import *
#BUTTON AND WHAT GOES WITH IT

class Button:
    def __init__(s,type,permanantargs,selfargs):
        s.type=type
        s.permanantargs=permanantargs
        s.permanantargs[0]=s.permanantargs[0]-textures[s.type].get_width()//2
        s.permanantargs[1]=s.permanantargs[1]-textures[s.type].get_height()//2
        s.selfargs=selfargs
    def doit(s,functionhash,args):
        returnedargs,s.selfargs=functionhash[s.type](args,s.permanantargs,s.type,s.selfargs)
        return returnedargs
lbuttons=[
    Button("intostartmenu",[WIDTH//2,HEIGHT//1.5],[]),
    Button("numofplayers",[WIDTH//2,HEIGHT//1.5],[1])
]
functionhash={"intostartmenu":startbutton,"numofplayers":doublenumofplayers}

