import random
random.seed(652)
def generate_halfsorted(n=8, idx_zero=None, pattern="random"):
   '''generates a half sorted list of length n
   
      Input
      -----
         n: int
            number of items in resutling list

         idx_zero: Union(int, None)
            desired index for 0, or None for random index

         pattern: str
            one of 'random', 'reverse', or 'sorted'. Denotes the ordering of the returned lists.

      Output
      ------
         L: list[int]
            half-sorted list of integers
         
         idx_zero: int
            index of zero in list

      Example
      -------
      >>> import random
      >>> random.seed(652)
      >>> generate_halfsorted(n=10, idx_zero=3, pattern='random')
      ([-8, -2, -1, 0, 9, 8, 6, 2, 2, 4], 3)
       <---neg--->  0  <-----pos------>     
   '''
   if idx_zero is None: idx_zero = random.randint(0, n-1)
   
   L = []

   if pattern == "random":
      # [-3, -1, -2, 0, 3, 1, 2]
      for i in range(idx_zero): L.append(random.randint(-n,-1))
      L.append(0)
      for i in range(n-1-idx_zero): L.append(random.randint(1, n))

   elif pattern == "reverse":
      # [-1, -2, -3, 0, 3, 2, 1]
      for i in range(idx_zero): L.append(-(1+i))
      L.append(0)
      for i in range(n-1-idx_zero): L.append(n-i)

   elif pattern == "sorted":
      # [-3, -2, -1, 0, 1, 2, 3]
      for i in range(idx_zero): L.append(-n+i)
      L.append(0)
      for i in range(n-1-idx_zero): L.append(i+1)

   return L, idx_zero

def is_sorted(L):
   'Returns True (False) if L is (is not) sorted'
   return not any(L[i] > L[i+1] for i in range(len(L)-1))