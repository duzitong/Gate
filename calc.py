def operate(a, b, gate_type):
    if gate_type == 0:
        return a & b
    elif gate_type == 1:
        return ~a & b
    elif gate_type == 2:
        return a & ~b
    elif gate_type == 3:
        return a | b
    elif gate_type == 4:
        return a ^ b

def gate_output_generator(line):
  for i in range(len(line)):
    for j in range(i+1, len(line)):
      for gate_type in range(5):
        yield operate(line[i], line[j], gate_type) 

def operate_line(line):
  output = set(gate_output_generator(line))
  for i in output:
    yield sorted(line + [i])
