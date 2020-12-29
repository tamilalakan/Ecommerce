# Find matrix
def matrix(n):
    s = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append("-")
        s.append(l)
    return s

# Print Cells
def print_(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            print(s[i][j],end=' ')
        print()

# Find Empty Cells
def find_empty(cell, s):
    cou_t = 0
    empty = []
    
    for i in range(len(cell)):
        if i%2 ==0:
            s[cell[i]][cell[i+1]] = "X"
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == "-":
                cou_t += 1
                empty.append([i,j])
        
    return s, empty, cou_t

# Main        
n, k = map(int, input().split())
cell = [int(x) for x in input().split()]
s = matrix(n)
s, empty, count = find_empty(cell,s)
print_(s)
print("Empty cells are: ",empty)
print("Number of empty cells in the matrix are: ", count)
