import os
import csv

data = open('ba.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

# for row in data_lines[:5]:
#     print(row)

all_emails = []

for row in data_lines[1:15]:
    #skipping the header row
    all_emails.append(row[3])


print(sorted(all_emails))


# --------- Creating a new file?
# the below content will completely overwrite a file IF IT EXISTS already

file_to_output = open('made_up_name', 'w', newline='')
# allows us to overwrite new line

csv_writer = csv.writer(file_to_output, delimiter=',')

csv_writer.writerow(['col1', 'col2', 'col3'])
# writes a new row.

csv_writer.writerows([[1,2,3], [4,5,6]])
# Write multi rows of lists for input

file_to_output.close()

# --------- Appending a new file

appened = open('mad_up_name', 'a', newline='')

csv_writer1 = csv.writer(appened)

csv_writer1.writerow([7,8,9])

appened.close()