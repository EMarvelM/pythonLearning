#!/usr/bin/env python3

"""Todo list class and engine"""
import json
import os

class TodoObject(object):
    _file = "file.json"

    def __init__(self):
        off_set = None
        title = None
        description = None
        priority = None

        self.reload()
        self.update()

    def to_dict(self):
        return self.__dict__

    def reload(self):
        if os.path.isfile(self._file):
            with open(self._file, "r") as file:
                # content = file.read()
                self._object = json.load(file)
        else:
            self._object = None


    def update(self):
        i = 1
        if self._object:
            while True:
                for arrange in self._object["todo"]:
                    if arrange["off_set"] == i:
                        pass
                    else:
                        self.off_set = i
                        data = self.to_dict()
                        self._object.append(data)
                    i += 1


    def save(self):
        self.reload()
        # self._object["todo"] # todo: edit and dump back
        with open(self._file, "w") as file:
            data = {"todo": self._object}
            json.dump(data, file, indent=2)
