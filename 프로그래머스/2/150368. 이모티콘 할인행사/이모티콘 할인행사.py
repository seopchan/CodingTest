def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    n = len(users)
    m = len(emoticons)
    best_result = [0, 0]

    def dfs(idx, discounts):
        nonlocal best_result

        if idx == m:
            subscribers = 0
            total_sales = 0
            for user in users:
                user_rate, user_limit = user
                user_spent = 0
                for i in range(m):
                    if discounts[i] >= user_rate:
                        user_spent += emoticons[i] * (100 - discounts[i]) // 100
                if user_spent >= user_limit:
                    subscribers += 1
                else:
                    total_sales += user_spent
            
            if subscribers > best_result[0] or (subscribers == best_result[0] and total_sales > best_result[1]):
                best_result = [subscribers, total_sales]
            return

        for rate in discount_rates:
            dfs(idx + 1, discounts + [rate])

    dfs(0, [])
    return best_result