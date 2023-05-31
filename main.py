def display_message_box(title, error_code, message):
    box_width = 400
    box_height = 300
    box_x = (window_width - box_width) // 2
    box_y = (window_height - box_height) // 2

    pygame.draw.rect(window, (255, 255, 255), (box_x, box_y, box_width, box_height))
    pygame.draw.rect(window, (0, 0, 0), (box_x, box_y, box_width, box_height), 3)

    font_title = pygame.font.Font(None, 36)
    text_title = font_title.render(title, True, (0, 0, 0))
    text_rect_title = text_title.get_rect(center=(box_x + box_width // 2, box_y + 40))
    window.blit(text_title, text_rect_title)

    font_error = pygame.font.Font(None, 24)
    text_error = font_error.render(f"Error Code: {error_code}", True, (0, 0, 0))
    text_rect_error = text_error.get_rect(center=(box_x + box_width // 2, box_y + 80))
    window.blit(text_error, text_rect_error)

    font_message = pygame.font.Font(None, 28)
    lines = message.split("\n")
    line_height = 30
    for i, line in enumerate(lines):
        text_message = font_message.render(line, True, (0, 0, 0))
        text_rect_message = text_message.get_rect(center=(box_x + box_width // 2, box_y + 140 + i * line_height))
        window.blit(text_message, text_rect_message)

    ok_button_rect = pygame.Rect(box_x + box_width - 260, box_y + box_height - 60, 120, 40)
    pygame.draw.rect(window, (200, 200, 200), ok_button_rect)
    font_button = pygame.font.Font(None, 24)
    text_ok = font_button.render("OK", True, (0, 0, 0))
    text_rect_ok = text_ok.get_rect(center=ok_button_rect.center)
    window.blit(text_ok, text_rect_ok)

    pygame.display.flip()  # Update the display
    clock.tick(60)

    return ok_button_rect

def wait_for_button_press(ok_button_rect):
    button_pressed = False

    while not button_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ok_button_rect.collidepoint(event.pos):
                    button_pressed = True
            pygame.display.flip()
            clock.tick(60)

import sys
import platform
try:
    import pygame
    import paths
    import pygame.time
    clock = pygame.time.Clock()
    import psutil
    import env
    import settings
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
        import env
        import settings
    except:
        print("something went wrong... try installing the following modules manualy:")
        for mod in modulesToInstall:
            print(f"{mod} - missing or requirements missing")
        exit(1)

print(f"{env.engine_name} V{env.engine_version} starting up...")
print(f"using {env.ui_name} V{env.ui_version}")
#init settings
settings.check_and_init()

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(env.engine_name)

# Load assets
background_image = pygame.image.load(paths.get_background("menuBG1"))  # Replace with your background image
title_font = pygame.font.Font(None, 60)
button_font = pygame.font.Font(None, 40)

# Set up menu options
menu_options = ["Story Mode", "Freeplay", "Options", "Exit"]
selected_option = 0
menu_scroll_speed = 5  # Adjust this value to control the scrolling speed
menu_item_spacing = 50

# Set up FPS and RAM counter
spec = pygame.font.Font(None, 24)
counter_padding = 10
counter_box_width = 150
counter_box_height = 70
counter_box_color = (100, 100, 100, 255)
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
            elif event.key == pygame.K_BACKQUOTE:
                    box_rect = display_message_box("test of message box error stuff", 0, "there is no error\nits just a test")  # Display the message box and get its rectangle
                    wait_for_button_press(box_rect)  # Wait for button press
            elif event.key == pygame.K_RETURN:
                if(menu_options[selected_option] == "Exit"):
                    sys.exit(0)
                if(menu_options[selected_option] == "Options"):
                    print("TODO: add option stuff")
                else:
                    print("Selected Option:", menu_options[selected_option])

                

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the background image
    window.blit(background_image, (0, 0))

    # Draw the title text
    title_text = title_font.render(env.engine_name, True, (102, 155, 102))
    title_x = window_width // 2 - title_text.get_width() // 2
    title_y = window_height // 4 - title_text.get_height() // 2
    window.blit(title_text, (title_x, title_y))

    # Draw the menu options
    for i, option in enumerate(menu_options):
        option_text = button_font.render(option, True, (102, 155, 102))
        option_x = window_width // 2 - option_text.get_width() // 2
        option_y = window_height // 2 - option_text.get_height() // 2 + i * menu_item_spacing
        window.blit(option_text, (option_x, option_y))

    # Draw the selected option indicator
    indicator_text = button_font.render(">", True, (255, 0, 0))
    indicator_x = window_width // 2 - option_text.get_width() // 2 - 50
    indicator_y = window_height // 2 - option_text.get_height() // 2 + selected_option * menu_item_spacing
    window.blit(indicator_text, (indicator_x - 30, indicator_y - 3))


    #why does this work, re-using already activated values somehow doesn't break
    #surely it should either crash or only display one value
    #but each draw and update at the same time
    #unintentional optimisation?

    # Draw the RAM usage counter
    ram_text = spec.render("RAM: {} MB".format(int(psutil.virtual_memory().used / (1024 * 1024))), True, (255, 255, 255))
    ram_rect = ram_text.get_rect(topleft=(counter_box_pos[0] + counter_padding, counter_box_pos[1] + counter_padding))
    pygame.draw.rect(window, counter_box_color, pygame.Rect(counter_box_pos, (counter_box_width, counter_box_height)), 0)
    window.blit(ram_text, ram_rect)

    # Draw the CPU usage counter
    cpu_text = spec.render("CPU: {} %".format(float(psutil.cpu_percent())), True, (255, 255, 255))
    ram_rect = ram_text.get_rect(topleft=(counter_box_pos[0] + counter_padding, counter_box_pos[1] + counter_box_height // 2 + counter_padding))
    window.blit(cpu_text, ram_rect)

    # Draw the FPS counter
    fps_text = spec.render("FPS: {:.2f} ".format(clock.get_fps()), True, (255, 255, 255))
    ram_rect = ram_text.get_rect(topleft=(counter_box_pos[0] + counter_padding, counter_box_pos[1] + counter_box_height // 4 + counter_padding))
    window.blit(fps_text, ram_rect)



    # Update the display
    pygame.display.flip()

    if(settings.read_settings("fps") < 10):
        settings.update_settings("fps", 30)
        box_rect = display_message_box("Settings Error", 1, f"your FPS setting it set to {settings.read_settings('fps')}\nminimum is 10\nwe've set it to 30 for you")  # Display the message box and get its rectangle
        wait_for_button_press(box_rect)  # Wait for button press
    # Delay for consistent frame rate
    clock.tick(settings.read_settings("fps"))

