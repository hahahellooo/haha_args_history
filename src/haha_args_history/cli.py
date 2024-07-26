import argparse
from haha_args_history.db.utils import count, top
from tabulate import tabulate

def hello_msg():
    return "hello"

def cmd():
    msg = hello_msg()
    print(msg)

    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-s', '--scount') 
    parser.add_argument('-t', '--top', type = int)
    parser.add_argument('-d', '--dt' )
    parser.add_argument('-p', '--pretty', action='store_true')
    args = parser.parse_args()
    print(args.scount, args.top, args.dt, args.pretty)

    if args.scount: 
        df = count(args.scount)
        print(f"{args.scount} 사용 횟수는 {df}회 입니다")
        # TODO 명령어 카운트
    elif args.top:
        print(f"-t => {args.top}")
        if args.dt:
            df = top(args.top, args.dt)
            return df
            if args.pretty == True: 
                print(tabulate(df))
            # TODO 특정 날짜의 명령어 TOP N
            else:
                return df
        else: 
            parser.error("-t 옵션은 -d 옵션과 함께 사용하시오!")
    else:
        parser.print_help()

