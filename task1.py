def swap(ch, i, j):
    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp

def permutations(ch, index=0):

    if index == len(ch) - 1:
        print (''.join(ch))

    for i in range(index, len(ch)):
        swap(ch, index, i)
        permutations(ch, index+1)
        swap(ch, index, i)

if __name__ == '__main__':
   s = input("Please enter 3 character: ") 
   permutations(list(s))