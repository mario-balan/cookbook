# an example of argument parsing with getopt

import sys, getopt

infile =  None
outfile = None
verbose = False

try:
    myopts, args = getopt.getopt(sys.argv[1:],'i:o:hv') # h,v do not require arg
except getopt.GetoptError as e:
    print(str(e))
    print("Refer to '%s -h' for usage." % sys.argv[0])
    sys.exit(1)

for opt, arg in myopts:
    if opt == '-i':
        infile = arg
    elif opt == '-o':
        outfile = arg
    elif opt == '-h':
        print('How to use: %s -i input -o output' % sys.argv[0])
        sys.exit()
    elif opt == '-v':
        verbose = True

print('Input: %s \nOutput: %s' % (infile, outfile))
print('Execution mode:', 'verbose' if verbose == True else 'silent')
