class Solution:
    def vowelStrings(self, words, queries):
        vowels={'a','e','i','o','u'}
        ans=[]
        
        for i,j in queries:
            count=0
            for k in range(i,j):
                if words[k][0] in vowels and words[k][-1] in vowels:
                    count+=1
                    
            ans.append(count)
            
        return ans
            
            
            
