#!/usr/bin/env python3

"""Todo list class and engine"""
import json

class Todo(object):
    _file = "file.json"

    def __init__(self):
        off_set = None
        title = None
        Description = None
        Priority = None

    def to_dict(self):
        return self.__dict__

    def reload(self):
        with open(self._file, "r") as file:
            content = file.read()
            json.load(content)
            

    def save(self):
        with open(self._file, "w")
