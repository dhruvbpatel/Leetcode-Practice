#User function Template for python3
class Solution:
    def solve(self,idx,s,arr,N,ans):
        
        if(N==idx):
            ans.append(s)
            return
        
        temp = s+arr[idx]
        
        self.solve(idx+1,s,arr,N,ans);
        self.solve(idx+1,temp,arr,N,ans);
        
        return
        
        
	def subsetSums(self, arr, N):
		# code here
		idx = 0
		s = 0
		ans =[]
		self.solve(idx,s,arr,N,ans)
		return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends