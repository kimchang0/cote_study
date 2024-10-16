def solution(arr1, arr2):
    answer = []
    for i in zip(arr1, arr2):
        temp = []
        for j in range(len(i[0])):
            temp.append(i[0][j] + i[1][j])
        answer.append(temp)
    return answer