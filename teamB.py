# Read lab.txt
with open("lab.txt", "r") as file:
    data = file.readlines()

# ตัวแปรมารับ
name_line = data[0].strip() 
age_line = data[1].strip() 
grade_line = data[2].strip() 

# Convert Age to Buddhist Era
age = int(age_line.split(": ")[1])
christYear = 2024 - age
year_buddhist = christYear + 543

# Convert Grade to Ranking Table
grade = grade_line.split(": ")[1]

if grade == "A":
    Rank = "High Distinction"
elif grade in ["B+" ,"B"]:
    Rank = "Distinction"
elif grade in ["C+" ,"C"]:
    Rank = "Good"
elif grade in ["D+" ,"D"]:
    Rank = "Normal"
elif grade == "F":
    Rank = "Failed"

print(name_line)  
print(f"Buddhist Era: {year_buddhist}")
print(f"Software Testing Rank: {Rank}") 
