# Text Wrap

You are given a string ***S*** and width ***W***.  
Your task is to wrap the string into a paragraph of width .


 **Function Description**
_wrap_  has the following parameters:
-   _string string:_  a long string
-   _int max_width:_  the width to wrap to

**Returns**
-   _string:_  a single string with newline characters ('\n') where the breaks should be

**Input Format**

The first line contains a string,  .  
The second line contains the width,  .

**Constraints**
1. 0 < len(string) < 1000
2. 0 < max_width < len(string)

**Sample Input 0**

    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4

**Sample Output 0**

    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ