# app.py
from models.bankaccount import BankAccount

def main():
    # สร้างบัญชีสองบัญชี
    acc1 = BankAccount("AccountA", 1000)
    acc2 = BankAccount("AccountB", 2500)

    # แสดงข้อมูลบัญชี
    print(acc1)
    print(acc2)

    # รวมบัญชีด้วย operator +
    combined = acc1 + acc2
    print(combined)

if __name__ == "__main__":
    main()