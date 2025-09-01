def heapify(arr, n, i):
    """arr[0..n-1] 범위에서 i를 루트로 하는 서브트리를 최대 힙으로 만든다"""
    largest = i          # 루트
    left = 2 * i + 1     # 왼쪽 자식
    right = 2 * i + 2    # 오른쪽 자식

    # 왼쪽 자식이 루트보다 크면 largest 갱신
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 현재 largest보다 크면 largest 갱신
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 루트가 아니면 교환 후 재귀적으로 heapify 호출
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 1. 주어진 배열을 최대 힙으로 변환
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. 하나씩 요소를 꺼내 힙 정렬
    for i in range(n - 1, 0, -1):
        # 루트(최대값)와 끝 요소 교환
        arr[0], arr[i] = arr[i], arr[0]
        # 줄어든 힙에 대해 heapify 수행
        heapify(arr, i, 0)


# 사용 예시
if __name__ == "__main__":
    data = [3, 1, 6, 5, 2, 4]
    print("원본:", data)
    heap_sort(data)
    print("정렬:", data)
