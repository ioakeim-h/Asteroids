import pygame
import constants
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2) # player in mid of screen
    dt = 0     

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
            
        screen.fill("black")  
        player.draw(screen)
        pygame.display.flip() 

        # Limit framerate to 60 FPS: free up CPU
        dt = clock.tick(60) / 1000 # convert from ms to sec

    
if __name__ == "__main__":
    main()


