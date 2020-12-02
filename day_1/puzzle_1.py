# Find the product of the two values from input.txt which sum to 2020.
# Implementation is O(n) time complexity and O(n) space complexity.

SUM = 2020

def load_input():
  """
  Load the contents of input.txt into a list.

  Returns:
    ([int]): Lines of input.txt as a list of integers.
  """
  with open("input.txt", "r") as infile:
    lines = [int(line.rstrip()) for line in infile]
  return lines


def find_terms(values):
  """
  Find two terms in the given list which sum to 2020.

  Args:
    values ([int]): List of integer terms.
  Returns:
    (int, int): Pair of integers which sum to 2020.
  """
  # Sets cannot contain duplicates so they act as a hashing container
  hash_set = set()

  for value in values:
    temp = SUM - value
    
    # If current difference is in the set then we found the second term
    if temp in hash_set:
      return value, temp

    # Otherwise, add the current term to the set
    hash_set.add(value)


if __name__ == "__main__":
  values = load_input()
  first, second = find_terms(values)
  print("The two terms which add to %s are %s and %s" % (SUM, first, second))
  product = first * second
  print("The product of these terms is: %s" % product)
