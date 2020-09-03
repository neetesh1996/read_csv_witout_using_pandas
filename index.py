
import csv

this_student_id=""
this_class=""
this_vote=""
shyamvote=0
gopalnvote=0
ramvote=0

file_to_open="student.csv"


with open(file_to_open, "r") as this_csv_file:
    this_csv_reader = csv.reader(this_csv_file, delimiter=',')
    header = next(this_csv_reader)
    print(header)


    for line in this_csv_reader:
        

        this_student_id=line[0]
        this_vote=line[1]
       
        if this_vote=="ram":
            ramvote=ramvote+1
        if this_vote=="shyam":
            shyamvote=shyamvote+1
        if this_vote=="gopaln":
            gopalnvote=gopalnvote+1

print ("gopaln: " + str(gopalnvote))
print ("ram: " + str(ramvote))
print ("shyam: " + str(shyamvote)) 


 

        
           
        