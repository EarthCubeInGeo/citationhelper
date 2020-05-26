import os
import sys

def citehelp(workdirs):

    # create list of all python code files in workdirs
    pyfiles = []
    for wdir in workdirs:
        if not os.path.isdir(wdir):
            raise OSError('Cannot find {}'.format(wdir))
        for root, dirs, files in os.walk(wdir):
            pyfiles.extend([os.path.join(root,fn) for fn in files if fn.endswith('.py')])


    all_packages = []

    for pyf in pyfiles:
        with open(pyf,'ro') as f:
            lines = f.readlines()

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

    packages = list(set(all_packages))

    # print report
    print('Summary Report of All Packages Imported:')
    for p in packages:
        print(p)

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
