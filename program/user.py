from character_manager import CharacterManager


class UI:
    def __init__(self):
        self.character_manager = CharacterManager()

    def run(self):
        while True:
            print("\nMENU")
            print("1. Create Character")
            print("2. Search Character")
            print("3. Edit Character")
            print("4. Delete Character")
            print("5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                id = input("Enter ID: ")
                name = input("Enter name: ")
                race = input("Enter race: ")
                character_class = input("Enter class: ")
                level = input("Enter level: ")
                self.character_manager.create_character(
                    id, name, race, character_class, level)
            elif choice == "2":
                searchname = input("Enter name for search: ")
                searchrace = input("Enter race for searchr: ")
                searched_characters = self.character_manager.search_character(
                    searchname, searchrace)
                for character in searched_characters:
                    print("ID:", character.id)
                    print("Name:", character.name)
                    print("Race:", character.race)
                    print("Class:", character.character_class)
                    print("Level:", character.level)
            elif choice == "3":
                id = input("Enter ID of character: ")
                new_name = input("Enter new name: ")
                new_race = input("Enter new race: ")
                new_character_class = input("Enter new class: ")
                new_level = input("Enter new level: ")
                self.character_manager.edit_character(
                    id, new_name, new_race, new_character_class, new_level)
            elif choice == "4":
                id = input("Enter ID of character: ")
                confirmation = input(
                    "Are you sure you want to delete this character?(y/n): ").lower()
                if confirmation == ("y" or "yes"):
                    self.character_manager.delete_character(id)
                elif confirmation == ("n" or "no"):
                    print("Character has not been deleted.")
            elif choice == "5":
                break
            else:
                print(f"Incorrect Input: No option with input {choice}")


prog = UI()
prog.run()
