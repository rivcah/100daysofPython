##Checks if you exceeded your budget.

def over_bugdet(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < food_bill+electricity_bill+internet_bill+rent:
        return(True)
    else:
        return(False)
    
