def binary_search(a_list, item):
    a_list.sort()  # Just in case list isn't sorted
    print(f"Sorted list: {a_list}")
    
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid = (first + last) // 2
        print(f"Checking index {mid} → {a_list[mid]}")

        if a_list[mid] == item:
            print(f"✅ Found {item} at index {mid}")
            return mid
        elif item < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1

    print(f"❌ {item} not found")
    return -1


if __name__ == "__main__":
    binary_search([1, 2, 73, 3, 4, 5], 3)
