import pygame

pygame.init()
gamewindow=pygame.display.set_mode((800,800))
pygame.display.set_caption("GJ Game")
white=(255,255,255)
black=(0,0,0)
blue=(0,255,0)
red=(255,0,0)

#Game Variables----------------------------------------------------------------------------------------
game_exit=True
crash=0
size=30
x=45
y=730
x1=0
y1=760
x2=80
y2=760
velocity=25

clock=pygame.time.Clock()
#Game Variables-----------------------------------------------------------------------------------------

#Gameloop-----------------------------------------------------------------------------------------------
while  game_exit:

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            game_exit = False

         if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_RIGHT:
                 crash=70

             if event.key == pygame.K_LEFT:
                 crash=-70



    if x>=770:
        velocity=-25
    if x<=0 or (x1<=x<=x2 and 730<=y<=y2):
        velocity=25

    x+=velocity
    y-=velocity

    if x1<=0:
        crash =20

    if x2>=800:
        crash=-20

    x1=crash+x1
    x2=crash+x2
    gamewindow.fill(white)

    list1= []
    list2=[]
    for i in range(800):
        if i%32==0:
            for j in range(350):
                if j%32==0:
                    list1.append(i)
                    list2.append(j)

    for p in list1:
        for q in list2:
            pygame.draw.rect(gamewindow,red,(p,q,size,size))
            if abs(x-p)<15 and abs(y-q)<15:
                print("eat")
                pygame.draw.rect(gamewindow,white,(p,q,size,size))
    pygame.draw.rect(gamewindow,blue,(x,y,size,size))
    pygame.draw.line(gamewindow,black,(x1,y1),(x2,y2),10)




    pygame.display.update()
    clock.tick(60)#frames per second
#Gameloop-------------------------------------------------------------------------------------------------

pygame.quit()
quit()
