def comb_bin(n, res=''):
  if n == 0:
    return
  if res == '':
    res = '0'*n
    print(res)
  
  str_print_0 = res[:n-1] + '0' + res[n:]
  str_print_1 = res[:n-1] + '1' + res[n:]
  print(str_print_1)

  comb_bin(n-1, str_print_0)
  comb_bin(n-1, str_print_1)

comb_bin(4)

# output from print
# 0000
# 0001
# 0010
# 0100
# 1000
# 1100
# 0110
# 1010
# 1110
# 0011
# 0101
# 1001
# 1101
# 0111
# 1011
# 1111
