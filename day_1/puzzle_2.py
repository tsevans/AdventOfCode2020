# Find the product of the three values from input.txt which sum to 2020.

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
  Find three terms in the given list which sum to 2020.

  Args:
    values ([int]): List of integer terms.
  Returns:
    (int, int, int): Triad of integers which sum to 2020.
  """
  # TODO: Do this!
  return 2018, 1, 1


if __name__ == "__main__":
  values = load_input()
  first, second, third = find_terms(values)
  print("The three terms which add to %s are %s, %s, and %s" % (SUM, first, second, third))
  product = first * second * third
  print("The product of these terms is: %s" % product)
