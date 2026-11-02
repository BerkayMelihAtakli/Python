"""
game_engine.py - Arcade-engine voor Sprint 6 (v1, ATTRIBUUT-gebaseerd). NIET AANPASSEN.

Jij schrijft de classes; deze engine opent het venster, draait de game-loop,
leest de ATTRIBUTEN van jouw objecten en tekent ze als rechthoeken. Jouw classes
zijn dus pure data; de engine verzorgt alle beweging en het tekenwerk.

--------------------------------------------------------------------------
HET CONTRACT - wat de engine van jouw objecten verwacht:

  player  - een object met:
      x, y      (int)    positie van de linkerbovenhoek
      width     (int)    breedte in pixels
      height    (int)    hoogte in pixels
      color     (tuple)  RGB, bijvoorbeeld (0, 200, 255)
      speed     (int)    pixels die de speler per toetsstap opschuift
      health    (int)    OPTIONEEL - levens; bij 0 stopt het spel

  enemies - een LIJST objecten, elk met:
      x, y, width, height, color   (zoals hierboven)
      speed     (int)    pixels die deze enemy per frame ZAKT

  world   - OPTIONEEL (US4 + project) - een object met:
      player, enemies, bullets, score, width, height

  bullet_factory(player) -> bullet   - OPTIONEEL, een gewone functie die een
      nieuw bullet-object teruggeeft met: x, y, width, height, color, speed
      (speed = pixels die de kogel per frame OMHOOG gaat)

  y telt naar BENEDEN: y groter = lager op het scherm. Vijanden vallen dus met
  een POSITIEVE speed; kogels gaan omhoog. Kleuren zijn RGB-tuples, geen strings.
--------------------------------------------------------------------------
"""

import random
import pygame


def _overlap(a, b):
    """True als twee rechthoeken (objecten met x/y/width/height) elkaar raken."""
    return (a.x < b.x + b.width and a.x + a.width > b.x and
            a.y < b.y + b.height and a.y + a.height > b.y)


def run_game(player, enemies, width=480, height=640, fps=60,
             world=None, bullet_factory=None):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sprint 6 - Arcade Dodge")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    bullets = getattr(world, "bullets", []) if world is not None else []

    running = True
    while running:
        # 1) Vensterknop / afsluiten en schieten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if bullet_factory is not None:
                    bullets.append(bullet_factory(player))

        # 2) Toetsen lezen -> speler-attribuut aanpassen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player.speed
        if keys[pygame.K_RIGHT]:
            player.x += player.speed
        player.x = max(0, min(player.x, width - player.width))

        # 3) Vijanden laten vallen; onderaan -> herspawnen bovenaan
        for enemy in enemies:
            enemy.y += enemy.speed
            if enemy.y > height:
                enemy.y = -enemy.height
                enemy.x = random.randint(0, width - enemy.width)
                if world is not None:
                    world.score += 1

        # 4) Kogels omhoog; buiten beeld -> weg
        for bullet in bullets:
            bullet.y -= bullet.speed
        bullets[:] = [b for b in bullets if b.y + b.height > 0]

        # 5) Botsing - kogel raakt vijand
        for bullet in bullets:
            for enemy in enemies:
                if _overlap(bullet, enemy):
                    enemy.y = -enemy.height
                    enemy.x = random.randint(0, width - enemy.width)
                    bullet.y = -100
                    if world is not None:
                        world.score += 5

        # 6) Botsing - vijand raakt speler
        for enemy in enemies:
            if _overlap(player, enemy):
                enemy.y = -enemy.height
                enemy.x = random.randint(0, width - enemy.width)
                if hasattr(player, "health"):
                    player.health -= 1
                    if player.health <= 0:
                        running = False

        # 7) Tekenen (alles als rechthoek, op basis van attributen)
        screen.fill((15, 15, 22))
        pygame.draw.rect(screen, player.color,
                         (player.x, player.y, player.width, player.height))
        for enemy in enemies:
            pygame.draw.rect(screen, enemy.color,
                             (enemy.x, enemy.y, enemy.width, enemy.height))
        for bullet in bullets:
            pygame.draw.rect(screen, bullet.color,
                             (bullet.x, bullet.y, bullet.width, bullet.height))

        score = getattr(world, "score", 0) if world is not None else 0
        hp = getattr(player, "health", None)
        text = f"Score: {score}" + (f"    HP: {hp}" if hp is not None else "")
        screen.blit(font.render(text, True, (240, 240, 240)), (10, 10))

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


def run_world(world, bullet_factory=None):
    """Voor US4 + project: geef je hele Game/World-object mee."""
    run_game(world.player, world.enemies,
             width=world.width, height=world.height,
             world=world, bullet_factory=bullet_factory)