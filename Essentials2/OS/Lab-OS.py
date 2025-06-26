import os

class DirectorySearcher:
    def find(self, path, dir):
        try:

            for entry in os.listdir(path): # list all files and folders in current dir
                full_path = os.path.join(path, entry)
                #check if entry is directory
                if os.path.isdir(full_path):
                    if entry == dir:
                        print("Found:", full_path)
                    
                    self.find(full_path, dir) #recursive into sub directory
        except PermissionError:
            print("Permission denied", path)
        except FileNotFoundError:
            print("Path not found", path)


directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "c")