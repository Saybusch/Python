inputData = "abacdedcfcghihijkllkjihgffedcbaabcddcbaefghefhgijkllkjihgabcddcbaabcdedcfaabccbaeeffgghhiijjkkll"
ls = []
ls_pal = []
def ifPalindrome(string):
    return string == string[::-1]
for i in range(len(inputData)-2):
    ls.append(inputData[i:i+3])
for i in ls:
    ch = ifPalindrome(i)
    if ch:
        ls_pal.append(i)
print(ls)
print(ls_pal)
print(len(ls_pal))

