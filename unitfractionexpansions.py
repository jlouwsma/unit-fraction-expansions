from copy import deepcopy

def Move1R(solution):
    newsolution=deepcopy(solution)
    newsolution[-1][1]=newsolution[-1][1]-1
    newsolution[-1][2]=newsolution[-1][2]+2
    return newsolution

def Move1L(solution):
    newsolution=deepcopy(solution)
    newsolution[-1][0]=newsolution[-1][0]-1
    newsolution[-1][1]=newsolution[-1][1]+2
    return newsolution

def Move2NewTopRow(solution,k):
    newsolution=deepcopy(solution)
    newrow=[k,0,0]
    newsolution[-1][0]=newsolution[-1][0]-1
    return(newsolution+[newrow])

def Move2SameTopRow(solution,k):
    newsolution=deepcopy(solution)
    newsolution[-2][0]=newsolution[-2][0]-1
    newsolution[-1][0]=newsolution[-1][0]+k
    return newsolution

def Move3NewTopRow(solution,k):
    newsolution=deepcopy(solution)
    newsolution[-1][2]=newsolution[-1][2]-1
    if (k%4==1):
        newrow=[int((k-1)/4),0,1]
    if (k%4==3):
        newrow=[int((k-3)/4),1,1]
    return(newsolution+[newrow])

def Move3SameTopRow(solution,k):
    newsolution=deepcopy(solution)
    newsolution[-2][2]=newsolution[-2][2]-1
    if (k%4==1):
        newsolution[-1][0]=newsolution[-1][0]+int((k-1)/4)
    if (k%4==3):
        newsolution[-1][0]=newsolution[-1][0]+int((k-3)/4)
        newsolution[-1][1]=newsolution[-1][1]+1
    newsolution[-1][2]=newsolution[-1][2]+1
    return newsolution

def Move4NewTopRow(solution,k):
    newsolution=deepcopy(solution)
    newsolution[-1][1]=newsolution[-1][1]-1
    newrow=[int((k-1)/2),1,0]
    return(newsolution+[newrow])

def Move4SameTopRow(solution,k):
    newsolution=deepcopy(solution)
    newsolution[-2][1]=newsolution[-2][1]-1
    newsolution[-1][0]=newsolution[-1][0]+int((k-1)/2)
    newsolution[-1][1]=newsolution[-1][1]+1
    return newsolution

def Move5NewTopRow(solution,k):
    newsolution=deepcopy(solution)
    newsolution[-1][1]=newsolution[-1][1]-1
    newsolution[-1][2]=newsolution[-1][2]-1
    if (k%4==1):
        newrow=[int((3*k-3)/4),1,1]
    if (k%4==3):
        newrow=[int((3*k-1)/4),0,1]
    return(newsolution+[newrow])

def Move5SameTopRow(solution,k):
    newsolution=deepcopy(solution)
    newsolution[-2][1]=newsolution[-2][1]-1
    newsolution[-2][2]=newsolution[-2][2]-1
    if (k%4==1):
        newsolution[-1][0]=newsolution[-1][0]+int((3*k-3)/4)
        newsolution[-1][1]=newsolution[-1][1]+1
    if (k%4==3):
        newsolution[-1][0]=newsolution[-1][0]+int((3*k-1)/4)
    newsolution[-1][2]=newsolution[-1][2]+1
    return newsolution

def Move1LIsPriorityExpansion(solution):
    return(solution[-1][2]<2)

def Move2IsPriorityExpansion(solution):
    return(solution[-1][1]<2 and solution[-1][2]<2)

def Move3IsPriorityExpansion(solution,k):
    if (k%4==1):
        return(solution[-1][2]==0 and solution[-1][1]<2 and solution[-1][0]+(k-1)/4<k)
    if (k%4==3):
        return(solution[-1][2]==0 and solution[-1][1]==0 and solution[-1][0]+(k-3)/4<k)

def Move4IsPriorityExpansion(solution,k):
    return(solution[-1][2]==0 and solution[-1][1]==0 and solution[-1][0]+(k-1)/2<k)

def Move5IsPriorityExpansion(solution,k):
    if (k%4==1):
        return(False)
    if (k%4==3):
        return(solution[-1][2]==0 and solution[-1][1]==0 and solution[-1][0]+(3*k-1)/4<k)

def FindSolutions(k,n):
    solutionlist=[[] for i in range(n+1)]
    additionalterms=0
    solutionlist[1]=[[[1,0,0]]]
    for i in range(2,n+1):
        for solution in solutionlist[i-1]:
            if (solution[-1][1]>0):
                solutionlist[i].append(Move1R(solution))
            if (solution[-1][0]>0 and Move1LIsPriorityExpansion(solution)):
                solutionlist[i].append(Move1L(solution))
        if (i>k-1):
            for solution in solutionlist[i-(k-1)]:
                if (solution[-1][0]>0):
                    solutionlist[i].append(Move2NewTopRow(solution,k))
                if (len(solution)>=2):
                    if (solution[-2][0]>0 and Move2IsPriorityExpansion(solution)):
                        solutionlist[i].append(Move2SameTopRow(solution,k))
        if (k%4==1):
            additionalterms=int((k-1)/4)
        if (k%4==3):
            additionalterms=int((k+1)/4)
        if (i>additionalterms):
            for solution in solutionlist[i-additionalterms]:
                if (solution[-1][2]>0):
                    solutionlist[i].append(Move3NewTopRow(solution,k))
                if (len(solution)>=2):
                    if (solution[-2][2]>0 and Move3IsPriorityExpansion(solution,k)):
                        solutionlist[i].append(Move3SameTopRow(solution,k))
        if (i>(k-1)/2):
            for solution in solutionlist[i-int((k-1)/2)]:
                if (solution[-1][1]>0):
                    solutionlist[i].append(Move4NewTopRow(solution,k))
                if (len(solution)>=2):
                    if (solution[-2][1]>0 and Move4IsPriorityExpansion(solution,k)):
                        solutionlist[i].append(Move4SameTopRow(solution,k))
        if (k%4==3 and i>(3*k-5)/4):
            for solution in solutionlist[i-int((3*k-5)/4)]:
                if(solution[-1][1]>0 and solution[-1][2]>0):
                    solutionlist[i].append(Move5NewTopRow(solution,k))
                if (len(solution)>=2):
                    if (solution[-2][1]>0 and solution[-2][2]>0 and Move5IsPriorityExpansion(solution,k)):
                        solutionlist[i].append(Move5SameTopRow(solution,k))
    return(solutionlist[n])

def CountSolutions(k,n):
    return(len(FindSolutions(k,n)))

def IsNontrivial(solution):
    for rowindex in range(1,len(solution)):
        if (sum(solution[rowindex])!=0):
            return(True)
    return(False)

def FindNontrivialSolutions(k,n):
    return([solution for solution in FindSolutions(k,n) if IsNontrivial(solution)])

def CountNontrivialSolutions(k,n):
    return(len(FindNontrivialSolutions(k,n)))

def IsDistinct(solution):
    for rowindex in range(len(solution)):
        if (max(solution[rowindex])>1):
            return(False)
    return(True)

def FindDistinctSolutions(k,n):
    return([solution for solution in FindSolutions(k,n) if IsDistinct(solution)])

def CountDistinctSolutions(k,n):
    return(len(FindDistinctSolutions(k,n)))

def FindNontrivialDistinctSolutions(k,n):
    return([solution for solution in FindSolutions(k,n) if (IsNontrivial(solution) and IsDistinct(solution))])

def CountNontrivialDistinctSolutions(k,n):
    return(len(FindNontrivialDistinctSolutions(k,n)))
