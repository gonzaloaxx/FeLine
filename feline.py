#!usr/bin/python3
# -*- coding: utf-8 -*-

from lib.argumentparser import ArgParser
from lib.googlegenai import Genai
from lib.imageparser import ImageParser

if __name__ == '__main__':
    parser = ArgParser()
    args = parser.parse_args()

    if args.message:
        genai = Genai()
        text = ' '.join(args.message)
        
        if args.images:
            # Image and text recognition
            contents = [ImageParser.get_image(x) for x in args.images]
            contents.insert(0, text)

            model = 'gemini-2.0-flash'
            response = genai.get_response(model, contents)
        
        else:
            # Text recognition
            contents = [text]

            model = 'gemini-2.0-flash'
            response = genai.get_response(model, *contents)
    else:
        parser.print_help()

    print('\n' + response.text)

