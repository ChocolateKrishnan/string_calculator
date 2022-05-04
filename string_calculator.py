def Add(string_number_list):
    delimiter=","
    if string_number_list.startswith("//"):
        string_number_list=string_number_list[2:]
        string_number_list=string_number_list.split("\\n")
        delimiter=string_number_list[0]
        new_string_list=string_number_list[1:]
        string_number_list=''
        string_number_list=string_number_list.join(new_string_list)
    string_number_list=string_number_list.split(delimiter)
    number_sum=0
    for i in string_number_list:
        try:
            if i=='':
                i=0
            if int(i)<0:
                raise Exception("negatives not allowed")
            else:
                number_sum+=int(i)
        except:
            if i.find("\\n"):
                i_list=i.split("\\n")
                print(i_list)
                for j in i_list:
                    if j=='':
                        j=0
                    if int(j)<0:
                        raise Exception("negatives not allowed")
                    number_sum+=int(j)  
    return number_sum
print("Enter the String Argument")
string_number_list=input()
print(Add(string_number_list))
