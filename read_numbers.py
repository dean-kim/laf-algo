"""
숫자 배열을 받아 문자열로 변환
"""


def read_num(arr):

    # 배열의 요소가 하나일 경우 바로 결과를 반환
    if len(arr) == 1:
        return str(arr[0])

    # 배열의 요소가 2개 이상일 경우
    else:
        sorted_input = sorted(arr)
        result_list = []
        temp_result = []
        str_result = []
        former_num = sorted_input[0] - 1

        # 연속된 숫자들을 그룹화
        for num in sorted_input:
            if num - former_num == 1 and sorted_input.index(num) < len(sorted_input) - 1:
                temp_result.append(num)
            elif num - former_num == 1 and sorted_input.index(num) == len(sorted_input) - 1:
                temp_result.append(num)
                result_list.append(temp_result)
            elif num - former_num > 1 and sorted_input.index(num) < len(sorted_input) - 1:
                result_list.append(temp_result)
                temp_result = []
                temp_result.append(num)
            else:
                result_list.append(temp_result)
                temp_result = []
                temp_result.append(num)
                result_list.append(temp_result)

            former_num = num

        # 각 그룹을 형식화
        for element in result_list:
            if len(element) > 1:
                tmp_str = '{}~{}'.format(element[0], element[len(element)-1])

            else:
                tmp_str = '{}'.format(element[0])

            str_result.append(tmp_str)

        return ", ".join(x for x in str_result)
