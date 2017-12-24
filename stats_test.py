import unittest
import stats

DATA = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]


class Test(unittest.TestCase):

    def test_mean(self):
        self.assertEquals(stats.mean([10]), 10)
        self.assertEquals(stats.mean([10, 30]), 20)
        self.assertEquals(stats.mean([10, 30, 50]), 30)
        self.assertEquals(stats.mean(DATA), 477.75)

    # @unittest.skip
    def test_median(self):
        self.assertEquals(stats.median([10]), 10)
        self.assertEquals(stats.median([10, 30]), 20)
        self.assertEquals(stats.median([10, 40, 50]), 40)
        self.assertEquals(stats.median([50, 10, 40]), 40)
        self.assertEquals(stats.median(DATA), 500)

    def test_mode(self):
        self.assertEqual(stats.mode([10]), 10)
        self.assertEqual(stats.mode([10, 20, 30, 40, 20]), 20)

