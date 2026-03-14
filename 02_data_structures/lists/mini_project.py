"""
=====================================================
        Student Score Manager CLI
=====================================================

A command-line application to manage student scores.

## Features

- Add Student
- View Students
- Update Score
- Delete Student
- Find Top Student
- Leaderboard (Top 5)
- Calculate Average Score
- Show Failed Students
- JSON Data Storage

## Concepts Used
- Lists
- Dictionaries
- Loops
- JSON File Handling
- Input Validation
- CRUD Operations


Author : Mohammad Faizan
Date   : 14/03/2026
=====================================================
"""

import json


FILE = "data/student.json"
students = []

def student_leaderboard():
    
    
    if not students:
        print("No students available")
        return 
    
    print("\n== Leaderboard (Top 5 Students)==")
    sorted_student = sorted(
        students,
        key = lambda  x : x['score'],
        reverse = True
    )[:5]
    
    for rank, student in enumerate(sorted_student, start = 1):
       
        print(
            f"{rank} - {student['name']} -> {student['score']} marks"
        )
        
    


def load_students():
    
    try:
        with open(FILE,'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_students(students):
    
        with open(FILE,'w') as f:
            json.dump(students, f, indent=4)
        
    
students = load_students()
    
def add_student():
    
    
        name = input("Enter the student name: ")
        
        try:
            score = int(input("Enter the marks: "))
            
            if score < 0 or score > 100:
                print("Marks must be between 0 and 100")
                return
            
        except ValueError:
            print("Please enter the valid marks")
            return 
        
        student = {
            "name":name,
            "score":score
        }
        
        students.append(student)
        
        save_students(students)
        
        print(f"Student {student['name']} Added Successfully")
        

def view_student():
    
    if not students:
        print("No student added !")
        return 
    
    print("\n--print student list--")
    for index, student in enumerate(students, start = 1):
        
        print(f"{index}.  {student['name']} | score: {student['score']}")
        
        

def update_score():
    
    if not students:
        print("No student available")
        return
    
    view_student()
    
    try:
        student_number =int(input("Enter the number: "))
        if not (1 <= student_number <= len(students)):
            print("Invalid student number")
            return
        
        new_score = int(input("Enter the new score: "))
        if new_score < 0 or new_score > 100:
            print("Marks must be between 0 and 100")
            return
        
       
        
    
        students[student_number-1]["score"] = new_score
        
        save_students(students)
     
        print(" Score Updated Successfully")
     
    except ValueError:
        print("Invalid Score")
     
    
def delete_student():
    
    
    if not students:
        print("No student available")
        return 
    
    view_student()
    
    try:
      
        student_number = int(input("enter the student number to delete: "))
        if not (1 <= student_number <= len(students)):
            print("Invalid student number")
            return
        
        
        
        removes = students.pop(student_number-1)
        
        save_students(students)
        
        print(f"{removes['name']} delete successfully!")
    except ValueError:
        print("invalid Input")
        
        return 
    
def top_student():
    
    if not students:
        print("No student available")
        return 
        
    top = max(students, key= lambda s:s['score'])
            
    print(f"Top Student: {top['name']} | score: {top['score']}")
        
        
def average_score():
    
    if not students:
        print("No student available")
        
        return 
        
    total = sum(student["score"] for student in students)
    average = total / len(students)
        
    print(f"Average Score: {average:.2f}")       
        
        
def fail_students():
    
    if not students:
        print("No student available")
        return 
    
    failed = [s for s in students if s['score'] < 40]
    
    if not failed:
        print("No student Failed")
        return 
    print("\n--Failed Student--") 
    
    for student in failed:
        print(f"{student['name']} | score: {student['score']} Failed")
        
        
    
def main():
    
    while True:
        
        print("\n==Student Score Manager==")
        print("\n--Choose the number between 1 to 9: ")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Score")
        print("4. Delete Student")
        print("5. Top Student")
        print("6. Leaderboard")
        print("7. Average Score")
        print("8. Failed Student")
        print("9. Exit")
        
        
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
                student_leaderboard()
                
            elif choice  == 7:
                average_score()
                
            
            elif choice == 8:
                fail_students()
            
            elif choice == 9:
                print("Goodbye!")
                break
            else:
                print(f"Invalid input. Please select 1-9.")
        except ValueError:
            print("invalid input")
                
if __name__ == "__main__":
    main()
        
        
        
        
        
    
    
    