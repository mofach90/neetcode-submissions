class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        j = 0
        count = 0 
        # stutop = students[i + 0]  
        # santop = sandwichs[j + 0]
        while sandwiches[j + 0] in students:
            print(students, sandwiches)
            print(students[i + 0],sandwiches[j + 0] )
            if students[i + 0] == sandwiches[j + 0]:
                students[i + 0] = 2
                i += 1
                count += 1
                if (j + 1) < len(sandwiches):
                    j += 1

            else:
                students.append(students[i + 0])
                students[i + 0] = 2
                i += 1
        return len(sandwiches) - count
                






# # how i check the matching : 
# students[0] == sandwichs[0]
# # how i can remove a sandwich
# create a pointer top = sandwitch[i+0]
# i + 1 
# # how i can remove a student
# createa a pointer top = students[i+0]
# top = 2 
# i ++
# # how i can place a student from top to tail
# create a pointer of tail = student[len(student)- i]
# tmp = top
# top ++
# student.append[tmp]
# # how i can check that the process freezes
# - each student get the sandwich --> student and sandwich len == 0 
# - no student want the top of the sandwich stack =
# --> sandwich top not in student



# # input dsa:
# 2 lists: 
# - student list --> queue  , top --> student[0]
# - sandwich list --> stack  , top --> sandwichss[0]

# # transformation means to the ds:
# - sandwich --> if the top of array and top of the student match , sandwich schrink by one
# - students --> popping the top if match with the stack top , or 
# top become tail
# - process freeze , if after one students iteration no match happens

# # what condition confirm the transformation:
# for the student transformation : the list shrink to one element or
# the ordre change so that the old top == new tail
