def bucket_sort(arr, bucket_size=10):
    if not arr:
        return arr

    # 1. 최소/최대값 찾기
    min_val, max_val = min(arr), max(arr)

    # 2. 버킷 개수 계산
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # 3. 각 원소를 적절한 버킷에 분배
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    # 4. 각 버킷 정렬 (여기서는 내장 정렬 사용)
    for b in buckets:
        b.sort()

    # 5. 모든 버킷 합치기
    sorted_arr = []
    for b in buckets:
        sorted_arr.extend(b)

    return sorted_arr


# 사용 예시
if __name__ == "__main__":
    data = [42, 32, 33, 52, 37, 47, 51]
    print("원본:", data)
    sorted_data = bucket_sort(data, bucket_size=5)
    print("정렬:", sorted_data)
