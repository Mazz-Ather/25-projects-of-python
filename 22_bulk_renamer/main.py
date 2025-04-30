import os 

def main():
    i = 0
    path = "E:/Python/04_assignment/assignment_01/online_class_projects/04_bulk_renamer/img"
    for filename in os.listdir(path):
        my_dest = 'my_image' + str(i) + '.jpg'
        my_sorce = path + '/' + filename
        my_dest = path + '/' + my_dest
        os.rename(my_sorce, my_dest)
        i += 1

if __name__ == '__main__':
    main()