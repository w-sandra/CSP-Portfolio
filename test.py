#Sandra
#Test scores

scores = [88, 42, 95, 70, 63, 82, 55, 91, 74, 85,
38, 77, 90, 61, 89, 72, 59, 98, 45, 81,
67, 73, 88, 52, 94, 79, 100, 68, 83, 71]
#Min and max
print(min(scores))
print(max(scores))
#Average
total=sum(scores)
average= total/len(scores)

print(average)
#Sort
scores.sort()
print(scores)

scores.sort(reverse=True)
print(scores)

#Extra credit
i=0
for i in range(len(scores)):
    scores[i]= scores[i] + 5
    i= i+1
print(scores)
