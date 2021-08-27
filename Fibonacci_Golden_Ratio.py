# Program to display the Fibonacci sequence up to n-th term
n_terms = int(input('How many terms? '))
# store Fibonacci numbers & golden ratio approximations in list f & phi_list
f = []
phi_list = []

# first two terms
n1, n2 = 1, 1
count = 0

# check if the number of terms is valid
if n_terms <= 0:
    print('Please enter a positive integer')
# if there is only one term, return n1
elif n_terms == 1:
    f.append(n1)
    phi_list.append(n1)
# generate fibonacci sequence & phi_list
else:
    while count < n_terms:
        f.append(n1)
        nth = n1 + n2
        phi_list.append(n2 / n1)
        n1 = n2
        n2 = nth
        count += 1
print('Fibonacci sequence upto', n_terms, 'terms')
print(f)
print(n_terms, 'th golden ratio approximation \n', phi_list[-1])
