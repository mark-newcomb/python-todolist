# Tasklist class

class Tasklist:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.pop(task)

    def get_tasks(self):
        return self.tasks

    def get_list_name(self):
        return self.name

    def __str__(self):
        return self.name