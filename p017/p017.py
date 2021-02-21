"""
    Problem 17
    Number letter counts
"""
def p017():
    print("Number letter counts")
    # Digits numbers 
    digits = []
    digits.append('one'  )
    digits.append('two'  )
    digits.append('three')
    digits.append('four' )
    digits.append('five' )
    digits.append('six'  )
    digits.append('seven')
    digits.append('eight')
    digits.append('nine' )

    # Teens numbers
    teens = []
    teens.append('ten'      )
    teens.append('eleven'   )
    teens.append('twelve'   )
    teens.append('thirteen' )
    teens.append('fourteen' )
    teens.append('fifteen'  )
    teens.append('sixteen'  )
    teens.append('seventeen')
    teens.append('eighteen' )
    teens.append('nineteen' )

    # Tens Number
    tens = []
    tens.append('twenty' )
    tens.append('thirty' )
    tens.append('forty'  )
    tens.append('fifty'  )
    tens.append('sixty'  )
    tens.append('seventy')
    tens.append('eighty' )
    tens.append('ninety' )

    # Hundred and Thousand
    hundred  = 'hundredand'
    hundred2 = 'hundred'
    thousand = 'onethousand'

    letter_sum = 0 # sum holder

    for d in digits:
        letter_sum += len(d)

    #11-19
    for t in teens:
        letter_sum += len(t)

    #20 - 99
    for t in tens:
        letter_sum += len(t)
        for d in digits:
            letter_sum += len(t)
            letter_sum += len(d)

    #100 - 999
    for h in digits:
        letter_sum += len(h)
        letter_sum += len(hundred2)
        for d in digits:
            letter_sum += len(h)
            letter_sum += len(hundred)
            letter_sum += len(d)
        for t in teens:
            letter_sum += len(h)
            letter_sum += len(hundred)
            letter_sum += len(t)
        for t in tens:
            letter_sum += len(h)
            letter_sum += len(hundred)
            letter_sum += len(t)
            for d in digits:
                letter_sum += len(h)
                letter_sum += len(hundred)
                letter_sum += len(t)
                letter_sum += len(d)
    #1000
    letter_sum += len(thousand)

    # Output
    return(f"p017 Ans: {letter_sum}")
