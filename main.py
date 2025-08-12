#allows us to use pygame functions
import pygame # pyright: ignore[reportMissingImports]
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    game_time = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    exit = False

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updateable, drawable)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable) 

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    playing_field = AsteroidField()

    while exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            keys = pygame.key.get_pressed()
            if player.timer <= 0 and keys[pygame.K_SPACE]:
                player.shoot()

        screen.fill("black")
        
        for shape in drawable:
            shape.draw(screen)

        pygame.display.flip()
        dt = game_time.tick(60)/1000
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                exit = True
                print("Game Over!")
            for shot in shots:
                if asteroid.collision(shot) == True:
                    asteroid.split()
                    shot.kill()
            

if __name__ == "__main__":
    main()
