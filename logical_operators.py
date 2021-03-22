## Logical Operatos in python
## && = and
## || = or
## ! = not

## if the applicant has high income and good credit
## then it is eligible for load

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan!")


## if the applicant has high income or good credit
## then it is eligible for load


if has_high_income or has_good_credit:
    print("Eligible for loan!")

## if the applicant has good credit and not has criminal record
## then it is eligible for load

has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan!")
