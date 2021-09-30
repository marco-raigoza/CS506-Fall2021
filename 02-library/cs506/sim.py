from cs506.kmeans import distance


def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    # raise NotImplementedError()
    res = []
    for i in range(len(x)):
        res.append(abs(x[i] - y[i]))
    return sum(res)

def jaccard_dist(x, y):
    if len(x) == 0:
        return 0
    # jaccard_sim = 0
    # for i in x:
    #     if i in y:
    #         jaccard_sim += 1
    # return 1 - (jaccard_sim / len(y))

    # intersection = len(list(set(x).intersection(y)))
    # union = (len(x) + len(y)) - intersection
    # return 1 - (float(intersection) / union)

    res = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            res += 1

    return 1 - (res / len(x))

def norm(x):
    res = 0
    for i in x:
        res += i ** 2
    return res ** (1/2)

def dot(x, y):
    res = 0
    for i in range(len(x)):
        res += x[i] * y[i]
    
    return res


def cosine_sim(x, y):
    if len(x) == 0 or len(y) == 0 or len(x) != len(y):
        return 0
    # raise NotImplementedError()
    return dot(x, y)/(norm(x)*norm(y))

# Feel free to add more
