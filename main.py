from extract2 import extract_text
import re
import json
import os

cwd = os.getcwd()#gets the current directory
imagepath = str(cwd + r"\dataset_documents")
os.chdir(imagepath)

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
    
    
def convert_to_json()->json:
    text: str = extract_text("data1.pdf")
    original_text = text
    #create the resultant json as extracted from the pdf
    result_dict = {}
    #TODO: To write the rest
    

#searches the location of the end of the first string using Regular expressions and the beginning of the second string
def search(first: str, second: str, original_text: str):
    text = original_text
    print(re.match(r"{first}\s+", text))
    text = original_text
    print(re.match(r"{second}\s+", text))
    
search(first="Patient Name", second="DOB", original_text=original_text)