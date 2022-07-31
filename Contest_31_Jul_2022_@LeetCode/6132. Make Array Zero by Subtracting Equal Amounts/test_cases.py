from main import Solution


# test cases data
# Case 1

test_case = {
    
#  Case 1   
'Input_case1' : [1,5,0,3,5],
'Output_case1' : 3,

# Case 2
'Input_case2' : [0],
'Output_case2' : 0,


    
    
}



# run test cases3
case_num = int(len(test_case)/2)
test = Solution()


for i in range(1,case_num+1):
    
    output = test.minimumOperations(test_case[f'Input_case{i}'])
    expect = test_case[f'Output_case{i}']
    
    res =  output == expect
    
    if not res :
        
        print(f'Case {i} : ', res, )
        print(f'>>> Input : {test_case[f"Input_case{i}"]}')
        print(f'>>> Output : {output} | Expected : {expect}')
        
        
        break
    
    print(f'Case {i} : ', res)