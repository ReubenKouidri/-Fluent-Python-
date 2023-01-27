import json
from collections import abc
import os

root = os.getcwd()
path = os.path.join(root, "config.json")


def load(fp):
    with open(fp) as f:
        return json.load(f)


class Config:
    """ object providing read-only access to configurations """
    def __init__(self, mapping):
        self.__data = dict(mapping)  # ensure we got a dict or something that can be converted to one

    def __getattr__(self, name):
        """
        This method is called when an attribute is accessed on an object,
        but it is not found in the object's state dictionary
        Checks the __data dictionary for the attribute and returns the attribute using getattr if present
        Else builds a new Config object
        """
        if hasattr(self.__data, name):
            return getattr(self.__data, name)  # check and return attribute from __data instance
        else:
            return Config.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        """
        - If obj instance is a mapping then return a Config obj by passing it directly to constructor
        - This is because an abc.Mapping is, or can be converted to a dict directly
        - If Mutable sequence, it must be a list (only collection types is a json file are dict and list)
            => return a list of Config objects
        - If neither of these, return obj as is
        """
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


def main():
    config = Config(load(path))
    print(config.__dict__)
    print(config.modelConfigs.training.file_path)


main()
