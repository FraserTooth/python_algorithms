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
        self.current_job = None

    def get_job(self, queue):
        try:
            self.current_job = queue.dequeue()
        except IndexError:
            return "No More Jobs in Queue"

    def print_job(self):
        while not self.current_job.check_complete():
            self.current_job.print_page()

        print("Printing Complete")
