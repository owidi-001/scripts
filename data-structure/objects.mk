#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 08:04:32 2021

@author: whoami
"""

### accesors => these are methods that do not change the state of the object eg ###
response='Something something'
response.startswith('y')
### mutators/update methods => class methods that returns a new object on call ###
mylist=[3,4,2,5,6,4,5]
mylist.sort()

'''
### Python in-built classes ###
=======================

1:bool() => defaults to false
    can be created from a nonboolean data type eg:
        bool(int,str,list)
        defaults to true for a nonzero,empty integers,list and strings respectively

2:int and float => are primary numerical classes
    int() constructor returns 0 by default
    numerical data can also be represented in binary,octal,hexadecimal formart eg:
        0b1011,0o52,0x7f
        
        eg 0x7f*16 =2032
        
    floats may use scientific notations eg 6.022e23 may represent 6.022 × 10**23
    eg 4e2 =400.0
3: sequences: list,set,str,tuple,frozenset
    list [] represents a sequence of arbitrary objects,zeroindexed,arraybased
    tuple () is an immutable version of a list
    string '',"" represents immutable sequence of characters
    set {} elements without duplicates and order elements consist of only immutable types eg int,str not list.

4: dict class
    represents a dictionary or mapping from a set of distinct keys and mapped values



### Expressions,operators and precedence ###
====================================
    operators can be combined to form expressions
    The semantics of the expression depend on the order & type of operators
    
logical operators
    not-unary operator
    and-conditional
    or-conditional
    
equality operators
    is-same identity
    is not-different identity
    ==-equal
    !=-not equal
    
comparison operators
    < proper subset
    > proper superset
    <= subset
    >= superset
Arithmetic operators
    +-
    */
    //
    %
    
Bitwise operators
    ~ bitwise complement
    & bitwise and
    | bitwise or
    ^ bitwise exclusive-or
    << shift bits left,filling in with zeros
    >> shift bits right, filling in with sign bit
    
Sequence operators
    s[j] element at index j
    s[start:stop] slice including index [start,stop]
    s[start:stop:step] slice including indices [start,stop+step] N/B upto but not inluding stop
    s+t concatenation sequence
    k*s short for s+s...+s ie s (k times)
    val in s containment operators
    val not in s non-containment
    
### sequence operators ###
==================
    s == t equivalent (element by element)
    s != t not equivalent
    s < t lexicographically less than
    s <= t lexicographically less than or equal to
    s > t lexicographically greater than
    s >= t lexicographically greater than or equal to

    
### Operators for Sets and Dictionaries ###
==================================
Sets and frozensets support the following operators:    
    key in s containment check
    key not in s non-containment check
    s1 == s2 s1 is equivalent to s2
    s1 != s2 s1 is not equivalent to s2
    s1 <= s2 s1 is subset of s2
    s1 < s2 s1 is proper subset of s2
    s1 >= s2 s1 is superset of s2
    s1 > s2 s1 is proper superset of s2
    s1 | s2 the union of s1 and s2
    s1 & s2 the intersection of s1 and s2
    s1 − s2 the set of elements in s1 but not s2
    s1 ˆ s2 the set of elements in precisely one of s1 or s2

### Dictionary operators ###
==================
d[key]  value associated with given key
d[key] = value set (or reset) the value associated with given key
del d[key]
key in d
key not in d
d1 == d2
d1 != d2


remove key and its associated value from dictionary
containment check
non-containment check
d1 is equivalent to d2
d1 is not equivalent to d2

### Extended assignement operator

alpha=[1,2,3]
beta=alpha
beta+=[4,5]
beta=beta+=[6,7]
print(alpha)


## Loops
Python has 2 loops:
    while
    for
While allows for general repeatetion testing based on a Boolean condition
For loop provides a covenient iteration over a defined series eg list,string,numbers in a given range

>>> data='owidirexe the ninaj kid'
>>> j=0
>>> while j<len(data) and data[j] != 'x':
...     j+=1
...     print(data[j])



'''
