import os
import google.generativeai as genai

try:
    path="GEMINI_KEY.txt"
    os.environ["GEMINI_KEY"] = open(path, 'r').read()
except:
    print("txt file with key missing.")

genai.configure(api_key=os.environ['GEMINI_KEY'])
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

def gemini_agent(prompt):
    response = model.generate_content(prompt)

    return response.text