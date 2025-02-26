import json
import requests


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=my_obj, timeout=30)
    response_formatted = json.loads(response.text)

    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    score = {}
    max_score = 0
    for emotion in emotions:
        score[emotion] = response_formatted['emotionPredictions'][0]['emotion'][emotion]
        if score[emotion] > max_score:
            max_score = score[emotion]
            dominant_emotion = emotion
    score['dominant_emotion'] = dominant_emotion
    # print(json.dumps(response_formatted['emotionPredictions'][0]['emotion'], indent=2))
    return score