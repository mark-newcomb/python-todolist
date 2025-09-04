# Add tasklist controller
from src.main.python.view.view import View


class AddTasklistController:
    def __init__(self, tasklists):
        self.view = View()
        self.tasklists = tasklists

    def run(self):
        self.tasklists.add_tasklist(self.view.get_user_input("Enter valid tasklist name: "))