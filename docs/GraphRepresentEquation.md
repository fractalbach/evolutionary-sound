"use strict";
~~~

Using Graphs to Represent Equations
==========================================================================

Tree Graphs can be used to present equations.  In turn, these graphs can be stored as an encoded Array.  In the context of the *Evolutionary Sound* project, these equations will be used to affect sound.  The stored Array will be saved in the "DNA", and will be decoded when the sounds are created.

~~~ javascript 
var hello = 'there';
~~~

Encodings
--------------------------------------------------------------------------

Operators will be treated as functions.  For example, 1 + 1 will be treated as Add(1,1) and then encoded into A11.  This allows storage as an array, because the decoder can understand that "A" is equivalent to Add(), and the parameters are the numbers that follow




Test
--------------------------------------------------------------------------


Hello! Testing an equation here: $x^2 + y^2 = z^2$
and another equation $$\sum_{0 \leq x \leq n} {x} = \frac{x(x+1)}{2}$$
