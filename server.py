"""Provides server functionality"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Serves home page"""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def analyze():
    """Defines API endpoint for text analysis"""
    text = request.args.get("textToAnalyze")
    data = emotion_detector(text)
    if data["dominant_emotion"] == "None":
        return "<b>Invalid text! Please try again!</b>"

    return f"For the given statement, the system response is \
    'anger': {data['anger']}, \
    'disgust': {data['disgust']}, \
    'fear': {data['fear']}, \
    'joy': {data['joy']} and \
    'sadness': {data['sadness']}. \
    The dominant emotion is {data['dominant_emotion']}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
