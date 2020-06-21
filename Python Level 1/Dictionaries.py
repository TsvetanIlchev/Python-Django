my_dictionary = {"key1":123, "key2":"value2", "key3":[1, 2, 3]}
print(my_dictionary["key2"])

my_dictionary2 = {"key1":123, "key2":"value2", "key3":{"123":[1, 2,"GrabMe"]}}
print(my_dictionary2["key3"]["123"][2])

my_stuff = {"lunch":"pizza", "breakfast":"eggs"}
print(my_stuff)
my_stuff["lunch"] = "burger"
my_stuff["dinner"] = "pasta"
print(my_stuff)
