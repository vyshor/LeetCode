class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        indegrees = [0] * n
        edges = {}
        for i in range(n):
            indegrees[i] = len(ingredients[i])
            for ingredient in ingredients[i]:
                if ingredient not in edges:
                    edges[ingredient] = [i]
                else:
                    edges[ingredient].append(i)

        for supply in supplies:
            if supply in edges:
                for i in edges[supply]:
                    indegrees[i] -= 1

        q = []
        for i, degree in enumerate(indegrees):
            if degree == 0:
                q.append(i)

        ans = []
        while q:
            i = q.pop()
            ans.append(recipes[i])

            if recipes[i] in edges:
                for j in edges[recipes[i]]:
                    indegrees[j] -= 1
                    if indegrees[j] == 0:
                        q.append(j)

        return ans
