def p029():
    print("Distinct powers")
    List = []

    for a in range(2, 101):
        for b in range(2,101):
            result = pow(a,b)
            if result not in List:
                List.append(result)

    return(f"p029 Ans: {len(List)}")