# Python If-else
## Task
Given an integer, _n_, perform the following conditional actions:

- If _n_ is odd, print **Weird**
- If _n_ is even and in
the inclusive range of **2** to **5**, print **Not Weird**
- If _n_ is even and in the inclusive range of **6** to **20**, print **Weird**
- If _n_ is even and greater than **20**, print **Not Weird**

## Input format
A single line containing a positive integer, _n_.

## Constraints
- 1 ≤ n ≤ 100

### Output format
Print **Weird** if the number is weird. Otherwise, print 
**Not Weird**.

### Sample Input 0

```
3
```
### Sample Output 0
```
Weird
```

## Explanation 0 
_n_ = 3

_n_ is odd and odd numbers are weird, so print **Weird**

### Sample Input 1
```
24
```
### Sample Output 1
```
Not Weird
```

## Explanation 1
_n_ = 24

_n_ > 20 and _n_ is even, so it is not weird