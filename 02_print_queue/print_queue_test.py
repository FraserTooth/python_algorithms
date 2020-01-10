import unittest
from print_queue import Job, Printer, PrintQueue


class TestJob(unittest.TestCase):
    def test_setup(self):
        j = Job(5)
        self.assertEqual(j.pages, 5)

    def test_print_page(self):
        j = Job(2)
        self.assertEqual(j.pages, 2)
        j.print_page()
        self.assertEqual(j.pages, 1)
        j.print_page()
        self.assertEqual(j.pages, 0)
        j.print_page()
        self.assertEqual(j.pages, 0)

    def test_check_complete(self):
        j = Job(1)
        self.assertEqual(j.check_complete(), False)
        j.print_page()
        self.assertEqual(j.check_complete(), True)


class TestPrinter(unittest.TestCase):
    def test_setup(self):
        printer = Printer()
        self.assertEqual(printer.current_job, None)

    def test_get_job(self):
        q = PrintQueue()
        job1 = Job(1)
        job2 = Job(2)
        p = Printer()
        # Doing it
        q.enqueue(job1)
        q.enqueue(job2)
        self.assertEqual(q.items, [job2, job1])
        p.get_job(q)
        self.assertEqual(p.current_job, job1)
        self.assertEqual(q.items, [job2])

    def test_print_job(self):
        q = PrintQueue()
        job1 = Job(5)
        job2 = Job(2)
        p = Printer()
        # Doing it
        q.enqueue(job1)
        q.enqueue(job2)
        p.get_job(q)
        self.assertEqual(p.current_job.pages, 5)
        self.assertEqual(p.current_job.check_complete(), False)
        p.print_job()
        self.assertEqual(p.current_job.pages, 0)
        self.assertEqual(p.current_job.check_complete(), True)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
