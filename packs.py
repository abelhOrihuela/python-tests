import re

str1 = "'I AM NOT YELLING', sehasaid. Tough we knew it to not be true"
print(str1)

new = re.sub('[a-z]', '', str1)
print(new)

new = re.sub('[A-Z]', '', str1)
print(new)

new = re.sub('[.,;\']', '', str1)
print(new)
