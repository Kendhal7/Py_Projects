##files-rename
  
# importing os module 
import os 
 

#Definition of the rename function
def renameFiles(src_dir, newname, newtype):
    #Initialise the loop parameter
    i = 0
    #Loop to rename every file in the source directory  
    for file in os.listdir(src_dir):
        #Define the actual path of the file
        path = os.path.join(src_dir, file)
        if newtype=='same':
            #Get the type of the file
            file_extension = os.path.splitext(file)[1][1:]
            #Rename the file by 'newname'i. with the same extension 
            dst = newname + str(i) + "." + file_extension
        else:
            #Rename the file by 'newname'i.'newtype' 
            dst = newname + str(i) + "." + newtype
        #Define the new path of the file
        target = os.path.join(src_dir, dst)
        #Rename
        os.rename(path, target)
        #Move to next element
        i += 1


# Main and getters for the source, name and type
def main():
    # Library Parser for command-line options
    import argparse

    # Setup command line parsing
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
        description='Rename files in a specific folder using a given name template')

    parser.add_argument('src_dir', type=str, help='source directory')
    parser.add_argument('newname', type=str, help='Name template for the files (ie IMG)')
    parser.add_argument('newtype', type=str, help='Extension for the files (ie jpg)\n Enter same to keep the existing extension')


    # parse command line arguments
    args = parser.parse_args()

    # Call of the function
    renameFiles(args.src_dir, args.newname, args.newtype)
      
    
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 

