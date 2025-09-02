import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.load(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar= random.choices("!@#$%^&*",k=1)
        id=alpha+num+spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
            "name": input("tell your name:- "),
            "age": int(input("tell your age:- ")),
            "email": input("Tell your email:- "),
            "pin": int(input("Tell you area pin number:- ")),
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }
        if info['age']<18 or len(str(info['pin'])) != 4:
            print("sorry you can't create an account")
        else:
            print("your account is created successfully")
            for i in info:
                print(f"{i}: {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("please tell your account no:- ")
        pin = int(input("Please tell your pin number aswell:- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin']== pin]
        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("how much you want to deposit "))
            if amount >10000 or amount < 0:
                print("sorry the amount id too much you can deposit below 10000 and above 0")
            else:
                print(userdata)
                userdata [0]['balance'] += amount
                Bank.__update()
                print("amount deposit succesfully")


user = Bank()
print("press 1 for creating an account")
print("press 2 for deposititng the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting the account")

check = int(input("tell your response:- "))

if check==1:
    user.Createaccount()
if check==2:
    user.depositmoney()