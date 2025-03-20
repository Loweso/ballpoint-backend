from django.http import JsonResponse
import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()

def get_cheese_recommendation(request):
    api_key = os.getenv("MISTRAL_API_KEY")
    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {
                "role": "user",
                "content": "What is the best French cheese?",
            },
        ]
    )
    
    response_content = chat_response.choices[0].message.content
    return JsonResponse({'answer': response_content})
