# Todolist main console app view

class View:
    def get_user_input(self, prompt):
        return input(prompt)

    def show_message(self, message):
        print(message)

    def display_items(self, items):
        count = 1
        for item in items:
            print(f"{count}. {item}")
            count += 1
