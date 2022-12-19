import sys
import getopt

args_list = sys.argv[1:]
short_opts = "xyh:"
long_opts = ["width=", "height=", "help"]

try:
    option, argument = getopt.getopt(args_list, shortopts=short_opts, longopts=long_opts)
    #print(option, argument)
    print(option)
    for currentArgument, currentValue in option:
        print(currentArgument, currentValue)
    # for arg in argument:
        #print(arg)
except getopt.error as err:
    print(str(err))