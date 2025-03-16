#!usr/bin/python3
# -*- coding: utf-8 -*-

from google.genai import Client
from os import getenv

class Genai(Client):
    def __init__(self):
        super().__init__(api_key=getenv('GEMINI_API_KEY'))

    def get_response(self, model:str, *args):
        contents = [*args]
        response = self.models.generate_content(model=model, contents=contents)
        return response
