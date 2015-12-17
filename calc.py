def operate(a, b, length, gate_type):
  gates = [[[0, 0], [0, 1]],  #  a and  b
           [[0, 0], [1, 0]],  #  a and ~b
           [[0, 1], [0, 0]],  # ~a and  b
           [[1, 0], [0, 0]],  # ~a and ~b
           [[0, 1], [1, 0]],  #  a xor  b
          ]
  output = 0
  for i in range(length):
    output = (output + gates[gate_type][(a >> (length-i-1)) & 1][(b >> (length-i-1) & 1)]) << 1
  return output >> 1

def gate_output_generator(line, length):
  for i in range(len(line)):
    for j in range(i+1, len(line)):
      for gate_type in range(5):
        yield operate(line[i], line[j], length, gate_type) 

def operate_line(line, length):
  output = set(gate_output_generator(line, length))
  for i in output:
    yield sorted(line + [i])
