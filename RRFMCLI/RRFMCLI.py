#--------------------------------------------------------------------------------------------------
# RRFMCLI
#    © 2026 Remus Rigo
#       v1.0 20260726   
#--------------------------------------------------------------------------------------------------

import sys

def parse_args():
    uf_flag = False
    srcFile=None
    srcPath=None
    for arg in sys.argv[1:]:
        if arg.upper() == '/UF':
            uf_flag = True
        elif arg.lower().startswith('/source:'):
            srcFile = arg.split(':',1)[1]
            srcFile = srcFile.strip('"')
        elif arg.lower().startswith('/search'):
            srcPath = arg.split(':',1)[1]
            srcPath = srcPath.strip('"')
    return uf_flag, srcFile, srcPath

if __name__ == '__main__':
    uf_flag, srcFile, srcPath = parse_args()
    print("uf_flag: ", uf_flag)
    print(f"srcFile: {srcFile}")
    print(f"srcPath: {srcPath}")
    #sys.exit(0)