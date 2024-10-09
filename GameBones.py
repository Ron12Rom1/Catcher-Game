import pygame

pygame.init()

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Best Game Ever")

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

running = True
while running:
    running = handle_events()

    screen.fill((255, 255, 255))
    
    
    
    
    
    
    
    
    
    
    pygame.display.update()
pygame.quit()
print("Closing game\n\n")