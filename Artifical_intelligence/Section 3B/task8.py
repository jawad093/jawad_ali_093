import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
   
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))


scores = [3, 5, 6, 9, 1, 2, 0, -1] 
depth = math.log2(len(scores))  
result = minimax(0, 0, True, scores, int(depth))
print("The optimal score is:", result)
