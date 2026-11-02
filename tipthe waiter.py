def total_calc(bill_amount, tip_perc):
#define function to calculate the tip on bill
    tip=(tip_perc/100)*bill_amount
    total = bill_amount+tip
    total = round(total,2)
    print (f"please pay ${total}")
# specify only bill_amount
# default value of tip percentage is used 

total_calc(1000,20 )
total_calc(1000,30 )