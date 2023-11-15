import re

text = "the quick brown fox jumps over the lazy dog"

print("All occurances of 'the': " + str(re.findall('the', text)))
print("Index of first whitespace: ", re.search('\s', text).start())
print("Replace whitespace with underscore: " + re.sub('\s', '_', text))

