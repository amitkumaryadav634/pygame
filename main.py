import pgzrun # pip install pgzero
WIDTH=800
HEIGHT=600
change_x=2
change_y=2
golden_egg=Actor('golden_egg', pos=(100,100))
def draw():
    # clear the screen
    screen.clear()
    #screen.fill((125,138,251))
    screen.blit(image='farm' , pos=(0,0))

    golden_egg.draw()
def on_mouse_down(pos):
    if golden_egg.collidepoint(pos):
        golden_egg.image = 'broken-golden'
        music.play_once('egg_cracking')
        music.set_volume(1)


def on_mouse_up():
    golden_egg.image='golden_egg'
    #music.pause()
def update():
    global change_x, change_y
    if golden_egg.right>=WIDTH or golden_egg.left<=0:
        change_x= change_x* (-1)
    if golden_egg.bottom >=HEIGHT or golden_egg.top<=0:
        change_y= change_y* (-1)

    golden_egg.left+= change_x
    golden_egg.bottom+= change_y

#music.play('egg_cracking')
pgzrun.go( )