def main():
  # Read depth values from file
  depth_list = []
  with open('input/1.txt') as f:
    for line in f.readlines():
      depth_list.append(int(line))

  # Part 1
  prev_depth = 1000000 # always decrease for first depth value
  increase_count = 0
  for depth in depth_list:
    increase_count += 1 if (depth > prev_depth) else 0
    prev_depth = depth
  print(increase_count)

  # Part 2
  increase_count = 0
  for i in range(len(depth_list) - 3):
    increase_count += 1 if (depth_list[i] < depth_list[i+3]) else 0
  print(increase_count)
      

if __name__ == '__main__':
  main()

