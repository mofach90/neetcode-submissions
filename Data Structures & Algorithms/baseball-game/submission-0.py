class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = [0,0,0,0,0,0,0]
        j=-1
        for i in range(len(operations)):
            print("recods", records)
            print("operation", operations[i])
            if operations[i] == "+" or operations[i] == "D":
                x = 1 if operations[i] == "+" else 0
                records[j+1] = records[j] + records[j-x]
                j+=1
            elif operations[i] == "C":
                records[j] = 0
                j-=1
            else:
                records[j+1] = (int(operations[i]))
                j+=1
        print("records", records)
        print("j",j)
        return sum(records)


# class Solution:
#     def calPoints(self, operations: List[str]) -> int:
#         records = []
#         for i in range(len(operations)):
#             print("recods", records)
#             print("operation", operations[i])
#             if operations[i] == "+":
#                 records.append(records[len(records)-1] + records[len(records)-2])
#             elif operations[i] == "D":
#                 print(records[len(records)-1], records[len(records)-2])
#                 records.append(records[len(records)-1] * 2)
#             elif operations[i] == "C":
#                 records.pop(len(records)-1)
#             else:
#                 records.append(int(operations[i]))
#         return sum(records)
        
        



# baseball game , strange rules, 
# start with empty record
# Input list of strings "operations"
# operation[i] is the operation that you must apply to thte record
# operataion[i]: 
# x integer
# + : sum of previous two last scores and create a record
# 'D' : double of the previous score and crreate a new record
# "C" : Pop the previous score
# apply all operation and calculate the sum of records
# output : the sum of all scores 