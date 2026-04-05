def process_prompt(request):
    user_prompt = request.GET.get('prompt', '').strip()
    if not user_prompt:
        return JsonResponse({"error": "Empty prompt"}, status=400)

    # --- ADVANCED BRAIN LOGIC ---
    
    # 1. Complexity Score (Length matters)
    is_long = len(user_prompt) > 100

    # 2. Intent Detection (The 'Brain' part)
    # We check for structural complexity (commas, question depth, technical verbs)
    technical_indicators = ['how to', 'implement', 'debug', 'architecture', 'refactor', 'optimize']
    creative_indicators = ['write a story', 'critique', 'philosophy', 'analyze the meaning']
    
    is_technical = any(word in user_prompt.lower() for word in technical_indicators)
    is_creative = any(word in user_prompt.lower() for word in creative_indicators)

    # 3. Final Routing Decision
    # If it's long OR technical OR creative, we go 'Expert'
    is_complex = is_long or is_technical or is_creative

    try:
        if is_complex:
            engine_model, display_name, cost = "gpt-4o", "GPT-4o (Reasoning Engine)", "~$0.02"
        else:
            # Simple chat/factual queries
            engine_model, display_name, cost = "gpt-4o-mini", "GPT-4o-Mini (Fast Edge)", "< $0.001"

        # The AI Call remains the same
        response = client.chat.completions.create(
            model=engine_model,
            messages=[{"role": "user", "content": user_prompt}]
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