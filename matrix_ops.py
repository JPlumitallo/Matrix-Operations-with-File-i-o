################################
## J Plumitallo             ##
## Matrix Operations class    ##
################################

#
#class initialization
class Matrix:

    #
    #default constructor
    def __init__(self, matrix = []):
    
        if(self.checkMatrix(matrix) != True):

            print 'Please input a valid matrix.'

        elif(matrix == []):

            self.matrix = matrix

        else:
            
            self.matrix = matrix
            self.nRows = len(matrix)
            self.nCols = len(matrix[0])

                

    #
    #function to ensure that a matrix has proper dimensions
    def checkMatrix(self, matrix2):

        checkDim = True

        for numLists in range(len(matrix2)):

            for numElements in range(len(matrix2[numLists])):
                    
                if(len(matrix2[numLists]) != len(matrix2[numLists - 1])):

                    checkDim = False

        return checkDim

    #
    #function to return the dimensions of an additional matrix
    def getDimensions(self, matrix):

        if(self.checkMatrix(matrix)):
                
            nRows = len(matrix)
            nCols = len(matrix[0])


        else:

            print 'Sorry, the dimensions of your matrix are invalid'

        return(nRows, nCols)

    #
    #function to add two matrices
    def __add__(self, other):

        if(self.checkMatrix(other.matrix) == True):
        
            nMatrix = []
            nElements = []

            if(self.getDimensions(self.matrix) == self.getDimensions(other.matrix)):

                for i in range(len(self.matrix)):

                    for j in range(len(self.matrix[i])):

                        x = self.matrix[i][j] + other.matrix[i][j]

                        nElements.append( x )

                    nMatrix.append( nElements )
                    nElements = []

        return Matrix(nMatrix)

    #
    #function to multiply two matrices
    def __mul__(self, other):

        Mdim = self.getDimensions(self.matrix)
        M2dim = self.getDimensions(other.matrix)

        if(self.checkMatrix(self.matrix) and self.checkMatrix(other.matrix) and Mdim[1] == M2dim[0] ):

            x = 0
            nElements = []
            nMatrix = []

            for i in range(len(self.matrix)):

                for j in range(len(other.matrix[0])):

                    for k in range(len(other.matrix)):

                        x += self.matrix[i][k] * other.matrix[k][j]

                    nElements.append(x)
                    x = 0

                nMatrix.append(nElements)
                nElements = []

            return Matrix(nMatrix)

    #
    #function that raise a matrix by a defined power
    def __pow__(self, power):

        Mdim = self.getDimensions(self.matrix)

        if(self.checkMatrix(self.matrix) and Mdim[1] == Mdim[0] ):

            matrix = self.matrix
            x = 0
            nElements = []
            nMatrix = []
            
            for z in range(int(power)-1):
            
                if(z > 0):

                    matrix = nMatrix
                    nMatrix = []

                for i in range(len(matrix)):

                    for j in range(len(matrix[0])):

                        for k in range(len(matrix)):

                            x += matrix[i][k] * matrix[k][j]

                        nElements.append(x) 
                        x = 0

                    nMatrix.append(nElements)
                    nElements = []

            return Matrix(nMatrix)

        else:

            print 'Sorry, this is not a square matrix.'

    #
    #function to scale a matrix by a defined scalar
    def scale(self, scalar):

        if(self.checkMatrix(self.matrix)):

            nMatrix = []
            nElements = []

            for i in range(len(self.matrix)):

                for j in range(len(self.matrix[i])):

                    x = self.matrix[i][j]*int(scalar)

                    nElements.append(x)

                nMatrix.append(nElements)
                nElements = []

        return Matrix(nMatrix)

    #
    #function to transpose a matrix
    def transpose(self):

        if(self.checkMatrix(self.matrix)):

            nMatrix = []
            nElements = []

            for i in range(len(self.matrix)):

                for j in range(len(self.matrix[i])):

                    x = self.matrix[j][i]

                    nElements.append( x )

                nMatrix.append( nElements )
                nElements = []

            return Matrix(nMatrix)

    #
    #function to perform Guassian Elimination
    def elimination(self, b):

        if(self.checkMatrix(self.matrix) and len(b) == len(self.matrix)):

            n = len(self.matrix)
            M = self.matrix

            i = 0

            for x in M:

                x.append(b[i])

                i += 1

            for k in range(n):

                for i in range(k,n):

                    if abs(M[i][k]) > abs(M[k][k]):

                        M[k], M[i] = M[i],M[k]

                    else:

                        break

                for j in range(k+1,n):

                    try:

                        q = float(M[j][k]) / M[k][k]

                    except Exception:

                        print 'This system is linearly independent.'
                        x = 'No solution'
                        break

                    for m in range(k, n+1):

                        M[j][m] -=  q * M[k][m]

        return x

    #
    #function to perfrom backward substitution
    def backward(self):

        if(self.checkMatrix(self.matrix)):

            n = len(self.matrix)
            M = self.matrix

            x = [0 for i in range(n)]

            try:
                    
                x[n-1] = float(M[n-1][n])/M[n-1][n-1]
                
            except Exception:
                    
                print 'This system is linearly independent.'

            for i in range (n-1,-1,-1):

                Sum = 0

                for j in range(i+1,n):

                    Sum += float(M[i][j])*x[j]
                
                try:
                    
                    x[i] = float(M[i][n] - Sum)/M[i][i]

                except Exception:

                    print 'This system is linearly independent.'
                    x = 'No solution.'
                    break

            return x

    #
    #function to print a matrix in a presentable fashion
    def display(self):

        for i in range(len(self.matrix)):

            print self.matrix[i]


if__name__ = '__main__'
