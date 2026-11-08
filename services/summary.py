from clients.gemini_client import generate_response

def summarize(requirement):
    prompt = open("prompts/summary.txt", encoding="utf-8").read()
    return generate_response(prompt.format(requirement=requirement))