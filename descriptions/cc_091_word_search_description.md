Description of daily coding challenge number 91 (2025-11-09) from freeCodeCamp.org

# Word Search
# Given a matrix (an array of arrays) of single letters and a word to find, return the
# start and end indices of the word in the matrix.
#
# - The given matrix will be filled with all lowercase letters (a-z).
# - The word to find will always be in the matrix exactly once.
# - The word to find will always be in a straight line in one of these directions:
#   - left to right
#   - right to left
#   - top to bottom
#   - bottom to top
#
# For example, given the matrix:
#
# md
# [
#   ["a", "c", "t"],
#   ["t", "a", "t"],
#   ["c", "t", "c"]
# ]
#
# And the word "cat", return:
#
# md
# [[0, 1], [2, 1]]
#
# Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the
# indices for the "t" (end of the word).
