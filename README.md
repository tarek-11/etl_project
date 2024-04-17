# Extract, Transform, and Load Data using Python

![Skills Network Logo](skills_network_logo.png)

## Introduction
Extract, Transform, and Load (ETL) operations are essential for Data Engineers in managing and processing data. This project focuses on implementing ETL operations using Python, where data is extracted from various sources, transformed according to specific requirements, and then loaded into a database for further analysis.

## Objectives
Upon completing this project, you will be able to:

- Read data from CSV, JSON, and XML file formats.
- Extract necessary data from different file types.
- Transform data into the desired format.
- Save the transformed data in a format suitable for loading into a Relational Database Management System (RDBMS).

## Getting Started
To begin with, ensure you have Python installed on your system. Additionally, install the necessary libraries by running the following command in your terminal:

```bash
python3.11 -m pip install pandas
```

Once the installation is complete, import the required libraries into your Python script (`etl_code.py`) using the following commands:

```python
import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 
```

Note that only the `ElementTree` function is imported from the `xml.etree` library since it's required for parsing XML data.

You'll also need to define two file paths that will be used globally in the code:
- `log_file.txt`: to store all logs generated during the ETL process.
- `transformed_data.csv`: to store the
## ETL Code Summary

The `etl_code.py` script performs Extract, Transform, and Load (ETL) operations on data from various file formats. Here's a breakdown of its functionality:

### Extraction
- The script defines functions to extract data from CSV, JSON, and XML files using pandas and ElementTree libraries.
- For CSV files, it uses `pd.read_csv()` to read the data.
- For JSON files, it reads each line and converts it into a DataFrame using `pd.read_json()`.
- For XML files, it parses the XML tree and extracts specific elements to create a DataFrame.

### Transformation
- The script defines a `transform()` function to convert height from inches to meters and weight from pounds to kilograms, rounding off to two decimal places.

### Loading
- After extraction and transformation, the script saves the transformed data to a CSV file using `to_csv()` function.

### Logging
- The script logs the progress of the ETL process to a log file (`log_file.txt`) with timestamps.
- It logs the start and end of each phase: Extraction, Transformation, and Loading.

### Execution
- The script executes the ETL process in sequence: Extraction, Transformation, and Loading.
- Progress logs are written to `log_file.txt` to track the process.

By running `etl_code.py`, you can perform ETL operations on your data efficiently, extracting, transforming, and loading it into a ready-to-use format for further analysis or database storage.
