from main import Solution


# test cases data
# Case 1

test_case = {
    
'words1_case1' : ["amazon","apple","facebook","google","leetcode"],
'words2_case1'  : ["e","o"],
'Output_case1' : ["facebook","google","leetcode"],

# Case 2
'words1_case2' : ["amazon","apple","facebook","google","leetcode"],
'words2_case2' : ["l","e"],
'Output_case2' : ["apple","google","leetcode"],

# Case 3
'words1_case3' : ["amazon","apple","facebook","google","leetcode"],
'words2_case3' : ["lo","eo"],
'Output_case3' : ["google","leetcode"],
    

#Case 4
'words1_case4' : ["amazon","apple","facebook","google","leetcode"],
'words2_case4' : ["e","oo"],
'Output_case4' : ["facebook","google"],

    
    
}






# run test cases3
case_num = int(len(test_case)/3)
test = Solution()


for i in range(1,case_num+1):
    
    output = test.wordSubsets(test_case[f'words1_case{i}'], test_case[f'words2_case{i}'])
    expect = test_case[f'Output_case{i}']
    
    res =  output == expect
    
    if not res :
        
        print(f'Case {i} : ', res, )
        print(f'>>> Input : {test_case[f"words1_case{i}"]} | {test_case[f"words2_case{i}"]}')
        print(f'>>> Output : {output} | Expected : {expect}')
        
        
        break
    
    print(f'Case {i} : ', res)


