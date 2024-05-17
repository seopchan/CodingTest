from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    result = [0, 0]

    all_combinations = product(discount_rates, repeat=len(emoticons))

    for discounts in all_combinations:
        subs = 0
        sales = 0

        for user_rate, user_limit in users:
            spent = 0
            for i in range(len(emoticons)):
                if discounts[i] >= user_rate:
                    spent += emoticons[i] * (100 - discounts[i]) // 100
            if spent >= user_limit:
                subs += 1
            else:
                sales += spent

        if (subs > result[0]) or (subs == result[0] and sales > result[1]):
            result = [subs, sales]

    return result