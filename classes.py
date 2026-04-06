from personalfunc import *

class Player:
    def __init__(s,index,pic,money,position,owns):
        s.index=index
        s.money=money
        s.pos=position
        s.pic=pic
        s.owns=owns 
    def draw(s,l_players,turn):
        squished_decreaser=0.8
        s.pos%=40
        x=-1
        y=-1
        angle=0
        koji_po_redu=-1
        ukupno=0
        fixed=None
        for u in range(turn,turn+4):
            ukupno+=1
            koji_po_redu+=1
            i=u%4
            if s.index==i:
                fixed=koji_po_redu
            else:
                if l_players[i].pos!=s.pos:
                    koji_po_redu-=1
                    ukupno-=1
        if fixed!=None:
            koji_po_redu=fixed
        x,y,angle=s.returnnececerydraw()
        name=f"boardon{s.pic}{angle}"
        prex=WIDTH//2-HEIGHT//2
        pomeranje=0
        if ukupno==2:
            pomeranje=(1-2*koji_po_redu)*(WIDTH//67*squished_decreaser)
        elif ukupno==3:
            pomeranje=(1-koji_po_redu)*(WIDTH//67*squished_decreaser)
        elif ukupno==4:
            pomeranje=(2-koji_po_redu)*(WIDTH//67*squished_decreaser)
            if pomeranje<=0:
                pomeranje-=1
        
        if s.pos<10 and s.pos>0 or s.pos>20 and s.pos<30:
            y-=pomeranje
        elif s.pos>=10 and s.pos<20 or s.pos>30 and s.pos<=39:
            x-=pomeranje
        window.blit(textures[name],textures[name].get_rect(center=(x+prex,y)))
    def returnnececerydraw(s):
        x=-1
        y=-1
        offset=HEIGHT//7.692307692307692
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
            y=(HEIGHT//12.19512195121951)*(howmuch-0.5)+offset
        if x==-1:#                                -1 jer treba plus veliko mesto ali +0.5 jer treba centar
            x=(HEIGHT//12.19512195121951)*(howmuch-0.5)+offset
        return x,y,angle
        
L_p=[
    Player(0,1,0,10,[]),
    Player(1,2,0,5 ,[]),
    Player(2,3,0,34,[]),
    Player(3,4,0,25,[]) 
]

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
    Button("playerconfig",[WIDTH//5,  HEIGHT//2],[0],[0,0]),
    Button("playerconfig",[WIDTH//5*2,HEIGHT//2],[0],[0,0]),
    Button("playerconfig",[WIDTH//5*3,HEIGHT//2],[0],[0,0]),
    Button("playerconfig",[WIDTH//5*4,HEIGHT//2],[0],[0,0]) 
    
    ]

    
]
functionhash={"intostartmenu":startbutton,"numofplayers":doublenumofplayers,"playerconfig":playerconfig}