
#include "project.h"

int main(void)
{   
    int Count1;
    int Count2;
    int Count_Difference;
    float cpr=825.9;
    float speed;
    int Compare;
   // int Pot;
    QuadDec_1_Start();
    LCD_Char_1_Start();
    //ADC_SAR_Seq_1_Start();
   // ADC_SAR_Seq_1_StartConvert();
    PWM_1_Start();
    for(;;)
    {
        
        PWM_1_WriteCompare1(100);
        PWM_1_WriteCompare2(0);
           
        CyDelay(2000);
        
        PWM_1_WriteCompare1(0);
        PWM_1_WriteCompare2(100);
        
        CyDelay(2000);
//        Compare=0;
//        while (Compare<=100)
//        {
//            QuadDec_1_SetCounter(0);
//            PWM_1_WriteCompare(Compare);//Trun Motor ON
//            CyDelay(1500);//Allow 1 sec for motor to get up to speed
//      //  ADC_SAR_Seq_1_IsEndConversion(ADC_SAR_Seq_1_WAIT_FOR_RESULT);
//       // Pot=ADC_SAR_Seq_1_GetResult16(0);
//            Count1=QuadDec_1_GetCounter(); //Get encoder
//            CyDelay(1500); //Wait 1 sec
//            Count2=QuadDec_1_GetCounter(); //Get encoder
//            PWM_1_WriteCompare(100);
//            Count_Difference=Count2-Count1;
//            speed=(Count_Difference*60.0)/cpr;//speed in rpm
//            
//            LCD_Char_1_ClearDisplay();
//            LCD_Char_1_Position(0,0);
//            LCD_Char_1_PrintNumber(Compare);
//            LCD_Char_1_Position(1,0);
//            LCD_Char_1_PrintNumber(speed);
//            CyDelay(2000);
//            Compare=Compare+10;
//        }        
////       if (Switch_1_Read()==1)
////    {
////        LCD_Char_1_ClearDisplay();
////        LCD_Char_1_Position(0,0);
////        LCD_Char_1_PrintString("On");
////        CyDelay(50);
////    }
////    else
////    {
////        LCD_Char_1_ClearDisplay();
////        LCD_Char_1_Position(0,0);
////        LCD_Char_1_PrintString("Off");
////        CyDelay(50);
////    }
  }
}


