from dndresource import Character
from data_persistence import CharacterPersistence

# TODO: Delete character.


class CharacterManager:
    def __init__(self, file_path):
        self.characters = []
        self.characterpersistence = CharacterPersistence(file_path)
        self.characterpersistence.load_characters()

    def load_characters(self):
        self.characters = self.characterpersistence.load_characters()

    def save_characters(self):
        self.characterpersistence.save_characters(self.characters)

    def create_character(self, id, name, race, character_class, level):
        character = Character(id, name, race, character_class, level)
        self.characters.append(character)
        self.save_characters()

    def search_character(self, searchname, searchrace):
        searched_characters = []
        for character in self.characters:
            if character.name == searchname and character.race == searchrace:
                searched_characters.append(character)
        return searched_characters

    def edit_character(self, id, new_name, new_race, new_character_class, new_level):
        for character in self.characters:
            if character.id == id:
                character.name = new_name
                character.race = new_race
                character.character_class = new_character_class
                character.level = new_level
                self.save_characters()

    def delete_character(self, id):
        for character in self.characters:
            if character.id == id:
                self.characters.remove(character)
                self.save_characters()
