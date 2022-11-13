class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list) #graph
        in_degree = defaultdict(int) #in degree, used for topological ordering
        
        for r,ing in zip(recipes,ingredients):
            for i in ing:
                graph[i].append(r) #build graph
                in_degree[r]+=1 #add indegree for recipes
        
        
        q = supplies[:] #add all supplies in q
        ans = []
        
        while q:
            
            ing = q.pop(0) #pop 1st element
            
            if ing in recipes:  #if we get ing in recipes ,it means it was added after it's all dependencies were travelled, i.e pre-req were met
                ans.append(ing) # so simply add
            
            for child in graph[ing]: #iterate in childs of curr ingredients and decrease indg of child
                in_degree[child]-=1
            
                if in_degree[child]==0: #if 0 i.e met all requirements
                    q.append(child) #append 
        
        return ans
            
        