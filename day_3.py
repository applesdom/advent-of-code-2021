def main():
  # Read binary strings from file
  binary_string_list = []
  with open('input/3.txt') as f:
    for line in f.readlines():
      binary_string_list.append(line)

  # Part 1
  binary_sum = [0] * 12
  for binary_string in binary_string_list:
    for i in range(12):
      binary_sum[i] += 1 if (binary_string[i] == '1') else 0

  gamma = 0
  for i in range(12):
    if binary_sum[i] > len(binary_string_list) / 2:
      gamma += 2**(11 - i)
  epsilon = (2**12 - 1) - gamma
  print(gamma * epsilon)

  # Part 2
  oxy_list = binary_string_list.copy()
  for i in range(12):
    if len(oxy_list) == 1:
      break
    binary_sum = 0
    print('i=%d' % i)
    for binary_string in oxy_list:
      print(binary_string[0:11])
      binary_sum += 1 if (binary_string[i] == '1') else 0
    valid_bit = '0' if (binary_sum < len(oxy_list) / 2) else '1'
    print(valid_bit)
    for j in range(len(oxy_list) - 1, -1, -1):
      if oxy_list[j][i] != valid_bit:
        del oxy_list[j]

  co2_list = binary_string_list.copy()
  for i in range(12):
    if len(co2_list) == 1:
      break
    binary_sum = 0
    for binary_string in co2_list:
      binary_sum += 1 if (binary_string[i] == '1') else 0
    valid_bit = '1' if (binary_sum < len(co2_list) / 2) else '0'
    for j in range(len(co2_list) - 1, -1, -1):
      if co2_list[j][i] != valid_bit:
        del co2_list[j]
  print(int(oxy_list[0], 2) * int(co2_list[0], 2))

if __name__ == '__main__':
  main()

