"""
Student Score Manager(Mini Projects)

Features:
 - Add student
 - Veiw Student
   
"""
students = []

def add_student():
    
    
        name = input("Enter the student name: ")
        
        try:
            score = int(input("Enter the marks: "))
            
        except ValueError:
            print("Please enter the valid marks")
            return 
        
        student = {
            "name":name,
            "score":score
        }
        
        students.append(student)
        print(student)
        
        print("Student Added Successfully")
        

def view_student():
    
    if not students:
        print("No student added !")
        return 
    
    print("\n--print student list--")
    for index, student in enumerate(students, start = 1):
        
        print(f"{index} - {student['name']} -> {student['score']}")
        
        

def update_score():
    
    view_student()
    
    try:
        student_number =int(input("Enter the number: "))
        new_score = int(input("Enter the new score: "))
        if not (1 <= student_number <= len(students)):
            print("Out of index")
            return
        
    
        students[student_number-1]["score"] = new_score
     
        print(" Score Updated Successfully")
     
    except ValueError:
        print("Invalid Score")
     
    
def delete_student():
    
    view_student()
    
    try:
      
        student_number = int(input("enter the student number to delete: "))
        if not (1 <= student_number <= len(students)):
            print("Out of index")
            return
        
        
        
        removes = students.pop(student_number-1)
        
        print(f"{removes['name']} delete successfully!")
    except ValueError:
        print("invalid Input")
        
        return 
    
def top_student():
    
    if not students:
        print("No student available")
        return 
        
    top = students[0]
    
    for student in students:
        if student["score"] > top["score"]:
            
            top = student
            
    print(f"Top Student: {top['name']}, {top['score']}")
        
        
def average_score():
    
    if not students:
        print("No studnet available")
        
        return 
        
    total = 0
    for student in students:
        total += student["score"]
    average = total / len(students)
        
    print(f"Average Score: {average}")       
        
        
def fail_students():
    
    if not students:
        print("No student available")
        return 
    
    print("\n--Failed Student--") 
    for student in students:
        if student["score"] < 40:
            print(f"{student['name']}, {student['score']} Failed")
        
        
    
def main():
    
    while True:
        
        print("\n==Student Score Manager==")
        print("\n--Choose the number between 1 to 8: ")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Score")
        print("4. Delete Student")
        print("5. Top Student")
        print("6. Average Score")
        print("7. Failed Student")
        print("8. Exit")
        
        
        try:
            
            choice = int(input("Enter the Choice: "))
            
            if  choice == 1:
                add_student()
            
            elif  choice == 2:
                view_student()
            
            elif choice == 3:
                update_score()
            
            elif choice == 4:
                delete_student()
            
            elif choice== 5:
                top_student()
            
            elif choice == 6:
                average_score()
            
            elif choice == 7:
                fail_students()
            
            elif choice == 8:
                print("Goodbye!")
                break
            else:
                return f"Invalid Input"
        except ValueError:
            print("invalid input")
                
if __name__ == "__main__":
    main()
        
        
        
        
        
    
    
    