from extract2 import extract_text
import os
import re
import json
import sqlite3
con = sqlite3.connect("medical_records.db")
cur = con.cursor()
#TODO: To make it iteratively extract text
text = extract_text("data1.pdf")

#a function that searches the location of the end of the first string using regular expressions and the beginning of the second string
def search(first: str, second: str):
    trial_text = text
    first_word_begin = trial_text.find(first)
    second_word_begin = trial_text.find(second)
    total_first = first_word_begin + len(first)
    extracted_word = text[total_first:second_word_begin]
    return extracted_word


def summarise(line: str) -> int:
    #switch case to match every number found between 1 to 5 if something is not found, tag it
    nums: str = line.strip()
    if(nums.find('1')!= -1):
        pass
    else:
        return 1
    if(nums.find('2')!=-1):
        pass
    else: 
        return 2
    if(nums.find('3')!=-1):
        pass
    else:
        return 3
    if(nums.find('4')!=-1):
        pass
    else:
        return 4
    if(nums.find('5')!=-1):
        pass
    else: 
        return 5

def summarise_symptoms(line: str):
    for i in range(0,11):
        if(line.find(fr"{i}") != -1):
            return i
    return 0
    
def summarise_ma_data(line: str):
    argus = line.split('_')
    for x in argus:
        if(x.isspace()==True or x==''):
            continue
        else:
            return x
    return ' '
        
    
# print(summarise_ma_data(search("Height:",'"')))


def create_json()->dict:
    #this contains the dictionary that would eventually be converted to a key, value pair json
    result = {}
    result['patient_name'] = search("Patient Name:","DOB:")
    result['dob'] = search("DOB:","R").strip()
    result['injection'] = search("INJECTION:","Exercise")
    result['exercise_therapy'] = search("Exercise Therapy :","Functional").strip()
    result['difficulty_ratings'] = {}
    result['difficulty_ratings']['bending'] = summarise(search("Bending or Stooping:","Putting on shoes:").strip())
    result['difficulty_ratings']['putting_on_shoes'] = summarise(search("Putting on shoes:","Sleeping:").strip())
    result['difficulty_ratings']['sleeping'] = summarise(search("Sleeping:","Standing for an hour:").strip())
    result['patient_changes'] = {}
    result['patient_changes']['since_last_treatment'] = search("Patient Changes since last treatment:","Patient changes since the start of treatment:").strip()
    result['patient_changes']['since_start_of_treatment'] = search("Patient changes since the start of treatment:","Describe any functional changes within the last three days (good or bad):").strip()
    result['patient_changes']['last_3_days'] = search("Describe any functional changes within the last three days (good or bad):","Rate pain symptoms on a scale of 0-10 (10 being the highest):").strip()
    result['pain_symptoms'] = {}
    result['pain_symptoms']['pain'] = summarise_symptoms(search("Pain:","Numbness:").strip())
    result['pain_symptoms']['numbness'] = summarise_symptoms(search("Numbness:","Tingling:").strip())
    result['pain_symptoms']['tingling'] = summarise_symptoms(search("Tingling:","Burning:").strip())
    result['pain_symptoms']['tightness'] = summarise_symptoms(search("Burning:","Tightness:").strip())
    result['medical_assistant_data'] = {}
    result['medical_assistant_data']['blood_pressure'] = summarise_ma_data(search("Blood Pressure:","HR:"))
    result['medical_assistant_data']['hr'] = summarise_ma_data(search("HR:","Weight:"))
    result['medical_assistant_data']['weight'] = summarise_ma_data(search("Weight:","Height:"))
    result['medical_assistant_data']['height'] = summarise_ma_data(search("Height:",'"'))
    os.chdir("..")
    os.chdir(os.getcwd()+fr"\json_file_storage")
    with open("result.json","w") as fp:
        json.dump(result, fp)
    
    result_text=str(json.dumps(result))
    cur.execute(fr"""INSERT INTO patients (name, dob) VALUES ('{result['patient_name']}',{result['dob']})""")
    patient_id = cur.lastrowid
    print(patient_id)
    cur.execute(fr"INSERT INTO forms_data (patient_id, form_json) VALUES (?,?)",(patient_id, result_text))
    return result

create_json()
