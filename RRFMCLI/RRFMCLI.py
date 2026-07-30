#--------------------------------------------------------------------------------------------------
# RRFMCLI - Remus Rigo File Manager Command Line Interface
#    © 2026 Remus Rigo
#       v1.0.20260728
#--------------------------------------------------------------------------------------------------

import sys
import os
import shutil

#--------------------------------------------------------------------------------------------------
# parse command line arguments
def parse_args():
   uf_flag = False
   srcFile=None
   srcPath=None

   # /UF update file
   if len(sys.argv) > 1 and sys.argv[1].upper() == '/UF':
      uf_flag = True

      # /source:<path/sourcefile>
      if len(sys.argv) > 2:
         param2 = sys.argv[2]
         if param2.lower().startswith('/source:'):
            srcFile = param2.split(':', 1)[1]
            srcFile = srcFile.strip('"')

      # /search:<path>
      if len(sys.argv) > 3:
         param3 = sys.argv[3]
         if param3.lower().startswith('/search:'):
            srcPath = param3.split(':', 1)[1]
            srcPath = srcPath.strip('"')

   return uf_flag, srcFile, srcPath

#--------------------------------------------------------------------------------------------------
# Update files
def update_files(srcFile, srcPath):
   fileName = os.path.basename(srcFile)
   srcFullPath = os.path.abspath(srcFile)
   updated = 0

   for root, dirs, files in os.walk(srcPath):
      for fname in files:
         if fname.lower() == fileName.lower():
            targetFullPath = os.path.abspath(os.path.join(root, fname))

            # skip if the found file IS the source file
            if targetFullPath == srcFullPath:
               print(f"Skip source: {targetFullPath}")
               continue

            shutil.copy2(srcFile, targetFullPath)
            print(f"Updated: {targetFullPath}")
            updated += 1

   print()
   print(f"Total files updated: {updated}")

#--------------------------------------------------------------------------------------------------
# print information about the command line arguments
def print_info():
   print("RRFMCLI v1.0.20260728")
   print("   © 2026 Remus Rigo")
   print()
   print("RRFMCLI /UF /source:<sourcefile> /search:<searchpath>")
   print("/UF - Update files")
   print("/source:<sourcefile> - Specify the source file (path included)")
   print("/search:<searchpath> - Specify the search path")

#--------------------------------------------------------------------------------------------------
# main function
if __name__ == '__main__':
   if len(sys.argv) < 2:
      print_info()
      sys.exit(0)

   uf_flag, srcFile, srcPath = parse_args()

   if uf_flag:
      if srcFile is None or not os.path.isfile(srcFile):
         print(f"Error: source file not found: {srcFile}")
         print()
         print_info()
         sys.exit(1)

      if srcPath is None or not os.path.isdir(srcPath):
         print(f"Error: search path not found: {srcPath}")
         print()
         print_info()
         sys.exit(1)

   update_files(srcFile, srcPath)
   