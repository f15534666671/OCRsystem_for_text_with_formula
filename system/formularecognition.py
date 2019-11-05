# {
#   "src": "data:image/jpeg;base64,...",
#   "ocr": ["math", "text"],
#   "skip_recrop": true,
#   "formats": [
#     "text",
#     "latex_simplified",
#     "latex_styled",
#     "mathml",
#     "asciimath",
#     "latex_list"
#    ]
# }
#!/usr/bin/env python
import sys
import base64
import requests
import json

# put desired file path here
# file_path = './imagedata/IMG_2.jpg'
def formula_recognition(img_path):
    image_uri = "data:image/jpg;base64," + base64.b64encode(open(img_path, "rb").read()).decode()
    r = requests.post("https://api.mathpix.com/v3/latex",
        data=json.dumps({'src': image_uri, 'formats': ['latex_normal']}),
        headers={"app_id": "f15534666671_163_com", "app_key": "f9592783fef7fd5aad77",
                 "Content-type": "application/json"})
    json_txt = json.loads(r.text)
    formula = json_txt["latex_normal"]
    # formula = json.dumps(json.loads(r.text), indent=4, sort_keys=True)
    #print(OCR_latex)lll

    return formula
