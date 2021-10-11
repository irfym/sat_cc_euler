import timeit
start = timeit.default_timer()

lst = list(range(1, 1000))
multiples_three = lst[2::3]
multiples_five = lst[4::5]
multiples_both = list(set(multiples_three)|set(multiples_five))
answer = sum(multiples_both)

stop = timeit.default_timer()
print('Time: ', stop - start)
# print(multiples_three)
# print(multiples_five)
# print(multiples_both)
print(answer)
