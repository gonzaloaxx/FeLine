#!usr/bin/python3
#-*- coding: utf-8 -*-

import google.generativeai
from os import getenv

class Gemini():
    def __init__(self):
        google.generativeai.configure(api_key=getenv('GEMINI_API_KEY'))

    def set_model(self):
        self.model = google.generativeai.GenerativeModel('gemini-2.0-flash')
    
    def send_prompt(self, *args):
        message = [*args]
        response = self.model.generate_content(message)
        return response
