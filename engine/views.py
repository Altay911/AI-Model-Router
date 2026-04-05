from django.http import JsonResponse
from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def home_view(request):
    # This renders the beautiful UI we are about to create
    return render(request, 'engine/index.html')

def process_prompt(request):
    user_prompt = request.GET.get('prompt', 'What is the meaning of life?')

    # Expanded Keyword Analysis List
    complex_keywords = [
        'code', 'python', 'javascript', 'bug', 'refactor', 'architect', 'database', 'algorithm', 
        'analyze', 'evaluate', 'compare', 'strategy', 'framework', 'comprehensive',
        'calculate', 'derivative', 'quantum', 'physics', 'equation', 'theorem',
        'philosophical', 'nuance', 'critique', 'detailed', 'perspective', 'optimize'
    ]

    is_complex = len(user_prompt) > 60 or any(word in user_prompt.lower() for word in complex_keywords)

    try:
        if is_complex:
            engine_model, display_name, cost = "gpt-4o", "GPT-4o (Expert)", "~$0.02"
        else:
            engine_model, display_name, cost = "gpt-4o-mini", "GPT-4o-Mini (Budget)", "< $0.001"

        response = client.chat.completions.create(
            model=engine_model,
            messages=[
                {"role": "system", "content": "You are a helpful, high-end AI assistant."},
                {"role": "user", "content": user_prompt}
            ]
        )
        ai_answer = response.choices[0].message.content

        return JsonResponse({
            "status": "success",
            "ai_response": ai_answer,
            "routed_to": display_name,
            "estimated_cost": cost,
            "is_complex": is_complex
        })
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)