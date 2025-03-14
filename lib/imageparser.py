#!usr/bin/python3
#-*- coding: utf-8 -*-

from PIL import Image
from requests import get as r_get
from urllib.parse import urlparse


def get_image(resource:str) ->bytes:
        if urlparse(resource).scheme:
            request = r_get(resource)
            image = Image.open(request.content)
        else:
            image = Image.open(resource)

        return image
