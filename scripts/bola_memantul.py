from vpython import *

#PEMANTULAN BOLA DENGAN GERAK JATUH BEBAS DAN GAYA  GRAVITASI

#membuat objek lantai dan bola
lantai = box(pos=vec(0,-5,0), size=vec(12, 0.5, 12), color=vec(0.8,0.6,0.3))
bola = sphere(pos=vec(0, 12, 0), radius=1, color=color.red)

#Inisialisasi kecepatan awal, waktu, dt, dan percepatan gravitasi
bola.velocity = vec(0,0,0)
t = 0
dt = 0.02
g = -9.8

#Membuat pergerakan bola (memantul)
while (t<30):
    rate(50)
    
    #Update kecepatan arah y dan posisi bola
    bola.velocity.y = bola.velocity.y + g*dt - 0.3 #0.3 dimaksudkan agar ketinggian bola setelah memantul berkurang
    bola.pos = bola.pos + bola.velocity * dt
    
    #Jika bola mencapai lantai, diatur kecepatan berlawanan dengan arah kecepatan sebelum memantul
    if (bola.pos.y <= lantai.pos.y+bola.radius):
        bola.velocity.y = -bola.velocity.y
        
    #Update waktu t
    t += dt