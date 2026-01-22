##Project: Student Record Management System (Using JSON)

#  1.Add a student
#  2.View all students
#  3.Search student by roll number
#  4.Update student marks
#  5.Delete student record
#  6.Data saved permanently in a JSON file

import json 

FILE_NAME = 'mini_2.json'
## load file 
def load_data ():
    try :
        with open (FILE_NAME,'r') as load_file :
            json.load(load_file)
    except :
        return []
## save data by indent(space) = 4 
def save_data (data):
    with open (FILE_NAME,'w') as save_Data :
        json.dump(data,save_Data,indent=4)
        
def add_student ():
    data = load_data()
    
    name = input ('what is the name of the student : ')
    roll_no = input('what is the Roll.NO of the student :')
    total_marks = input ('Enter the total marks of the student :')
    
    student_details = {
        'name': name,
        'roll_no':roll_no,
        'total_marks':total_marks
    }
    
    data.append(student_details)
    save_data(data)
    print ('Student Data add Successfully')
    
# to save the data
def view_data ():
    data = load_data ()
    if not data :
        return "There is no such a data "
    for s in data :
        return (s)
    
# search data 
def search_data ():
    data = load_data ()
    Roll_no = input('Enter students roll number :')
    
    for i in data :
        if i['roll_no'] == Roll_no :
            print (i)
            return
    print ('Student is not found')

# Up date marks 
def up_date_marks ():
    roll_no = input('Enter Student Marks : ')
    data = load_data ()
    
    for i in data :
        if i['roll_no'] == roll_no :
            i['marks'] = input('Enter Marks')
            save_data(data)
            print ('Marks are up date')
            return
    print ('Student is not found ')
    
# deleting student 
def delete_student ():
    roll = input('Enter the Roll.No :')
    data = load_data()
    new_data = [s for s in data if s["roll"] != roll]
    save_data(new_data)
    print("Student deleted")

##teas

def test () :
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")
        
        test_input = input ('choose number between 1 to 6')
        if test_input == 1:
            add_student()
        elif test_input == 2:
            view_data()
        elif test_input == 3:
            search_data()
        elif test_input == 4:
            up_date_marks()
        elif test_input== 5 :
            delete_student ()
        elif test_input == 6 :
            break
        else :
            print ('INVALID NUMBER')
test ()