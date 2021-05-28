
def f23(m):
    def unicify(matrix):
        first, current = 0, 1
        while first != len(matrix) :
            while current != len(matrix):
                if matrix[first] == matrix[current]:
                    matrix.pop(current)
                else:
                    current += 1
            first += 1
            current = first + 1
            
        j=0
        while j < len(m):
            i = 0
            while i < len(m[j])-1:
                if m[j][i]=='None':
                    del m[j][i]
                if m[j][i] == m[j][i+1]:
                    del m[j][i]
                else:
                    i += 1
            j+=1

        return matrix
    
    m = unicify(m)
    for line in m:
        line[0] = line[0][:len(line[0]) - 6] 
        line[1] = 'N' if line[1] == '0' else 'Y'
        line[2] = line[2][:len(line[2]) - 1]
        line[2] = float(line[2])/100
        line[2] = str(round(float(line[2]),1))
    return m
