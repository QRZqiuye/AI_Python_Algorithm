def merge(left, right):
    """두 정렬된 리스트 left, right 를 병합하여 새 정렬 리스트 반환"""
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= 를 써서 stable(안정) 정렬 유지
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    # 남은 요소들 추가
    out.extend(left[i:])
    out.extend(right[j:])
    return out

def merge_sort(arr):
    """입력 리스트 arr의 정렬된 새 리스트를 반환 (원본 불변)"""
    if len(arr) <= 1:
        return arr[:]  # 안전을 위해 복사 반환
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# 사용 예
if __name__ == "__main__":
    a = [5, 2, 9, 1, 5, 6]
    print("original:", a)
    print("sorted:  ", merge_sort(a))
