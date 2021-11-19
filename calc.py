class DiegoProgram:
    num1 = 0
    num2 = 0
    def __init__(self):

        self.tricks = []

    def calcsquare(self, num1):
        square = int(num1**2)
        print(square)

    def add(self):
        print("More calculations")
        num1 = int(input("please enter number"))
        num2 = int(input("please second number"))

        mesj = "la suma de ", num1, " mas ", num2, " es : ", num1 + num2
        return mesj

    def usernames(self):
        usernames = ["joey tribanni", "monica gallaguer", "Chandler bing", "Phoebe Buffay", "novita ", "Luou louo",
                     "nana",
                     "gata", " diego", "stephi joncas", "denis republica dom", "ferdinando", "sin covid "]

        for i in range(len(usernames)):
            usernames[i] = usernames[i].upper().replace("I", "&")

        print(usernames)

    def enter_usernames(self):
        size = int(input("entra numero de usuarios que quieras agregar"))
        usernames = ["diego", "nana"]

        for i in range(0, size):
            name = input("entra un nombre")
            usernames.append(name)

        print(usernames)
        option = int(input('''
        entra cero para ir a menu principal, y uno de borrar usuarios.
        
        '''))
        while option != 0:
            print(usernames)
            name = input("entra un nombre a borrar")
            usernames.remove(name)
            print(usernames)
            option = int(input("entra cero para salir y uno para continuar borrando"))

        print("has salido, gracias por usar el programa")

if __name__ == '__main__':

    test = DiegoProgram()
    option = int(input("entra cero para salir y uno para continuar"))

    while option != 0:
        menu = int(input('''
        1-Suma de dos numeros
        2-square of a number
        3- users
        4- enter_Users'''))
        if menu == 1:

            suma = test.add()
            print(suma)

        elif menu ==2:
            numero = int(input("enter a number"))
            test.calcsquare(numero)
        elif menu ==3:
            test.usernames()
        elif menu ==4:
            test.enter_usernames()
            

        option = int(input("entra cero para salir y uno para continuar"))

    print("Thanks for using this piece of software")
