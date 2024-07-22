import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    input = { "raw_document": { "text": text_to_analyze } }
    emotions = {}

    try:
        response = requests.post(url, json = input, headers = headers)
        status_code = response.status_code
        print("STATUS CODE")
        print(status_code)
        print(response.text)
        response_dict = json.loads(response.text)
        predictions = response_dict["emotionPredictions"][0]["emotion"]

        for key, value in predictions.items():
            emotions[key] = value
            if "dominant_emotion" in emotions:
                if value > predictions[emotions["dominant_emotion"]]:
                    emotions["dominant_emotion"] = key
            else:
                emotions["dominant_emotion"] = key
    except:
        if status_code == 400:
            emotions["dominant_emotion"] = "None"
            for key in ["anger", "disgust", "fear", "joy", "sadness"]:
                emotions[key] = "None"
        
    return emotions
