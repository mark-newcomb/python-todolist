# Edit list class
from src.main.python.view.view import View


class EditListController:
    def __init__(self, tasklists):
        self.tasklists = tasklists
        self.view = View()

    def run(self):
        if len(self.tasklists.return_tasklists()) == 0:
            self.view.show_message("No tasklists found.")
            return
        else:
            while True:
                self.view.display_items(self.tasklists.return_tasklists())
                response = self.view.get_user_input("Enter task list to edit or \"C\" to cancel.")
                match response:
                    case _ if response.lower() == "c":
                        break
                    case _ if response.isalpha():
                        self.view.show_message("Invalid input entered. Please try again.")
                    case _ if int(response) <= 0 or int(response) > len(self.tasklists.return_tasklists()):
                        self.view.show_message("Invalid input entered. Please try again.")
                    case _:
                        self.display_list_tasks(int(response) - 1)
                        break

    def display_list_tasks(self, list_id):
        while True:
            tasklist = self.tasklists.return_tasklists()[int(list_id)]
            self.view.show_message(f"Editing tasklist {tasklist.get_list_name()}")
            count = 1
            for task in tasklist.get_tasks():
                self.view.show_message(f"{count} - {task}")
                count += 1
            response = self.view.get_user_input("Enter \"A\" to add a new task, \"D\" to delete a task or \"C\" to cancel.")
            match response:
                case _ if response.lower() == "a":
                    new_task = self.view.get_user_input("Write the new task name >>>")
                    self.view.show_message(f"You entered {new_task}")
                    tasklist.add_task(new_task)
                case _ if response.lower() == "d":
                    item_to_delete = int(self.view.get_user_input("Enter item to delete"))
                    tasklist.remove_task(item_to_delete - 1)
                case _ if response.lower() == "c":
                    break