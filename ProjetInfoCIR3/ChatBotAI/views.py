from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import openai
import json
from openai import OpenAI


@csrf_exempt
def chat_with_ai(request):
    if request.method == "POST":
        try:
            # Récupérer la question de l'utilisateur depuis le corps de la requête
            data = json.loads(request.body)
            question = data.get("question", "")

            # Vérifier si une question a été fournie
            if not question:
                return JsonResponse({"error": "Aucune question fournie."}, status=400)

            # Configurer la clé API OpenAI
            client = OpenAI(
                api_key=settings.APIKEY2)

            # Envoyer la requête à l'API OpenAI
            response = completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": question}
            ]
            )

            # Extraire la réponse de l'IA
            ai_response = response.choices[0].message.content.strip()
            return JsonResponse({"response": ai_response})

        except openai.OpenAIError as e:
            # Gérer les erreurs liées à l'API OpenAI
            return JsonResponse({"error": "Erreur avec l'API OpenAI.", "details": str(e)}, status=500)

        except json.JSONDecodeError:
            # Gérer les erreurs de décodage JSON
            return JsonResponse({"error": "Requête JSON invalide."}, status=400)

    else:
        return JsonResponse({"error": "Méthode non autorisée."}, status=405)
