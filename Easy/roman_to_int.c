#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int romanToInt(char* s){
    printf("%s\n", s);
    int final = 0;
    int len = strlen(s);
    int romanI = 1, romanV = 5, romanX = 10, romanL = 50, romanC = 100, romanD = 500, romanM = 1000;
    int nextc;
    int * new_s = calloc(len, sizeof(int)); 
    for(int i = 0; i < len; i++){
        if(s[i] == s[i+1]){
            switch(s[i]){
                case 'I':
                    final += 1;
                    break;
                case 'V':
                    final += 5;
                    break;
                case 'X':
                    final += 10;
                    break;
                case 'L':
                    final += 50;
                    break;
                case 'C':
                    final += 100;
                    break;
                case 'D':
                    final += 500;
                    break;
                case 'M':
                    final += 1000;
                    break;
            }
        }
        if(s[i] != s[i+1]){
            if(s[i+1] == '\0'){

            }
            
        }
    }
    return(final);
}
int main(){
    char * s = "IIV";
    int val = romanToInt(s);
    printf("%i", val);
    return(0);
}
