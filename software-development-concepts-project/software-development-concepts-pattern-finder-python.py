text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
for index in range(len(text)):
  match_count = 0
  for char in range(len(pattern)):
    if pattern[char] == text[index + char]:
      match_count += 1
  if match_count == len(pattern):
    print("Pattern found!")
