def quick_sort(arr):
    # 원소가 1개 이하라면 이미 정렬된 상태
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 피벗을 가운데 값으로 선택
    left = [x for x in arr if x < pivot]  # 피벗보다 작은 값
    middle = [x for x in arr if x == pivot]  # 피벗과 같은 값
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 값

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    data = [35, 12, 43, 8, 51, 27, 99, 18]
    print("정렬 전:", data)
    sorted_data = quick_sort(data)
    print("정렬 후:", sorted_data)
