# router/logic.py
import os

def get_routing_decision(user_prompt):
    # Intent Detection Logic
    is_long = len(user_prompt) > 100
    technical_indicators = ['how to', 'implement', 'debug', 'architecture', 'refactor', 'optimize', 'python', 'code']
    creative_indicators = ['write a story', 'critique', 'philosophy', 'analyze', 'creative']
    
    is_technical = any(word in user_prompt.lower() for word in technical_indicators)
    is_creative = any(word in user_prompt.lower() for word in creative_indicators)

    is_complex = is_long or is_technical or is_creative
    
    if is_complex:
        return "gpt-4o", "GPT-4o (Reasoning Engine)", "~$0.02", True
    else:
        return "gpt-4o-mini", "GPT-4o-Mini (Fast Edge)", "< $0.001", False