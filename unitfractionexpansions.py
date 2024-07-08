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
    if (k%4==0):
        newrow=[int(k/4),0,0]
        newsolution[-1][2]=newsolution[-1][2]-1
    if (k%4==1 or k%4==3):
        newrow=[k,0,0]
        newsolution[-1][0]=newsolution[-1][0]-1
    if (k%4==2):
        newrow=[int(k/2),0,0]
        newsolution[-1][1]=newsolution[-1][1]-1
    return(newsolution+[newrow])

def Move2SameTopRow(solution,k):
    newsolution=deepcopy(solution)
    if (k%4==0):
        newsolution[-2][2]=newsolution[-2][2]-1
        newsolution[-1][0]=newsolution[-1][0]+int(k/4)
    if (k%4==1 or k%4==3):
        newsolution[-2][0]=newsolution[-2][0]-1
        newsolution[-1][0]=newsolution[-1][0]+k
    if (k%4==2):
        newsolution[-2][1]=newsolution[-2][1]-1
        newsolution[-1][0]=newsolution[-1][0]+int(k/2)
    return newsolution

def Move3NewTopRow(solution,k):
    newsolution=deepcopy(solution)
    if (k%4==0):
        raise Exception("Move 3 not defined when k%4==0")
    if (k%4==1):
        newsolution[-1][2]=newsolution[-1][2]-1
        newrow=[int((k-1)/4),0,1]
    if (k%4==2):
        raise Exception("Move 3 not defined when k%4==2")
    if (k%4==3):
        newsolution[-1][1]=newsolution[-1][1]-1
        newsolution[-1][2]=newsolution[-1][2]-1
        newrow=[int((3*k-1)/4),0,1]
    return(newsolution+[newrow])

def Move3SameTopRow(solution,k):
    newsolution=deepcopy(solution)
    if (k%4==0):
        raise Exception("Move 3 not defined when k%4==0")
    if (k%4==1):
        newsolution[-2][2]=newsolution[-2][2]-1
        newsolution[-1][0]=newsolution[-1][0]+int((k-1)/4)
        newsolution[-1][2]=newsolution[-1][2]+1
    if (k%4==2):
        raise Exception("Move 3 not defined when k%4==2")
    if (k%4==3):
        newsolution[-2][1]=newsolution[-2][1]-1
        newsolution[-2][2]=newsolution[-2][2]-1
        newsolution[-1][0]=newsolution[-1][0]+int((k-3)/4)
        newsolution[-1][2]=newsolution[-1][2]+1
    return newsolution

def Move4NewTopRow(solution,k):
    newsolution=deepcopy(solution)
    if (k%4==0):
        raise Exception("Move 4 not defined when k%4==0")
    if (k%4==1 or k%4==3):
        newsolution[-1][1]=newsolution[-1][1]-1
        newrow=[int((k-1)/2),1,0]
    if (k%4==2):
        newsolution[-1][2]=newsolution[-1][2]-1
        newrow=[int((k-2)/4),1,0]
    return(newsolution+[newrow])

def Move4SameTopRow(solution,k):
    newsolution=deepcopy(solution)
    if (k%4==0):
        raise Exception("Move 4 not defined when k%4==0")
    if (k%4==1 or k%4==3):
        newsolution[-2][1]=newsolution[-2][1]-1
        newsolution[-1][0]=newsolution[-1][0]+int((k-1)/2)
        newsolution[-1][2]=newsolution[-1][2]+1
    if (k%4==2):
        newsolution[-2][2]=newsolution[-2][2]-1
        newsolution[-1][0]=newsolution[-1][0]+int((k-2)/4)
        newsolution[-1][2]=newsolution[-1][2]+1
    return newsolution

def Move5NewTopRow(solution,k):
    newsolution=deepcopy(solution)
    if (k%4==0):
        raise Exception("Move 5 not defined when k%4==0")
    if (k%4==1):
        newsolution[-1][1]=newsolution[-1][1]-1
        newsolution[-1][2]=newsolution[-1][2]-1
        newrow=[int((3*k-3)/4),1,1]
    if (k%4==2):
        raise Exception("Move 5 not defined when k%4==2")
    if (k%4==3):
        newsolution[-1][2]=newsolution[-1][2]-1
        newrow=[int((k-3)/4),1,1]
    return(newsolution+[newrow])

def Move5SameTopRow(solution,k):
    newsolution=deepcopy(solution)
    if (k%4==0):
        raise Exception("Move 5 not defined when k%4==0")
    if (k%4==1):
        newsolution[-2][1]=newsolution[-2][1]-1
        newsolution[-2][2]=newsolution[-2][2]-1
        newsolution[-1][0]=newsolution[-1][0]+int((3*k-3)/4)
        newsolution[-1][1]=newsolution[-1][1]+1
        newsolution[-1][2]=newsolution[-1][2]+1
    if (k%4==2):
        raise Exception("Move 5 not defined when k%4==2")
    if (k%4==3):
        newsolution[-2][2]=newsolution[-2][2]-1
        newsolution[-1][0]=newsolution[-1][0]+int((k-3)/4)
        newsolution[-1][1]=newsolution[-1][1]+1
        newsolution[-1][2]=newsolution[-1][2]+1
    return newsolution

def Move2AdditionalTerms(k):
    if (k%4==0):
        return(int(k/4-1))
    if (k%4==1 or k%4==3):
        return(int(k-1))
    if (k%4==2):
        return(int(k/2-1))
    
def Move3AdditionalTerms(k):
    if (k%4==0):
        raise Exception("Move 3 not defined when k%4==0")
    if (k%4==1):
        return(int((k-1)/4))
    if (k%4==2):
        raise Exception("Move 3 not defined when k%4==2")
    if (k%4==3):
        return(int((3*k-5)/4))
    
def Move4AdditionalTerms(k):
    if (k%4==0):
        raise Exception("Move 4 not defined when k%4==0")
    if (k%4==1 or k%4==3):
        return(int((k-1)/2))
    if (k%4==2):
        return(int((k-2)/4))
    
def Move5AdditionalTerms(k):
    if (k%4==0):
        raise Exception("Move 5 not defined when k%4==0")
    if (k%4==1):
        return(int((3*k-3)/4))
    if (k%4==2):
        raise Exception("Move 5 not defined when k%4==2")
    if (k%4==3):
        return(int((k+1)/4))

def Move1RIsApplicable(solution):
    return(solution[-1][1]>0)

def Move1LIsApplicable(solution):
    return(solution[-1][0]>0)

def Move2NewTopRowIsApplicable(solution,k):
    return ((k%4==0 and solution[-1][2]>0) or ((k%4==1 or k%4==3) and solution[-1][0]>0) or (k%4==2 and solution[-1][1]>0))

def Move2SameTopRowIsApplicable(solution,k):
    return ((k%4==0 and solution[-2][2]>0) or ((k%4==1 or k%4==3) and solution[-2][0]>0) or (k%4==2 and solution[-2][1]>0))

def Move3NewTopRowIsApplicable(solution,k):
    return ((k%4==1 and solution[-1][2]>0) or (k%4==3 and solution[-1][1]>0 and solution[-1][2]>0))

def Move3SameTopRowIsApplicable(solution,k):
    return ((k%4==1 and solution[-2][2]>0) or (k%4==3 and solution[-2][1]>0 and solution[-2][2]>0))

def Move4NewTopRowIsApplicable(solution,k):
    return (((k%4==1 or k%4==3) and solution[-1][1]>0) or ((k%4==2) and solution[-1][2]>0))

def Move4SameTopRowIsApplicable(solution,k):
    return (((k%4==1 or k%4==3) and solution[-2][1]>0) or ((k%4==2) and solution[-2][2]>0))

def Move5NewTopRowIsApplicable(solution,k):
    return ((k%4==1 and solution[-1][1]>0 and solution[-1][2]>0) or (k%4==3 and solution[-1][2]>0))

def Move5SameTopRowIsApplicable(solution,k):
    return ((k%4==1 and solution[-2][1]>0 and solution[-2][2]>0) or (k%4==3 and solution[-2][2]>0))

def Move1LIsPriorityExpansion(solution):
    return(solution[-1][2]<2)

def Move2SameTopRowIsPriorityExpansion(solution,k):
    return(solution[-1][1]<2 and solution[-1][2]<2)

def Move3SameTopRowIsPriorityExpansion(solution,k):
    if (k%4==0):
        return(False)
    if (k%4==1):
        return(solution[-1][2]==0 and solution[-1][1]<2 and solution[-1][0]+(k-1)/4<k)
    if (k%4==2):
        return(False)
    if (k%4==3):
        return(solution[-1][2]==0 and solution[-1][1]<2 and solution[-1][0]+(3*k-1)/4<k)

def Move4SameTopRowIsPriorityExpansion(solution,k):
    if (k%4==0):
        return(False)
    if (k%4==1):
        return(solution[-1][2]==0 and solution[-1][1]==0 and solution[-1][0]+(k-1)/2<k)
    if (k%4==2):
        return(solution[-1][2]<2 and solution[-1][1]==0 and solution[-1][0]+(k-2)/4<k/2)
    if (k%4==3):
        return(solution[-1][2]<2 and solution[-1][1]==0 and solution[-1][0]+(k-1)/2<k and (solution[-1][2]==0 or solution[-1][0]+(k-1)/2<(3*k-1)/4))

def Move5SameTopRowIsPriorityExpansion(solution,k):
    if (k%4==0):
        return(False)
    if (k%4==1):
        return(False)
    if (k%4==2):
        return(False)
    if (k%4==3):
        return(solution[-1][2]==0 and solution[-1][1]==0 and solution[-1][0]+(k-3)/4<k and solution[-1][0]+(k-3)/4<(3*k-1)/4 and solution[-1][0]+(k-3)/4<(k-1)/2)

def FindSolutions(k,n):
    solutionlist=[[] for i in range(n+1)]
    additionalterms=0
    solutionlist[1]=[[[1,0,0]]]
    for i in range(2,n+1):
        for solution in solutionlist[i-1]:
            if (Move1RIsApplicable(solution)):
                solutionlist[i].append(Move1R(solution))
            if (Move1LIsApplicable(solution) and Move1LIsPriorityExpansion(solution)):
                solutionlist[i].append(Move1L(solution))
        if (i>Move2AdditionalTerms(k)):
            for solution in solutionlist[i-Move2AdditionalTerms(k)]:
                if (Move2NewTopRowIsApplicable(solution,k)):
                    solutionlist[i].append(Move2NewTopRow(solution,k))
                if (len(solution)>=2):
                    if (Move2SameTopRowIsApplicable(solution,k) and Move2SameTopRowIsPriorityExpansion(solution,k)):
                        solutionlist[i].append(Move2SameTopRow(solution,k))
        if ((k%4==1 or k%4==3) and i>Move3AdditionalTerms(k)):
            for solution in solutionlist[i-Move3AdditionalTerms(k)]:
                if (Move3NewTopRowIsApplicable(solution,k)):
                    solutionlist[i].append(Move3NewTopRow(solution,k))
                if (len(solution)>=2):
                    if (Move3SameTopRowIsApplicable(solution,k) and Move3SameTopRowIsPriorityExpansion(solution,k)):
                        solutionlist[i].append(Move3SameTopRow(solution,k))
        if (k%4!=0 and i>Move4AdditionalTerms(k)):
            for solution in solutionlist[i-Move4AdditionalTerms(k)]:
                if (Move4NewTopRowIsApplicable(solution,k)):
                    solutionlist[i].append(Move4NewTopRow(solution,k))
                if (len(solution)>=2):
                    if (Move4SameTopRowIsApplicable(solution,k) and Move4SameTopRowIsPriorityExpansion(solution,k)):
                        solutionlist[i].append(Move4SameTopRow(solution,k))
        if (k%4==3 and i>Move5AdditionalTerms(k)):
            for solution in solutionlist[i-Move5AdditionalTerms(k)]:
                if (Move5NewTopRowIsApplicable(solution,k)):
                    solutionlist[i].append(Move5NewTopRow(solution,k))
                if (len(solution)>=2):
                    if (Move5SameTopRowIsApplicable(solution,k) and Move5SameTopRowIsPriorityExpansion(solution,k)):
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
