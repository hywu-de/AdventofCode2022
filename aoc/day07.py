# day07_1

##goal: the sum of the total sizes of directories that each is at most 100000
# files can be counted more than once
# --> check the first four elements: "$ cd" or "$ ls" or "dir " / just a file

def get_dir_size(current_dir, path_dict, dir_size):
    '''Get directories sizes

      all_dir_sizes: collect all sizes
      path_dict: path to path mapping
    '''        
    # child dirs
    child_paths = path_dict[current_dir][1]
    dir_size += path_dict[current_dir][0]

    if child_paths == []: 
        return dir_size
    else:
        for child_path in child_paths:
            dir_size = get_dir_size(child_path, path_dict, dir_size)  
        return dir_size

# initiate current_directory
current_directory = None 

## to record all paths
# key: path, value: [file size, all children paths]
# --> {"/": [123, [/a, /b]], "/a": [13, []]}
paths = dict()

with open('day07.txt', 'r') as f:
    lines = f.read().splitlines()

## --- record all paths --- ##
for i in lines:
    if i == "":
        continue
    # firstly, check if the first fourth characters is either "$ ls" or "$ cd"
    first_four_char = i[:4]
    # ls
    if first_four_char == "$ ls":
        continue
    # cd
    elif first_four_char == "$ cd":
        ### process the current directory ###
        # '$ cd FolderName'
        # split whitespace -> [$, cd, FolderName] -> extract the last element(foldername)
        dir_name = i.split()[-1].strip()  # --> '/' or 'FolderName' or '..'
        
        ## if move out one level('..'), update current path: "/bgmjrlz/dhqzgdl/jjshzrhd" -> /bgmjrlz/dhqzgdl"
        # split: "/bgmjrlz/dhqzgdl/jjshzrhd" ->  [bgmjrlz, dhqzgdl, jjshzrhd]
        # [bgmjrlz, dhqzgdl, jjshzrhd][-1] -> [bgmjrlz, dhqzgdl]
        # "/".join([bgmjrlz, dhqzgdl]) -> "bgmjrlz/dhqzgdl"
        if dir_name == "..":
            current_directory = "/".join(current_directory.split("/")[:-1]) 
            #print(current_directory)
            continue

        # if it is a folder name, update to the new path 
        else:  # dir_name == "FolderName"
            
            if current_directory == None:  # if current directory is None -> root file
                current_directory = dir_name  # "/"

            else:  
                # if current directory is "/", directly add "dir_name"
                if current_directory == "/":
                    current_directory = "/" + dir_name  #/foldername

                # if current directory is "a/b", add "/dir_name"
                else:
                    current_directory = current_directory + "/" + dir_name
                    
        #print("commnad", i)
        #print("new dir", current_directory, end="\n\n")
        '''
        commnad $ cd bgmjrlz
        new dir /bgmjrlz

        commnad $ cd dhqzgdl
        new dir /bgmjrlz/dhqzgdl

        '''
        # after processing current directory, check whether directories are in paths = dict()
        # add directory path to paths
        if current_directory not in paths:
            # if directory path isn't in paths, create value [0, []] for it
            paths[current_directory] = [0, []]  # {'/vfrtt/zblsznh/tdpv/sggm': [0, []]}

        
    # if the path name is e.g. dir bhp
    # --> it is child path of "current_directory" 
    # --> add to "current_directory" list
    elif first_four_char == "dir ":
        # "dir dhqzgdl".split() -> [dir, dhqzgdl]
        # [dir, dhqzgdl][-1] -> dhqzgdl
        dir_name = i.split()[-1]

        ### create child directory ###
        if current_directory == "/":    # if current directory is "/" -> /dir_name
            child_path = "/" + dir_name

        else:    # if current directory is "/abc" -> "/abc/dir_name"
            child_path = current_directory + "/" + dir_name
         
        if child_path not in paths:
            paths[child_path] = [0, []]
            # paths: {"/abc": [0, []]} -> {"/abc": [0, [/abc/dir_name]]}
            paths[current_directory][1].append(child_path) 

    # if it is a file
    else:
        # "99548 pqpslbtn" -> [99548, pqpslbtn]
        size, file_name = i.split()
        size = int(size)

        # add size
        paths[current_directory][0] += size


# Get size
# --> find every directory which size is < 100000
all_file_sizes = list()

for all_dir in paths:
    # use get_dir_size() function to get file size
    dir_size = get_dir_size(all_dir, paths, 0)
    if dir_size < 100000:
        all_file_sizes.append(dir_size)
print(sum(all_file_sizes))


# day07_2

# we need at least 30000000 spaces

root_size = get_dir_size("/", paths, 0)   # root size is 45349983
free_space = 70000000 - root_size
required_space = 30000000 - free_space  # required_space 5349983

ans = 100000000  # initiate a huge number for later comparison

# check every path
for all_dir in paths:
    dir_size = get_dir_size(all_dir, paths, 0)
    # find dir_size that is bigger than required space
    if dir_size >= required_space:
        ans = min(ans, dir_size)
print(ans)

