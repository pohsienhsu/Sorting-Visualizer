import pygame
import random as rand
import math
pygame.init()

from sorting import bubble_sort, insertion_sort

class DrawConfigs:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    BG_COLOR = WHITE
    
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    
    FONT = pygame.font.SysFont('comicsans', 20)
    LARGE_FONT = pygame.font.SysFont('comicsans', 30)
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
        self.bar_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
        

def draw(draw_data, sorting_algo_name, ascending):
    draw_data.window.fill(draw_data.BG_COLOR)
    
    title = draw_data.LARGE_FONT.render(f"{sorting_algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_data.BLUE)
    draw_data.window.blit(title, (draw_data.width//2-title.get_width()//2, 5))
    
    controls = draw_data.FONT.render("R - Reset | SPACE - Start | A - Ascending | D - Descending", 1, draw_data.BLACK)
    draw_data.window.blit(controls, (draw_data.width//2-controls.get_width()//2, 45))
    
    sorting = draw_data.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_data.BLACK)
    draw_data.window.blit(sorting, (draw_data.width//2-sorting.get_width()//2, 75))
    
    draw_bars(draw_data)
    pygame.display.update()
    
    
def draw_bars(draw_data, color_positions={}, clear_bg=False):
    data = draw_data.data
    
    if clear_bg:
        clear_rect = (draw_data.SIDE_PAD//2, draw_data.TOP_PAD, draw_data.width - draw_data.SIDE_PAD, draw_data.height - draw_data.TOP_PAD)
        pygame.draw.rect(draw_data.window, draw_data.BG_COLOR, clear_rect)
    
    for i, val in enumerate(data):
        x = draw_data.start_x + i * draw_data.bar_width
        y = draw_data.height - ((val - draw_data.min_val) * draw_data.bar_height)
        color = draw_data.GRADIENTS[i % 3]
        
        if i in color_positions:
            color = color_positions[i]
        
        pygame.draw.rect(draw_data.window, color, (x, y, draw_data.bar_width, draw_data.height))

    if clear_bg:
        pygame.display.update()


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
    
    sorting = False
    ascending = True
    
    sorting_algo = bubble_sort
    sorting_algo_name = 'Bubble Sort'
    sorting_algo_generator = None
    
    while run:
        clock.tick(80)
        
        if sorting:
            try:
                next(sorting_algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_data, sorting_algo_name, ascending)   
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r:
                data = generate_starting_data(n, min_val, max_val)
                draw_data.set_list(data)
                sorting = False
                            
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algo_generator = sorting_algo(draw_data, ascending, draw_bars)
                
            elif event.key == pygame.K_a and not sorting and not ascending:
                ascending = True
                
            elif event.key == pygame.K_d and not sorting and ascending:
                ascending = False
            
            elif event.key == pygame.K_i and not sorting:
                sorting_algo = insertion_sort
                sorting_algo_name = "Insertion Sort"
                
            elif event.key == pygame.K_b and not sorting:
                sorting_algo = bubble_sort
                sorting_algo_name = "Bubble Sort"
                
    pygame.quit()
    
    
if __name__ == '__main__':
    main()
