list3 = ['a',10086,'wo',10010,]
list3.sort(key=lambda x:str(x))
print(list3)

list1 = ['我','爱','python',[1,2,3]]
list1.sort(key=lambda x:str(x))
print(list1)

list=["delphi","Delphi","python","Python","c++","C++","c","C","golang","Golang"]
list.sort() #按字典顺序升序排列
print("升序:",list)
migration_list = [(n, p,q) for n in list for p in [True, False,"aa"]for q in [True, False,"aa"]]
print(migration_list)
list.sort(reverse=True) #按降序排列
print("降序:",list)

def two_d_list_sort2(sort_index="0,1,2"): # 动态的根据传入的元素索引进行排序
    list=[ ["1","c++","demo"],
           ["1","c","test"],
           ["2","java",""],
           ["8","golang","google"],
           ["4","python","gil"],
           ["5","swift","apple"]
           ]
    key_set=""
    for item in sort_index.split(","):
        key_set+="ele["+item+"]+"
    key_set=key_set.rstrip("+")
    list.sort(key=lambda ele:eval(key_set))
    print("排序索引:",sort_index,list)

if __name__=="__main__":
    two_d_list_sort2("0")
    two_d_list_sort2("1")
    two_d_list_sort2("2")
    two_d_list_sort2("1,0")