import unittest
import main


class TestMarkov(unittest.TestCase):

    def test_move(self):

        # tie
        try:
            self.assertEqual(main.move('rock', 'rock'), 0)
        except ValueError:
            self.fail('invalid inputs')
        try:
            self.assertEqual(main.move('paper', 'paper'), 0)
        except ValueError:
            self.fail('invalid inputs')
        try:
            self.assertEqual(main.move('scissors', 'scissors'), 0)
        except ValueError:
            self.fail('invalid inputs')

        # 1 beats 2
        try:
            self.assertEqual(main.move('rock', 'scissors'), 1)
        except ValueError:
            self.fail('invalid inputs')
        try:
            self.assertEqual(main.move('scissors', 'paper'), 1)
        except ValueError:
            self.fail('invalid inputs')
        try:
            self.assertEqual(main.move('paper', 'rock'), 1)
        except ValueError:
            self.fail('invalid inputs')

        # 2 beats 1
        try:
            self.assertEqual(main.move('rock', 'paper'), 2)
        except ValueError:
            self.fail('invalid inputs')
        try:
            self.assertEqual(main.move('paper', 'scissors'), 2)
        except ValueError:
            self.fail('invalid inputs')
        try:
            self.assertEqual(main.move('scissors', 'rock'), 2)
        except ValueError:
            self.fail('invalid inputs')

    def test_init_markov(self):
        # main.markov_matrix
        main.init_markov()
        self.assertEqual(main.markov_matrix, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_update_markov(self):
        main.markov_matrix = ['lol']
        try:
            main.update_markov('rock', 'scissors')
            self.fail('didn\'t properly raise exception for illegal matrix')
        except ValueError:
            pass

        main.markov_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # rock
        try:
            main.update_markov('rock', 'rock')
            self.assertEqual(main.markov_matrix, [[1, 0, 0], [0, 0, 0], [0, 0, 0]])
        except ValueError:
            self.fail('raised exception despite matrix being legal')
        main.update_markov('rock', 'paper')
        self.assertEqual(main.markov_matrix, [[1, 1, 0], [0, 0, 0], [0, 0, 0]])
        main.update_markov('rock', 'scissors')
        self.assertEqual(main.markov_matrix, [[1, 1, 1], [0, 0, 0], [0, 0, 0]])

        # paper
        main.update_markov('paper', 'rock')
        self.assertEqual(main.markov_matrix, [[1, 1, 1], [1, 0, 0], [0, 0, 0]])
        main.update_markov('paper', 'paper')
        self.assertEqual(main.markov_matrix, [[1, 1, 1], [1, 1, 0], [0, 0, 0]])
        main.update_markov('paper', 'scissors')
        self.assertEqual(main.markov_matrix, [[1, 1, 1], [1, 1, 1], [0, 0, 0]])

        # scissors
        main.update_markov('scissors', 'rock')
        self.assertEqual(main.markov_matrix, [[1, 1, 1], [1, 1, 1], [1, 0, 0]])
        main.update_markov('scissors', 'paper')
        self.assertEqual(main.markov_matrix, [[1, 1, 1], [1, 1, 1], [1, 1, 0]])
        main.update_markov('scissors', 'scissors')
        self.assertEqual(main.markov_matrix, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    def test_best_markov_move(self):
        main.markov_matrix = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
        self.assertEqual(main.best_markov_move('rock'), 'paper')
        main.markov_matrix = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
        self.assertEqual(main.best_markov_move('paper'), 'rock')
        main.markov_matrix = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
        self.assertEqual(main.best_markov_move('scissors'), 'scissors')
        main.markov_matrix = [[1, 0, 0], [0, 2, 1], [0, 1, 0]]
        self.assertEqual(main.best_markov_move('paper'), 'scissors')

    def test_markov_move(self):
        result = None
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
