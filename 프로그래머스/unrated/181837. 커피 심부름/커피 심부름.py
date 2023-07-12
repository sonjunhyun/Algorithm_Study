def solution(order):
    price = []
    for o in order:
        if "latte" in o:
            price.append(5000)
        else:
            price.append(4500)
    return sum(price)