import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

def extract_from_csv(file_to_process):
    try:
        dataframe = pd.read_csv(file_to_process)
        return dataframe
    except pd.errors.EmptyDataError:
        print("Empty or malformed CSV file:", file_to_process)
        return pd.DataFrame()

def extract_from_json(file_to_process):
    dataframes = []
    with open(file_to_process, 'r') as file:
        for line in file:
            try:
                json_data = pd.read_json(line, typ='series')
                dataframes.append(pd.DataFrame([json_data]))
            except ValueError:
                print("Error reading JSON object:", line)
    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    else:
        return pd.DataFrame()

def extract_from_xml(file_to_process):
    data = {"name": [], "height": [], "weight": []}
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        data["name"].append(name)
        data["height"].append(height)
        data["weight"].append(weight)
    return pd.DataFrame(data)

def extract(): 
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data 

    # process all csv files 
    for csvfile in glob.glob("*.csv"): 
        data = extract_from_csv(csvfile)
        extracted_data = pd.concat([extracted_data, data], ignore_index=True) 

    # process all json files 
    for jsonfile in glob.glob("*.json"): 
        data = extract_from_json(jsonfile)
        extracted_data = pd.concat([extracted_data, data], ignore_index=True) 

    # process all xml files 
    for xmlfile in glob.glob("*.xml"): 
        data = extract_from_xml(xmlfile)
        extracted_data = pd.concat([extracted_data, data], ignore_index=True) 

    return extracted_data

def transform(data): 
    '''Convert inches to meters and round off to two decimals 
    1 inch is 0.0254 meters '''
    data['height'] = round(data.height * 0.0254,2) 
 
    '''Convert pounds to kilograms and round off to two decimals 
    1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data.weight * 0.45359237,2) 
    
    return data 

def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file, index=False)

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()  
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + ',' +  message + '\n')

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended")
