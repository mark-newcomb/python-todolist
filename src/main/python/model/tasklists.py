# Tasklists class
from src.main.python.model.tasklist import Tasklist


class Tasklists:
    def __init__(self):
        self.tasklists = []

    def add_tasklist(self, tasklist_name):
        new_list = Tasklist(tasklist_name)
        self.tasklists.append(new_list)

    def remove_tasklist(self, tasklist_number):
        self.tasklists.pop(tasklist_number)

    def return_tasklists(self):
        return self.tasklists