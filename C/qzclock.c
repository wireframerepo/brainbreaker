#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv){

    if(argc < 4){
        printf("\n\nCOMMAND SINTAX \n");
        printf("\nqzclock [hertz(int)] [readcycles(int)] [start index(int)] \n");
        printf("\nHertz, how many times per second \n");
        printf("\nreadCycles, how many times it will run, if 0 will run forever until ctrl c \n");
        printf("\nstartIndex, will start from startIndex until readCycles \n");
        printf("\nplease try again \n\n");
        return 0;
    }

    int Hz = atoi(argv[1]); //hertz, will divide 1M microseconds to make this iterations in 1 second
    int reads = atoi(argv[2]); //how many cycles want you the program to go
    int i = atoi(argv[3]); //index, 0 is the first step, until reads is reached
    int microsToSecond = 1000000;

// how to validate an entry coming. if entry expected but not coming is null. cc on unix and mingw 
// on windows, probably the same in linux (unix is from a macbook pro intel processor)
/*
    if(!argv[1]){
        printf("the argument is null \n");
    }else {
        int result = atoi(argv[1]);
        printf("%s %d \n",argv[1],result);
    }
*/

   printf("this is a clock \n\n");
   while(reads == 0 ? 1 == 1 : i <= reads){
       printf("tick tock %d \n",i);
       usleep(microsToSecond / Hz);
       i = i + 1;
   }

}