def reverseVowels(s):
  """
  :type s: str
  :rtype: str
  """
  s = list(s)
  vow_ind = []
  vow = []
  for i, c in enumerate(s):
      if c in "aieouAIEOU":
          vow_ind.append(i)
          vow.append(c)
  for i, char in zip(vow_ind, reversed(vow)):
      s[i] = char
      
  return ''.join(s)

print(reverseVowels("leetcode"))
print(reverseVowels("hello"))
print(reverseVowels("aA"))
