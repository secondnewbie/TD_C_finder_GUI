import argparse

parser = argparse.ArgumentParser(description='Arugment 설명')#parser객체 생성

#parser에 인자 추가시키기, first, second, third 인자 추가
parser.add_argument('--first', type=int)
parser.add_argument('--second', type=int)
parser.add_argument('--third', type=str)

#parse_args()를 통해 parser객체의 인자들 파싱
args = parser.parse_args()

print(args)
print(type(args))

#인자에 해당하는 인수를 받아 저장할 변수 초기화 1)각 변수에 저장하기
first="a"
second="b"
third="c"

#변수 초기화 확인
print(first, second, third)

#args객체의 인자에 값이 들어오면 각 변수에 args의 인수를 대입한다.
if args.first != None: first=args.first
if args.second != None: second=args.second
if args.third != None and len(args.third) >= 1: third=args.third

#변수에 대입된 args객체의 각 인수를 출력
#print("first=%d, second=%d, third=%s" % (first, second, third))
#print("first={0}, second={1}, third={2}".format(first, second, third))
print(f"first={first}, second={second}, third={third}")

#args_list 리스트를 만들어 args객체의 인수를 추가시켜준다.2)리스트에 저장하기
args_list=[]
args_list.append(args.first)
args_list.append(args.second)
args_list.append(args.third)

#리스트의 값들 출력
for i in range(len(args_list)):
    print(args_list[i])

#args의 딕셔너리 값을 대입하고 출력한다.3)딕셔너리로 저장하기
args_dict=vars(args)
print(args_dict)
for i in args_dict.values():
    print(i)