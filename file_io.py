#########################
## JPlumitallo      ##
## Matrix File i/o lab ##
#########################

import mc as m

#
#attempting to open the file
try:
    of = open('matrices.dat','r')

except FileNotFoundError as E:
    print E

except Exception:  
    print 'Whoops! Something went wrong.'

#
#counteing the number of lines in the file to create an empty matrix of that size
numLines = sum(1 for line in of)

#
#ensuring each matrix has a counterpart
if(numLines%2 != 0):

    print 'Please ensure that each matrix has a counterpart matrix.'

else:

    #
    #creating an empty matrix to hold the matrices read from the file
    matrices = [[] for i in range(numLines)]

    #
    #resetting the file pointer
    of.seek(0)

    n = 0

    for line in of:
       
        try:
            matrices[n] = m.Matrix(eval(line))
            n+=1
        except Exception:
            print'Whoops! Something went wrong. Please ensure that this file and its contents are properly formatted.'

    #
    #closing file
    of.close()

    try:
        wf = open('matrices2.dat','w')
    
    except FileNotFoundError as F:
        print F

    except Exception as E:
        print E

    for i in range(1,numLines,2):
     
        #
        #there is an intentional error (incompatible matrix multiplication) to show that it writes a error to the file
        try:
            wf.write('Sum of pair: '+ str(i-1) + ' and ' + str(i) + '\n')
            wf.write(str((matrices[i]+matrices[i-1]).matrix)+'\n')
        
            wf.write('Product of pair: '+ str(i-1) + ' and ' + str(i) + '\n')
            wf.write(str((matrices[i]*matrices[i-1]).matrix)+'\n')
        
        except Exception as E:
            wf.write(str(E)+'\n')

    
