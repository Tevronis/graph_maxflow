# 1kkk
import time


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


class edge:
    def __init__(self, flow=0, cup=0, first=None, second=None):
        self.first = first
        self.second = second
        self.flow = flow
        self.cup = cup


def printMatrix(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            print(M[i][j], end=' ')
        print()


def matrix_to_str(M):
    result = ''
    for i in range(len(M)):
        for j in range(len(M)):
            result += str(M[i][j]) + ' '
        result += '\n'
    return result


def get_matrix_stats(M):
    vertexes = len(M)
    edges = 0
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] != 0:
                edges += 1
    return {'e': edges, 'v': vertexes}



def log_report(*args):
    print(' '.join(map(str, args)))
    with open('..\log.log', 'a') as file:
        file.write(' '.join(map(str, args)))


def clear_log():
    with open('..\log.log', 'w') as file:
        file.write('')
    print("Log is cleared")
