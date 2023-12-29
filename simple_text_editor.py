# Enter your code here. Read input from STDIN. Print output to STDOUT
class TextEditor():
    def __init__(self):
        self.string = ''
        
    def append(self, w):
        self.string += w
        
    def delete(self, len_del):
        self.string = self.string[:-1 * len_del]
        
    def print_char(self, k):
        if k <= len(self.string):
            print(self.string[k-1])
            
if __name__ == '__main__':
    n = int(input())
    queries, history = [], []
    te = TextEditor()
    
    for _ in range(n):
        query = input().strip().split(' ')
        queries.append(query)
        
    for query in queries:
        if query[0] == '1':
            history.append((query[0], len(query[1])))
            te.append(query[1])
        elif query[0] == '2':
            history.append((query[0], te.string[-1 * int(query[1]):]))
            te.delete(int(query[1]))
        elif query[0] == '3':
            te.print_char(int(query[1]))
        elif query[0] == '4':
            if len(history) != 0:
                q = history.pop()
                if q[0] == '1':
                    te.delete(q[1])
                elif q[0] == '2':
                    te.append(q[1])
