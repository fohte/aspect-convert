import unittest

from aspect import utils


class TestUtils(unittest.TestCase):

    def test_aspect_ratio(self):
        self.assertEqual(utils.aspect_ratio((1920, 1080)), (16, 9))
        self.assertEqual(utils.aspect_ratio((600, 800)), (3, 4))
        self.assertEqual(utils.aspect_ratio((1000, 1000)), (1, 1))

    def test_convert(self):
        self.assertEqual(
            utils.convert((1920, 1080), (16, 9), trim=True), (1920, 1080))
        self.assertEqual(
            utils.convert((1920, 1080), (4, 3), trim=True), (1440, 1080))
        self.assertEqual(
            utils.convert((1920, 1080), (4, 3), trim=False), (1920, 1440))
        self.assertEqual(
            utils.convert((600, 800), (4, 3), trim=True), (600, 450))
        self.assertEqual(
            utils.convert((600, 800), (4, 3), trim=False), (1066, 800))
        self.assertEqual(
            utils.convert((1920, 1080), (1, 1), trim=True), (1080, 1080))
        self.assertEqual(
            utils.convert((1920, 1080), (1, 1), trim=False), (1920, 1920))
        self.assertEqual(
            utils.convert((1000, 1000), (4, 3), trim=True), (1000, 750))
        self.assertEqual(
            utils.convert((1000, 1000), (4, 3), trim=False), (1333, 1000))
