import pygame
import random as rand
pygame.init()

class DrawConfigs:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BG_COLOR = WHITE
    
    SIDE_PAD = 100
    TOP_PAD = 150
    
    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(data)
        
    def set_list(self, data):
        self.data = data
        self.min_val = min(data)
        self.max_val = max(data)
        
        self.bar_width = round((self.width - self.SIDE_PAD) / len(data))
        self.bar_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
        

def generate_starting_data(n, min_val, max_val):
    data = []
    
    for _ in range(n):
        val = rand.randint(min_val, max_val)
        data.append(val)
    return data
        

def main():
    run = True
    clock = pygame.time.Clock()
    
    n = 50
    min_val = 0
    max_val = 100
    
    data = generate_starting_data(n, min_val, max_val)
    draw_data = DrawConfigs(800, 600, data)
    
    while run:
        clock.tick(60)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()
    
    
if __name__ == '__main__':
    main()
