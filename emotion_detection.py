import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json, headers)
    response_dict = json.loads(response)
    emotions = {}
    
    for key, value in response_dict.emotionPredictions[0].emotion.items():
        emotions[key] = value
        if "dominant_emotion" in emotions
            if value > emotions["dominant_emotion"]:
                emotions["dominant_emotion"] = key
        else:
            emotions["dominant_emotion"] = key
    
    return emotions
