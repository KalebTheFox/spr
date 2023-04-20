import pygame


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True
        self.spaceship = Spaceship(self, 370, 515)

        self.background_img = pygame.image.load("spr_space_himmel.png")

        while self.running:
            self.clock.tick(60)

            self.screen.fill((60, 15, 30))
            self.screen.blit(self.background_img, (0, 0))
            self.spaceship.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(-10)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(10)
                    if event.key == pygame.K_SPACE:
                        self.spaceship.fire_bullet()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(10)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(-10)

            self.spaceship.update()
            if len(self.spaceship.bullets) > 0:
                for bullets in self.spaceship.bullets:
                    if bullet.is_fired == True
                        bullet.update()



            pygame.display.update()


class Spaceship:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.change_x = 0
        self.change_y = 0
        self.game = game
        self.spaceship_img = pygame.image.load("spr_spaceship.png")
        self.bullets = []

    def fire_bullet(self):
        self.bullets.append(Bullet(self.game, self.x, self.y))
        self.bullets[len(self.bullets) - 1].fire()

    def move(self, speed):
        self.change_x += speed

    def update(self):
        self.x += self.change_x
        if self.x < 0:
            self.x = 0
        elif self.x > 736:
            self.x = 736
        self.game.screen.blit(self.spaceship_img, (self.x, self.y))


class Bullet:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.is_fired = False
        self.bullet_speed = 10
        self.bullet_img = pygame.image.load("spr_patrone.png")

    def fire(self):
        self.is_fired = True

    def update(self):
        self.game.screen.blit(self.bullet_img, (self.x, self.y))

if __name__ == "__main__":
    game = Game(800, 600)
