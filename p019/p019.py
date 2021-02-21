"""
    Problem 19
    Counting Sundays
    ---------------------------------
    let Sunday = 0
    1st Jan 1901 (Tuesday)  = 2

"""
def p019():
    print("Counting Sundays")
    #days in each month
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 2
    suns = 0
    #1901 > 2000 (100 years)
    for years in range(1, 101):
        # 12 months Jan > Dec
        for months in range(0, 12):
            #no of the day starting from Tuesday = 2 to the rest of the month
            day += days[months]
            #if it was FEB and on a leap year then extra day is added to 29th FEB
            # Note 2000 is a century leap year thus a leap year
            if months == 1 and years%4==0:
                day += 1
            #If the day is divisable by 7 thus the beginning of a month is a Sunday
            if day% 7 == 0:
                suns += 1
    #Output           
    return(f"p019 Ans: {suns}")
        
