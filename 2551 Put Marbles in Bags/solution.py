class Solution:

    def putMarbles(self, weights: List[int], k: int) -> int:
        # Let start by checking the conditions of k bag
        # if the bag is empty we return 0
        if k == 1 : return 0
        
        distribution = []
        # we start in 1 for weight[i] + weight[j]
        for i in range(1,len(weights)):
            distribution.append(weights[i-1] + weights[i])
        # If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
        distribution.sort()
        
        # distribution of score
        max_score = 0
        min_score = 0

        for i in range(k-1):
            min_score += distribution[i]
            max_score += distribution[len(distribution)- 1 - i]
        
        # we return the difference of max distribution minus the minimun distribution
        return max_score - min_score


        
