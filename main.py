from pokemon import Pokemon
import random
import requests
import pygame
import json
import io

# 1 - 1010 pokemon

# create the nine images from the URL
# save them in a list of Images

#code works for 1, but 2 types do not work

pygame.init()
pygame.font.init()
main_font = pygame.font.Font("PressStart2P-Regular.ttf", 40)
info_font = pygame.font.Font("PressStart2P-Regular.ttf", 24)
text_font = pygame.font.Font("PressStart2P-Regular.ttf", 16)
input_font = pygame.font.SysFont("Arial", 20)
FPS = 20
clock = pygame.time.Clock()

icon = pygame.image.load("pokeball.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("PykeDex!")

start_screen = pygame.image.load("start_screen.png")
main_screen = pygame.image.load("main_screen.png")

reset_button = pygame.image.load("reset_button.png")
reset_button_rect = reset_button.get_rect()
reset_button_coords = (810, 13)
reset_button_rect.x = reset_button_coords[0]
reset_button_rect.y = reset_button_coords[1]

home_button = pygame.image.load("home_button.png")
home_button_rect = home_button.get_rect()
home_button_coords = (800, 13)
home_button_rect.x = home_button_coords[0]
home_button_rect.y = home_button_coords[1]

search_unhighlighted = pygame.image.load("search_unhighlighted.png")
search_highlighted = pygame.image.load("search_highlighted.png")
search_button = search_unhighlighted
search_button_rect = search_button.get_rect()
search_button_coords = (140, 17)
search_button_rect.x = search_button_coords[0]
search_button_rect.y = search_button_coords[1]
text = ""

# pokemon types and images setup
bug_type = pygame.image.load("bug.png")
bug_type_rect = bug_type.get_rect()
dark_type = pygame.image.load("dark.png")
dark_type_rect = dark_type.get_rect()
dragon_type = pygame.image.load("dragon.png")
dragon_type_rect = dragon_type.get_rect()
electric_type = pygame.image.load("electric.png")
electric_type_rect = electric_type.get_rect()
fairy_type = pygame.image.load("fairy.png")
fairy_type_rect = fairy_type.get_rect()
fighting_type = pygame.image.load("fight.png")
fighting_type_rect = fighting_type.get_rect()
fire_type = pygame.image.load("fire.png")
fire_type_rect = fire_type.get_rect()
flying_type = pygame.image.load("flying.png")
flying_type_rect = flying_type.get_rect()
ghost_type = pygame.image.load("ghost.png")
ghost_type_rect = ghost_type.get_rect()
grass_type = pygame.image.load("grass.png")
grass_type_rect = grass_type.get_rect()
ground_type = pygame.image.load("ground.png")
ground_type_rect = ground_type.get_rect()
ice_type = pygame.image.load("ice.png")
ice_type_rect = ice_type.get_rect()
normal_type = pygame.image.load("normal.png")
normal_type_rect = normal_type.get_rect()
poison_type = pygame.image.load("poison.png")
poison_type_rect = poison_type.get_rect()
psychic_type = pygame.image.load("psychic.png")
psychic_type_rect = psychic_type.get_rect()
rock_type = pygame.image.load("rock.png")
rock_type_rect = rock_type.get_rect()
steel_type = pygame.image.load("steel.png")
steel_type_rect = steel_type.get_rect()
water_type = pygame.image.load("water.png")
water_type_rect = water_type.get_rect()
type_1 = ""
type_1_rect = ""
type_2 = ""
type_2_rect = ""

screen_height = start_screen.get_height()
screen_width = start_screen.get_width()
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

Quit = False

while True:
    clock.tick(FPS)
    show_start_screen = True
    show_main_screen = False
    home_active = False
    reset_active = False
    search_active = False
    generate_random = True
    chosen = ""
    pokemon_IDs = []
    pokemons = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    object_names = []
    positions = [[170, 75], [450, 75], [740, 75], [170, 290], [450, 290], [740, 290], [170, 500], [450, 500], [740, 500]]

    while show_start_screen:
        reset_active = True
        search_active = True
        home_active = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_start_screen = False
                show_main_screen = False
                Quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                mouse_position = (mouse_x, mouse_y)
                for pokemon in pokemons:
                    if pokemon.rect.collidepoint(mouse_position):
                        chosen = pokemon
                        chosen.chosen(216, 287, 480, 329)
                        show_start_screen = False
                        show_main_screen = True
                if reset_button_rect.collidepoint(mouse_position) and reset_active:
                    generate_random = True
                if search_button_rect.collidepoint(mouse_position) and search_active:
                    search_button = search_highlighted
                else:
                    search_button = search_unhighlighted
            if event.type == pygame.KEYDOWN:
                if search_button == search_highlighted:
                    if event.key == pygame.K_RETURN:
                        chosen = Pokemon(1, 1, text.lower())
                        chosen.chosen(216, 287, 480, 329)
                        text = ""
                        show_start_screen = False
                        show_main_screen = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        if generate_random:
            pokemon_IDs = random.sample(range(1, 1010), 9)  # 9 random unique numbers
            for i in range(9):
                generate_number = "pokemon_" + str(i+1)
                object_names.append(generate_number)
            for i in range(9):  # make 8 pokemon objects
                ID = pokemon_IDs[i]
                pokemon = Pokemon(positions[i][0], positions[i][1], ID)
                pokemons[i] = pokemon
                # pokemons.append(pokemon)
            generate_random = False

        display_text = input_font.render(text, True, "black")
        screen.blit(start_screen, (0, 0))
        screen.blit(reset_button, reset_button_rect)
        screen.blit(search_button, search_button_rect)
        screen.blit(display_text, (search_button_rect.x + 45, search_button_rect.y + 8))
        for i in range(9):
            screen.blit(pokemons[i].image, pokemons[i].rect)
        pygame.display.update()

    while show_main_screen:
        reset_active = False
        search_active = False
        home_active = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_start_screen = False
                show_main_screen = False
                Quit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                mouse_position = (mouse_x, mouse_y)
                if home_button_rect.collidepoint(mouse_position) and home_active:
                    show_start_screen = True
                    show_main_screen = False

        pokemon_name = chosen.name.upper()
        pokemon_weight = round((chosen.weight * .1), 5) # meters
        pokemon_height = round((chosen.height * .1), 5) # kilograms
        pokemon_types = chosen.tipes
        pokemon_generation = chosen.generation
        pokemon_baby = chosen.is_baby
        pokemon_mythical = chosen.is_mythical
        pokemon_legendary = chosen.is_legendary

        if len(pokemon_types) == 1 or len(pokemon_types) == 2:
            if pokemon_types[0] == 'bug':
                type_1 = bug_type
                type_1_rect = bug_type_rect
            if pokemon_types[0] == 'dark':
                type_1 = dark_type
                type_1_rect = dark_type_rect
            if pokemon_types[0] == 'dragon':
                type_1 = dragon_type
                type_1_rect = dragon_type_rect
            if pokemon_types[0] == 'electric':
                type_1 = electric_type
                type_1_rect = electric_type_rect
            if pokemon_types[0] == 'fairy':
                type_1 = fairy_type
                type_1_rect = fairy_type_rect
            if pokemon_types[0] == 'fighting':
                type_1 = fighting_type
                type_1_rect = fighting_type_rect
            if pokemon_types[0] == 'fire':
                type_1 = fire_type
                type_1_rect = fire_type_rect
            if pokemon_types[0] == 'flying':
                type_1 = flying_type
                type_1_rect = flying_type_rect
            if pokemon_types[0] == 'ghost':
                type_1 = ghost_type
                type_1_rect = ghost_type_rect
            if pokemon_types[0] == 'grass':
                type_1 = grass_type
                type_1_rect = grass_type_rect
            if pokemon_types[0] == 'ground':
                type_1 = ground_type
                type_1_rect = ground_type_rect
            if pokemon_types[0] == 'ice':
                type_1 = ice_type
                type_1_rect = ice_type_rect
            if pokemon_types[0] == 'normal':
                type_1 = normal_type
                type_1_rect = normal_type_rect
            if pokemon_types[0] == 'poison':
                type_1 = poison_type
                type_1_rect = poison_type_rect
            if pokemon_types[0] == 'psychic':
                type_1 = psychic_type
                type_1_rect = psychic_type_rect
            if pokemon_types[0] == 'rock':
                type_1 = rock_type
                type_1_rect = rock_type_rect
            if pokemon_types[0] == 'steel':
                type_1 = steel_type
                type_1_rect = steel_type_rect
            if pokemon_types[0] == 'water':
                type_1 = water_type
                type_1_rect = water_type_rect
            type_1_size = type_1.get_size()
            type_1_scale = (type_1_size[0] * .52, type_1_size[1] * .52)
            type_1 = pygame.transform.scale(type_1, type_1_scale)
            type_1_rect = type_1.get_rect()
            type_1_rect.x = 557
            type_1_rect.y = 251
        if len(pokemon_types) == 2:
            if pokemon_types[1] == 'bug':
                type_2 = bug_type
                type_2_rect = bug_type_rect
            if pokemon_types[1] == 'dark':
                type_2 = dark_type
                type_2_rect = dark_type_rect
            if pokemon_types[1] == 'dragon':
                type_2 = dragon_type
                type_2_rect = dragon_type_rect
            if pokemon_types[1] == 'electric':
                type_2 = electric_type
                type_2_rect = electric_type_rect
            if pokemon_types[1] == 'fairy':
                type_2 = fairy_type
                type_2_rect = fairy_type_rect
            if pokemon_types[1] == 'fighting':
                type_2 = fighting_type
                type_2_rect = fighting_type_rect
            if pokemon_types[1] == 'fire':
                type_2 = fire_type
                type_2_rect = fire_type_rect
            if pokemon_types[1] == 'flying':
                type_2 = flying_type
                type_2_rect = flying_type_rect
            if pokemon_types[1] == 'ghost':
                type_2 = ghost_type
                type_2_rect = ghost_type_rect
            if pokemon_types[1] == 'grass':
                type_2 = grass_type
                type_2_rect = grass_type_rect
            if pokemon_types[1] == 'ground':
                type_2 = ground_type
                type_2_rect = ground_type_rect
            if pokemon_types[1] == 'ice':
                type_2 = ice_type
                type_2_rect = ice_type_rect
            if pokemon_types[1] == 'normal':
                type_2 = normal_type
                type_2_rect = normal_type_rect
            if pokemon_types[1] == 'poison':
                type_2 = poison_type
                type_2_rect = poison_type_rect
            if pokemon_types[1] == 'psychic':
                type_2 = psychic_type
                type_2_rect = psychic_type_rect
            if pokemon_types[1] == 'rock':
                type_2 = rock_type
                type_2_rect = rock_type_rect
            if pokemon_types[1] == 'steel':
                type_2 = steel_type
                type_2_rect = steel_type_rect
            if pokemon_types[1] == 'water':
                type_2 = water_type
                type_2_rect = water_type_rect
            type_2_size = type_2.get_size()
            type_2_scale = (type_2_size[0] * .52, type_2_size[1] * .52)
            type_2 = pygame.transform.scale(type_2, type_2_scale)
            type_2_rect = type_2.get_rect()
            type_2_rect.x = 747
            type_2_rect.y = 251

        display_name = main_font.render(pokemon_name, True, "black")
        display_weight = info_font.render(str(pokemon_weight), True, "black")
        display_height = info_font.render(str(pokemon_height), True, "black")
        if pokemon_baby:
            display_info = text_font.render(pokemon_name + " is a baby pokemon introduced in ", True, "black")
        elif pokemon_mythical:
            display_info = text_font.render(pokemon_name + " is a mythical pokemon introduced in ", True, "black")
        elif pokemon_legendary:
            display_info = text_font.render(pokemon_name + " is a legendary pokemon introduced in ", True, "black")
        else:
            display_info = text_font.render(pokemon_name + " is a pokemon introduced in ", True, "black")
        display_info2 = text_font.render(pokemon_generation + ". On average, it weighs ", True, "black")
        display_info3 = text_font.render(str(pokemon_weight) + " kilograms and has a height of " + str(pokemon_height) + " meters.", True, "black")

        screen.blit(main_screen, (0, 0))
        screen.blit(home_button, home_button_rect)
        screen.blit(display_name, (415, 165))
        screen.blit(display_weight, (657, 381))
        screen.blit(display_height, (657, 440))
        screen.blit(display_info, (101, 514))
        screen.blit(display_info2, (101, 542))
        screen.blit(display_info3, (101, 570))
        screen.blit(type_1, type_1_rect)
        if len(pokemon_types) == 2:
            screen.blit(type_2, type_2_rect)
        screen.blit(chosen.image, chosen.rect)
        screen.blit(chosen.back_image, chosen.back_rect)
        pygame.display.update()

    if Quit:
        break
