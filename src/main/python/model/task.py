# Task class

class Task:
    def __init__(self, name):
        self.name = name

    def get_task_name(self):
        return self.name

    def set_task_name(self, name):
        self.name = name