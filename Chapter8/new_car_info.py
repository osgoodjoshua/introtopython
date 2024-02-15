def carinfo (make, model, **extra):
    """storing car informatino"""
    cars = {}
    cars['manufacturer'] = make
    cars['model'] = model
    for x, y in extra.items():
        cars[x] = y
    return cars