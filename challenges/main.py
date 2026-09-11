def unmatched_skus(warehouse_a, warehouse_b):
    all_skus = warehouse_a.union(warehouse_b)
    shared_skus = warehouse_a.intersection(warehouse_b)
    unmatched = all_skus.difference(shared_skus)

    return unmatched
print(unmatched_skus({"A1", "A2"}, {"A2", "A3"}))