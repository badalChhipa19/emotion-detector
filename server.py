"""
Flask server for detecting emotions from text input using the Watson NLP API.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_detect():
    """
    Endpoint that receives text via query parameter and returns emotion analysis.
    """
    text = request.args.get('textToAnalyze')

    response = emotion_detector(text)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return (
        "For the given statement, the system response is 'anger': "
        f"{response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index.html page for user input.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
