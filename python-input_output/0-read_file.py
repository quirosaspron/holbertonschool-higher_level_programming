#!/usr/bin/python3
""" The function reads a text file and prints it """


def read_file(filename=""):
    """ Reads file and prints its contents """
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
