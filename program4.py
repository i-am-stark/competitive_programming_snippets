""" Given a string str of lowercase ASCII characters, count the number of
distinct continuous palindromic sub-strings which are present in the string str. """

for _ in range(int(input())) :
    st = input()
    n = len(st)
    res = []
    for i in range(len(st)):
        for j in range(i+1,len(st)+1):
            sub =st[i:j]
            if sub == sub[::-1]:
                if(st[i:j] not in res):
                    res.append(st[i:j])
                
    print(len(res))