# My solution - works, just slow
# Too slow for CODEWARS test cases, which set a maximum of 12 seconds

lst = []

# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele) 

i_factors = []
i_factors_counts_final = []
i_common_factors = []
extend_primes = []
    
#Gets list of factors for each number in given array question
for i in lst:
    if (i > 0):
        for j in range(2, i + 1):
            if (i % j == 0):
                i_factors.append(j)
    elif (i < 0):
        for j in range(2, (-i) + 1):
            if (i % j == 0):
                i_factors.append(j)
    
#Gets tuple list of all factors with their respective number
i_factors_counts_final = [(k,i_factors.count(k)) for k in set(i_factors)]
    
for m in lst:
    for n in i_factors_counts_final:
        if (m % n[0] == 0):
            i_common_factors.append([n[0],m])
    
#does prime test for those factors
def is_prime(n):
    for i in range(2, int(n[0] ** 0.5) + 1):
        if n[0] % i == 0:
            return False
    return True

def get_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes
    extend_primes.extend(primes)
    
#gets tuple list of common prime factors with their respective number
prime_list = get_primes(i_common_factors)
prime_list = sorted(prime_list)
    
#list of common prime factors and associated sums
prime_factor_list = []
lst = sorted(lst)
    
#matching a number to its prime factors
final_list = []
    
for j in prime_list:
    counter = 0
    for i in lst:
        if i % j[0] == 0:
            counter = counter + i
    final_list.append(list((j[0], counter)))
    
new_final_list = []
for elem in final_list:
    if elem not in new_final_list:
        new_final_list.append(elem)
    
print(new_final_list)
