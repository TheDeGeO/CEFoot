import contextlib
with contextlib.redirect_stdout(None):
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

def img_load(file_name, sub_folder, size):
    path = "imgs/" + sub_folder + "/" + file_name
    result = pygame.image.load(path)
    result = pygame.transform.scale(result, size)
    return result

def img_block(img, size, coords, bg=grey, margin=20):
    img = pygame.transform.scale(img, size)
    img_rect = img.get_rect()

    block_sf = pygame.Surface((img_rect.width + margin, img_rect.height + margin))
    block_rect = block_sf.get_rect(center = coords)

    block_sf.fill(bg)
    block_sf.blit(img, (margin//2, margin//2))

    return (block_sf, block_rect)

#Load music and sounds
title_bg = "sounds/music/waltz2.mp3"
click_1 = load_sound("button_click1.wav", 0.2)
click_2 = load_sound("button_click2.wav", 0.2)

#Load imgs
barca_img = img_load("barca.png", "teams", (200, 200))
madrid_img = img_load("madrid.png", "teams", (200, 200))
milan_img = img_load("milan.png", "teams", (200, 200))

bale_img = img_load("bale.png", "players", (200, 200))
benzema_img = img_load("benzema.png", "players", (200, 200))
casillas_img = img_load("casillas.png", "players", (200, 200))
claudio_img = img_load("claudio.png", "players", (200, 200))
curtois_img = img_load("curtois.png", "players", (200, 200))
dida_img = img_load("dida.png", "players", (200, 200))
inzaghi_img = img_load("inzaghi.png", "players", (200, 200))
kaka_img = img_load("kaka.png", "players", (200, 200))
maignan_img = img_load("maignan.png", "players", (200, 200))
messi_img = img_load("messi.png", "players", (200, 200))
navas_img = img_load("navas.png", "players", (200, 200))
neymar_img = img_load("neymar.png", "players", (200, 200))
ronaldo_img = img_load("ronaldo.png", "players", (200, 200))
rossi_img = img_load("rossi.png", "players", (200, 200))
suarez_img = img_load("suarez.png", "players", (200, 200))
terstegen_img = img_load("terstegen.png", "players", (200, 200))
victor_img = img_load("victor.png", "players", (200, 200))
zlatan_img = img_load("zlatan.png", "players", (200, 200))

class Team:
    def __init__(self, name, img, shooters, goalkeepers):
        self.name = name
        self.img = img
        self.shooters = shooters
        self.goalkeepers = goalkeepers

class Player:
    def __init__(self, name, img):
        self.name = name
        self.img = img
    
#Add players
bale = Player("Bale", bale_img)
benzema = Player("Benzema", benzema_img)
casillas = Player("Casillas", casillas_img)
claudio = Player("Claudio", claudio_img)
curtois = Player("Curtois", curtois_img)
dida = Player("Dida", dida_img)
inzaghi = Player("Inzaghi", inzaghi_img)
kaka = Player("Kaka", kaka_img)
maignan = Player("Maignan", maignan_img)
messi = Player("Messi", messi_img)
navas = Player("Navas", navas_img)
neymar = Player("Neymar", neymar_img)
ronaldo = Player("Ronaldo", ronaldo_img)
rossi = Player("Rossi", rossi_img)
suarez = Player("Suarez", suarez_img)
terstegen = Player("Terstegen", terstegen_img)
victor = Player("Victor", victor_img)
zlatan = Player("Zlatan", zlatan_img)

#Add teams
barca = Team("Barcelona", barca_img, [bale, benzema, casillas], [kaka, neymar, ronaldo])
madrid = Team("Madrid", madrid_img, [dida, inzaghi, messi], [maignan, navas, terstegen])
milan = Team("Milan", milan_img, [curtois, kaka, ronaldo], [rossi, suarez, zlatan])

teams = [barca, madrid, milan]

click_cooldown = 500
last_click_time = 0

potentiometer = 0
potentiometer_range = 65535
potentiometer_range_divider = potentiometer_range - potentiometer_range/5

#Main loop
music = ""
screen_type = "title"
run = True
while run:

    #Get current time
    current_time = pygame.time.get_ticks()

    #Get key presses
    key = pygame.key.get_pressed()

    #(Temporal) simulate potetiometer 0 to 65000
    if key[pygame.K_SPACE]:
        if current_time - last_click_time < click_cooldown:
            pass
        else:
            potentiometer += potentiometer_range//3 - 1
            if potentiometer > potentiometer_range:
                potentiometer = 0
            
            potentiometer_value = int((potentiometer/potentiometer_range_divider) * 2)
            print(potentiometer_value)
            last_click_time = current_time

    #Get potentiometer value
    

    #Get cursor position
    cursor_cords = pygame.mouse.get_pos()

    #Get events
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

        #Add Play button
        play_button = button("Play", 30, (window_width/2, 400))
        screen.blit(play_button[0], play_button[1])

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_time - last_click_time < click_cooldown:
                pass
            elif about_button[1].collidepoint(cursor_cords):
                click_1.play()
                screen_type = "about"
                last_click_time = current_time
            elif settings_button[1].collidepoint(cursor_cords):
                click_1.play()
                #screen_type = "settings"
                last_click_time = current_time
            elif play_button[1].collidepoint(cursor_cords):
                click_1.play()
                screen_type = "pre-game"
                choosing_team = "goalkeepers"
                goalkeepers_index = 0
                goalkeepers = teams[goalkeepers_index]
                shooters_index = 1
                shooters = teams[shooters_index]
                last_click_time = current_time
        


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

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_time - last_click_time < click_cooldown:
                pass
            elif back_button[1].collidepoint(cursor_cords):
                click_2.play()
                screen_type = "title"
                last_click_time = current_time
    
    #Pre-game screen
    elif screen_type == "pre-game":
        screen.fill(grey)
        #Choose team text
        choose_team_text = text_block("Choose team:", 50, (window_width/2, 50))
        screen.blit(choose_team_text[0], choose_team_text[1])

        if choosing_team == "goalkeepers":
            choosing_text = text_block("Choosing Goalkeepers", 30, (window_width/2, 100))
        elif choosing_team == "shooters":
            choosing_text = text_block("Choosing Shooters", 30, (window_width/2, 100))
        screen.blit(choosing_text[0], choosing_text[1])

        #Team icons
        #Goalkeepers
        goalkeepers_icon = img_block(goalkeepers.img, (200, 200), (window_width/2 - 200, window_height/2))
        screen.blit(goalkeepers_icon[0], goalkeepers_icon[1])

        #Shooters
        shooters_icon = img_block(shooters.img, (200, 200), (window_width/2 + 200, window_height/2))
        screen.blit(shooters_icon[0], shooters_icon[1])

        #Add select button
        select_button = button("Select", 30, (window_width/2, window_height - 50))
        screen.blit(select_button[0], select_button[1])

        #Add back button
        back_button = button("Back", 30, (50, 50))
        screen.blit(back_button[0], back_button[1])

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_time - last_click_time < click_cooldown:
                pass
            elif select_button[1].collidepoint(cursor_cords):
                click_1.play()
                if choosing_team == "goalkeepers":
                    choosing_team = "shooters"
                elif choosing_team == "shooters":
                    screen_type = "players"
                    shooter_index = 0
                    shooter = shooters.shooters[shooter_index]
                    goalkeeper_index = 0
                    goalkeeper = goalkeepers.goalkeepers[goalkeeper_index]
                last_click_time = current_time
            elif back_button[1].collidepoint(cursor_cords):
                click_1.play()
                screen_type = "title"
                last_click_time = current_time

        if choosing_team == "goalkeepers":
            goalkeepers = teams[potentiometer_value]
        elif choosing_team == "shooters":
            shooters = teams[potentiometer_value]
            
    
    elif screen_type == "players":
        screen.fill(grey)



    pygame.display.update()
    clock.tick(60)

pygame.quit()
