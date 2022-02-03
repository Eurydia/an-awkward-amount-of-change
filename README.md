# an-awkward-amount-of-change

Determine amount of money you can pay that forces the other person to give you an awkward amount of change.

## Problem

We need to extend the length of a floating platform with a length of L.
We have N piles of wooden planks.
Planks from pile 1 all have the length of l_1.
Planks from pile 2 all have the length of l_2.
Planks from pile N all have the length of l_N

**What are the sets of planks we can use to extend the floating platform** 
Such that
1. For every planks, at least one unit of length of must stay on the platform. (No plank is free floating in the air)
2. Every arrangements of set of planks must obey rule (1.)

### Example 0:  
```
platform of length L(10)
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
(let's say that "=====|" is equal to one unit of length)
```

We have 3 piles of wooden planks with lengths of 
```
=====| (1)
=====|=====| (2)
=====|=====|=====|=====|=====| (5)
```

Using 4x2 and 1x5
and 2-2-2-2-5 arrangement.
```
     2     |     2     |     2     |     2     |     5                       |
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
------------------------------------------------------------
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
```

5-2-2-2-2 arrangement
```
     5                       |     2     |     2     |     2     |     2     |
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
------------------------------------------------------------
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
```

We can clearly see that the last piece of wood will fall down.
So, this set of planks is not valid (4x2 + 1x5)

Let's pick a different set of planks.
This time 3x2 and 1x5.
2-2-2-5 arrangement.
```
     2     |     2     |     2     |     5                       |
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
------------------------------------------------------------
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
```

5-2-2-2 arrangement.
```
     5                       |     2     |     2     |     2     |
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
------------------------------------------------------------
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
```

2-5-2-2 arrangement.
```
     2     |     5                       |     2     |     2     |
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
------------------------------------------------------------
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
```

2-2-5-2 arrangement.
```
     2     |     2     |     5                       |     2     |
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
------------------------------------------------------------
=====|=====|=====|=====|=====|=====|=====|=====|=====|=====|
```

This time every arrangements is valid.
So this set (3x2 + 1x5) is **one of the answer** we are looking for.