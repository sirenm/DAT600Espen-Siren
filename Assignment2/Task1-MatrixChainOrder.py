def matrix_chain_order(p):
    n = len(p)
    # Initialize matrix m
    m = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        m.append(row)

    # Initialize matrix s
    s = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        s.append(row)

    #Algorithm from textbook
    for length in range(2, n):
        for i in range(1, n-length+1):
            j = i+length-1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    #Print in matrix form from copilot
    print("Matrix M")
    for i in range(1, n):
        print(m[i][1:])
    print("Matrix S")
    for i in range(1, n):
        print(s[i][1:])
    return m, s

#Our parameters from our handwritten loops
p = [2,1,3,4,5,6]
m , s = matrix_chain_order(p)