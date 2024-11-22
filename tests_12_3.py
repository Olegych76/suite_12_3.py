import unittest
from tests_12_1 import Runner
from tests_12_2 import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        self.runner = Runner("Леонардо")
        for _ in range(10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50, 'Дистанция должна быть 50 после 10 прогулок')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        self.runner = Runner("Донателло")
        for _ in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100, 'Дистанция должна быть 100 после 10 пробежек')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        self.runner1 = Runner("Микеланджело")
        self.runner2 = Runner("Рафаэль")
        for _ in range(10):
            self.runner1.walk()
            self.runner2.run()
        self.assertNotEqual(self.runner1.distance, self.runner2.distance, 'Дистанция должна быть разная')


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.p1, self.p2, self.p3 = Runner('Усэйн', 10), Runner('Андрей', 9), Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f'{key}: ''{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_start_one(self):
        t = Tournament(90, self.p1, self.p3)
        result = t.start()
        self.__class__.all_results['Тест 1'] = result
        self.assertTrue(result[max(result.keys())].name == 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_start_two(self):
        t = Tournament(90, self.p2, self.p3)
        result = t.start()
        self.__class__.all_results['Тест 2'] = result
        self.assertTrue(result[max(result.keys())].name == 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_start_three(self):
        t = Tournament(90, self.p1, self.p2, self.p3)
        result = t.start()
        self.__class__.all_results['Тест 3'] = result
        self.assertTrue(result[max(result.keys())].name == 'Ник')


if __name__ == "__main__":
    unittest.main()
