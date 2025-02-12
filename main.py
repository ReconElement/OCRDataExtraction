from extract2 import extract_text
import re
import json

text: str = extract_text("data1.pdf")

original_text = text
result_dict = {}

#create the resultant JSON as extracted from the pdf
result_dict = {
    "patient_name":""
}

#create JSON from the dict so build
with open("result.json",'w') as fp:
    json.dump(result_dict,fp)
    
    
def patient_name(text):
    