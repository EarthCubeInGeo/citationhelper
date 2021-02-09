import os
import sys
import json
import re
import importlib

SEARCH_FTYPES = ['.py','.ipynb'] # in lower case

def citehelp(workdirs):

    # create list of all python code files in workdirs
    pyfiles = []
    for wdir in workdirs:
        if not os.path.isdir(wdir):
            print('Cannot find path : {}'.format(wdir))
            continue
        for root, dirs, files in os.walk(wdir):
            pyfiles.extend([os.path.join(root,fn) for fn in files if
                os.path.splitext(fn)[-1].lower() in SEARCH_FTYPES])


    all_imports = []

    for pyf in pyfiles:
        if os.path.splitext(pyf)[-1].lower() == '.py':
            with open(pyf,'r') as f:
                lines = f.readlines()
        elif os.path.splitext(pyf)[-1].lower() == '.ipynb':
            with open(pyf,'r') as f:
                notebook = json.load(f)
            lines = list()
            for cell in notebook['cells']:
                if cell['cell_type']=='code':
                    lines.extend(cell['source'])

        for line in lines:
            sline = line.split()

            m1 = re.search('^import (.+) as (.+)', line)
            m2 = re.search('^from (.+) import (.+)', line)
            m3 = re.search('^import (.+)', line)
            if m1:
                pack = m1.group(1).split(',')
            elif m2:
                pack = m2.group(1).split(',')
            elif m3:
                pack = m3.group(1).split(',')
            else:
                continue

            all_imports.extend([p.strip().split('.')[0] for p in pack])

    all_imports = sorted(list(set(all_imports)))


    installed_packages = []
    custom_imports = []
    for p in all_imports:
        if importlib.find_loader(p):
            installed_packages.append(p)
        else:
            custom_imports.append(p)

    try:
        full_citations = read_pkg_citations(os.environ["CITEHELP_REFFILE"])
    except KeyError:
        full_citations = {}

    # print report
    if len(all_imports) == 0:
        print('No imported packages were found!')
    else:
        print('The following packages were imported in *.py and *.ipynb scripts.  Where known, the recommended citation is given.')
        print('\nInstalled Packages:')
        for p in installed_packages:
            print(p)
            try:
                print(full_citations[p])
            except KeyError:
                continue
        print('\nOther Imports:')
        for p in custom_imports:
            print(p)
            try:
                print(full_citations[p])
            except KeyError:
                continue

        print('\nDisclaimer: The citehelp utility is intended only to make it easier to keep track of what packages are being used for citation purposes.  The list provided may not be comprehensive, so users are STRONGLY encourage to review it and make sure all software used is given proper credit.\n')

def read_pkg_citations(filename):

    with open(filename, 'r') as f:
        citations = json.load(f)

    return citations



def main():
    from argparse import ArgumentParser, RawTextHelpFormatter

    des = 'Determine which python packages were imported in all scripts and jupyter notebooks in a particular directory to assist with citing these packages correctly.'
    # Build the grument parser tree
    parser = ArgumentParser(description=des, formatter_class=RawTextHelpFormatter)
    parser.add_argument('dirs', nargs='+', help='directories to search for python programs')

    args = parser.parse_args()

    citehelp(args.dirs)

if __name__=='__main__':
    main()
