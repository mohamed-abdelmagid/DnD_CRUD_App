from dndresource import Character
from data_persistence import CharacterPersistence

# TODO: Search character, edit character, delete character.
# TODO: Save character after editing the character.


class CharacterManager:
    def __init__(self, file_path):
        self.characters = []
        self.characterpersistence = CharacterPersistence(file_path)
        self.characterpersistence.load_characters()

    def load_characters(self):
        self.characters = self.characterpersistence.load_characters()
        # loads the characters from the CSV file specified by the file_path argument, and stores them in the characters

    def save_characters(self):
        self.characterpersistence.save_characters(self.characters)

    def create_character(self, id, name, race, character_class, level):
        character = Character(id, name, race, character_class, level)
        self.characters.append(character)
        self.save_characters()

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
