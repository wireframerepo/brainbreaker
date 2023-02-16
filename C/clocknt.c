#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
    int Hz = 43000; //hertz, will divide 1M microseconds to make this iterations in 1 second
    int reads = 100; //how many cycles want you the program to go
    int i = 0; //index, 0 is the first step, until reads is reached

   printf("this is a clock \n\n");
   while(reads == 0 ? 1 == 1 : i <= reads){
       printf("tick tock %d \n",i);
       usleep(1000000 / Hz);
       i = i + 1;
   }
}