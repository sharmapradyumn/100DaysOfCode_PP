def count_substring(string, sub_string):
    count = 0 
    m = 0
    for i in range(len(string)):
        #residual string
        res = string[count:]
        if sub_string in res:
            m = m+1
            pos = res.find(sub_string)
            count = count+pos+1
        #print(m, pos , count)
    return m


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


#Note: my option was also optimal just used some more variables

#optimal solution
#   ct = 0
#   while sub_string in string:
#     ct += 1
#     string = string[string.find(sub_string)+1:]
#   return ct