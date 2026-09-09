def dedupe_preserve_order(items):
    # TODO: use a set to track seen values while building a new list
    # that preserves the original order of first appearances
    return list(dict.fromkeys(items))

print(dedupe_preserve_order([3, 1, 3, 2, 1]))