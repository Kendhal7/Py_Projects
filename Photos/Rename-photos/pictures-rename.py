# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
 

#Definition of the rename function
def renamePhotos(src_dir, newname, newtype):
    #Initialise the loop parameter
    i = 0
    #Loop to rename every file in the source directory  
    for file in os.listdir(src_dir):
        #Rename the file by 'newname'i.'newtype' 
        dst = newname + str(i) + "." + newtype
        #Define the actual path of the file and the new one
        path = os.path.join(src_dir, file)
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
                                     description='Sort files (primarily photos and videos) into folders by date\nusing EXIF and other metadata')

    parser.add_argument('src_dir', type=str, help='source directory')
    parser.add_argument('newname', type=str, help='Name template for the files (ie IMG)')
    parser.add_argument('newtype', type=str, help='Type of documents (ie jpg)')


    # parse command line arguments
    args = parser.parse_args()

    # Call of the function
    renamePhotos(args.src_dir, args.newname, args.newtype)
      
    
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 

