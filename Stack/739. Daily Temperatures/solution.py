class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Pairs of [index, temp]
        stack = []
        res = [0 for i in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_i, stack_t = stack.pop()
                res[stack_i] = i - stack_i
            stack.append([i, t])
        
        return res
