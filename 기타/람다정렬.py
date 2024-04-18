#1.리스트 안의 튜플의 두 번째 요소를 기준으로 오름차순으로 정렬하는 문제.
lst = [[3,2],[2,1],[5,0]]
lst = sorted(lst,key = lambda x: x[1])
print(lst)
#2.딕셔너리의 값(value)을 기준으로 내림차순으로 정렬하는 문제.
dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 2}
sorted_dict = sorted(dict.items(),key = lambda x: x[1])
#3.문자열의 길이를 기준으로 오름차순으로 정렬하는 문제.
lst = ["hello","hi","what'sup","hihi"]
lst = sorted(lst,key = lambda x : len(x))
print(lst)
#4.리스트 안의 문자열을 알파벳 순서로 정렬하는데, 대소문자를 구분하지 않고 소문자 우선으로 정렬하는 문제.
lst = ["hello","Hi","What'sup","hihi"]
print(sorted(lst))
lst = sorted(lst,key = lambda x : x.lower())
print(lst)
#5.리스트 안의 문자열을 마지막 문자를 기준으로 오름차순으로 정렬하는 문제.
lst = ["hello3","hi2","what'sup1","hihi"]
lst = sorted(lst, key = lambda x : x[-1])
print(lst)