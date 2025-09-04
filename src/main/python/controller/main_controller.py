# Console App main controller
from src.main.python.controller.add_tasklist_controller import AddTasklistController
from src.main.python.controller.edit_tasklist_controller import EditListController
from src.main.python.controller.remove_tasklist_controller import RemoveListController
from src.main.python.model.tasklist_db import TasklistDB
from src.main.python.model.tasklists import Tasklists
from src.main.python.view.view import View


class MainController:
    def __init__(self):
        self.view = View()
        self.model = Tasklists()
        self.add_list = AddTasklistController(self.model)
        self.remove_list = RemoveListController(self.model)
        self.edit_list = EditListController(self.model)
        self.db = TasklistDB()

    def run(self):
        self.db.test_db()
        while True:
            self.view.show_message("Python Todolist:")
            self.view.show_message("A - Add New Tasklist")
            self.view.show_message("D - Delete Tasklist")
            self.view.show_message("E - Edit Tasklist")
            self.view.show_message("V - View Tasklists")
            self.view.show_message("Q - Quit")
            response = self.view.get_user_input(">>> ")

            match response.lower():
                case "a":
                    self.add_list.run()
                case "d":
                    self.remove_list.run()
                case "e":
                    self.edit_list.run()
                case "v":
                    self.view.show_message("Current Tasklists:")
                    self.view.display_items(self.model.return_tasklists())
                case "q":
                    self.view.show_message("Exiting...")
                    break
                case _:
                    self.view.show_message("Invalid response")
