from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import openai
import json
from openai import OpenAI
import base64

# Decrypt the API key
def decrypt_api_key(encrypted_key: str) -> str:
    return base64.b64decode(encrypted_key.encode()).decode()


@csrf_exempt
def chat_with_ai(request):
    if request.method == "POST":
        try:
            # Recuperer la question de l'utilisateur depuis le corps de la requête
            data = json.loads(request.body)
            question = data.get("question", "")

            # Verifier si une question a ete fournie
            if not question:
                return JsonResponse({"error": "Aucune question fournie."}, status=400)

            # Configurer la cle API OpenAI
            client = OpenAI(
                api_key=decrypt_api_key(settings.APIKEY3))

            # Envoyer la requête à l'API OpenAI
            response = completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": question}
            ]
            )

            # Extraire la reponse de l'IA
            ai_response = response.choices[0].message.content.strip()
            return JsonResponse({"response": ai_response})

        except openai.OpenAIError as e:
            # Gerer les erreurs liees à l'API OpenAI
            return JsonResponse({"error": "Erreur avec l'API OpenAI.", "details": str(e)}, status=500)

        except json.JSONDecodeError:
            # Gerer les erreurs de decodage JSON
            return JsonResponse({"error": "Requête JSON invalide."}, status=400)

    else:
        return JsonResponse({"error": "Methode non autorisee."}, status=405)
