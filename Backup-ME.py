from ast import arg
import os
import sys
import argparse
import time
import datetime

hora = datetime.date.today()
nombre = f"backup-{hora}.tar.gz"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", type=str, help="Ruta del directorio para hacer el backup")
    parser.add_argument("-d", type=str, help="Ruta donde se guardara el archivo")
    parser.add_argument("-t", type=int, help="Tiempo en segundos para el otro backup")
    args=parser.parse_args()
    sys.stdout.write(str(backup(args)))

def backup(args):
    if not len(sys.argv) > 0:
        if os.path.exists(args.d):
            if os.path.exists(args.b):
                while True:
                    os.system("clear")
                    os.system(f"tar -cpzf {args.d}/{nombre} {args.b}")
                    print(f"Se creo el backup... El siguiente en {args.t} segundos")
                    time.sleep(args.t)
            else:
                print("El directorio no existe")
        else:
            print("El directorio destino no existe")
    else:
        print("No has ingresado ningun parametro, -h para mostrar el menu de ayuda")

if __name__ == "__main__":
    main()
