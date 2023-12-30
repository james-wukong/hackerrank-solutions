# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

class QHeap():
    data=[]
    ch=False
    
    def __init__(self, data=[]):
        self.data = data
        heapq.heapify(self.data)
    
    def add(self, v):
        heapq.heappush(self.data, v)
            
    def delete(self, v):
        if v==self.data[0]:
            self.ch=True
        self.data.remove(v)
        
        
    def pmin(self):
        if self.ch:
            heapq.heapify(self.data)
            self.ch=False
        print(self.data[0])
        
if __name__ == '__main__':
    cases = int(input())
    queries = []
    queue = QHeap()
    for _ in range(cases):
        q = input().strip().split(' ')
        queries.append(q)
        
    for query in queries:
        if query[0] == '1':
            queue.add(int(query[1]))
        elif query[0] == '2':
            queue.delete(int(query[1]))
        elif query[0] == '3':
            queue.pmin()
        else:
            pass
