
#include "project.h"

int main(void)
{   
    int Count;
    int Compare;
    int time;
    int Target_Count1=1000;
    int Target_Count2=2000;
    int error;
    float Kp=0.47;
    uint8 receive;
    uint8 val1;
    uint8 val2;
    uint8 i;
    uint8 j;
    int speed;
    QuadDec_1_Start();
    LCD_Char_1_Start();
    PWM_1_Start();
    UART_1_Start();
    for(;;)
    {
            receive=UART_1_GetChar();
                while (receive==0)
            {
            receive=UART_1_GetChar();
            }
            
//                while(1)
//                {
//                    receive=UART_1_GetChar();
//                        while (receive==0)
//                    {
//                    receive=UART_1_GetChar();
//                    }
//                    LCD_Char_1_ClearDisplay();
//                    LCD_Char_1_Position(0,0);
//                    LCD_Char_1_PrintNumber(receive);
//                    i=1;
//                    j=1;
//                    while(i<=10)
//                    {
//                        UART_1_PutChar(j);
//                        CyDelay(200);
//                        i=i+1;
//                        j=j+10;
//                    }
//                    
//                }
        time=0;
        
        while(time<2000)
        {
            Count=QuadDec_1_GetCounter();
            error=Target_Count1-Count;
            if (error>0)
            {
                speed=Kp*error;
                if (speed>100)
                {
                    speed=100;
                }
                PWM_1_WriteCompare1(speed);
                PWM_1_WriteCompare2(0);
                
            }
            else
            {
                speed=-Kp*error;
                if (speed>100)
                {
                    speed=100;
                }
                PWM_1_WriteCompare1(0);
                PWM_1_WriteCompare2(speed);
            }
            LCD_Char_1_ClearDisplay();
            LCD_Char_1_Position(0,0);
            LCD_Char_1_PrintNumber(Count);
            val1=Count/256;
            val2=Count-val1*256;
            UART_1_PutChar(val1);
            CyDelay(10);
            UART_1_PutChar(val2);
            time=time+10;
        }
        
        time=0;
        while(time<2000)
        {
            Count=QuadDec_1_GetCounter();
            error=Target_Count2-Count;
            if (error>0)
            {
                speed=Kp*error;
                if (speed>100)
                {
                    speed=100;
                }
                PWM_1_WriteCompare1(speed);
                PWM_1_WriteCompare2(0);
                
            }
            else
            {
                speed=-Kp*error;
                if (speed>100)
                {
                    speed=100;
                }
                PWM_1_WriteCompare1(0);
                PWM_1_WriteCompare2(speed);
            }
            LCD_Char_1_ClearDisplay();
            LCD_Char_1_Position(0,0);
            LCD_Char_1_PrintNumber(Count);
            val1=Count/256;
            val2=Count-val1*256;
            UART_1_PutChar(val1);
            CyDelay(10);
            UART_1_PutChar(val2);
            time=time+10;
        }
        
  }
}


