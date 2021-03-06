from snake.game.tiles import rows, columns
from snake.assets import apple_sprite, rect_length
import random

class Apple():
    dist_from_origin = 5.5 + rect_length/2
    def __init__(self, canvas):
        self.canvas = canvas
        self.apple = canvas.create_image((self.dist_from_origin, self.dist_from_origin), image=apple_sprite)
        self.apple_pos = self.rand_apple_pos()

    def rand_apple_pos(self):
        x = random.randint(1, columns)
        y = random.randint(1, rows)
        return self.set_apple_pos(x, y)

    def set_apple_pos(self, x, y):
        self.apple_pos = (x - 1, y - 1)
        apple_x = self.dist_from_origin + self.apple_pos[0]*rect_length
        apple_y = self.dist_from_origin + self.apple_pos[1]*rect_length
        self.canvas.coords(self.apple, (apple_x, apple_y))
        return self.apple_pos

