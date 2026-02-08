# Python Syntax – Correct vs Wrong

A quick reference for Python syntax with examples of **correct** and **wrong** usage.

---

## 1. Indentation

Python uses indentation to define blocks (no `{}`). Use **4 spaces** per level; be consistent.

### ✅ Correct

```python
if True:
    print("inside block")
    if 1:
        print("nested block")
```

### ❌ Wrong

```python
# Tabs mixed with spaces (can cause IndentationError or hidden bugs)
if True:
	print("tab used")

# No indentation after colon
if True:
print("forgot to indent")

# Inconsistent spaces
if True:
  print("2 spaces")
    print("4 spaces")
```

---

## 2. Comments

### ✅ Correct

```python
# Single-line comment
x = 1  # inline comment

"""
Multi-line comment or docstring.
Often used at top of file or under def/class.
"""
```

### ❌ Wrong

```python
# No multi-line comment with /* */ – that's not Python
/* comment */
```

---

## 3. Identifiers (Names)

Names can use letters, digits, and underscores. Cannot start with a digit.

### ✅ Correct

```python
name = "api"
server_count = 3
_config = {}
```

### ❌ Wrong

```python
2nd_server = 1   # cannot start with digit
my-var = 1       # hyphen not allowed
class = 1        # 'class' is a keyword
```

---

## 4. Strings

### ✅ Correct

```python
s1 = 'single quotes'
s2 = "double quotes"
s3 = "embed 'quotes' inside"
s4 = 'embed "quotes" inside'
multiline = """line one
line two"""
path = "C:\\Users\\file.txt"   # or use raw: r"C:\Users\file.txt"
```

### ❌ Wrong

```python
s = 'unclosed string        # missing closing quote
s = "mismatched quotes'     # different open/close
```

---

## 5. Numbers

### ✅ Correct

```python
a = 42
b = 3.14
c = 1_000_000
d = 0xFF
e = 2 + 3j
```

### ❌ Wrong

```python
a = 1,000,000   # comma is tuple, not number: (1, 0, 0)
b = 10.5.6      # invalid literal
```

---

## 6. Lists and Tuples

### ✅ Correct

```python
lst = [1, 2, 3]
empty_list = []
nested = [1, [2, 3]]

tup = (1, 2, 3)
single = (1,)    # single-element tuple needs comma
```

### ❌ Wrong

```python
lst = [1, 2, 3   # missing ]
lst = (1)        # not a tuple, just 1 in parentheses; use (1,)
```

---

## 7. Dictionaries

### ✅ Correct

```python
d = {"a": 1, "b": 2}
d = {"key": "value", "num": 42}
empty = {}
```

### ❌ Wrong

```python
d = {a: 1}           # keys must be quoted (unless variable name)
d = {"a" 1}          # missing colon
d = {"a": 1, "b": 2  # missing }
```

---

## 8. If / Elif / Else

### ✅ Correct

```python
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
```

### ❌ Wrong

```python
if x > 0
    print("positive")    # missing colon after condition

if x > 0:
print("positive")        # body must be indented

else:                    # else without matching if
    print("?")
```

---

## 9. For and While Loops

### ✅ Correct

```python
for x in [1, 2, 3]:
    print(x)

for i, name in enumerate(names):
    print(i, name)

while n > 0:
    n -= 1
```

### ❌ Wrong

```python
for x in [1, 2, 3]
    print(x)             # missing colon

for x in [1, 2, 3]:
print(x)                 # body not indented

while n > 0:             # missing colon (same as if)
    n -= 1
```

---

## 10. Functions

### ✅ Correct

```python
def greet(name):
    return f"Hello, {name}"

def no_args():
    pass

def with_default(x=0):
    return x
```

### ❌ Wrong

```python
def greet(name)
    return "hi"          # missing colon

def greet(name):
return "hi"              # body not indented

def ():                  # missing function name
    pass
```

---

## 11. Classes

### ✅ Correct

```python
class Server:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(self.name)
```

### ❌ Wrong

```python
class Server
    def __init__(self):  # missing colon after class

class Server:
def start(self):         # method not indented under class
    pass
```

---

## 12. Try / Except / Finally

### ✅ Correct

```python
try:
    x = int("42")
except ValueError:
    x = 0
finally:
    print("done")
```

### ❌ Wrong

```python
try
    x = 1               # missing colon
except ValueError
    x = 0               # missing colon
```

---

## 13. Common Syntax Errors

| Error | Cause | Fix |
|-------|--------|-----|
| `SyntaxError: invalid syntax` | Missing `:`, wrong indentation, unclosed bracket/quote | Add colon after `if`/`for`/`def`/`class`, close `()[]{}""` |
| `IndentationError` | Tabs vs spaces, or no indent after block | Use 4 spaces consistently; indent block under `if`/`for`/`def` |
| `NameError: name 'x' is not defined` | Using variable before assignment or typo | Define `x` first or fix spelling |
| `EOL while scanning string` | Unclosed string | Add closing `'` or `"` |

---

## 14. Quick Checklist

- **Blocks:** Colon `:` at end of `if`, `elif`, `else`, `for`, `while`, `def`, `class`, `try`, `except`, `finally`.
- **Body:** Indent the next line(s) under that colon (same indent = same block).
- **Strings:** Match opening and closing quotes; escape or use raw for backslashes.
- **Tuples:** Single value needs comma: `(1,)`.
- **Dict keys:** Use quotes for string keys: `{"a": 1}`.
- **No trailing commas in wrong places:** `(1,)` is OK; `(1,,)` is not.

---

*Use this with your other demos (collections, control_flow, function, error_handling) for a full Python syntax and usage reference.*
