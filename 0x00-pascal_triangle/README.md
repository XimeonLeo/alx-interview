# Pascal's Triangle

## Task

**Pascal's Triangle**

Create a function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`.
- You can assume `n` will always be an integer.

## Example

```python
from pascal_triangle import pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```


## Output
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]

