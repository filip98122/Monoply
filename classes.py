from personalfunc import *

class Player:
    def __init__(s,index,money,position):
        s.index=index
        s.money=money
        s.pos=position
    def draw(s):
        s.pos%=40
        howmuch=-1
        x=-1
        y=-1
        angle=0
        if s.pos<=10 and s.pos>=0:
            y=HEIGHT//1.152737752161383
            y+=(HEIGHT-y)//2
            howmuch=10-s.pos
            angle=270
        if s.pos>=10 and s.pos<=20:
            x=HEIGHT//1.152737752161383
            x=(HEIGHT-x)//2
            howmuch=20-s.pos
            angle=0
        if s.pos>=20 and s.pos<=30:
            y=HEIGHT//1.152737752161383
            y=(HEIGHT-y)//2
            howmuch=s.pos-20
            angle=90
        if s.pos>=30 and s.pos<=39 or s.pos==0:
            x=HEIGHT//1.152737752161383
            x+=(HEIGHT-x)//2
            howmuch=s.pos-30
            angle=180
        if y==-1:
            y=(HEIGHT//12.5)*(howmuch+1.25)
        if x==-1:
            x=(HEIGHT//12.5)*(howmuch+1.25)
        name=f"boardon{s.index}{angle}"
        prex=WIDTH//2-HEIGHT//2
        window.blit(textures[name],textures[name].get_rect(center=(x+prex,y)))
p=Player(2,0,5)

#BUTTON AND WHAT GOES WITH IT

class Button:
    def __init__(s,type,permanantargs,selfargs,plus):
        s.type=type
        s.permanantargs=permanantargs
        s.permanantargs[0]=s.permanantargs[0]+plus[0]
        s.permanantargs[1]=s.permanantargs[1]+plus[1]
        s.selfargs=selfargs
    def doit(s,functionhash,args):
        returnedargs,s.selfargs=functionhash[s.type](args,s.permanantargs,s.type,s.selfargs)
        return returnedargs
lbuttons=[
    Button("intostartmenu",[WIDTH//2,HEIGHT//1.5],["playmenu"],[0,0]),
    Button("intostartmenu",[WIDTH//2,HEIGHT//1.25],["game"],[0,0]),
    Button("numofplayers",[WIDTH//2,HEIGHT//4],[0],[0,0]),
    
    [
    Button("playerconfig",[WIDTH//5,HEIGHT//2],[0],[0,0]  ),
    Button("playerconfig",[WIDTH//5*2,HEIGHT//2],[0],[0,0]),
    Button("playerconfig",[WIDTH//5*3,HEIGHT//2],[0],[0,0]),
    Button("playerconfig",[WIDTH//5*4,HEIGHT//2],[0],[0,0])
    
    ]

    
]
functionhash={"intostartmenu":startbutton,"numofplayers":doublenumofplayers,"playerconfig":playerconfig}