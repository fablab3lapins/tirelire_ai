from tkinter import ttk
import cv2
import numpy as np
from picamera import PiCamera
from time import sleep
from tkinter import *
import RPi.GPIO as GPIO
import os

os.popen('sudo python3 ledplus.py')




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

bun = 2

GPIO.setup(bun, GPIO.IN)

a1 = 24
a2 = 25
b1 = 8
b2 = 7
delay = 0.003

GPIO.setup(a1, GPIO.OUT)
GPIO.setup(a2, GPIO.OUT)
GPIO.setup(b1, GPIO.OUT)
GPIO.setup(b2, GPIO.OUT)


un = 0
deux = 0
cinq = 0
dix = 0
vingt = 0
cinquante = 0
cent = 0
deuxcent = 0
somme=0

piece = 0

oun = 0
odeux = 0
ocinq = 0
odix = 0
ovingt = 0
ocinquante = 0
ocent = 0
odeuxcent = 0


he = []
wi = []
per =[]
moyh = 0
moyw = 0
moyp = 0
minh = 0
minw = 0
minp = 0
maxh = 0
maxw = 0
maxp = 0


iun = 0
ideux = 0
icinq = 0
idix = 0
ivingt = 0
icinquante = 0
icent = 0
ideuxcent = 0

aun = 0
adeux = 0
acinq = 0
adix = 0
avingt = 0
acinquante = 0
acent = 0
adeuxcent = 0


pun = 0
pdeux = 0
pcinq = 0
pdix = 0
pvingt = 0
pcinquante = 0
pcent = 0
pdeuxcent = 0


iiun = 0
iideux = 0
iicinq = 0
iidix = 0
iivingt = 0
iicinquante = 0
iicent = 0
iideuxcent = 0

aaun = 0
aadeux = 0
aacinq = 0
aadix = 0
aavingt = 0
aacinquante = 0
aacent = 0
aadeuxcent = 0


ppun = 0
ppdeux = 0
ppcinq = 0
ppdix = 0
ppvingt = 0
ppcinquante = 0
ppcent = 0
ppdeuxcent = 0


with open("peri", "r+") as p:
    peri = p.readlines()
    pun = float(peri[0])
    pdeux = float(peri[1])
    pcinq = float(peri[2])
    pdix = float(peri[3])
    pvingt = float(peri[4])
    pcinquante = float(peri[5])
    pcent = float(peri[6])
    pdeuxcent = float(peri[7])
    p.close()

with open("perimax", "r+") as pm:
    per = pm.readlines()
    ppun = float(per[0])
    ppdeux = float(per[1])
    ppcinq = float(per[2])
    ppdix = float(per[3])
    ppvingt = float(per[4])
    ppcinquante = float(per[5])
    ppcent = float(per[6])
    ppdeuxcent =  float(per[7])
    pm.close()

with open("width", "r+") as w:
    wi = w.readlines()
    iun = float(wi[0])
    ideux = float(wi[1])
    icinq = float(wi[2])
    idix = float(wi[3])
    ivingt = float(wi[4])
    icinquante =float( wi[5])
    icent = float(wi[6])
    ideuxcent = float(wi[7])
    w.close()

with open("widthmax", "r+") as wi:
    wm = wi.readlines()
    iiun = float(wm[0])
    iideux = float(wm[1])
    iicinq = float(wm[2])
    iidix = float(wm[3])
    iivingt = float(wm[4])
    iicinquante = float(wm[5])
    iicent = float(wm[6])
    iideuxcent = float(wm[7])
    wi.close()

with open("virus", "r+") as vr:
    sm = vr.readlines()
    somme = float(sm[0])
    vr.close()

    

def arriere():
    setp(1,0,0,0)
    setp(1,1,0,0)
    setp(0,1,0,0)
    setp(0,1,1,0)
    setp(0,0,1,0)
    setp(0,0,1,1)
    setp(0,0,0,1)
    setp(1,0,0,1)
    
   


def avant():
    setp(1,0,0,1)
    setp(0,0,0,1)
    setp(0,0,1,1)
    setp(0,0,1,0)
    setp(0,1,1,0)
    setp(0,1,0,0)
    setp(1,1,0,0)
    setp(1,0,0,0)
    




def setp(pin1, pin2, pin3, pin4):
    GPIO.output(a1, pin1)
    GPIO.output(a2, pin2)
    GPIO.output(b1, pin3)
    GPIO.output(b2, pin4)
    sleep(delay)

def quartp():
    for i in range(128):
        avant()

def quartm():
    for i in range(128):
        arriere()



def mise():
    i=0
    global bun
    while ( i == 0):
        avant()
        if (GPIO.input(bun) == False):
            i=1
    for i in range(105):
        arriere()
            
        

def edit():
    global minh 
    global minw 
    global minp 
    global maxh 
    global maxw 
    global maxp 


    with open("peri", "w+") as peri:
        for per in minp:
            peri.write(str(per) + "\n")
        peri.close()

    with open("perimax", "w+") as peri:
        for per in maxp:
            peri.write(str(per) + "\n")
        peri.close()

    with open("width", "w+") as width:
        for wi in minw:
            width.write(str(wi) + "\n")
        width.close()

    with open("widthmax", "w+") as width:
        for wi in maxw:
            width.write(str(wi) + "\n")
        width.close()
                
    

def sommes():
    global somme

    with open("virus", "w+") as vr:
        vr.write(str(somme))
        vr.close()
        
        




res=0
et = 0
res1 = 0
tr =0


camera = PiCamera()

def etalon():
    quartm()
    banque= [16.25, 18.75, 21.25, 19.75, 22.25, 24.25, 23.25, 25.75]
    global res
    global et
    global tr
    global somme
    
    res = float(entry.get())
    tr = int(res)
    
    if tr == 1:
        et = banque[0]
    elif tr == 2:
        et = banque[1]
    elif tr==5:
        et = banque[2]
    elif tr == 10:
        et = banque[3]
    elif tr==20:
        et = banque[4]
    elif tr== 50:
        et = banque[5]
    elif tr == 100:
        et = banque[6]
    elif tr==200:
        et = banque[7]
    else:
        truc= Tk()
        tri = Label(truc, text="c'est qui que tu crois douiller là !!!!", font= ("Courrier", 45), fg='red')
        tri.pack()
        tri.mainloop()
        sleep(5)
        pass
    


    global he 
    global wi 
    global per
    global moyh 
    global moyw 
    global moyp 
    global minh 
    global minw 
    global minp 
    global maxh 
    global maxw 
    global maxp 


    global iun 
    global ideux 
    global icinq 
    global idix 
    global ivingt 
    global icinquante 
    global icent 
    global ideuxcent 

    global aun 
    global adeux 
    global adix 
    global avingt 
    global acinquante 
    global acent 
    global adeuxcent 


    global pun 
    global pdeux 
    global pcinq 
    global pdix 
    global pvingt 
    global pcinquante 
    global pcent 
    global pdeuxcent 


    global iiun 
    global iideux 
    global iicinq 
    global iidix 
    global iivingt 
    global iicinquante 
    global iicent 
    global iideuxcent 

    global aaun 
    global aadeux 
    global aacinq 
    global aadix 
    global aavingt 
    global aacinquante 
    global aacent 
    global aadeuxcent 


    global ppun 
    global ppdeux 
    global ppcinq 
    global ppdix 
    global ppvingt 
    global ppcinquante 
    global ppcent 
    global ppdeuxcent 

    he = []
    wi = []
    per =[]
    moyh = 0
    moyw = 0
    moyp = 0
    minh = []
    minw = []
    minp = []
    maxh = []
    maxw = []
    maxp = []


    iun = 0
    ideux = 0
    icinq = 0
    idix = 0
    ivingt = 0
    icinquante = 0
    icent = 0
    ideuxcent = 0

    aun = 0
    adeux = 0
    acinq = 0
    adix = 0
    avingt = 0
    acinquante = 0
    acent = 0
    adeuxcent = 0


    pun = 0
    pdeux = 0
    pcinq = 0
    pdix = 0
    pvingt = 0
    pcinquante = 0
    pcent = 0
    pdeuxcent = 0


    iiun = 0
    iideux = 0
    iicinq = 0
    iidix = 0
    iivingt = 0
    iicinquante = 0
    iicent = 0
    iideuxcent = 0

    aaun = 0
    aadeux = 0
    aacinq = 0
    aadix = 0
    aavingt = 0
    aacinquante = 0
    aacent = 0
    aadeuxcent = 0


    ppun = 0
    ppdeux = 0
    ppcinq = 0
    ppdix = 0
    ppvingt = 0
    ppcinquante = 0
    ppcent = 0
    ppdeuxcent = 0

    etal['value'] = 0
    
    
    for i in range (25):
        camera.resolution = (1024, 768)

        camera.start_preview(fullscreen = False, window= (50, 50, 30, 30))

        

        camera.capture("/home/pi/gdf.jpeg")

        camera.stop_preview()
         
        img = cv2.imread("/home/pi/gdf.jpeg")



        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



        gauss = cv2.GaussianBlur(gray, (5,5), 0)


        canny = cv2.Canny(gauss, 50, 210)


        cont = canny.copy()

        contr, hier = cv2.findContours(cont, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contr:
            area = cv2.contourArea(cnt)
            #print(area)

            
                

            peri = cv2.arcLength(cnt, True) 
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            objcor = len(approx)
            #print(len(approx))
            x,y,w,h = cv2.boundingRect(approx)
            #print(h)
            #print(w)
            ratio = w/float(h)
            if objcor == 8 and 0.95<ratio<1.05 and 750<peri<1400 and 200<h<450 and 200<w<450:
                he.append(h)
                wi.append(h)
                per.append(peri)

               
        etal['value'] += 4

        win.update_idletasks()

    for i in range (0,len(he),1):
        moyh += he[i]
        moyw += wi[i]
        moyp += per[i]

    moyh = moyh/(len(he))
    moyw = moyw/(len(he))
    moyp = moyp/(len(he))

    cofmin = 0.978
    cofmax = 1.022

    for i in banque :
        a =  i / et
        th = a * moyh
        tw = a * moyw
        tp = a * moyp

        thi = th * cofmax
        thm = th * cofmin
        twi = tw * cofmax
        twm = tw * cofmin
        tpi = tp * cofmax
        tpm = tp * cofmin
        
        maxh.append(thi)
        maxw.append(twi)
        maxp.append(tpi)
        minh.append(thm)
        minw.append(twm)
        minp.append(tpm)
    #print(maxh)
    #print("  ")
    #print(minh)
    #print("  ")
    #print(maxp)
    #print("  ")
    #print(minp)
    #print("  ")
    #print(maxw)
    #print("  ")
    #print(minw)

    edit()
    
    ppun = maxp[0]
    ppdeux = maxp[1]
    ppcinq = maxp[2]
    ppdix = maxp[3]
    ppvingt = maxp[4]
    ppcinquante = maxp[5]
    ppcent = maxp[6]
    ppdeuxcent = maxp[7]

    aaun = maxh[0]
    aadeux = maxh[1]
    aacinq = maxh[2]
    aadix = maxh[3]
    aavingt = maxh[4]
    aacinquante = maxh[5]
    aacent = maxh[6]
    aadeuxcent = maxh[7]

    iiun = maxw[0]
    iideux = maxw[1]
    iicinq = maxw[2]
    iidix = maxw[3]
    iivingt = maxw[4]
    iicinquante = maxw[5]
    iicent = maxw[6]
    iideuxcent = maxw[7]

    pun = minp[0]
    pdeux = minp[1]
    pcinq = minp[2]
    pdix = minp[3]
    pvingt = minp[4]
    pcinquante = minp[5]
    pcent = minp[6]
    pdeuxcent = minp[7]

    aun = minh[0]
    adeux = minh[1]
    acinq = minh[2]
    adix = minh[3]
    avingt = minh[4]
    acinquante = minh[5]
    acent = minh[6]
    adeuxcent = minh[7]

    iun = minw[0]
    ideux = minw[1]
    icinq = minw[2]
    idix =minw[3]
    ivingt = minw[4]
    icinquante = minw[5]
    icent = minw[6]
    ideuxcent =minw[7]

    sleep (0.5)
    etal['value'] = 0
    somme = somme + res/100.0
    somme = round(somme, 3)
    win.update_idletasks()
    title3.config(text = somme )
    mise()





def remisezero():
    global un
    global deux
    global cinq
    global dix
    global vingt
    global cinquante
    global cent
    global deuxcent
    global somme
    
    un = 0
    deux = 0
    cinq = 0
    dix = 0
    vingt = 0
    cinquante = 0
    cent = 0
    deuxcent = 0
    somme = 0
    title3.config(text = somme)
    sommes()
    title3.config(text = somme )


def photocap():
    global un
    global deux
    global cinq
    global dix
    global vingt
    global cinquante
    global cent
    global deuxcent
    global somme
    global osomme

    global iun 
    global ideux 
    global icinq 
    global idix 
    global ivingt 
    global icinquante 
    global icent 
    global ideuxcent 

    global aun 
    global adeux 
    global adix 
    global avingt 
    global acinquante 
    global acent 
    global adeuxcent 


    global pun 
    global pdeux 
    global pcinq 
    global pdix 
    global pvingt 
    global pcinquante 
    global pcent 
    global pdeuxcent 


    global iiun 
    global iideux 
    global iicinq 
    global iidix 
    global iivingt 
    global iicinquante 
    global iicent 
    global iideuxcent 

    global aaun 
    global aadeux 
    global aacinq 
    global aadix 
    global aavingt 
    global aacinquante 
    global aacent 
    global aadeuxcent 

    
    global ppun 
    global ppdeux 
    global ppcinq 
    global ppdix 
    global ppvingt 
    global ppcinquante 
    global ppcent 
    global ppdeuxcent

    global oun 
    global odeux 
    global ocinq 
    global odix 
    global ovingt 
    global ocinquante 
    global ocent 
    global odeuxcent 
    global piece
    
    quartp()
    quartp()
    quartm()
    un = 0
    deux = 0
    cinq = 0
    dix = 0
    vingt = 0
    cinquante = 0
    cent = 0
    deuxcent = 0

    osomme = somme
  
    scan[ 'value' ] = 0

    for i in range(5):
        camera.resolution = (1024, 768)

        camera.start_preview(fullscreen = False, window= (50, 50, 300, 300))

       

        camera.capture("/home/pi/gdf.jpeg")

        camera.stop_preview()
         
        img = cv2.imread("/home/pi/gdf.jpeg")



        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



        gauss = cv2.GaussianBlur(gray, (5,5), 0)


        canny = cv2.Canny(gauss, 50, 210)


        cont = canny.copy()

        contr, hier = cv2.findContours(cont, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contr:
            area = cv2.contourArea(cnt)
            #print(area)

            
                

            peri = cv2.arcLength(cnt, True) 
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            objcor = len(approx)
            #print(len(approx))
            x,y,w,h = cv2.boundingRect(approx)
            #print(h)
            #print(w)
            ratio = w/float(h)
            
            #cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2) 
            
            
                
            #cv2.drawContours(img, cnt, -1, (0,0, 255), 1)
                
            if objcor == 8:
                if pun<peri<ppun :
                    un += 1
                    cv2.putText(img,"1ct", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)

                    
                elif pdeux<peri<ppdeux :
                    deux += 1
                    cv2.putText(img,"2cts", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)


                elif pcinq<peri<ppcinq :
                    cinq += 1
                    cv2.putText(img,"5cts", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)

                    
                elif pdix<peri<ppdix :                                    
                    dix += 1
                    cv2.putText(img,"10cts", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)

                    
                elif pvingt<peri<ppvingt :
                    vingt += 1
                    cv2.putText(img,"20cts", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)


                elif pcinquante<peri<ppcinquante :
                    cinquante += 1
                    cv2.putText(img,"50cts", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)


                elif pcent<peri<ppcent :
                    cent += 1
                    cv2.putText(img,"1euro", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)


                elif pdeuxcent<peri<ppdeuxcent :
                    deuxcent += 1
                    cv2.putText(img,"2euro", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)

                                
            else :
                
                if 0.95<ratio<1.05:
                    j = max(w,h)
                    
                    if iun<j<iiun and 0.95<ratio<1.05 :
                        un += 1
                        cv2.putText(img,"1ct", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)
                        
                    if ideux<j<iideux and 0.95<ratio<1.05 :
                        deux += 1
                        cv2.putText(img,"2cts", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)

                    if icinq<j<iicinq and 0.95<ratio<1.05 :
                        cinq += 1
                        cv2.putText(img,"5cts", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)

                    if idix<j<iidix and 0.95<ratio<1.05 :
                        dix += 1
                        cv2.putText(img,"10cts", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)

                    if ivingt<j<iivingt and 0.95<ratio<1.05 :
                        vingt += 1
                        cv2.putText(img,"20cts", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)

                    if icinquante<j<iicinquante and 0.95<ratio<1.05 :
                        cinquante += 1
                        cv2.putText(img,"50cts", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)

                    if icent<j<iicent and 0.95<ratio<1.05 :
                        cent += 1
                        cv2.putText(img,"1euro", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)

                    if ideuxcent<j<iideuxcent and 0.95<ratio<1.05 :
                        deuxcent += 1
                        cv2.putText(img,"2euro", (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),3)
        scan[ 'value' ] += 20
        win.update_idletasks()

        
    jsp = []
    jsp.append(un)
    jsp.append(deux)
    jsp.append(cinq)
    jsp.append(dix)
    jsp.append(vingt)
    jsp.append(cinquante)
    jsp.append(cent)
    jsp.append(deuxcent)
    print(jsp)

    oo = max(un, deux, cinq, dix, vingt, cinquante, cent, deuxcent)

    if oo == un and oo>2 :
        somme = somme + 0.01
        oun +=1
        piece = 0.01


    elif oo == deux and oo>2:
        somme =somme + 0.02
        odeux +=1
        piece = 0.02


    elif oo == cinq and oo>2:
        somme = somme + 0.05
        cinq +=1
        piece = 0.05


    elif oo == dix and oo>2:
        somme = somme + 0.1
        odix +=1
        piece = 0.1


    elif oo == vingt and oo>2:
        somme = somme + 0.2
        ovingt +=1
        piece = 0.2


    elif oo == cinquante and oo>2:
        somme = somme + 0.5
        ocinquante +=1
        piece = 0.5


    elif oo == cent and oo>2:
        somme = somme + 1.0
        ocent +=1
        piece = 1.0


    elif oo ==deuxcent and oo>2:
        somme = somme + 2.0
        odeuxcent +=1
        piece = 2.0

   

    
    somme = round(somme, 3)
    quartp()
    
    
    sleep (0.5)
    scan['value'] = 0
    win.update_idletasks()

    


                        
    #cv2.imshow("origanl", img)

    cv2.waitKey(3)
    sommes()
    
    print(somme)
    title3.config(text = somme )
    title5.config(text = piece )

    if oo>=2 :
        photocap()
    

def alaide():
    res= float(entry.get())
    
    res= res*3
    print(res)
    tr = int(res)
    print(tr)

  
def fenmesrein():
    etal = Tk()
    etal.title("le machin du demon")
    etal.geometry("380x180")
    etal.minsize(380,180)
    etal.config(background='#155F1F')
    
    res = entry.get()
    
    
    print(res)
    etal.mainloop()

    
        


    
                

win = Tk()

win.title("La tirelire magique ")
win.geometry("1220x880")
win.minsize(480, 360)
win.config(background='#FF6EE7')

frame = Frame(win, bg='#FF6EE7')

title1= Label(win, text='Bienvenue dans votre tirelire', font=("Courrier", 30), bg='#FF6EE7')
title1.pack()





title4 = Label(win, text='(+' , font=("Courrier", 18), bg='#FF6EE7')
title4.place(x = 415, y = 500)

title5 = Label(win, text =piece , font=("Courrier", 18), bg='#FF6EE7')
title5.place( x = 455, y = 500)

title6 = Label(win, text =')' , font=("Courrier", 18), bg='#FF6EE7')
title6.place( x = 510, y = 500)

title3  =Label(win, text=somme, font=("Courrier", 20), bg='#FF6EE7')
title3.place(x = 325, y = 500)




#title3.config(text=somme + "(+" + piece + ")")




title2 = Label( win, text= 'Vous avez actuellement :', font=("Courrier", 20), bg='#FF6EE7')
title2.place(x = 250, y = 450)

but1= Button(win, text='scan mes pièces', bg='#FF6EE7', command=photocap)
but1.place(x = 250, y = 400)

but2= Button(win, text='Je veux récuperer mes pièces', bg='#FF6EE7', command=remisezero)
but2.place(x = 385 , y = 400)

fram = Frame(win, bg="#FF6EE7")




tit = Label(win, text="rentrez la valeur de l'étalon en centimes", font= ("Courrier", 12), bg = '#FF6EE7', fg='white')
tit.place(x= 650, y = 400)

entry = Entry(win, width=30)
entry.place(x = 685, y = 430)

but = Button(win, text="étalonnage", bg='#FF6EE7', command=etalon, fg = "white")
but.place( x = 760, y = 460)


ss = Button(win, text="mise a niveau du bras", bg='#FF6EE7', command=mise, fg='white')
ss.place(x= 725, y = 490)


#butt = Button(fram, text="oskour", bg='#155F1F', command=alaide, fg = "white")
#butt.pack()

eta = Label( win, text= 'progression étalonnage', font=("Courrier", 12), bg='#FF6EE7')
eta.place(x = 50, y = 570)


etal = ttk.Progressbar(win, orient=HORIZONTAL, length= 700, mode= 'determinate')
etal.place(x = 50, y = 610)



sac = Label( win, text= 'progression scan', font=("Courrier", 12), bg='#FF6EE7')
sac.place(x = 50, y = 640)

scan = ttk.Progressbar(win, orient=HORIZONTAL, length= 700, mode= 'determinate')
scan.place(x = 50, y = 680)


width =600
height =300
image = PhotoImage(file= "hawk1.png")    #.zoom(1).subsample(1)
zx = int (width / image.width())
zy = int (height / image.height())
back= image.zoom(zx, zy)
canvas = Canvas(win, width = width, height = height, bg = '#FF6EE7', bd = 0, highlightthickness = 0)

canvas.pack()
canvas.create_image(width/2, height/2, image=back)


fram.pack(side = RIGHT)
frame.pack(expand=YES, side=LEFT)
win.mainloop()


