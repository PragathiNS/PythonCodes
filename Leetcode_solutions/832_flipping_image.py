def flipAndInvertImage(A):
  """
  :type A: List[List[int]]
  :rtype: List[List[int]]
  """
  # Reverse each row
  for row in range(len(A)):
      A[row].reverse()
  # Invert the Image
  for i in range(len(A)):
      for j in range(len(A)):
          if A[i][j] == 0:
              A[i][j] = 1
          else:
              A[i][j] = 0

  return (A)
        
print (flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print (flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
