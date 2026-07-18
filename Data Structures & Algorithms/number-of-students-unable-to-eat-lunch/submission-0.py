
from collections import Counter



class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        print(cnt)
        for s in sandwiches:
            if cnt[s] > 0:
                cnt[s] -= 1
                print(cnt)
            else:
                return max(cnt[1], cnt[0])   
        return 0 



            







# create from the student array a queue
# keep track of the student numbers
# if the q head = sandwich: q head = q head.next & student numbers -= 1
# if q.head != sandwich , iteration = student numbers , while iretation: 
# q.tail.next = q.head , q.tail = q.tail.next , q.tail.next = None , ietration -=
# if not iteration retrun student numbers
        