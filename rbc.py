# rbc - A command line manager for the mpc runtime code
import os
import argparse

def execute_script(path, files):
    os.system(f'python runtime/{path} \"{files}\"')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog='rbc',
                        description='A command line tool for decompiling minecraft and creating mods')
    
    parser.add_argument('--command', required=True, choices=["cleanup","decompile","recompile","reobfuscate","startclient","startserver","updatemd5","updatenames"])
    
    # Add argument to capture any extra words after the main command
    parser.add_argument('files', nargs='*', help='List of files')

    args = parser.parse_args()

    if args.files:
        files_parsed = " ".join(args.files)
    else:
        files_parsed = []
    
    # We could use 'match' here but to maximise python version compatibility old style if-elif blocks are used
    execute_script(args.command + ".py", files_parsed)