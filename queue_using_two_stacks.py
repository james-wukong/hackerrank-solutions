# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue:
    def __init__(self):
        self.q = []
        
    def enqueue(self, x):
        self.q.append(x)
        
    def dequeue(self):
        del self.q[0]
        
    def print_top(self):
        print(self.q[0])
        
if __name__ == '__main__':
    que = Queue()
    
    q = int(input())
    queries = []
    for _ in range(q):
        query = list(map(int, input().strip().split(' ')))
        queries.append(query)
    for query in queries:
        if query[0] == 1:
            que.enqueue(query[1])
        elif query[0] == 2:
            que.dequeue()
        elif query[0] == 3:
            que.print_top()
        else:
            pass
