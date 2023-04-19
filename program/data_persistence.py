import csv
from character_manager import Character


class CharacterPersistence:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_characters(self):
        characters = []
        with open(self.file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                id = row[0]
                name = row[1]
                race = row[2]
                character_class = row[3]
                level = row[4]
                character = Character(id, name, race, character_class, level)
                characters.append(character)

    def save_characters(self, characters):
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Race", "Class", "Level"])
            for character in characters:
                writer.writerow([character.id, character.name, character.race,
                                character.character_class, character.level])
