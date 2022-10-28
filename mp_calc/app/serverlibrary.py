def mergesort(array, byfunc=None):
  if len(array) > 1:
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    mergesort(left, byfunc)
    mergesort(right, byfunc)

    i = j = k = 0

    while (i < len(left)) and (j < len(right)):
      if byfunc(left[i]) <= byfunc(right[j]):
        array[k] = left[i]  
        i += 1
      else:
        array[k] = right[j]
        j += 1
      k += 1
    
    while (i < len(left)):
      array[k] = left[i]
      i += 1
      k += 1
    
    while (j < len(right)):
      array[k] = right[j]
      j += 1
      k += 1
    return array


class Stack:
  def __init__(self):
    self._items = []  

  def push(self, item):
    return self._items.append(item)
  
  def pop(self):
    return self._items.pop() if self.is_empty else None
  
  def peek(self):
    return self._items[-1]
  
  def is_empty(self):
    return self._items == []


class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self._expression = string

  @property
  def expression(self):
    return self._expression

  @expression.setter
  def expression(self, new_expr):
    self._expression = new_expr if (isinstance(new_expr, str)) and (all(c in EvaluateExpression.valid_char for c in new_expr)) else ""

  def insert_space(self):
    self._expression = list(self._expression)
    for i in range(len(self._expression)):
      if self._expression[i] in "+-*/()":
        self._expression[i] = f" {self._expression[i]} "
    return "".join(self._expression)

    
  def process_operator(self, operand_stack, operator_stack):
    operator = operator_stack.pop()
    top_item = int(operand_stack.pop())
    bottom_item = int(operand_stack.pop())

    if operator == "+":
      operand_stack.push(bottom_item + top_item)

    elif operator == "-":
      operand_stack.push(bottom_item - top_item)

    elif operator == "*":
      operand_stack.push(bottom_item * top_item)

    elif operator == "/":
      operand_stack.push(bottom_item // top_item)

  def evaluate(self):
    operand_l = "0123456789"
    operator_l = "+-*/"

    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()

    for i in tokens:
        if (i in operand_l):
            operand_stack.push(i)
        
        elif (i == "("):
            operator_stack.push(i)
        
        elif (i == ")"):
            while operator_stack.peek() != "(":
                self.process_operator(operand_stack, operator_stack)
            operator_stack.pop()

        elif (i in operator_l):
            while (not operator_stack.is_empty()) and (operator_stack.peek() in "*/"):
                self.process_operator(operand_stack, operator_stack)
            operator_stack.push(i)
    
    while (not operator_stack.is_empty()):
        self.process_operator(operand_stack, operator_stack)

    return operand_stack.peek()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





