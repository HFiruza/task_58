import unittest
import Runner
import runner_and_tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        jump = Runner.Runner('бегать')
        for _ in range(10):
            jump.walk()
        self.assertEqual(jump.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        to_go = Runner.Runner('ходить')
        for _ in range(10):
            to_go.run()
        self.assertEqual(to_go.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        jump_2 = Runner.Runner('бежим')
        to_go_2 = Runner.Runner('ходим')
        for _ in range(10):
            jump_2.walk()
            to_go_2.run()
        self.assertNotEqual(to_go_2.distance, jump_2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.setup_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.setup_2 = runner_and_tournament.Runner('Андрей', 9)
        self.setup_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        self.tnm_1 = runner_and_tournament.Tournament(90, self.setup_1, self.setup_3)
        self.all_results = self.tnm_1.start()
        last_result = max(self.all_results)
        self.assertTrue(last_result != 'Ник')
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        self.tnm_2 = runner_and_tournament.Tournament(90, self.setup_2, self.setup_3)
        self.all_results = self.tnm_2.start()
        last_result = max(self.all_results)
        self.assertTrue(last_result != 'Ник')
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        self.tnm_3 = runner_and_tournament.Tournament(90, self.setup_1, self.setup_2,
                                                      self.setup_3)
        self.all_results = self.tnm_3.start()
        last_result = max(self.all_results)
        self.assertTrue(last_result != 'Ник')
        TournamentTest.all_results[3] = self.all_results

if __name__ == '__main__':
    unittest.main()