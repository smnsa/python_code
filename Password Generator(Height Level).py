import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ②取り出したデータを並べ替え複雑なパスワードを作成するコード
password = ""
password_list = []
# ここで使うshuffle関数はリストで機能するのでデータ格納をリスト型にする
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# 上述のコードを簡単にして、symbolのデータをループした回数文ランダムに取り出し順にpasswordに追加する
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# numberのデータをループした回数分ランダムに取り出し順にpasswordに追加する
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
# password = ''.join(password_list)
for char in password_list:
    password += char

print(f"Your password is: {password}")




