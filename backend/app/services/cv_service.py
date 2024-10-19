# detects and classifies toilet images with gemini 1.5


import google.generativeai as genai
from IPython.display import Markdown

api_key = 'AIzaSyDNLKzcDnfXbgnUa9GsfIg54H_ZHBn4NY4'

genai.configure(api_key=api_key)

def classify(file):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash-8b")
    file_upload = genai.upload_file(file, display_name="toilet")
    response = model.generate_content([file_upload, "Classify this toilet as clean or dirty. Also, classify is as accessible or not. Give a response formatted like clean, accessible or dirty, not accessible. Accessible means handicap accessible"])
    print(response)
    return response

classify('toilet.jpg')