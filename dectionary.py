#DICTIONARY DECLARATION
student={
    "name":"shivam yadav",
    "course" : "BCA",
    "CGPA":8.6,
    "MARKS":[78,88,83,85,79,]
}
#DICTIONARY  ACCESSING

print(" ",student["name"]," ",student["course"]," ",student["CGPA"]," ",student["MARKS"]," ")


# DICTIONARY METHODS
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"city":"kanpur"})
student.update({"state":"UP"})
print(student)