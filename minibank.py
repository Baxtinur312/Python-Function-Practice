# Global balans o'zgaruvchisi
balance: float = 0.0
account_created: bool = False

def create_account() -> None:
    """Yangi bank hisob raqamini ochadi."""
    global account_created, balance
    if account_created:
        print("\n Hisob allaqachon ochilgan.")
    else:
        account_created = True
        balance = 0.0
        print("\n Hisob muvaffaqiyatli ochildi.")

def deposit() -> None:
    """Pul qo'yish funksiyasi."""
    global balance
    if not account_created:
        print("\n Avval hisob oching.")
        return
    amount_str = input("\n Qo‘yiladigan summani kiriting: ")
    if amount_str.replace('.', '', 1).isdigit():
        amount = float(amount_str)
        if amount > 0:
            balance += amount
            print(f" {amount} so'm qo'yildi.")
        else:
            print(" Musbat summa kiriting.")
    else:
        print(" To'g'ri raqam kiriting.")

def withdraw() -> None:
    """Pul yechib olish funksiyasi."""
    global balance
    if not account_created:
        print("\n Avval hisob oching.")
        return
    amount_str = input("\n Yechiladigan summani kiriting: ")
    if amount_str.replace('.', '', 1).isdigit():
        amount = float(amount_str)
        if 0 < amount <= balance:
            balance -= amount
            print(f" {amount} so'm yechildi.")
        else:
            print(" Yetarli mablag' mavjud emas yoki noto'g'ri summa.")
    else:
        print(" To'g'ri raqam kiriting.")

def check_balance() -> None:
    """Hisobdagi balansni ko'rsatadi."""
    if not account_created:
        print("\n❌ Avval hisob oching.")
    else:
        print(f"\n📊 Hisobingizdagi balans: {balance} so'm")

def main() -> None:
    """Dastur boshqaruv markazi (menu)."""
    while True:
        print("\n===== MiniBank Menyusi =====")
        print("1. 🏦 Hisob ochish")
        print("2. 💵 Pul qo‘yish")
        print("3. 🏧 Pul yechib olish")
        print("4. 📊 Balansni ko‘rish")
        print("0. ❌ Chiqish")
        print("============================")
        choice = input("Tanlang (0-4): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "0":
            print("\n Dasturdan chiqildi.")
            break
        else:
            print(" Noto'g'ri tanlov! Qayta urinib ko'ring.")

# Dastur avtomatik ishga tushadi
type_here = input("Boshlash uchun biror tugmani bosing...\n")
main()

