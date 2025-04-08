import json
import requests

def emotion_detector(text_to_analyze):
    """
    Ejecuta la detección de emociones en el texto proporcionado utilizando
    la función Emotion Predict de Watson NLP.
    
    Args:
        text_to_analyze (str): El texto a analizar para detectar emociones
        
    Returns:
        dict: Diccionario con los puntajes de las emociones y la emoción dominante
    """
    # URL del servicio Watson NLP para EmotionPredict
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Encabezados requeridos para la solicitud
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Datos de entrada en formato JSON
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Realizar la solicitud POST
        response = requests.post(url, headers=headers, json=input_data)
        
        # Convertir la respuesta a un diccionario
        result = json.loads(response.text)
        
        # Extraer los puntajes de las emociones
        emotions = result['emotionPredictions'][0]['emotion']
        
        # Extraer los puntajes individuales
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        # Encontrar la emoción dominante (la de mayor puntaje)
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Crear el diccionario de resultado con el formato solicitado
        result_dict = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        return result_dict
        
    except Exception as e:
        # En caso de error, devolver un diccionario con valores nulos
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }