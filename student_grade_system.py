
import math

# ==========================================
# SYSTEM HEADER & INTRODUCTION (Topic 1)
# ==========================================
print("=" * 60)
print("     STUDENT ACADEMIC PERFORMANCE EVALUATION SYSTEM     ")
print("=" * 60)

# ==========================================
# INPUT & ELEMENTARY PROGRAMMING (Topic 2)
# ==========================================
student_name = input("Enter Student Name: ").strip()
student_id = input("Enter Student ID: ").strip()

# Input scores as floating-point values
quiz1 = float(input("Enter Quiz 1 Score (out of 100): "))
quiz2 = float(input("Enter Quiz 2 Score (out of 100): "))
exam_score = float(input("Enter Exam Score (out of 100): "))

# Weight calculations
quiz_weight = 0.40
exam_weight = 0.60

# ==========================================
# MATH FUNCTIONS, STRINGS & OBJECTS (Topic 3)
# ==========================================
# Calculate weighted averages using standard math operators
average_quiz = (quiz1 + quiz2) / 2
final_score = (average_quiz * quiz_weight) + (exam_score * exam_weight)

# Application of math functions
rounded_score = round(final_score, 2)
curved_score = math.ceil(final_score)  # Ceiling function to calculate curved grade

# String manipulation methods
formatted_name = student_name.upper()
id_length = len(student_id)

# ==========================================
# SELECTIONS & DECISION MAKING (Topic 4)
# ==========================================
# Input validation check using logical operators
if quiz1 < 0 or quiz1 > 100 or quiz2 < 0 or quiz2 > 100 or exam_score < 0 or exam_score > 100:
    print("\n[ERROR] Invalid score entered! All scores must be between 0 and 100.")
else:
    # Determine Letter Grade and Academic Status using nested selection logic
    if curved_score >= 90:
        grade_letter = 'A'
        academic_status = "Excellent"
    elif curved_score >= 80:
        grade_letter = 'B'
        academic_status = "Very Good"
    elif curved_score >= 70:
        grade_letter = 'C'
        academic_status = "Satisfactory"
    elif curved_score >= 60:
        grade_letter = 'D'
        academic_status = "Needs Improvement"
    else:
        grade_letter = 'F'
        academic_status = "Failed"

    # Additional Selection Check for Honors Eligibility
    if curved_score >= 88 and (quiz1 >= 85 and quiz2 >= 85):
        honors_eligible = True
    else:
        honors_eligible = False

    # ==========================================
    # OUTPUT GENERATION (Topic 1 & 3 String Formatting)
    # ==========================================
    print("\n" + "-" * 60)
    print("                EVALUATION SUMMARY               ")
    print("-" * 60)
    print(f"Student Name      : {formatted_name}")
    print(f"Student ID        : {student_id} (Length: {id_length} digits)")
    print(f"Quiz Average      : {average_quiz:.2f} / 100")
    print(f"Exam Score        : {exam_score:.2f} / 100")
    print(f"Calculated Score  : {rounded_score:.2f}%")
    print(f"Curved Grade      : {curved_score}%")
    print(f"Letter Grade      : {grade_letter}")
    print(f"Academic Status   : {academic_status}")
    
    if honors_eligible:
        print("Honors Status     : Qualified for Dean's List")
    else:
        print("Honors Status     : Not Qualified for Dean's List")
        
    print("=" * 60)