"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 02: Strings & Conditional Statements
==============================================================

 Name     : tabssum shafique
 Save as  : yourname_task_02.py   (example: ali_task_02.py)
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 How to use this file
 --------------------
 1. Write your code below each "# Your code here" line.
 2. Run the file in VS Code and check your output against
    the example output given with each task.
 3. Make sure the whole file runs without errors before
    you upload it.
"""
Exercise_01: " Predict the Output "



### Part_01:
           print("Python"[1:4])
           output: yth
Reason: 
      Python indexing starts from 0.
      P = 0, y = 1, t = 2, h = 3.
      [1:4] takes characters from index 1 up to, but not including, index 4.


### Part_02:
           print("banana".count("an"))
           output: 2
Reason: The sequence "an" appears two times in "banana".

### Part_03:
           print("Hello"[-1])
           output: o
Reason: Index -1 selects the last character of a string.

### Part_04:
           print("zebra" < "apple")
           output: False
Reason: Python compare alphabates. Since z comes after a, the condition is false.
### Part_05:
            print(5 > 3 and 2 > 4)
            output: False
Reason:
       5 > 3 = True
       2 > 4 = False
       True AND False = False

### Part_06:
            print(not "")
            output: True
Reason: An empty string is considered False in Python. The not operator reverses it to True.
                      Exercise_02: " Find and Fix 4 Bugs "

marks = int(input("Marks: "))

if marks >= 50:
    print("Pass")
else:
    print("Fail")

answer = input("Again? ")

if answer == "yes":
    print("Restarting...")



    Case 1: Student gets 75 marks and enters yes
Input:
      Marks: 75
      Again? yes
output:
       Pass
       Restarting...
Explanation:
           75 is greater than 50, so the result is Pass.
           The answer is yes, so Restarting... is printed.
           Case 2: Student gets 35 marks and enters no
Input: 
     Marks: 35
     Again? no
output:
      Fail
Explanation:
           35 is less than 50, so the result is Fail.
           The answer is no, so Restarting... is not printed.


           Case 3: Student gets exactly 50 marks and enters yes
Input:
     Marks: 50
     Again? yes
output:
      Pass
      Restarting...
Explanation:
          The condition is marks >= 50.
          Here, 50 is equal to 50, so the student passes.




                Case 4: Student gets 90 marks and enters no
                Input:
      Marks: 90
      Again? no
output:
      Pass
Explanation:
           90 is greater than 50, so Pass.
           The answer is no, so Restarting... does not appear.


               Case 5: Student gets 0 marks and enters yes
Input:
     Marks: 0
     Again? yes
output:
       Fail
       Restarting...
Explanation:
           0 is less than 50, so Fail.
           The answer is yes, so Restarting... appears.


               Case 6: Student gets 100 marks and enters yes
Input:
      Marks: 100
      Again? yes
      output:
       Pass
       Restarting...
Explanation:
          100 is greater than 50, so Pass.
          The answer is yes, so Restarting... appears.


                   Case 7: Student gets 49 marks and enters yes
Input:
      Marks: 49
      Again? yes
output: 
      Fail
      Restarting...
Explanation:
           49 is less than 50, so Fail.
           The answer is yes, so Restarting... appears.


               Case 8: Student gets 60 marks and enters YES (capital letters)
Input:
      Marks: 60
      Again? YES
output:
      Pass
      Explanation:
          Python is case-sensitive.
          "yes" and "YES" are different.
          Therefore, the condition answer == "yes" becomes False.
          Restarting... is not printed.


                 Case 9: Student gets 80 marks and enters Yes (capital Y)
Input:
      Marks: 80
      Again? Yes
output:
       Pass
Explanation:
           Yes is not equal to yes, so Restarting... is not printed.



                 Case 10: Student gets 45 marks and enters yes
Input:
      Marks: 45
      Again? Yes
output:
       Fail
       Restarting...
Explanation:
           45 is less than 50, so Fail.
           yes matches the condition, so Restarting... appears.


              Exercise_03: " Student Grader "


              name = input("Enter student name: ").strip().title()

marks = input("Enter marks (0-100): ")

if marks.isdigit():
    marks = int(marks)

    if marks > 100:
        print("Marks must be between 0-100")

    elif marks >= 90:
        grade = "A+"

    elif marks >= 80:
        grade = "A"

    elif marks >= 70:
        grade = "B"

    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    if marks <= 100:
        print(f"{name} scored {marks}/100 → Grade {grade}")

else:
    print("Invalid input! Please enter numeric marks.")


    Example_01:

Input:
      Enter student name: ali raza
      Enter marks (0-100): 86
output:
      Ali Raza scored 86/100 → Grade B


    Example 2:
Input:
     Enter student name: Sara
     Enter marks (0-100): 95
output:
       Sara scored 95/100 → Grade A+
       Example_03:

Input:
      Enter student name: Ahmed
      Enter marks (0-100): abc
output:
       Invalid input! Please enter numeric marks.



           T1 – String Explorer

word = input("Enter a word: ").strip()

print("Length:", len(word))
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Reversed:", word[::-1])
print("Uppercase:", word.upper())

vowels = "aeiou"
count = 0
for letter in word.lower():
    if letter in vowels:
        count += 1

print("Vowel count:", count)

Input:
      Enter a word: Biology
output:
       Length: 7
First letter: B
Last letter: y
Reversed: ygolo iB
Uppercase: BIOLOGY
Vowel count: 3

         Correction: The exact reversed output is: ygoloiB


T_4

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a Leap Year")
elif year % 100 == 0:
    print(f"{year} is not a Leap Year")

elif year % 4 == 0:
    print(f"{year} is a Leap Year")

else:
    print(f"{year} is not a Leap Year")


Input:
      Enter a year: 2024
output:
       2024 is a Leap Year

Input 2:
         Enter a year: 1900
output:
       1900 is not a Leap Year
       Input 3:
       Enter a year: 2000
output:
       2000 is a Leap Year
Reason:
       % is the modulus operator. It gives the remainder.
       year % 4 == 0 means the year is divisible by 4.
       year % 100 == 0 means it is divisible by 100.
       year % 400 == 0 means it is divisible by 400.
The order of conditions matters because years divisible by 400 are leap years even though they are also divisible by 100.



T5 – Your Field (Biology)


ph = float(input("Enter pH value: "))

if ph < 7:
    result = "Acidic"

elif ph == 7:
    result = "Neutral"

else:
result = "Basic (Alkaline)"

print(f"The pH value is {ph}, which is {result}.")

Input 1:
        Enter pH value: 3
output:
       The pH value is 3.0, which is Acidic.

Input 2:
        Enter pH value: 7
output:
       The pH value is 7.0, which is Neutral.

Input 3:
       Enter pH value: 10
output:
      The pH value is 10.0, which is Basic (Alkaline).

Reason:
       pH below 7 = Acidic.
       pH equal to 7 = Neutral.
       pH above 7 = Basic.
       float() allows decimal values.
       if-elif-else selects the correct classification.
       f-string prints the result.


# ==============================================================
