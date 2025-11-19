import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        str_1 = "I am glad this happened"
        self.assertEqual(emotion_detector(str_1)['dominant_emotion'], "joy")

        str_2 = "I am really mad about this"
        self.assertEqual(emotion_detector(str_2)['dominant_emotion'], "anger")

        str_3 = "I feel disgusted just hearing about this"
        self.assertEqual(emotion_detector(str_3)['dominant_emotion'], "disgust")

        str_4 = "I am so sad about this"
        self.assertEqual(emotion_detector(str_4)['dominant_emotion'], "sadness")

        str_5 = "I am really afraid that this will happen"
        self.assertEqual(emotion_detector(str_5)['dominant_emotion'], "fear")

unittest.main()