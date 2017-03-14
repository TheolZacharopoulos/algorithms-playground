import os


def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendants."""

    # account for direct usage
    total = os.path.getsize(path)

    # if this is a directory
    if os.path.isdir(path):

        # then for each child:
        for filename in os.listdir(path):

            # compose full path to child
            child_path = os.path.join(path, filename)

            # add child’s usage to total
            total += disk_usage(child_path)

    print('{0: < 7}'.format(total), path)
    return total


disk_usage(".")
