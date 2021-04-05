from vpython import *
#ISLAMUDDIN ALIMURRIJAL
#18509030111018

#BOLA MEMANTUL DALAM KOTAK DENGAN GERAK PARABOLA
scene.center = vec(0,1,-1)


#Inisialisasi panjang dan lebar rusuk, posisi awal tiap silinder (rusuk)
sldr_radius = 0.2
rusuk_panjang = 4
rusuk_pendek = 2
posisi = 2

#Membuat objek silinder sebanyak 12 buah membentuk sebuah kotak
sldr1 = cylinder(pos=vec(-posisi,0,0), axis=vec(1,0,0), size=vec(rusuk_panjang, sldr_radius, sldr_radius), color=color.red)
sldr2 = cylinder(pos=vec(-posisi,posisi,0), axis=vec(1,0,0), size=vec(rusuk_panjang, sldr_radius, sldr_radius), color=color.red)
sldr3 = cylinder(pos=vec(-posisi,0,posisi), axis=vec(1,0,0), size=vec(rusuk_panjang, sldr_radius, sldr_radius), color=color.red)
sldr4 = cylinder(pos=vec(-posisi,posisi,posisi), axis=vec(1,0,0), size=vec(rusuk_panjang, sldr_radius, sldr_radius), color=color.red)

sldr5 = cylinder(pos=vec(-posisi,0,0), axis=vec(0,1,0), size=vec(rusuk_pendek, sldr_radius, sldr_radius), color=color.red)
sldr6 = cylinder(pos=vec(posisi,0,0), axis=vec(0,1,0), size=vec(rusuk_pendek, sldr_radius, sldr_radius), color=color.red)
sldr7 = cylinder(pos=vec(-posisi,0,posisi), axis=vec(0,1,0), size=vec(rusuk_pendek, sldr_radius, sldr_radius), color=color.red)
sldr8 = cylinder(pos=vec(posisi,0,posisi), axis=vec(0,1,0), size=vec(rusuk_pendek, sldr_radius, sldr_radius), color=color.red)

sldr9 = cylinder(pos=vec(-posisi,0,0), axis=vec(0,0,1), size=vec(rusuk_pendek, sldr_radius, sldr_radius), color=color.red)
sldr10 = cylinder(pos=vec(posisi,posisi,0), axis=vec(0,0,1), size=vec(rusuk_pendek, sldr_radius, sldr_radius), color=color.red)
sldr11 = cylinder(pos=vec(posisi,0,0), axis=vec(0,0,1), size=vec(rusuk_pendek, sldr_radius, sldr_radius), color=color.red)
sldr12 = cylinder(pos=vec(-posisi,posisi,0), axis=vec(0,0,1), size=vec(rusuk_pendek, sldr_radius, sldr_radius), color=color.red)

#membuat objek bola
bola = sphere(pos=vec(-1.8,0.2,0.2), radius=0.1, color=color.white)
trail_garis = attach_trail(bola, trail_type='curve', color=color.blue, radius=0.01,  retain=100)
#trail_bola = attach_trail(bola, trail_type='points', color=color.white, opacity=0.3, radius=0.1, pps=1retain=10)


#Inisialisasi nilai fisis, kecepatan awal, sudut, dll
v0 = 5
sudut = 45*pi/180
bola.mass = 1

#Agar pergerakannya berbentuk parabola, diatur kecepatan dengan komponen sudut
bola.velocity = vec(v0*cos(sudut), v0*sin(sudut), v0*sin(0.5*sudut))
#Percepatan gravitasi (dengan arah minus y)
g = vec(0, -9.8, 0)
#Inisalisasi t dan dt
t = 0
dt = 0.01

#Membuat pergerakan bola
while t < 30:
    rate(20)
    
    #Update posisi dan kecepatan bola
    bola.velocity = bola.velocity + g * dt
    bola.pos = bola.pos + (bola.velocity)*dt
    
    #Jika bola mencapai dinding kotak, kecepatannya diupdate (arahnya ditukkar) sehingga mengalami
    #pergerakan berlawanan dengan arah datangnya
    if not (posisi-bola.radius > bola.pos.x > -posisi+bola.radius):
        bola.velocity.x = -bola.velocity.x

    if not (posisi-bola.radius > bola.pos.y > 0+bola.radius):
        bola.velocity.y = -bola.velocity.y
        
    if not (posisi-bola.radius > bola.pos.z > 0+bola.radius):
        bola.velocity.z = -bola.velocity.z
        
    t += dt