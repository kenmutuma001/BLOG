import unittest
from app.models import Article
import get_headlines
import get_sources_headlines


class TestPopular(unittest.TestCase):

    def setUp(self):

        self.new_quote = Popular("Rome was not build in a day")

    def test_init(self):

        self.assertTrue(self.new_quote.author, "Abraham Lincon")
