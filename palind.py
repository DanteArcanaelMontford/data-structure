#---------------------O(n)-----------------------#
# def palind(string):
#     return string == string[::-1]

#---------------------O(1)-----------------------#

def palind(string):
    left_p = len(string) - 1

    for rigth_p in range(len(string)):
        if string[rigth_p] != string[left_p]:
            return False
        if rigth_p == left_p:
            return True
        left_p -= 1
    return True

#------------------------TEST-----------------------#


string = 'ana'

print(palind(string))
