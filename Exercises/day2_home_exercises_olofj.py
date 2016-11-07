
#EXERCISE ?
s1='abcabcabc'
s2='abc'


def test_repeats(s1,s2):
    '''
    takes two strings s1 and s2 as input 
    
    returns true if s1 only contain repetitions of s2
    
    returns false if anything else happens. 
    '''
    s0=s1[:]
    times = len(s1)/len(s2)
    if s1 == s2 *times:
        return True
    else:
        return False

print test_repeats(s1,s2)

def test_repeats2(s1,s2):
    '''
    takes two strings s1 and s2 as input 
    
    returns true if s1 only contain repetitions of s2
    
    returns false if anything else happens. 
    '''
    return s1 == s2 * (len(s1)/len(s2))


print test_repeats2(s1,s2)


#EXERCISE 4b
'''find_motifs(s1) that returns s2, the shortest motif that builds s1. if s1 is the smallest it returns s1'''
def find_motifs(s1):
    for i in range(1,len(s1)):
        motif = s1[0:i]
        times = len(s1) / len(motif)
        if s1==motif*times:
            return motif
    return s1



print find_motifs(s1)
