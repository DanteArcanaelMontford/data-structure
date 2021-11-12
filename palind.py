#---------------------O(n)-----------------------#
# def palind(string):
#     return string == string[::-1]

#---------------------O(1)-----------------------#

def palind(string):
    rigth_p = len(string) - 1

    for left_p in range(len(string)):
        if string[left_p] != string[rigth_p]:
            return False
        if left_p == rigth_p:
            return True
        rigth_p -= 1
    return True

#------------------------TEST-----------------------#


string = 'ana'

print(palind(string))
