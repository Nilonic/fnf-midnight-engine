import sys
import platform
try:
    import pygame
    import paths
    import pygame.time
    clock = pygame.time.Clock()
    import psutil
except:
    import os  
    # Get the operating system name
    os_name = platform.system()

    # Check if the operating system is Windows
    if os_name == "Windows" or sys.platform.startswith("win"):
        clear = "cls"
    else:
        clear = "clear"
    os.system(clear)
    modulesToInstall = ["psutil", "pygame"]
    print(f"some modules have to be installed, please wait...")
    for modules in modulesToInstall:
        os.system(f"pip install {modules}")
    print("installed, executing startup")
    try:
        import pygame
        import paths
        import pygame.time
        clock = pygame.time.Clock()
        import psutil
    except:
        print("something went wrong... try installing the following modules manualy:")
        for mod in modulesToInstall:
            print(f"{mod} - missing")
        exit(1)

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Friday Night Funkin // Midnight Engine")

# Load assets
background_image = pygame.image.load(paths.get_background("menuBG1"))  # Replace with your background image
title_font = pygame.font.Font(None, 60)
button_font = pygame.font.Font(None, 40)

# Set up menu options
menu_options = ["Option 1", "Option 2", "Option 3", "Option 4"]
selected_option = 0
menu_scroll_speed = 5  # Adjust this value to control the scrolling speed
menu_item_spacing = 50

# Set up FPS and RAM counter
fps_font = pygame.font.Font(None, 24)
ram_font = pygame.font.Font(None, 24)
counter_padding = 10
counter_box_width = 150
counter_box_height = 60
counter_box_color = (100, 100, 100, 150)
counter_box_pos = (counter_padding, counter_padding)

# Set up clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                print("Selected Option:", menu_options[selected_option])

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the background image
    window.blit(background_image, (0, 0))

    # Draw the title text
    title_text = title_font.render("Friday Night Funkin' // Midnight Engine", True, (255, 255, 255))
    title_x = window_width // 2 - title_text.get_width() // 2
    title_y = window_height // 4 - title_text.get_height() // 2
    window.blit(title_text, (title_x, title_y))

    # Draw the menu options
    for i, option in enumerate(menu_options):
        option_text = button_font.render(option, True, (255, 255, 255))
        option_x = window_width // 2 - option_text.get_width() // 2
        option_y = window_height // 2 - option_text.get_height() // 2 + i * menu_item_spacing
        window.blit(option_text, (option_x, option_y))

    # Draw the selected option indicator
    indicator_text = button_font.render(">", True, (255, 0, 0))
    indicator_x = window_width // 2 - option_text.get_width() // 2 - 50
    indicator_y = window_height // 2 - option_text.get_height() // 2 + selected_option * menu_item_spacing
    window.blit(indicator_text, (indicator_x, indicator_y))

    # Draw the FPS counter
    fps_text = fps_font.render("FPS: {:.2f}".format(clock.get_fps()), True, (255, 255, 255))
    fps_rect = fps_text.get_rect(topleft=(counter_box_pos[0] + counter_padding, counter_box_pos[1] + counter_padding))
    pygame.draw.rect(window, counter_box_color, pygame.Rect(counter_box_pos, (counter_box_width, counter_box_height)), 0)
    window.blit(fps_text, fps_rect)

    # Draw the RAM usage counter
    ram_text = ram_font.render("RAM: {} MB".format(int(psutil.virtual_memory().used / (1024 * 1024))), True, (255, 255, 255))
    ram_rect = ram_text.get_rect(topleft=(counter_box_pos[0] + counter_padding, counter_box_pos[1] + counter_box_height // 2 + counter_padding))
    pygame.draw.rect(window, counter_box_color, pygame.Rect(counter_box_pos, (counter_box_width, counter_box_height)), 0)
    window.blit(ram_text, ram_rect)

    # Update the display
    pygame.display.flip()

    # Delay for consistent frame rate
    clock.tick(60)