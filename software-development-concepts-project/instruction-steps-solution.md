

# Instruction Steps Solution

1. Input the `text` that we plan to search and the `pattern` that we hope to find.  

2. Has the entire `text` been searched?

   If not, continue to step 3.

   If so, skip to step 8.

3. Iterate to the next character in the `text`.

4. To keep track of similar characters between the `pattern` and the `text`, we establish a `match_count` variable and initially set it to `0`.  

5. Has the entire `pattern` been searched?  

   If not, continue to step 6.

   If so, go back to step 2.

6. Iterate to next character in `pattern` . 

7. Does this character from the `pattern` match the character from the `text`?  

   If not, go straight back to step 5.

   If so, increment `match_count`, then go back to step 5.

8. Does `match_count` equal the length of the `pattern`?  

   If not, go back to step 2.

   If so, `pattern` found!  