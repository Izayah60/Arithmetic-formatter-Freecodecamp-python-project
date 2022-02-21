def arithmetic_arranger(problems, *args):
  if len(problems) > 5:
    return "Error: Too many problems."
  arranged_problems = []
  for index, value in enumerate(problems):
    operation = value.split()
    if operation[1] not in "+-":
      return "Error: Operator must be '+' or '-'."

    if not (operation[0].isnumeric() and operation[2].isnumeric()):
      return "Error: Numbers must only contain digits."

    if len(operation[0]) > 4 or len(operation[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    longest = max(len(operation[0]), len(operation[2]))
    length = longest + 2

    line1 = (f"{operation[0]:>{length}}")
    line2 = operation[1] + f"{operation[2]:>{length-1}}"
    line3 = "-"*length

    try:
      arranged_problems[0] += (" " * 4) + line1
    except IndexError:
      arranged_problems.append(line1)

    try:
      arranged_problems[1] += (" " * 4) + line2
    except IndexError:
      arranged_problems.append(line2)

    try:
      arranged_problems[2] += (" " * 4) + line3
    except IndexError:
      arranged_problems.append(line3)
    
    if args:
      a = int(operation[0]) + int(operation[2]) if operation[1] == '+' else int(operation[0]) - int(operation[2])
      answer = f"{str(a):>{length}}"
      try:
        arranged_problems[3] += (" " * 4) + answer
      except IndexError:
        arranged_problems.append(answer)

  output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
  output = output + f"\n{arranged_problems[3]}" if args else output
  return output

#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

   # return arranged_problems
