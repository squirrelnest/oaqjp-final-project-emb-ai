import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input, headers = headers).text
    response_dict = json.loads(response)
    predictions = response_dict["emotionPredictions"][0]["emotion"]
    emotions = {}
    
    for key, value in predictions.items():
        emotions[key] = value
        if "dominant_emotion" in emotions:
            if value > predictions[emotions["dominant_emotion"]]:
                emotions["dominant_emotion"] = key
        else:
            emotions["dominant_emotion"] = key
    
    return emotions
