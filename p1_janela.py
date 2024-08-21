import pygame
import sys


pygame.init()


largura = 800
altura = 600


cor_circulo = (0, 255, 0)   
cor_fundo = (0, 0, 0)      


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Círculo segue o cursor do mouse')


raio_circulo = 30


while True:
   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    x_mouse, y_mouse = pygame.mouse.get_pos()

    
    tela.fill(cor_fundo)
    pygame.draw.circle(tela, cor_circulo, (x_mouse, y_mouse), raio_circulo)
    pygame.display.flip()

   
    pygame.time.Clock().tick(30)