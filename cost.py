import resources

distances = resources.distances
flows = resources.flows

# to_test = [12, 17, 4, 14, 7, 13, 5, 16, 9, 2, 18, 8, 11, 1, 10, 0, 15, 6, 3]
# to_test = [17, 7, 3, 5, 10, 4, 15, 11, 13, 0, 18, 6, 9, 16, 2, 14, 12, 1, 8]
# to_test = [4, 2, 11, 7, 9, 1, 16, 18, 6, 0, 13, 8, 14, 12, 5, 3, 15, 10, 17]
# to_test = [18, 2, 4, 12, 14, 11, 10, 15, 9, 1, 13, 6, 0, 5, 3, 17, 7, 16, 8]
# to_test = [18, 6, 13, 3, 2, 5, 7, 9, 17, 11, 1, 8, 12, 0, 15, 4, 10, 14, 16]
# to_test = [4, 13, 11, 5, 9, 0, 14, 7, 3, 18, 10, 1, 16, 6, 17, 2, 12, 15, 8]
to_test = [14, 9, 11, 10, 12, 5, 3, 8, 4, 13, 2, 1, 7, 16, 18, 17, 19, 6, 15]
# to_test = [13, 12, 5, 8, 6, 14, 15, 1, 0, 11, 3, 17, 18, 9, 7, 4, 16, 2, 10]
# to_test = [0, 14, 11, 17, 13, 6, 15, 18, 10, 4, 7, 2, 3, 8, 1, 16, 9, 12, 5]
to_test_2 = [9, 10, 7, 18, 14, 19, 13, 17, 6, 11, 4, 5, 12, 8, 15, 16, 1, 2, 3]

cost = 0
cost_2 = 0
for i in range(19):
    for j in range(i, 19):
        cost += distances[to_test[i] - 1][to_test[j] - 1] * flows[i][j]

for i in range(19):
    for j in range(i, 19):
        cost_2 += distances[to_test_2[i] - 1][to_test_2[j] - 1] * flows[i][j]

print(cost)
print(cost_2)
print(11281888 * 2)