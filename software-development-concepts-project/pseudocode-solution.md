## Pseudocode Solution

```text
define text
define pattern
if the entire text hasn't been searched:
  iterate to the next character of the text
  create a match_count variable and set it to 0
  if the entire pattern hasn't been searched:
    if this character from the pattern is equal to the character from text:
      increment the match_count variable
  if match_count is equal to the length of the pattern:
    pattern found!
```
