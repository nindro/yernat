import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    draw_mode = 'line'  # Default drawing mode
    points = []
    colors = ['blue', 'red', 'green', 'yellow', 'purple', 'white']
    color_index = 0
    
    while True:
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                if event.key == pygame.K_q:
                    draw_mode = 'rectangle'
                elif event.key == pygame.K_a:
                    draw_mode = 'circle'
                elif event.key == pygame.K_z:
                    draw_mode = 'eraser'
                elif event.key == pygame.K_s:
                    draw_mode = 'square'
                elif event.key == pygame.K_t:
                    draw_mode = 'right_triangle'
                elif event.key == pygame.K_e:
                    draw_mode = 'equilateral_triangle'
                elif event.key == pygame.K_r:
                    draw_mode = 'rhombus'
                elif event.key == pygame.K_LEFT:
                    color_index = (color_index - 1) % len(colors)
                    mode = colors[color_index]
                elif event.key == pygame.K_RIGHT:
                    color_index = (color_index + 1) % len(colors)
                    mode = colors[color_index]
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append((position, draw_mode, radius, mode))
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        for i in range(len(points)):
            drawElement(screen, points[i])
        
        pygame.display.flip()
        clock.tick(60)

def drawElement(screen, data):
    position, draw_mode, radius, color_mode = data
    
    color_map = {
        'blue': (0, 0, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'yellow': (255, 255, 0),
        'purple': (128, 0, 128),
        'white': (255, 255, 255)
    }
    
    color = color_map.get(color_mode, (255, 255, 255))
    
    if draw_mode == 'line':
        pygame.draw.circle(screen, color, position, radius)
    elif draw_mode == 'rectangle':
        pygame.draw.rect(screen, color, (position[0] - radius, position[1] - radius, radius * 2, radius * 2))
    elif draw_mode == 'circle':
        pygame.draw.circle(screen, color, position, radius)
    elif draw_mode == 'square':
        pygame.draw.rect(screen, color, (position[0] - radius, position[1] - radius, radius * 2, radius * 2))
    elif draw_mode == 'right_triangle':
        pygame.draw.polygon(screen, color, [(position[0], position[1] - radius), (position[0] - radius, position[1] + radius), (position[0] + radius, position[1] + radius)])
    elif draw_mode == 'equilateral_triangle':
        pygame.draw.polygon(screen, color, [(position[0], position[1] - radius), (position[0] - radius, position[1] + radius), (position[0] + radius, position[1] + radius)])
    elif draw_mode == 'rhombus':
        pygame.draw.polygon(screen, color, [(position[0], position[1] - radius), (position[0] + radius, position[1]), (position[0], position[1] + radius), (position[0] - radius, position[1])])
    elif draw_mode == 'eraser':
        pygame.draw.circle(screen, (0, 0, 0), position, radius * 2)

main()
#Square: S
#Right triangle: T
#Equilateral triangle: E
#Rhombus: R