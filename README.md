Extract, Transform, and Load Data using Python

Introduction
Extract, Transform, and Load (ETL) operations are essential for Data Engineers in managing and processing data. This project focuses on implementing ETL operations using Python, where data is extracted from various sources, transformed according to specific requirements, and then loaded into a database for further analysis.

Objectives
Upon completing this project, you will be able to:

Read data from CSV, JSON, and XML file formats.
Extract necessary data from different file types.
Transform data into the desired format.
Save the transformed data in a format suitable for loading into a Relational Database Management System (RDBMS).
Getting Started
To begin with, ensure you have Python installed on your system. Additionally, install the necessary libraries by running the following command in your terminal:

bash
Copy code
python3.11 -m pip install pandas
Once the installation is complete, import the required libraries into your Python script (etl_code.py) using the following commands:

python
Copy code
import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 
Note that only the ElementTree function is imported from the xml.etree library since it's required for parsing XML data.

You'll also need to define two file paths that will be used globally in the code:

log_file.txt: to store all logs generated during the ETL process.
transformed_data.csv: to store the final transformed data ready for database loading.
Add the following statements to your code to introduce these paths:

python
Copy code
log_file = "log_file.txt" 
target_file = "transformed_data.csv" 
Usage
Ensure you have all necessary data files (CSV, JSON, XML) placed in the appropriate directory. Modify the code as needed to specify the paths to these files.

Execute the etl_code.py script, which will perform the ETL operations as described in the objectives section. The extracted, transformed, and loaded data will be saved in the transformed_data.csv file.

Conclusion
By completing this project, you'll have gained practical experience in implementing ETL operations using Python. These skills are crucial for any aspiring Data Engineer, as ETL is a fundamental part of the data processing pipeline.

For any questions or issues, refer to the documentation or reach out to the project maintainers.

Happy coding!
