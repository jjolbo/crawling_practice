def is_a_exist(some_list):
    if 'a' in some_list:
        print('ok')
        return True
    else:
        print('not')
        return  False

somelist = ['a','b','c']
result = is_a_exist(somelist)
print(result)

def hello(say, name = 'beomi'):
    value = f"hi, {say}! {name}."
    return value

t_only = hello('there')
t_name = hello('there', 'jumbum')
s_only = hello(say='there')
r_all = hello(name ='jb', say='hola')

print(t_only, t_name, s_only, r_all)