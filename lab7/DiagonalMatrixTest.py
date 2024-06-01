import unittest
from DiagonalMatrix import DiagonalMatrix


class TestDiagonalMatrix(unittest.TestCase):

    def setUp(self):
        self.matrix = DiagonalMatrix(7, 7)

    def test_set_word_and_get_word(self):
        self.matrix.set_word([1, 0, 1], 0, 0)
        self.assertEqual(self.matrix.get_word(0, 0, 3), [1, 0, 1])

    def test_set_index_colum_and_get_index_column(self):
        self.matrix.set_index_colum([1, 0, 1], 0, 0)
        self.assertEqual(self.matrix.get_index_column(0, 0, 3), [1, 0, 1])

    def test_logical_or(self):
        self.matrix.set_word([1, 0, 1, 0], 0, 0)
        self.matrix.set_word([0, 1, 0, 1], 1, 1)
        self.assertEqual(self.matrix.logical_or(0, 1), [1, 1, 1, 1, 0, 0, 0])

    def test_logical_or_not(self):
        self.matrix.set_word([1, 0, 1, 0], 0, 0)
        self.matrix.set_word([0, 1, 0, 1], 1, 1)
        self.assertEqual(self.matrix.logical_or_not(0, 1), [0, 0, 0, 0, 1, 1, 1])

    def test_logical_not_and(self):
        self.matrix.set_word([1, 1, 1, 0], 0, 0)
        self.matrix.set_word([0, 1, 0, 1], 1, 1)
        self.assertEqual(self.matrix.logical_not_and(0, 1), [1, 0, 1, 0, 0, 0, 0])

    def test_implication(self):
        self.matrix.set_word([1, 0, 1, 0], 0, 0)
        self.matrix.set_word([0, 1, 0, 1], 1, 1)
        self.assertEqual(self.matrix.implication(0, 1), [0, 1, 0, 1, 1, 1, 1])

    def test_add_binary(self):
        self.assertEqual(self.matrix.add_binary([1, 1, 0], [1, 0, 1]), [1, 0, 1, 1])

    def test_sum_fields(self):
        self.matrix.set_word([1, 1, 1, 1, 0, 0], 0, 0)
        self.matrix.set_word([1, 0, 1, 0, 1, 0], 1, 1)
        self.matrix.sum_fields([1, 1])
        self.assertEqual(self.matrix.get_word(0, 0, 6), [1, 1, 1, 1, 1, 0])
        self.assertEqual(self.matrix.get_word(1, 1, 6), [1, 0, 1, 0, 1, 0])

    def test_find_words_in_range(self):
        self.matrix.set_word([1, 1, 1, 1, 0, 0], 0, 0)
        self.matrix.set_word([1, 0, 1, 0, 1, 0], 1, 1)
        self.assertEqual(self.matrix.find_words_in_range([1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]),
                         [True, True, True, True, True, True, True])


if __name__ == '__main__':
    unittest.main()
