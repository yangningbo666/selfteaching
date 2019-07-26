def anagram_solution(s1,s2):
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    pos = 0
    ismatched = True

    while pos <len(s2) and ismatched:
        if a_list1[pos] == a_list2[pos]:
            pos = pos + 1
        else:
            ismatched = False
    return ismatched
print(anagram_solution('abchde', 'edcba'))
