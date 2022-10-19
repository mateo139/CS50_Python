

def main():
    amount_due = 50
    print ("Amount due:", amount_due)
    denomination_check(amount_due)

def denomination_check(amount_due):
    while amount_due > 0:
        insert_coin = int(input("Insert coin: "))
        if insert_coin == 5 or insert_coin == 10 or insert_coin == 25:
            amount_due = amount_due - insert_coin

            ## ALTERNATIVELY this IF-ELSE STATEMENT MAY BE PRESENTED AS ADDITIONALL FUNCION e.g. "change_owe_check"
            if amount_due > 0:
                print ("Amount due: ", amount_due)
            else:
                print ("Change owe: ", -amount_due)

        else:
            print ("Amount due: ", amount_due)
            pass


main()