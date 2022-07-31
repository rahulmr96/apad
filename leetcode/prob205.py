def isIsomorphic(s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    else:
        hashMap=dict(zip(list(s),list(t)))
        hashMap_c=dict(zip(list(t),list(s)))
        if len(hashMap)!=len(hashMap_c):
            return False
        lstMap=[hashMap[i] for i in s]
        print(lstMap)
        res=''.join(str(e) for e in lstMap)
        if res==t:
            print(res,t)
            return True
        else: 
            return False
          
a=isIsomorphic('badc','baba')
print(a)
