print("モードを選んでね:")
print("1: たし算 (+)")
print("2: ひき算 (-)")

choice = input("> ")

# --- モード決定 ---
if choice == "1":
    operator = "+"
elif choice == "2":
    operator = "-"
else:
    print("1 か 2 を入力してね！")
    exit()

# --- 数の入力 ---
try:
    x = float(input("1 つ目の数: "))
    y = float(input("2 つ目の数: "))
except ValueError:
    print("数字を入れてね！")
    exit()

# --- 計算 ---
if operator == "+":
    result = x + y
else:
    result = x - y

# --- 結果表示 ---
print(f"{x} {operator} {y} = {result}")
