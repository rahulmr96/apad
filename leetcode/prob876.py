class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        cnt=1
        while cur:
            cur=cur.next
            cnt+=1
        val=floor(cnt/2)
        cur=head
        print(val)
        if(cnt%2==0):
            cnt1=1
            while cur:
                if(cnt1==val):
                    print(cur)
                    return cur
                cur=cur.next
                cnt1+=1
        else:
            cnt1=1
            while cur:
                if(cnt1==val+1):
                    return cur
                cur=cur.next
                cnt1+=1