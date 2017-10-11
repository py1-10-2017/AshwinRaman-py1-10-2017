students = [
     {'first_name': 'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
]

def student_list(list):
    for item in list:
        print item["first_name"] + " " + item["last_name"]

student_list(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def students_edited(dict):
    num = 1
    for key in dict:
        print key
        for value in dict[key]:
            full_name = str.upper(value["first_name"]+ " " + value["last_name"])
            num_chars = len(value["first_name"] + value["last_name"])
            print str(num) + " - " + full_name + " - " + str(num_chars)
            num += 1

students_edited(users)
