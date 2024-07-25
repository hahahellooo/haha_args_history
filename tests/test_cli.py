from haha_args_history.cli import hello_msg # ,hi_msg
#import haha_args_history.cli as cli

def test_hello():
    #m = cli.hello_msg()
    m = hello_msg()
    assert m == "hello"

#def test_hi():
   # m = hi_msg()
   # assert m == "hi"
