from django.shortcuts import render
from rest_framework.decorators import api_view
from transformers import pipeline
import numpy as np # Ensure NumPy is explicitly imported
import logging
import requests

from django.views.decorators.csrf import csrf_exempt
import json

from django.http import StreamingHttpResponse
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.http import JsonResponse
from django.http import HttpResponse


GEMINI_API_KEY = "AIzaSyCNbdDb9FsvXA8B2Gn_qzhQSxmuTHo_ifA"




def index(request):
    return render(request, "home.html")



genai.configure(api_key = GEMINI_API_KEY)

# Load Gemini Pro model
model = genai.GenerativeModel('gemini-2.0-flash')



@csrf_exempt
def generate_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('prompt', '')

            response = model.generate_content(prompt)
            return JsonResponse({'text': response.text.strip()})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

