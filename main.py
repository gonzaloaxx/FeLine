#!usr/bin/python3
#-*- coding: utf-8 -*-

from lib.argumentparser import ArgParser
from lib.imageparser import get_image
from lib.gemini import Gemini


if __name__ == "__main__":
    parser = ArgParser()
    args = parser.parse_args()

    gemini = Gemini()
    
    if args.images:
        # Vision model
        images = [get_image(x) for x in args.images]
        gemini.set_model()

        if args.message:
            # Text and image recognition
            text = ' '.join(args.message)
            response = gemini.send_prompt(text, *images)
            
            print(response.text)
        else:
            # Image recognition
            response = gemini.send_prompt(*images)
            print(response.text)

    elif args.message:
        # Text generation
        gemini.set_model()
        
        text = ' '.join(args.message)
        response = gemini.send_prompt(text)

        print(response.text)
