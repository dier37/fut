import json 
import csv 
import os
  
# Opening JSON file and loading the data 
# into the variable data 
for json_file in os.listdir('Images/train/'):
    with open(json_file) as open_file: 
        data = json.load(open_file) 
    
    employee_data = data['emp_details'] 
    
    # now we will open a file for writing 
    data_file = open('data_file.csv', 'w') 
    
    # create the csv writer object 
    csv_writer = csv.writer(data_file) 
    
    # Counter variable used for writing  
    # headers to the CSV file 
    count = 0
    
    for emp in employee_data: 
        if count == 0: 
    
            # Writing headers of CSV file 
            header = emp.keys() 
            csv_writer.writerow(header) 
            count += 1
    
        # Writing data of CSV file 
        csv_writer.writerow(emp.values()) 
    
    data_file.close()