#!/usr/bin/env python3

"""Todo list class and engine"""
import json
import os

class TodoObject(object):
    _file = "file.json"

    def __init__(self, title):
        self.off_set = None
        self.title = title
        self.description = None
        self.priority = None

        # holds the dictionary data
        self.__object = []

        self.reload()
        self.update()

    def to_dict(self):
        return {
            "off_set": self.off_set,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
        }

    def reload(self):
        if os.path.isfile(self._file):
            with open(self._file, "r") as file:
                data = json.load(file)
                if data["todo"]:
                    self.__object = data["todo"]


    def update(self):
        i = 1
        if self.__object:
            for arrange in self.__object:
                if arrange["off_set"] == i:
                    # print(f'seen {arrange["title"]}')
                    pass
                else:
                    break
                i += 1
            self.off_set = i
            data = self.to_dict()
            self.__object.append(data)

        else:
            self.off_set = i
            data = self.to_dict()
            self.__object.append(data)



    def save(self):
        # todo: updating the value before saving
        with open(self._file, "w") as file:
            data = {"todo": self.__object}
            json.dump(data, file, indent=2)
