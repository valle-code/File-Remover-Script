import os
import shutil 

print("CAUTION! This script can delete all of your disk files if you are not careful\n")

# CAUTION This script can delete all of your disk files if you are not careful

while True:
    path = input("Enter the path to delete: ")
    
    folder = path.split("\\")
    confirm = input("\nAre you sure you want to delete {}? (y/n): ".format(folder[-1].upper()))
    
    if confirm == "y":
        try:
            for file in os.listdir(path):
                if os.path.isfile(os.path.join(path, file)):
                    print("\nDeleting {}".format(file))
                    os.remove(os.path.join(path, file))
                else:
                    folder = os.listdir(os.path.join(path, file))
                    if len(folder) == 0:
                        print("\nDeleting {}".format(file))
                        os.rmdir(os.path.join(path, file))
                    else:
                        confirm_folder = input("\nAre you sure you want to delete {} and all files within that folder? (y/n): ".format(file.upper()))
                        if confirm_folder == "y":
                            print("\nDeleting {}".format(file))
                            shutil.rmtree(os.path.join(path, file)) #
        except FileNotFoundError:
            print("Path not found")
        except PermissionError:
            print("Permission denied")
        else:
            print("\nAll files were successfully removed")
            
    
   
    
    
    
    
