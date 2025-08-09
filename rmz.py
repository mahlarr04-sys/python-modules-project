while True:
    print("select your option:\n\t 1)Encrypt\n\t 2)Decrypt\n\t 3)Exit")
    choice =input("your choice: ")
    if choice== "1":
        plain_text = input("text: ")#متن ساده از کاربر
        encrypted_text =""#متن رمزگزاری شده ولی اولین بار خالی 
        for c in plain_text:
            x =ord(c)*2+5 #تک تک کارکتار ها رو میگیره و تبدیل به  رمز ک میخایم طبق فرمول ک داددیم میکنه///اینجا به عدد تبدیل میشه
            encrypted_text +=chr(x)#برای ذخیره دوباره انو باید به رشته تبدیل کنیم
            print("encrypted_text:",encrypted_text)
            print("*"*40 +"\n")
        
    
# اینجا برعکس بالا انجام میدیم جای متن ساده و رمز گزاری جابهجا میشه دقت کن
#مثلا بالا مهلا بدی رمز شده میده بهت/ انرو بزنی  مهلا بهت میده
    elif choice == "2":
         encrypted_text =input("encrypted text:")
         plain_text=""
         for c in encrypted_text:
             x=(ord(c) - 5) // 2
             plain_text +=chr(x)
             print("plain text:",plain_text)
             print("*"*40 +"\n")


    elif choice == "3":
        print("Goodby")
        break
    else :
        print("your choice is wrong!")
