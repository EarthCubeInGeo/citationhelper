import os
import sys
import json

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


    all_packages = []

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
            try:
                idx = sline.index('import')
                # idx=0: import package; idx=2: from package import subpackage
                if idx==0 or idx==2:
                    package = sline[1]
                    all_packages.append(package.split('.')[0])
            except ValueError:
                continue

    packages = sorted(list(set(all_packages)))

    try:
        full_citations = read_pkg_citations(os.environ["CITEHELP_REFFILE"])
    except KeyError:
        full_citations = {}

    # print report
    if len(packages) == 0:
        print('No imported packages were found!')
    else:
        print('The following packages were imported in *.py and *.ipynb scripts.  Where known, the recommended citation is given.')
        for p in packages:
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
    # try to get directories to search from command line
    cmd_args = sys.argv
    if len(cmd_args)>1:
        workdirs = cmd_args[1:]
    else:
        workdirs = ['/home/jovyan/work','/home/jovyan/mount']

    citehelp(workdirs)

if __name__=='__main__':
    main()
