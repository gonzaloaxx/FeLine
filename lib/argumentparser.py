#!usr/bin/python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

class ArgParser(ArgumentParser):
    def __init__(self):
        super().__init__(description='Command Line Client for LLM.')
        self.add_argument('--message', '-m', help='Prompt message as string.')
        self.add_argument('--images', '-i', nargs='*', help='Image path local or remote.')

