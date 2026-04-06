from django.http import JsonResponse
from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv
from router.logic import get_routing_decision

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def home_view(request):
    return render(request, 'engine/index.html')

def process_prompt(request):
    user_prompt = request.GET.get('prompt', '').strip()
    
    # Use the separated logic module
    model_id, display_name, cost, is_complex = get_routing_decision(user_prompt)

    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": user_prompt}]
        )
        return JsonResponse({
            "ai_response": response.choices[0].message.content,
            "routed_to": display_name,
            "estimated_cost": cost,
            "is_complex": is_complex
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)