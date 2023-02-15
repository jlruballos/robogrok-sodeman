
#include "project.h"

int main(void)
{   
    float Motor_Speed=10.0; //steps per second
    int Period=0;
    int Clock_Speed=10000;
    int Direction=2; //1 means forwards, 2 means backwards
    uint8 Receive1;
    uint8 Receive2;
    PWM_1_Start();
    PWM_2_Start();
    UART_1_Start();
     
   
    
    
    for(;;)
    {
        Receive1=UART_1_GetChar();
        while (Receive1==0)
        {
            Receive1=UART_1_GetChar();
        }
         
        Receive2=UART_1_GetChar();
        while (Receive2==0)
        {
            Receive2=UART_1_GetChar();
        }
        
        if (Receive1==1 || Receive1==2)
        {
            Direction=Receive1;
            Motor_Speed=Receive2;
        }
        else
        {
            Direction=Receive2;
            Motor_Speed=Receive1;
        }
        
        Period=4.0*Clock_Speed/Motor_Speed;
        PWM_1_WritePeriod(Period);
        PWM_1_WriteCompare(Period/2);
        PWM_2_WritePeriod(Period);
        PWM_2_WriteCompare(Period/2);
        
        if(Direction==1)
        {
            PWM_1_SetCompareMode(3);
            PWM_2_SetCompareMode(1);
            PWM_1_WriteCounter(0);
            PWM_2_WriteCounter(0);
        }
        if(Direction==2)
        {
            PWM_1_SetCompareMode(1);
            PWM_2_SetCompareMode(3);
            PWM_1_WriteCounter(0);
            PWM_2_WriteCounter(0);
        }
    }
}


