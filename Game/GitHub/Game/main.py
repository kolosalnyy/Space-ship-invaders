"""
Oto jak działą kod:

1. Tworzymy okno o wymiarach 800x600
2. Tworzymy kwadrat o wymiarach 50x50
3. Ustawiamy pozycje kwadratu na 100x100
4. Tworzymy listę obiektów, które będą przeszkodami
5. Ustawiamy pozycje kamery na 0x0
6. Wczytujemy obrazek mapy
7. Wchodzimy w nieskończoną pętlę
8. Sprawdzamy czy użytkownik chce zamknąć okno
9. Sprawdzamy czy użytkownik nacisnął klawisz
10. Ustawiamy pozycje kwadratu na aktualną pozycję
11. Sprawdzamy czy kwadrat nie koliduje z przeszkodami
12. Ustawiamy pozycję kwadratu na nową pozycję
13. Ustawiamy ograniczenia dla kwadratu
14. Ustawiamy ograniczenia dla kamery
15. Czyścimy okno
16. Rysujemy mapę
17. Rysujemy przeszkody
18. Rysujemy kwadrat
19. Wyświetlamy okno
20. Koniec pętli

"""

import pygame
import sys

pygame.init()

#1
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Window Test")

#2
Square = pygame.Surface((50, 50))
Square.fill((255, 255, 255))

#3
Square_pos_x = 100
Square_pos_y = 100

#4
objects = [
    pygame.Rect(300, 300, 50, 50),
    pygame.Rect(500, 200, 100, 100),
    pygame.Rect(700, 400, 75, 75)
]

#5
camera_x = 0
camera_y = 0

#6
map_image = pygame.image.load('Game/Assets/Images/Player/Player/TestMap.png')
map_width, map_height = map_image.get_size()

#7
while True:
    for event in pygame.event.get():
        #8
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #9
    keys = pygame.key.get_pressed()
    Square_x = Square_pos_x
    Square_y = Square_pos_y

    if keys[pygame.K_a]:
        Square_x -= 1
    if keys[pygame.K_d]:
        Square_x += 1
    if keys[pygame.K_w]:
        Square_y -= 1
    if keys[pygame.K_s]:
        Square_y += 1

    new_rect = pygame.Rect(Square_x, Square_pos_y, 50, 50)
    collision = False
    for obj in objects:
        if new_rect.colliderect(obj):
            collision = True
            break

    if not collision:
        Square_pos_x = Square_x
        Square_pos_y = Square_y

    Square_pos_x = max(0, min(Square_pos_x, map_width - 50))
    Square_pos_y = max(0, min(Square_pos_y, map_height - 50))

    camera_x = max(0, min(Square_pos_x - 400 + 25, map_width - 800))
    camera_y = max(0, min(Square_pos_y - 300 + 25, map_height - 600))

    window.fill((0, 0, 0))

    window.blit(map_image, (-camera_x, -camera_y))

    for obj in objects:
        pygame.draw.rect(window, (255, 0, 0), obj.move(-camera_x, -camera_y))

    window.blit(Square, (Square_pos_x - camera_x, Square_pos_y - camera_y))

    pygame.display.update()

#Nie chciało mi się dalej oznaczać, ale kod działa poprawnie