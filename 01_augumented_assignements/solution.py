# do not change the method name
def main():
    balance = 5000
    print("================== BALANCE ====================", end="\n\n")
    print(f"Current Balance: ${balance:.1f}")
    deposit = input("How much do you want to deposit: $")
    balance = balance + float(deposit)
    print(f"Balance Successfully Updated: ${balance:.1f}")
    withdraw = input(f"How much do you want to withdraw: $")
    print("There is a 3% transaction fee on the withdrawal.")
    fee = float(int(withdraw) * 3 / 100)
    print(f"Withdrawal: ${float(withdraw)} - Fee: ${fee}")
    balance = balance - float(withdraw) - fee
    print(f"Balance Successfully Updated: ${balance:.1f}")
    print("")
    print("============ TRANSACTION COMPLETED ============")


# do not change the following lines:    
if __name__ == "__main__":
    main()