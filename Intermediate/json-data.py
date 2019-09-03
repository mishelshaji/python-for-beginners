import json as j

# CONVERTING TO JSON
data = {
    "Name": "John Doe",
    "Age": "22"
}
y = j.dumps(data)
print(y)

# A LIST IS CONVERTED INTO JSON EQUIVALENT ARRAY
data = [1, 2, 3, 4, 5]
i = j.dumps(data)
print(i)

# READING FROM JSON
x = '{ "name":"John", "age":30, "city":"New York"}'
y = j.loads(x)
print(y)
print(y["age"])
