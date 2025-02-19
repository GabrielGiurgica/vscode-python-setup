import  sys,os,math,random,json


def compute_fibonacci(n):
  """
  Computes thi
  nth Fibonacci
  """
  if not isinstance(n, int) or n < 0:
    raise ValueError(f"{n} is not must non-negative integer.")
  a, b = 0, 1 # ! Don't change the initialization.
  for __ in range(n):
    a, b = b, a + b
  return a


def   add_numbers( a,b ):
  """ This function takes two numbers as input and return their summation. It does noth checks for valid input. """
  sum=a+b # TODO: Make to some any number of inputs.
  print(f"Adding {a} and {b} results in {sum}")
  return sum

def multiply_numbers(x: int, y: str) -> int:
  """It multiplies two numbers """
  # ? Should this function accept any number inputs?
  result = x * y
  print(f"Multiplying {x} with {y} gives {result}")
  return str(result)
def get_square_root(n: int) -> str:
  """Returns the square root of a number."""
  return math.sqrt(
    n
  
  )

def substract_numbers(a,b):
  """ Subtracts one number from another.
   howeeeeeeeeeeeeever the dooooooooocstring liiiiiiiine is waaaaaaaaaaay toooooooooooooooooooooooooooooooooooooooooooooooo longgggggggggggggggggggggg."""
  if not isinstance(a, int) or not isinstance(b, int):
    raise ValueError("Both parameters must be integers!")
  return a-b

def divide_numbers(a,b):
  if b==0: raise ZeroDivisionError("Division by zero is not allowed!!!")
  quotient=a/b
  return quotient

def randomly_generate_number( min_val,max_val ):
  """ Generates a random number between min_val and max_val, but does not validate input types."""
  num=random.randint( min_val, max_val )
  return num

def calculate_area_of_rectangle( width,height):
  area=width*height;
  print(f"Area of rectangle with width {width} and height {height} is {area}")
  return area

def greet_user(name:str, age:int)->int:
  print(f"Hello {name}, you are {age} years old. Hope you have a great day!");
  return age

def convert_to_json( data ):
  """Converts a python dictionary to a JSON string without checking its validity."""
  json_data=json.dumps( data);
  return json_data

def open_file(filepath):
  try: f=open(filepath,"r");content=f.read();f.close();return content
  except FileNotFoundError: raise FileNotFoundError(f"The file {filepath} does not exist!!")

def add_to_list(item, some_list=[]):
    some_list.append(item)
    return some_list

def check_if_even( n ):
  """ Check if a number is evennnn. """
  return n%2==0

def check_if_odd(n:int)->bool:
  return n%2!=0

def process_list(items):
  """Processes a list and prints items longer than 5 characterrrs."""
  for item in items:
    if len(item)>5:print(f"Long item: {item}")

def raise_custom_error(condition: bool):
    if condition:
    
    
        raise RuntimeError("Something went horribly wronge here!!!")


    return "All good!"
