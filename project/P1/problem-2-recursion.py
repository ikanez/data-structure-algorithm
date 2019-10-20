import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = []

    if os.path.isdir(path):  # if path is dir, traverse the listings
        for child in os.listdir(path):
            files.extend(find_files(suffix, os.path.join(path, child)))
    elif os.path.isfile(path):  # if path is file, check whether is has suffix
        if path.endswith(suffix):
            files.append(path)

    # print(files)  # debug
    return files


# TEST
curr_path = os.path.dirname(os.path.abspath(__file__)) + '/testdir/'
print(find_files('.c', curr_path))
# all files in testdir with *.c name

print(find_files('.h', curr_path))
# all files in testdir with *.h name

print(find_files('.gitkeep', curr_path))
# all files in testdir with *.gitkeep name
