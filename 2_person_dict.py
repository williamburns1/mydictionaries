person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
person['children'][1]
person['pets']['cat']
for index in range(len(person['children'])):
    print(person['children'][index])
for i, j in person['pets'].items():
    print(f"animal: {i}, name: {j}")
