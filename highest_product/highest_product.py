def firstOrSecondIsNegative(integers, product, positiveOne, positiveTwo, negativeOne):
    highest_value = product
    posNumbVisited = False
    negNumbVisited = False
    positiveProduct = positiveOne * positiveTwo
    negativeProduct = positiveOne * negativeOne
    for numb in integers[3:]:
        if posNumbVisited and negNumbVisited:
            break
        if numb >= 0:
            posNumbVisited = True
            value = positiveProduct * numb
            if value > highest_value:
                highest_value = value
        else:
            negNumbVisited = True
            value = negativeProduct * numb
            if value > highest_value:
                highest_value = value
    return highest_value, posNumbVisited


def highest_product(alist):
    if len(alist) < 3:
        raise ValueError("Needs minimum 3 values, you gave {}".format(len(alist)))

    alist = sorted(alist, key=abs, reverse=True)
    first = alist[0]
    second = alist[1]
    third = alist[2]
    product = first * second * third
    containsPosIntegers = True

    if product >= 0 or len(alist) == 3:
        return product

    if first * second >= 0:
        for numb in alist[3:]:
            if numb >= 0:
                return first * second * numb

    if first * third >= 0:
        highest_value, containsPosIntegers = firstOrSecondIsNegative(
            integers=alist,
            product=product,
            positiveOne=first,
            positiveTwo=third,
            negativeOne=second,
        )
        if highest_value >= 0:
            return highest_value

    if containsPosIntegers:
        highest_value, _ = firstOrSecondIsNegative(
            integers=alist,
            product=product,
            positiveOne=second,
            positiveTwo=third,
            negativeOne=first,
        )
        if highest_value >= 0:
            return highest_value

    # Know it's only negative numbers in the list, return product of the lowest numbers
    return alist[-3] * alist[-2] * alist[-1]
