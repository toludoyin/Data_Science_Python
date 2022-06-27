
# generators>>are>>functions>>that>>act>>like>>iterators.
def ktt():
  yield 44
  yield 3
  yield 2
  yield 5
for k in ktt():
  print(k)



import itertools

def prime_number():
    """function that iterate over prime numbers.
    prime numbers are divisible by itself and 1
    odd numbers are numbers that are not divisible by 2
    even numbers are numbers that are divisible by 2
    """
    yield 2
    prime_cache = [2]

    # starting value and how much to increase by in each step, loop over positive, odd integers
    for prime_num in itertools.count(3, 2):
        is_prime = True

        for num_in_cache in prime_cache:
            if prime_num % num_in_cache == 0:
                is_prime = False
                break

        if is_prime:
            prime_cache.append(prime_num)
            yield prime_num

for num_in_cache in prime_number():
    print (num_in_cache)
    if num_in_cache > 10:
        break



# generator expression
import itertools

square = (num ** 2 for num in itertools.count(1))

for num in square:
    print(num)
    if num >20:
        square.close()
