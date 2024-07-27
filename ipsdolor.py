def quick_sort_signal(signal):
    """
    Sorts a signal using the quick sort algorithm.

    Parameters:
    signal (list): The signal to be sorted.

    Returns:
    list: The sorted signal.
    """
    if len(signal) <= 1:
        return signal
    pivot = signal[len(signal) // 2]
    left = [x for x in signal if x < pivot]
    middle = [x for x in signal if x == pivot]
    right = [x for x in signal if x > pivot]
    return quick_sort_signal(left) + middle + quick_sort_signal(right)

# Example usage
signal = [64, 34, 25, 12, 22, 11, 90]
sorted_signal = quick_sort_signal(signal)
print("Sorted signal using Quick Sort:", sorted_signal)
