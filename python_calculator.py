letters = ""
print("---計算式を半角で入力してください---")
print("例） 3+4*5 ")
print()

while not letters =="end":
    x = eval(input("")) #入力された式を計算する
    print("="+ str(x))  #答えを出力する
    print()             #改行
    print("アプリを続ける場合はEnterキーを押してください")
    print("また、アプリを終了する場合はendと入力してください")
    print("終了しますか？", end ="")
    letters = input("")
    print()             #改行
    print()             #改行
