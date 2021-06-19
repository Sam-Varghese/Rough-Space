def math_competition(num1, multiply1, max_repitition_1, num2, multiply2, max_repitition_2):
    """
    -------------------------------------------------------
    Returns Winner of Math Competition.
    Use: winner = math_competition(num1, multiply1, max_repitition_1, num2, multiply2, max_repitition_2)
    -------------------------------------------------------
    Parameters:
        num1:  first value (int)
        multiply1: first multiplying factor (int)
        max_repitition_1: max repetition for the first value (int)
        num2: second value (int)
        multiply2: second multiplying factor (int)
        max_repitition_2: second repetition factor (int)
    Returns:
        winner - Winner of Math Competition 
    -------------------------------------------------------
    """
    print('Initiate Math Competition:')
    rounds = 1
    first_counter = 0
    second_counter = 0
    winner = ''
    while rounds <= 10 or num1 < num2:
        print('Round = {}'.format(rounds))
        if rounds == 11:
            import os
            os._exit(0)
        while first_counter != max_repitition_1:
            num1 = num1 * multiply1
            print('1 = {}'.format(num1))
            first_counter += 1
        while second_counter != max_repitition_2:
            num2 = num2 * multiply2
            print('2 = {}'.format(num2))
            second_counter += 1
        if num1 > num2:
            winner = '1'
            break
        elif rounds <= 10 and num2 > num1:
            rounds += 1
            continue
        else:
            winner = '2'
    print('Math Competition Closed')
    return winner


#-------------------------MAIN PROGRAM---------------------------#
cases = [[20, -8, 4, 30, 2, 3], [15, 2, 2, 18, 5, 3], [12, 4, 2, 3400, 1, 5]]
for c in cases:
    winner = math_competition(c[0], c[1], c[2], c[3], c[4], c[5])
    print('Winner is: {}'.format(winner))
