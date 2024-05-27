import json
import os
from models.base_model import BaseModel


class Filestorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """"""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        Filestorage.__objects[key] = obj

    
    def all(self):
        """
        return the object in the fiel
        """
        return Filestorage.__objects
    

    def save(self):
        """
            deserialized the object
        """
        all_objs = Filestorage.__objects
        obj_dict = {}

        for obj in all_objs.key():
            obj_dict[obj] = all_objs[obj].to_dict()
        
        with open(Filestorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)
    
    def reload(self):
        """
        """
        if os.path.isFile(Filestorage.__file_path):
            with open(Filestorage.__file_path, "w", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj

            
