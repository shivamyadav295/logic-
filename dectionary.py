#DICTIONARY DECLARATION
student={
    "name":"shivam yadav",
    "course" : "BCA",
    "CGPA":8.4,
    "MARKS":[78,88,83,85,79,90,95]
}
student2={
    "name":"ayush kumar",
    "course":"BBA",
    "CGPA":8.4,
    "MARKS":[80,85,82,87,81,90,92]
}
#DICTIONARY  ACCESSING

print(" ",student["name"]," ",student["course"]," ",student["CGPA"]," ",student["MARKS"]," ")
print(" ",student2["name"]," ",student2["course"]," ",student2["CGPA"]," ",student2["MARKS"]," ")


# DICTIONARY METHODS
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"city":"kanpur"})
student.update({"state":"Uttar Pradesh"})
print(student)
print(student.pop("CGPA"))
print(student.get("state"))
print(student["city"])