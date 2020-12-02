# Count the number of invalid passwords based on rules in the input.txt 'database'.

def load_input():
  """
  Load the contents of input.txt into a list.

  Returns:
    ([str]): Lines of input.txt as a list of strings.
  """
  with open("input.txt", "r") as infile:
    lines = [line.rstrip() for line in infile]
  return lines


def split_line(line):
  """
  Split up a single line into individual components.

  Args:
    line (str): Single line containing policy and password.
  Returns:
    (str, str, str, str): Min, max, character, and password.
  """
  policy, char, password = line.split()
  minimum, maximum = policy.split("-")
  char = char.rstrip(":")
  return minimum, maximum, char, password


def count_invalid_passwords(lines):
  """
  Count the number of invalid passwords in the database.

  Args:
    lines ([str]): Lines of input.txt database file as a list.
  Returns:
    (int): Number of invalid passwords.
  """
  invalid_count = 0

  for line in lines:
    lower, upper, char, password = split_line(line)
    occurrences = password.count(char)
    if occurrences < int(lower) or occurrences > int(upper):
      invalid_count += 1

  return invalid_count


if __name__ == "__main__":
  lines = load_input()
  num_valid = len(lines) - count_invalid_passwords(lines)
  print("%s out of %s passwords in this database are valid." % (num_valid, len(lines)))
