import pygame
import io
import requests
import json


class Pokemon:
    def __init__(self, x, y, ID):
        self.x = x
        self.y = y
        self.ID = str(ID)
        self.tipes = []
        self.url = "https://pokeapi.co/api/v2/pokemon/" + self.ID + "/"
        response = requests.get(self.url)
        json_dict = json.loads(response.text)
        self.name = json_dict["name"]
        self.sprite = json_dict["sprites"]["front_default"]
        self.back_sprite = json_dict["sprites"]["back_default"]
        self.back_image = ""
        self.back_image_size = ""
        self.back_data = ""
        self.back_rect = ""
        species = json_dict["types"]
        for specie in species:
            tipe = specie["type"]["name"]
            self.tipes.append(tipe)

        self.image_data = requests.get(self.sprite)
        image_load = io.BytesIO(self.image_data.content)
        self.image = pygame.image.load(image_load)
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

        self.weight = json_dict["weight"]
        self.height = json_dict["height"]
        self.is_baby = ""
        self.is_legendary = ""
        self.is_mythical = ""
        self.generation = ""
    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 2, self.image_size[1] * 2)
        self.image = pygame.transform.scale(self.image, scale_size)

    def scale_down(self):
        self.back_image_size = self.back_image.get_size()
        back_scale_size = (self.back_image_size[0] * 1.5, self.back_image_size[1] * 1.5)
        self.back_image = pygame.transform.scale(self.back_image, back_scale_size)

    def chosen(self, new_x, new_y, back_x, back_y):
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.rect.center = (new_x, new_y)

        self.back_data = requests.get(self.back_sprite)
        back_image_load = io.BytesIO(self.back_data.content)
        self.back_image = pygame.image.load(back_image_load)
        self.scale_down()
        self.back_image_size = self.back_image.get_size()
        self.back_rect = pygame.Rect(self.x, self.y, self.back_image_size[0], self.back_image_size[1])
        self.back_rect.center = (back_x, back_y)
        url2 = "https://pokeapi.co/api/v2/pokemon-species/" + self.ID + "/"
        response2 = requests.get(url2)
        json_dict2 = json.loads(response2.text)
        self.is_baby = json_dict2["is_baby"]
        self.is_legendary = json_dict2["is_legendary"]
        self.is_mythical = json_dict2["is_mythical"]
        self.generation = json_dict2["generation"]["name"]
