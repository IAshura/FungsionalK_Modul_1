random_list = [105, 3.1, "hello", 737, "Python", 2.7, "wold", 412, 5.5, "AI"]

int_data = {}
float_data = ()
string_data = []

for item in random_list:
    if isinstance(item, int):
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        int_data[item] = {'ratusan': ratusan,
                          'puluhan': puluhan, 
                          'satuan': satuan
                          }
    elif isinstance(item, float):
        float_data = float_data + (item, )
    elif isinstance(item, str):
        string_data.append(item)

print("Data int:", int_data)
print("Data float:", float_data)
print("Data string:", string_data)

print("\nTipe-tipe variabel diatas : ")
print("int data", type(int_data))
print("float data", type(float_data))
print("string_data", type(string_data))