from tiles import *
from spritesheet import Spritesheet
from player import Player
from player import Bola
from palancas import Palanca
################################# Cargar una ventana y un reloj interno #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 1280, 640
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()
TARGET_FPS = 60

################################# Cargar las imagenes y el spritesheet ###################################
spritesheet = Spritesheet('spritesheet.png')
player = Player()

#################################### Cargar el nivel  #######################################

map = TileMap('Niveles/Nivel1-1.csv', spritesheet )

player.position.x, player.position.y = map.start_x, map.start_y
player.bola = Bola(player.position, player.velocity, player)
palanca1 = Palanca(1150, 192, 66, 66)

################################# GAME LOOP ##########################

while running:
    dt = clock.tick(120) * 0.001 * TARGET_FPS
    ################################# Checar el input #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
               player.LEFT_KEY, player.FACING_LEFT = True, True
            elif event.key == pygame.K_d:
                player.RIGHT_KEY, player.FACING_LEFT = True, False
            elif event.key == pygame.K_SPACE:
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.LEFT_KEY = False
            elif event.key == pygame.K_d:
                player.RIGHT_KEY = False
            elif event.key == pygame.K_SPACE:
                if player.is_jumping:
                    player.velocity.y *= .25
                    player.is_jumping = False
        
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        player.bola.lanzarBola = True
        player.bola.throwClick()

    player.bola.throwSec()

    if(player.bola.contadorBola>=100):
        player.bola.ContadorBoolean=False
        player.bola.contadorBola=0
         
    player.bola.lanzarBola = False

    if palanca1.detect_collision(player.bola):
        map = TileMap('Niveles/Nivel1-1CLEAN.csv', spritesheet )
    ################################# Actualizar / Animar Sprites #################################

    if(player.bola.relativoX>player.position.x):
        player.FACING_LEFT = False
    elif(player.bola.relativoX<player.position.x):
        player.FACING_LEFT = True

    player.update(dt, map.tiles)
    player.bola.update(dt, player.position, map.tiles)

    ################################# Actualizar ventana #################################

    canvas.fill((0, 180, 240)) # Llena la ventana de azul
    map.draw_map(canvas)

    player.draw(canvas)
    player.bola.draw(canvas)
    window.blit(canvas, (0,0))
    pygame.display.update()