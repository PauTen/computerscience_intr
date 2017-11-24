# /~/computerscience_intr/

#Paying off debt. These are the functions required to solve the problem set 2 in the Computer Science course

#FUNCTION: rem_bal_one_year (balance,annualInterestRate,monthlyPaymentRate)
##Calculates the credit card balance after one year if a persion only pays the minimum monthly payment required by the credit card copany

def rem_bal_one_year(balance,annualInterestRate,monthlyPaymentRate):
    month = 1
    unpaid_bal = balance - monthlyPaymentRate*balance
    while month <= 12:
        balance = unpaid_bal * (1 + annualInterestRate/12)
        unpaid_bal = balance - monthlyPaymentRate*balance
        print('Month ',month,' Remaining balance: ',round(balance,2))
        month += 1
        
    print('Remaining Balance: ',round(balance,2))
    

def rem_bal_w_payment(balance,annualInterestRate,monthlyPayment):
    month = 1
    unpaid_bal = balance - monthlyPayment
    while month <= 12:
        balance = unpaid_bal * (1 + annualInterestRate/12)
        unpaid_bal = balance - monthlyPayment
        month += 1
        
    return balance


### Correct form to do it

def min_payment_one_year(balance,annualInterestRate):
    term_interest = 1 + (annualInterestRate/12)
    month = 0
    new_term = 0
    while month < 12:
        new_term = round(new_term + (term_interest ** month),2)
        month += 1
    payment = round(balance * (term_interest**12) / (new_term))
    print('Lowest Payment: ',payment)
    
    
    
### Iterative approach

def min_payment_one_year_iter(balance,annualInterestRate):
    payment = 10
    while rem_bal_w_payment(balance,annualInterestRate,payment) > 0:
        payment += 10
    return payment

### Iterative approach with bisection method

def min_pay_one_year_bisec(balance,annualInterestRate):
    upper_bound = (balance*((1+annualInterestRate/12)**12))/12
    lower_bound = balance/12
    payment = (upper_bound+lower_bound)/2
    while True:
        end_balance = rem_bal_w_payment(balance,annualInterestRate,payment)
        if abs(end_balance) < 0.01:
            break
        else:
            if end_balance > 0:
                lower_bound = payment
            else:
                upper_bound = payment
        payment = (upper_bound+lower_bound)/2
        
    print('Lowest Payment: ',round(payment,2))