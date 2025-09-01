def counting_sort_for_radix(arr, exp):
    """
    arr를 exp 자리수 기준으로 계수 정렬 (안정 정렬)
    exp = 1 → 1의 자리, exp = 10 → 10의 자리 ...
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 0~9 자릿수 카운트

    # 1. 해당 자릿수의 값 카운트
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # 2. 누적 합 → 실제 위치 계산용
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 3. 안정 정렬 위해 뒤에서부터 순회
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        count[index] -= 1
        output[count[index]] = arr[i]

    # 4. 정렬 결과를 원본 배열에 복사
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # 최대값을 기준으로 자릿수 결정
    max_val = max(arr) if arr else 0
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10


# 사용 예시
if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print("원본:", data)
    radix_sort(data)
    print("정렬:", data)
