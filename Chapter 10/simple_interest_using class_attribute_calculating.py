class Bank:
    bank_name='Bank of India'
    rate_of_interest=12.25


    @staticmethod
    def simple_interest(prin,n):
        si=(prin*n*Bank.rate_of_interest)/100
        print("The Simple interest of the bank named-", Bank.bank_name, "is:", si)


print("The name of the bank is:",Bank.bank_name)
prin = float(input("Enter principle amount: "))
n = int(input("Enter number of years: "))
Bank.simple_interest (prin,n)