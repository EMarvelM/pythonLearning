i = 0
while i < 3:
    print("meow")
    i += 1#i++ is not allowed in python


for i in [0, 1, 2]:#to avoid typing long list of interation we'd use range
    print("Hello, World")

for i in range(30):
    print(f"very easy{i}")
    i += 1

i = 0
while True: #infinit loop
    i += 1
    print(f"value i = {i}")
    if i == 10:
        break#having a breaking condition to inifinte loop