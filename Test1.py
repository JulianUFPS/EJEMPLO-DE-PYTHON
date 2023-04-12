import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar la ventana
ventana = pygame.display.set_mode((1200, 650))
pygame.display.set_caption("Mi Juego")

# Cargar la imagen del personaje
mi_imagen = pygame.image.load("Imagenes/pinguino.png")
# Redimensionar la imagen a 130x169 píxeles
mi_imagen = pygame.transform.scale(mi_imagen, (86, 112))
rectangulo1 = mi_imagen.get_rect()
rectangulo1.x = 400
rectangulo1.y = 100

# Crear un suelo
suelo = pygame.Rect(-200, 550, 1500, 200)

#Gravedad
velocidad_y = 6

# LIMITAR VELOCIDAD A 60 FPS
reloj = pygame.time.Clock()

volteado=False
colisionopiso=False
subir=False

contador=0
# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    #GRAVEDAD
    rectangulo1.y += velocidad_y
    if rectangulo1.colliderect(suelo):
        # Restablecer la velocidad vertical a cero
        velocidad_y = 0
        # Asegurarse de que el pingüino esté en la posición correcta en el suelo
        rectangulo1.y = suelo.y - rectangulo1.height
        colisionopiso=True
    else:
        velocidad_y=6
        colisionopiso=False

     # SALTO
    if teclas[pygame.K_UP] and colisionopiso:
        # Modificar la velocidad vertical para simular un salto
        subir=True
        contador=0

    if subir==True and contador<25 and teclas[pygame.K_UP]:
        velocidad_y-=11.5
        
    contador+=1   
    
    # Dibujar el fondo
    ventana.fill((255, 255, 255))

    # Dibujar el suelo
    pygame.draw.rect(ventana, (142, 255, 255), suelo)

    # Mover al personaje hacia la izquierda o la derecha
    if teclas[pygame.K_LEFT]:
        rectangulo1.x -= 5
        volteado=True
    if teclas[pygame.K_RIGHT]:
        rectangulo1.x += 5
        volteado=False
    
    #Dibujar al pingüino dependiendo de si está mirando hacia la izquierda o hacia la derecha
    if volteado:
        mi_imagen_flipped = pygame.transform.flip(mi_imagen, True, False)
        ventana.blit(mi_imagen_flipped, rectangulo1)
    else:
        ventana.blit(mi_imagen, rectangulo1)
    
    # Actualizar la pantalla
    pygame.display.update()
    #LIMITAR VELOCIDAD A 120 FPS
    reloj.tick(120)