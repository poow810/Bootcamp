# # 제너레이터
# def my_range(first=0, last =10, step=1):
#     number = first
#     while number < last :
#         yield number
#         number +=step
#
# ranger = my_range(1,5)
# for x in ranger:
#     print(x)
#
#
# # 데커레이터
# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Running function:', func.__name__)
#         print('Positional arguments:', args)
#         print('Keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('Result:', result)
#         return result
#     return new_function
#
# @document_it
# def add_ints(a, b):
#     return a+b
#
# print(add_ints(3,5))
#
#
# # 재귀 함수
# def factorial_iter(n):
#     """
#     반복문을 사용한 팩토리얼 함수
#     :param n: n!
#     :return: integer 팩토리얼 계산 결과 값
#     """
#     result = 1
#     for k in range(1, n+1):
#         result = result * k
#     return result
#
#
# def factorial_recu(n):
#     """
#     재귀 함수를 사용한 팩토리얼 계산 결과 값
#     :param n: n!
#     :return: 자기 자신을 호출 또는 1
#     """
#     if n == 1:
#         return 1    # 끝나는 지점
#     else:
#         return factorial_recu(n-1) * n # 5와 n값이 4로 설정된 recu함수로 되돌아감
#                                        # 5 * 4 * ,,, 반복
#
# print(factorial_iter(3))
# print(factorial_recu(3))
#

def div_calc(a, b):
    """
    나누기 함수
    :param a: 분자
    :param b: 분모
    :return: 계산결과
    """
    return a / b
# print(div_calc(15, 3))
# print(div_calc(15, 0))

try:
    # raise Exception("쉬는 시간")
    raise TypeError("타입 에러")
    expr = input('분자 분모 입력 (띄어쓰기로 구분) : ').split()
    print(int(expr[0])/int(expr[1]))

except ValueError as err:
    print(f'숫자를 입력해주세요.({err})')
except ZeroDivisionError as err:
    print(f'분모에 0이 올 수 없습니다.({err})')
except IndexError as err:
    print(f'인덱스의 범위를 벗어났습니다.({err})')
except Exception as other:
    print(f'예외 발생! : ({other})')
else:     # 예외가 발생하지 않았을 때 실행
    print('프로그램 정상', end=' ')
finally:  # 예외 발생 여부와 상관없이 무조건 실행
    print('종료')