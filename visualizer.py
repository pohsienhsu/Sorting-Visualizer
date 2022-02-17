import pygame
import random as rand
pygame.init()

class DrawConfigs:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BG_COLOR = WHITE
    
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    
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
        

def draw(draw_data):
    draw_data.window.fill(draw_data.BG_COLOR)
    draw_bars(draw_data)
    pygame.display.update()
    
def draw_bars(draw_data):
    data = draw_data.data
    
    for i, val in enumerate(data):
        x = draw_data.start_x + i * draw_data.bar_width
        y = draw_data.height - ((val - draw_data.min_val) * draw_data.bar_height)
        color = draw_data.GRADIENTS[i % 3]
        
        pygame.draw.rect(draw_data.window, color, (x, y, draw_data.bar_width, draw_data.height))


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
        
        draw(draw_data)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r:
                data = generate_starting_data(n, min_val, max_val)
                draw_data.set_list(data)
                
    pygame.quit()
    
    
if __name__ == '__main__':
    main()
