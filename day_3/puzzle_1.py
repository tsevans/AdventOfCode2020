# Count the number of '#' characters seen traversing a (3,1) slope on the given input.
# Implementation is O(n) time complexity and O(n) space complexity.

HORIZONTAL_INC = 3

def load_input():
  """
  Load the contents of input.txt into a list.

  Returns:
    ([str]): Lines of input.txt as a list of strings.
  """
  with open("input.txt", "r") as infile:
    lines = [line.rstrip() for line in infile]
  return lines


def highlight_character(line, index):
  """
  Print each line with character at given index highlighted.
  The '.' character is highlighted green and the '#' character
  is highlighted red. This function was useful for debugging.

  Args:
    line (str): Line to highlight.
    index (int): Index of character in line to highlight.
  """
  character = line[index]
  color_code = 41 if character == "#" else 42
  prefix = line[:index]
  suffix = line[index+1:]
  print("%s\x1b[6;30;%sm%s\x1b[0m%s" % (prefix, color_code, character, suffix))


def count_trees(lines):
  """
  Traverse lines on the slope (HORIZONTAL_INC, 1) and count
  how many trees ('#') are encountered.

  Args:
    lines ([str]): Slope representation to traverse.
  Returns:
    (int): Number of trees counted in traversal of lines.
  """
  tree_count = 0

  # Define rollover criteria (patterns repeat horizontally)
  rollover_size = len(lines[0])
  
  index = 1
  for line in lines:
    if index != rollover_size:
      index %= rollover_size

    highlight_character(line, index-1)

    if line[index-1] == "#":
      tree_count += 1

    index += HORIZONTAL_INC

  return tree_count


if __name__ == "__main__":
  lines = load_input()
  tree_count = count_trees(lines)
  print("\nEncountered %s trees." % tree_count)
