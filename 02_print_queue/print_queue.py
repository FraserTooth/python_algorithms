from queue import Queue as PrintQueue


class Job:
    def __init__(self, pages):
        self.pages = pages

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        return self.pages == 0


class Printer:
    def __init__(self):
        self.queue = PrintQueue()

    def get_job(self):
        pass

    def print_job(self):
        pass

