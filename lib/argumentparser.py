#!usr/bin/python3
#-*- coding: utf-8 -*-

from argparse import ArgumentParser

class ArgParser(ArgumentParser):
    def __init__(self):
        super().__init__(description="Cliente de linea de comandos para LLM")
        self.add_argument('message', nargs='*', help='Mensaje del prompt')
        self.add_argument('--images', '-i', nargs='*', help='Ruta de las imagenes localo remoto.')

