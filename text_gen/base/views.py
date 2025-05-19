from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from transformers import pipeline
import numpy as np # Ensure NumPy is explicitly imported
import logging
import requests
import ollama
from django.views.decorators.csrf import csrf_exempt
import json
from ollama import Client
from django.http import StreamingHttpResponse


def index(request):
    return render(request, "home.html")


client = Client()

@csrf_exempt
def generate_text(request):
    if request.method == "POST":
        data = json.loads(request.body)
        prompt = data.get("prompt", "")

        def generate():
            try:
                response = client.chat(

                    model='llama3',  # choose your model after pulling through ollama
                    messages=[{"role": "user", "content": prompt}],
                    stream=True
                )
                for chunk in response:
                    yield chunk['message']['content']
            except Exception as e:
                yield f"\n[ERROR] {str(e)}"

        return StreamingHttpResponse(generate(), content_type="text/plain")