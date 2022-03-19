import unittest
import sportsBot

class TestBot(unittest.TestCase):
    
    def testSpelling(self):
        self.assertEqual(sportsBot.PosTag("YO"),[])
    

if __name__ == '__main__':
    unittest.main()
