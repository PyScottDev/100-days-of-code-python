from google import genai
from google.genai import types
from dotenv import load_dotenv
import requests
from post import Post
import os
import json

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=GEMINI_API_KEY)
model = "gemini-2.5-flash-lite"

headline = "Global outcry after US launches strikes on Venezuela and captures president"
subheadline = "France, Russia, China and EU say Washington broke international law after US troops carried out the operation"

def simplify_headline(posts, level):
    items = []
    for p in posts:
        item = {
            "id": p.id,
            "headline": p.title,
            "subheadline": p.subtitle
        }
        items.append(item)

    prompt = f"""
    Role: Act as an English teacher simplifying news for {level.upper()} learners. 
    Task: Simplify the provided headline and subheadline. 
    Constraints: 
    - Use level appropriate vocabulary and structures.
    - Keep names, places, and numbers the same.
    - Do not add extra information. 
    Output
    - Return the result strictly in JSON format with the keys "id" "headline" and "subheadline". 
    - Do not include any conversational text.
    - The "id" must match the input id exactly.

    Input JSON:
    {json.dumps(items, ensure_ascii=False)}
    """

    response = client.models.generate_content(
        model=model, 
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )
    data = json.loads(response.text)
    return {item["id"]: {"headline": item["headline"], "subheadline": item["subheadline"]} for item in data}

def simplify_body(body, level):
    if level == "a1":
        word_count = 200
    elif level == "a2":
        word_count = 250
    elif level == "b1":
        word_count = 600
    else:
        word_count = 800
    news_body = {
        "id": body.id,
        "headline": body.title,
        "subheadline": body.subtitle,
        "body": body.body,
    }
    prompt = f"""
    Role: Act as an English teacher simplifying news for {level.upper()} learners. 
    Task: Simplify the provided news story. Write a maximum of {word_count} words. Create 3 discussion question based on the news contents. 
    Constraints: 
    - Use level appropriate vocabulary.
    - Use level appropriate grammar and structures. 
    - Keep names, places, and numbers the same.
    - Do not add extra information. 
    - Write in paragraphs following the style of the original.
    Output
    - Return the result strictly in JSON format with the keys "id", "headline", "subheadline" "body" and "questions".
    - Questions should be returned as a Python list. 
    - Do not include any conversational text.
    - The "id" must match the input id exactly.

    Input JSON:
    {json.dumps(news_body, ensure_ascii=False)}
    """

    response = client.models.generate_content(
        model=model, 
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )
    data = json.loads(response.text)
    print(data)
    return data
    

# print(type(response))
# print(f"Simplified Headline: {data['headline']}")
# print(f"Simplified Sub: {data['subheadline']}")

# print(response.text)

