# === Stage 61: Add performance timing for core list and search operations ===
# Project: PantryMate
import time

def benchmark_operations(data):
    """Benchmark core list and search operations."""
    iterations = 100
    results = {}

    # List length operation
    start = time.perf_counter()
    for _ in range(iterations):
        len(data)
    end = time.perf_counter()
    results['list_len'] = (end - start) / iterations * 1e6  # microseconds

    # Search operation
    search_items = ['apple', 'banana', 'cherry', 'date']
    for item in search_items:
        start = time.perf_counter()
        for _ in range(iterations):
            item in data
        end = time.perf_counter()
        results[f'search_{item}'] = (end - start) / iterations * 1e6

    # Filter operation
    min_quantity = 50
    start = time.perf_counter()
    for _ in range(iterations):
        [item for item in data if item['quantity'] >= min_quantity]
    end = time.perf_counter()
    results['filter_low_quantity'] = (end - start) / iterations * 1e6

    return results
