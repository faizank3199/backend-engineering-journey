"""
=========================================================
# Student Performance Analyzer
#========================================================

Dataset Contains Students names, marks

Tasks:
1. Calculate average marks:
2. Find topper
3. find failed student
4. Count total student 


Author : Mohammad Faizan
Date   : 17/03/2026

"""

# Dataset
students = (
    ("Ali", 85),
    ("Sara", 92),
    ("John", 78),
    ("Faizan", 95),
    ("Rohan", 33),
    ("Sana", 32)
)

def analyze_students():
    
    total_marks = 0
    students_count  = 0
    
    topper_name = ""
    topper_marks = 0
    
    failed_students = []
  
    for student , marks in students:
           
        # count student 
            students_count += 1
        
        # total marks 
            total_marks += marks
        
        # topper
            if marks > topper_marks:
                topper_marks = marks
                topper_name = student
        # failed student
            if marks < 35:
                failed_students.append((student,marks))
            
    average = total_marks/ students_count
    
    return (
        average,
        topper_name,
        topper_marks,
        failed_students,
        students_count,
    )
    
# main function
def main():
    (
        average,
        topper_name,
        topper_marks,
        failed_students,
        students_count, ) = analyze_students()
        
    print(f"Average marks of students: {average:.2f}")
    print(f"Topper: {topper_name} -> marks: {topper_marks}")
    print(f"Failed Students: {failed_students}")
    print(f"Total Students: {students_count}")
    

if __name__ == "__main__":
    main()
