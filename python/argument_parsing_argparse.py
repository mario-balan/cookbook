# an example of argument parsing with argparse

import argparse

parser = argparse.ArgumentParser(
            prog = 'argparse',
            description='This is a sample argument parser.',
            epilog='And this is how it works.')

parser.add_argument('-i','--input', help='Input file path.', required=True)
parser.add_argument('-o','--output', help='Output file path.', required=True)

parser.add_argument('-v', help='Verbose flag.',
                    action='store_true', required=False)

args = parser.parse_args()

print(args._get_kwargs())
print(args._get_args())

print('Input: %s \nOutput: %s' % (args.input, args.output))
print('Execution mode:', 'verbose' if args.v == True else 'silent')
