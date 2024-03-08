class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.outputs = []

    def add_student(self, name, month, day):
        if name in self.students:
            self.outputs.append(name + " already exists")
        elif int(month) < 4 or int(month) > 7:
            self.outputs.append("Invalid month for registration")
        elif int(day) > 31:
            self.outputs.append("Invalid day for registration")
        else:
            self.students[name] = month + "/" + day
            self.outputs.append(name + " added to list")

    def remove_student(self, name):
        if name in self.students:
            del self.students[name]
            self.outputs.append(name + " removed")
        else:
            self.outputs.append(name + " is not in list")

    def check_students(self):
        if not self.students:
            self.outputs.append("No students in the list")
        else:
            for i, (name, date) in enumerate(self.students.items(), 1):
                self.outputs.append(f"{i} : {name} ({date})")

    def get_student_by_id(self, id):
        if id > len(self.students) or id <= 0:
            self.outputs.append("No username with this id")
        else:
            name = list(self.students.keys())[id - 1]
            self.outputs.append(f"id {id} is {name}")

# Main code
n = int(input())
school = SchoolManagement()

for _ in range(n):
    command = input().split()
    if command[0] == "add":
        name, date = command[1], command[2]
        school.add_student(name, *date.split("/"))
    elif command[0] == "remove":
        school.remove_student(command[1])
    elif command[0] == "check":
        school.check_students()
    elif command[0] == "get_id":
        school.get_student_by_id(int(command[1]))

# Print all outputs together
for output in school.outputs:
    print(output)
