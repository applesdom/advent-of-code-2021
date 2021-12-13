def main():
  # Read commands from file
  command_list = []
  with open('input/2.txt') as f:
    for line in f.readlines():
      command_list.append(line.split(' '))

  # Part 1
  x = 0
  y = 0
  for command, value in command_list:
      if command == 'forward':
        x += int(value)
      elif command == 'down':
        y += int(value)
      elif command == 'up':
        y -= int(value)
  print('x=%d y=%d' % (x, y))
  print(x*y)

  # Part 2
  x = 0
  y = 0
  aim = 0
  for command, value in command_list:
      if command == 'forward':
        x += int(value)
        y += int(value) * aim
      elif command == 'down':
        aim += int(value)
      elif command == 'up':
        aim -= int(value)
  print('x=%d y=%d' % (x, y))
  print(x*y)   

if __name__ == '__main__':
  main()

