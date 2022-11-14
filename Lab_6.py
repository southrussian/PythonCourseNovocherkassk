import json

traffic = json.load(open('glossary.json'))

someitem = traffic.itervalues().next()
columns = list(someitem.keys())
print(columns)

