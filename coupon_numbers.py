"""
10 ~ 100,000개의 쿠폰 번호 발행
"""
import uuid
import csv


def create_coupon(product, max_create):
    idx = 0
    coupon_result = []

    # 쿠폰은 10개가 최소 발행 기준임.
    if max_create >= 10:
        while idx < max_create:
            coupon_result.append(str(uuid.uuid4()))
            idx += 1

        # 중복 검사
        if len(coupon_result) != len(set(coupon_result)):
            create_coupon(max_create)

        # csv 파일 생성
        with open('{}_coupon_code_list.csv'.format(product), 'w', newline='') as csvfile:
            coupon_writer = csv.writer(csvfile, delimiter='\n')
            coupon_writer.writerow(coupon_result)

        return coupon_result

    else:
        return "쿠폰은 10개 이상부터 생성할 수 있습니다."
