def Add(string_number_list):
    delimiter=","
    if string_number_list.startswith("//"):
        delimiter=string_number_list[2]
        string_number_list=string_number_list[5:]
    string_number_list=string_number_list.split(delimiter)
    number_sum=0
    for i in string_number_list:
        if i.isnumeric():
            if int(i)<0:
                raise Exception("negatives not allowed")
            number_sum+=int(i)
        else:
            if i.find("\\n"):
                i_list=i.split("\\n")
                for j in i_list:
                    if j.isnumeric():
                        if int(j)<0:
                            raise Exception("negatives not allowed")
                        number_sum+=int(j)  
    return number_sum
print("Enter the String Argument")
string_number_list=input()
print(Add(string_number_list))