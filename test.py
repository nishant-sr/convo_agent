import unittest
import sportsBot


class TestBot(unittest.TestCase):

    # def testSpelling(self):
    #self.assertEqual(sportsBot.PosTag("YO"), [])

    def testPOSPass(self):
        self.assertEqual(sportsBot.PosTag("Basketball"), [
                         ('Basketball', 'NN')])  # this shows passing test

    def testPOSFail(self):
        self.assertNotEqual(sportsBot.PosTag("Basketball"), [
            ('Basketball', 'VB')])  # this test will say pass if the POS Tag is incorrect

    def testNameRecPass(self):
        self.assertTrue(sportsBot.NameErrorRec("Steph Curry"))

    def testNameRecFail(self):
        self.assertFalse(sportsBot.NameErrorRec("How are you?"))

    def testSentimentPositive(self):  # these methods test if the sentiment is positive or negative based on the number from the sentiment method (-ve is sad sentiment, +ve is happy sentiment)
        self.assertTrue(sportsBot.Sentiment("I am happy") > 0)

    def testSentimentNegative(self):
        self.assertTrue(sportsBot.Sentiment("I am sad") < 0)


if __name__ == '__main__':
    unittest.main()
