#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():


    num=int(input("ingrese los segundos:"))
    hor=(int(num/3600))
    minu=int((num-(hor*3600))/60)
    seg=num-((hor*3600)+(minu*60))
    print(str(hor)+"h "+str(minu)+"m "+str(seg)+"s")
    


if __name__ == "__main__":
    main()





