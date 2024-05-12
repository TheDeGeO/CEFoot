import pygame

#Set up pygame
pygame.init()
clock = pygame.time.Clock()

window_height = 540
window_width = 700

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('CEFoot')

#Colors
grey = (75, 75, 75)

#Create rects with text
def text_block(text, size, coords, bg=grey, fg=(250, 250, 250), margin=20):

    #Set monogram font (free on itch.io by datagoblin)
    monogram = pygame.font.Font("monogram.ttf", size)

    text_sf = monogram.render(text, False, fg)
    text_rect = text_sf.get_rect(center = coords)

    block_sf = pygame.Surface((text_rect.width + margin, text_rect.height + margin))
    block_rect = block_sf.get_rect(center = coords)
    block_sf.fill(bg)

    block_sf.blit(text_sf, (margin//2, margin//2))

    return(block_sf, block_rect)

#Create Buttons
def button(text, size, coords, bg=grey, fg=(250, 250, 250), margin=20):

    block = text_block(text, size, coords, bg, fg, margin)
    block_rect = block[1]
    #Make background darker if cursor and button are colliding
    dark_factor = 0.5
    if block_rect.collidepoint(cursor_cords):
        bg = (bg[0] * dark_factor, bg[1] * dark_factor, bg[2] * dark_factor)
        
    return text_block(text, size, coords, bg, fg, margin)

#Play a song
def play_song(song, volume):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

#Load sounds with volume
def load_sound(sound, volume):
    result = pygame.mixer.Sound("sounds/sfx/" + sound)
    result.set_volume(volume)

    return result

#Load music and sounds
title_bg = "sounds/music/waltz2.mp3"
click_1 = load_sound("button_click1.wav", 0.2)
click_2 = load_sound("button_click2.wav", 0.2)


#Main loop
music = ""
screen_type = "title"
run = True
while run:

    cursor_cords = pygame.mouse.get_pos()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    
    if screen_type == "title":
        if music != title_bg:
            play_song(title_bg, 0.1)
            music = title_bg

        screen.fill(grey)
        #Add title block
        title_block = text_block("CEFoot", 100, (window_width/2, 100))
        screen.blit(title_block[0], title_block[1])

        #Add about button
        about_button = button("About", 30, (window_width/2, 300))
        screen.blit(about_button[0], about_button[1])

        #Add settings button
        settings_button = button("Settings", 30, (window_width/2, 350))
        screen.blit(settings_button[0], settings_button[1])

        if about_button[1].collidepoint(cursor_cords) and event.type == pygame.MOUSEBUTTONDOWN:
            click_1.play()
            screen_type = "about"


    elif screen_type == "about":
        screen.fill(grey)
        #Add title block
        title_block = text_block("About", 100, (window_width/2, 100))
        screen.blit(title_block[0], title_block[1])

        #Add two dev names and ids
        authors_text = text_block("Authors:", 30, (window_width/2 - 250, 200))
        screen.blit(authors_text[0], authors_text[1])

        dev1 = text_block("David Obando", 30, (window_width/2 - 100, 200))
        screen.blit(dev1[0], dev1[1])

        dev2 = text_block("Daniel Vega", 30, (window_width/2 - 100, 230))
        screen.blit(dev2[0], dev2[1])

        dev1_id = text_block("2024157494", 30, (window_width/2 + 100, 200))
        screen.blit(dev1_id[0], dev1_id[1])

        dev2_id = text_block("2024xxxxxx", 30, (window_width/2 + 100, 230))
        screen.blit(dev2_id[0], dev2_id[1])

        #Add academic info
        class_text = text_block("Class: Taller de Programacion", 30, (window_width/2, 300))
        screen.blit(class_text[0], class_text[1])

        major_text = text_block("Major: Ingenieria en Computadores", 30, (window_width/2, 330))
        screen.blit(major_text[0], major_text[1])

        year_text = text_block("Year: 2024", 30, (window_width/2, 360))
        screen.blit(year_text[0], year_text[1])
        
        country_text = text_block("Country: Costa Rica", 30, (window_width/2, 390))
        screen.blit(country_text[0], country_text[1])

        version_text = text_block("Version: 1.0", 30, (window_width/2, 420))
        screen.blit(version_text[0], version_text[1])



        #Add back button
        back_button = button("Back", 30, (50, 50))
        screen.blit(back_button[0], back_button[1])

        if back_button[1].collidepoint(cursor_cords) and event.type == pygame.MOUSEBUTTONDOWN:
            click_2.play()
            screen_type = "title"

    pygame.display.update()
    clock.tick(60)

pygame.quit()
