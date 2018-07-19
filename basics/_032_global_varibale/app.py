from contants import globvar
from holder import ContantHolder

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    print(globvar)
    globvar = 1

def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar


def global_variables_via_class():
    print(ContantHolder.name)
    ContantHolder.name = 999
    print(ContantHolder.name)

def main():
    set_globvar_to_one()
    print_globvar()       # Prints 1
    print(globvar)
    

if __name__ == '__main__':
    main()