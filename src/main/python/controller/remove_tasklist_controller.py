# Remove tasklist controller
from src.main.python.view.view import View


class RemoveListController:
    def __init__(self, tasklists):
        self.view = View()
        self.tasklists = tasklists

    def run(self):
        if len(self.tasklists.return_tasklists()) == 0:
            self.view.show_message("No tasklists found.")
            return
        else:
            while True:
                self.view.display_items(self.tasklists.return_tasklists())
                item_to_remove = self.view.get_user_input("Enter tasklist to remove or \"C\" to cancel: ")
                match item_to_remove:
                    case _ if item_to_remove.lower() == "c":
                        break
                    case _ if item_to_remove.isalpha():
                        self.view.show_message("Invalid input entered. Please try again.")
                    case _ if int(item_to_remove) <= 0 or int(item_to_remove) > len(self.tasklists.return_tasklists()):
                        self.view.show_message("Invalid input entered. Please try again.")
                    case _:
                        self.tasklists.remove_tasklist(int(item_to_remove) - 1)
                        break
