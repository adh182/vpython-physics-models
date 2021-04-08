from vpython import *

#GERAK CYCLOTRON SEBUAH BOLA (NON FISIS)

#Membuat objek bola dan trail-nya
bola = sphere(pos=vec(1,0,0), radius=0.2, color=color.white, make_trail=True, retain=1000)
trail = attach_trail(bola, color=color.white, radius=0.18, type='points', pps=5, retain=10, opacity=0.3)

#Inisialisasi waktu dan variabel a dan b
t = 0
dt = 0.01
a = 1       #Variabel a mengatur radius orbit
b = 0.7     #Variabel b mengatur ketinggian orbit

while (t < 50):
    rate(30)
    
    bola.pos.x = cos(a*t)
    bola.pos.y = sin(a*t)
    bola.pos.z = b*t
    
    #Update nilai a dan b, nilai a akan berubah sehingga ukuran orbit juga berubah
    a = a + dt
    t = t + dt
