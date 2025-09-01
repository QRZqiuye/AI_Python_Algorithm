def counting_sort(arr):
    if not arr:  # 빈 배열 처리
        return arr

    # 1. 최소값과 최대값 찾기
    min_val = min(arr)
    max_val = max(arr)

    # 2. 계수 배열 생성 (범위만큼 크기)
    count = [0] * (max_val - min_val + 1)

    # 3. 각 값 등장 횟수 세기
    for num in arr:
        count[num - min_val] += 1

    # 4. 누적 합으로 변환 (안정 정렬 위해)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 5. 결과 배열 생성 (역순으로 순회하여 안정성 유지)
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output


# 사용 예시
if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    print("원본:", data)
    sorted_data = counting_sort(data)
    print("정렬:", sorted_data)
