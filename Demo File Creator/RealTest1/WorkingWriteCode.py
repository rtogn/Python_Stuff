import csv
line =0
while line <5000:
    with open('Demo1.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        row = your_list[line]
        name = row [0]
        Rnumber = row [1]
        Sid = row[2]

    with open (f'{Rnumber}_Demo.csv','w', newline='') as csvfile:
        header = ['Patient Name', 'Requisition ID', 'Specimen ID', 'Replicate ID',
                  'DOB', 'Sample Date', 'Received Date', 'Reported Date', 'Clinic Address 1', 'Address 2',
                  'City', 'State', 'Zip', 'Country', 'Phone', 'Fax']
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerow({'Patient Name': f'{row[0]}', 'Requisition ID':f'{row[1]}', 'Specimen ID':f'{row[2]}', 'Replicate ID':f'{row[3]}',
                  'DOB':f'{row[4]}', 'Sample Date':f'{row[5]}', 'Received Date':f'{row[6]}', 'Reported Date':f'{row[7]}', 'Clinic Address 1':f'{row[8]}',
                         'Address 2':f'{row[9]}','City':f'{row[10]}', 'State':f'{row[11]}', 'Zip':f'{row[12]}',
                         'Country':f'{row[13]}', 'Phone':f'{row[14]}', 'Fax':f'{row[15]}'})
        line = line +1
        row = your_list[line]
        if name == "":
            break









#myfile = open(f'{Rnumber}_Demo.csv','w', newline='')
#with myfile:
 #   writer=csv.writer(myfile)
  #  writer.writerows(row)
#print('csv write complete')


        
        
        

