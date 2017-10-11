Ashwin = {
    "first_name": "Ashwin",
    "last_name": "Raman",
    "age": "26",
    "country": "The United States",
    "language": "Python"
    }

def about_person(person):
    print "My name is " + person["first_name"]
    print "My age is " + person["age"]
    print "My country of birth is " + person["country"]
    print "My favorite language is " + person["language"]

about_person(Ashwin)
