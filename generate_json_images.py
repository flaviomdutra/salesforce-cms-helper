import os
import json
from os import listdir
from os.path import isfile, join

import_json_structure = {"content": []}

media_dir = os.getcwd() + "/_media"
for image in listdir(media_dir):
    if isfile(join(media_dir, image)):
        import_json_structure["content"].append({
            "type": "cms_image",
            "urlName": os.path.splitext(image)[0],
            "body": {
                "title": os.path.splitext(image)[0],
                "altText": os.path.splitext(image)[0],
                "source": {
                    "ref": image
                }
            }
        })

with open('import.json', 'w') as f:
    json.dump(import_json_structure, f)
