words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over',
         'the', 'lazy', 'dog']

# a

print([word.upper() for word in words])

print([word.lower() for word in words])

print([len(word) for word in words])

print([word for word in words if len(word) >= 4])
