#--------------------------------------------------------------------------------------------------
# RRFMCLI - Remus Rigo File Manager Command Line Interface
#    © 2026 Remus Rigo
#       v1.0.20261125
#--------------------------------------------------------------------------------------------------

import sys
import os
import shutil

#--------------------------------------------------------------------------------------------------
# parse command line arguments (switches can be given in any order)
def parse_args():
   uf_flag = False
   srcFile = None
   srcPath = None

   for param in sys.argv[1:]:
      lower = param.lower()

      # /UF update file
      if lower == '/uf':
         uf_flag = True

      # /source:<path/sourcefile>
      elif lower.startswith('/source:'):
         srcFile = param.split(':', 1)[1].strip('"')

      # /search:<path>
      elif lower.startswith('/search:'):
         srcPath = param.split(':', 1)[1].strip('"')

   return uf_flag, srcFile, srcPath

#--------------------------------------------------------------------------------------------------
# report folders that cannot be read while searching
def walk_error(err):
   print(f"Warning: cannot read folder: {err.filename} ({err.strerror})")

#--------------------------------------------------------------------------------------------------
# Update files, returns the number of files that failed
def update_files(srcFile, srcPath):
   fileName = os.path.basename(srcFile)
   updated = 0
   failed = 0

   for root, dirs, files in os.walk(srcPath, onerror=walk_error):
      for fname in files:
         if fname.lower() == fileName.lower():
            targetFullPath = os.path.abspath(os.path.join(root, fname))

            # skip if the found file IS the source file (any letter case, or a link to it)
            try:
               if os.path.samefile(srcFile, targetFullPath):
                  print(f"Skip source: {targetFullPath}")
                  continue
            except OSError:
               pass

            try:
               shutil.copy2(srcFile, targetFullPath)
               print(f"Updated: {targetFullPath}")
               updated += 1
            except OSError as err:
               print(f"Failed: {targetFullPath} ({err.strerror or err})")
               failed += 1

   print()
   print(f"Total files updated: {updated}")
   if failed:
      print(f"Total files failed: {failed}")

   return failed

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

   if not uf_flag:
      print_info()
      sys.exit(1)

   if not srcFile or not os.path.isfile(srcFile):
      print(f"Error: source file not found: {srcFile}")
      print()
      print_info()
      sys.exit(1)

   if not srcPath or not os.path.isdir(srcPath):
      print(f"Error: search path not found: {srcPath}")
      print()
      print_info()
      sys.exit(1)

   failed = update_files(srcFile, srcPath)
   sys.exit(1 if failed else 0)
