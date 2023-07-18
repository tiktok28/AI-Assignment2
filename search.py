def ids(problem):
    depth_limit = 0
    while True:
        result = dls(problem, depth_limit)
        if result == 'found':
            return result
        depth_limit += 1

#def dls(problem, depth_limit):