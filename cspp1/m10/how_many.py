"""Exercise : how many"""
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    L = []
    k = 0
    print(aDict)
    for i in aDict:
    	L = aDict[i]
    	length = len(L)
    	k += length
    return i
def main():
	n=input()
	aDict={}
	for k in range(int(n)):
		s=input()
		l=s.split()
		if l[0][0] not in aDict:
			aDict[l[0]]=[l[1]]
		else:
			aDict[l[0]].append(l[1])
	print(how_many(aDict))
if __name__ == "__main__":
	main()
