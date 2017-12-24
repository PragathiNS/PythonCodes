# anti-vowel
def anti_vowel(text):
  ret = ""
  for i in text:
    if i not in "aeiouAEIOU":
      ret = ret + i
    else:
      continue
  return ret
