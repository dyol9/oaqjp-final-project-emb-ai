import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_joy_statement(self):
        text = "I am happy this happened"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'joy')
        
    def test_anger_statement(self):
        text = "I am really angry about this"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust_statement(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
    def test_sadness_statement(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'sadness')
        
    def test_fear_statement(self):
        text = "I am very afraid this will happen"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'fear')
        
if __name__ == "__main__":
    unittest.main()