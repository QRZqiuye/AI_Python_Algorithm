def find_min_max(arr):
    if not arr:
        return None, None  # 빈 배열 처리

    minimum = maximum = arr[0]
    for num in arr[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return minimum, maximum

def min_max_divide(arr, low, high):
    # 원소가 하나인 경우
    if low == high:
        return arr[low], arr[low]

    # 원소가 두 개인 경우
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # 배열을 반으로 나누어 처리
    mid = (low + high) // 2
    min1, max1 = min_max_divide(arr, low, mid)
    min2, max2 = min_max_divide(arr, mid + 1, high)

    return min(min1, min2), max(max1, max2)

# 사용 예시
if __name__ == "__main__":
    data = [3, 1, 8, -2, 7, 5]
    mn, mx = min_max_divide(data, 0, len(data) - 1)
    print("배열:", data)
    print("최소값:", mn, "최대값:", mx)

# 사용 예시
if __name__ == "__main__":
    data = [3, 1, 8, -2, 7, 5]
    mn, mx = find_min_max(data)
    print("배열:", data)
    print("최소값:", mn, "최대값:", mx)
