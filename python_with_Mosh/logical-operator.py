has_high_income = True
has_good_credit = True
has_criminal_record = False 

if has_high_income and has_good_credit:
    print("Eligible for loan")
# AND: both must be true

if has_high_income or has_good_credit:
    print("Eligible for loan")

# OR : one must be True

# NOT logical operator

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
