#https://codeinplace.stanford.edu/cip3/share/jTHb6EJEvCxqS8DXpVgj

from collections import Counter
import os
import sys
import string


def create_index(filenames, index, file_titles):
    """
    This function is passed:
        filenames:      a list of file names (strings)

        index:          a dictionary mapping from terms to file names (i.e., inverted index)
                        (term -> list of file names that contain that term)

        file_titles:    a dictionary mapping from a file names to the title of the article
                        in a given file
                        (file name -> title of article in that file)

    The function will update the index passed in to include the terms in the files
    in the list filenames.  Also, the file_titles dictionary will be updated to
    include files in the list of filenames.
    
    The output printed by the program for the small dataset should look as shown below.
    
    Index:
    {'file3': ['3.txt'], 'title': ['3.txt', '2.txt', '1.txt'], 
    'apple': ['3.txt', '2.txt', '1.txt'], 'ball': ['3.txt', '1.txt'], 
    'carrot': ['3.txt', '2.txt'], 'gerbil': ['3.txt'], 'hamster': ['3.txt'], 
    'iguana': ['3.txt'], 'lizard': ['3.txt'], 'file2': ['2.txt'], 
    'dog': ['2.txt', '1.txt'], 'file1': ['1.txt'], 'elephant': ['1.txt'], 
    'frog': ['1.txt']}
    
    File names -> document titles:
    {'3.txt': '** File3 title **', '2.txt': '** File2 title **', '1.txt': '** File1 title **'}
  
    """
    
index = {}
file_titles = {}
small = ['3.txt','2.txt','1.txt']
filenames = small
lines = []
for i in range(len(filenames)):
        
        with open(filenames[i]) as f:
            first_line = f.readline() 
            first_line = first_line.strip()
            file_titles[filenames[i]] = first_line    
            first_line = first_line.strip(string.punctuation)
            first_line = first_line.lower()
            l1= list(first_line.split())

            for line in f: # loops over remaining lines of file
                line = line.strip()
                lines.append(line)
                line = line.strip(string.punctuation)
                line = line.lower()
                l1 += list(line.split())
            l1 = list(Counter(l1).keys())
            file_titles[filenames[i]] = lines[0]# stores first line of file in first_lineprint("File names -> document titles: \n", file_titles,"\n")  
            lines.clear()
            
            for word in l1: # index dictionary mapping from terms to file names
                if word not in index:
                    index[word] = [filenames[i]]    
                else:
                    index[word] += [filenames[i]]

print('Index: \n', index)
print("\nFile names -> document titles: \n" + str(file_titles) + '\n')   

                        

def search(index, query):
    """
    This function is passed:
        index:      a dictionary mapping from terms to file names (inverted index)
                    (term -> list of file names that contain that term)

        query  :    a query (string), where any letters will be lowercase

    The function returns a list of the names of all the files that contain *all* of the
    terms in the query (using the index passed in).

    Example 1. Calling: search(index, 'apple')
    Should produce the list: ['1.txt', '2.txt', '3.txt']
    
    Example 2. Calling: search(index, 'ball')
    Should produce the list: ['1.txt', '3.txt']
    
    Example 3. Calling: search(index, 'lizard')
    Should produce the list: ['3.txt']
    
    Example 4. Calling: search(index, 'apple ball')
    Should produce the list: ['1.txt', '3.txt']
    
    Example 5. Calling: search(index, 'dog ball')
    Should produce the list: ['1.txt']
    
    Example 6. Calling: search(index, 'dog ball hamster')
    Should produce the list: []
    
    Example 7. Calling: search(index, 'nope')
    Should produce the list: []
    """

while True:
    # set varialbes
    # convert query to lowercase and no punctuation
    l2 = []
    search_result = []
    query = str(input("Query (empty query to stop): "))
    query = query.strip(string.punctuation)
    query = query.strip()
    l1 = list(query.split()) 
    
    if query == '':
        break
    
    # check the term of query in or not in index
    # create a list of all files the terms come from 
    for i in range(len(l1)):
        if l1[i] in index:
            l2 += index[l1[i]]
            
    # only keep those files that contain every term in the query.       
    for key, val in Counter(l2).items():
            if val == len(l1):
                search_result.append(key) 
                
    if search_result:   # check for non-empty results list
            for i in range(len(search_result)):
                title = file_titles[search_result[i]]
                print(str(i + 1) + ".  Title: " + title + ",  File: " + search_result[i])
                
    if search_result != []:
        print("Results for query '" + query + "':", sorted(search_result))
    else:
        print("No results match that query.")
 
           
def main():
    
    create_index(small, index, file_titles)
    
    search(index, query)
    

if __name__ == "__main__":
    main()