class Task:
    ''' A task that can be completed by setting the completed attribute to True. '''
    def __init__(self, task_name, completed, urgency=0.5):
        self.task_name = task_name
        self.completed = completed
        self.urgency = urgency

    def __repr__(self) -> str:
        return f'{self.task_name}: completed: {"Yes" if self.completed else "No"}'


def tasks_by_urgency(all_tasks):
    ''' Implement the body of this function so it returns a list of tasks sorted by urgency.
        Urgency ranges between 0 and 1 (lowest to highest).

        Args:
            all_tasks   | A list of Task objects. 
    '''

    return sorted(all_tasks, key=lambda tsk: tsk.urgency, reverse=True)



import unittest

class TestDevWorkflow(unittest.TestCase):

    def test_sorting(self):

        tasks = [
            ('Feed the cat', True, 1.0),
            ('Learn Python', True, 0.75),
            ('Break gravity', False, 0.25),
            ('Disprove time', False, 0.35),
        ]

        # Enables the comparison in the assertEqual to function.
        Task.__eq__ = lambda self, other: self.urgency >= other.urgency

        actual = [Task(name, completed, urgency) for (name, completed, urgency) in tasks]
        expect = [Task(name, completed, urgency) for (name, completed, urgency) in tasks]
        expect = sorted(expect, key=lambda tsk: tsk.urgency, reverse=True)

        self.assertEqual(tasks_by_urgency(actual), expect)

if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))

