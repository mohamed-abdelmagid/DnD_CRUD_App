# will manage the DnD character list
from dndresource import Character
# TODO: Make it so it calls the data_persistence module to save a character after creating


class CharacterManager:
    def __init__(self):
        self.characters = []

    def create_character(self, id, name, race, character_class, level):
        character = Character(id, name, race, character_class, level)
        self.characters.append(character)

    def search_character(self, searchname, searchrace):
        # will search for character based on the DnD character's name or race
        pass

    def edit_character(self, id, new_name, new_race, new_character_class, new_level):
        # looking at the code now, I need an ID for the characters
        # this will edit a character to change name, race, class, or level
        pass

    def delete_character(self, id):
        # will delete character by ID
        pass
