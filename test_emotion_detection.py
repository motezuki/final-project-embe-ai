import unittest
from EmotionDetection.emotion_detection import emotion_detector

class test_emotion_detection(unittest.TestCase):
    def test_detection(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'joy')

        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'anger')

        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'disgust')

        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'sadness')

        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'fear')

unittest.main()