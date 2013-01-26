__author__ = 'Admin'

def catalan(n):
    if n == 0:
        return ['']
    result = []
    for i in range(n):
        for w1 in catalan(n-1-i):
            for w2 in catalan(i):
                result.append("(" + w1 + ")" + w2)

    return result

print catalan(5)

