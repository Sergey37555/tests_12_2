import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            temp_dict = {}
            for j in cls.all_results[i]:
                temp_dict[j] = str(cls.all_results[i][j])
            print(temp_dict)

    def test_run_1(self):
        tournament1 = Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = tournament1.start()
        self.assertTrue(self.all_results[1][max(self.all_results[1].keys())] == 'Ник')

    def test_run_2(self):
        tournament2 = Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = tournament2.start()
        self.assertTrue(self.all_results[2][max(self.all_results[2].keys())] == 'Ник')

    def test_run_3(self):
        tournament3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[3] = tournament3.start()
        self.assertTrue(self.all_results[3][max(self.all_results[3].keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()