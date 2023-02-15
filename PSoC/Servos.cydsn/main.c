#include "project.h"
#include "math.h"

int Theta1(float Angle)
    {
        int Compare;
        int max_comp=1400;
        int min_comp=7250;
        int min_angle=0;
        int max_angle=180;
        Compare=((max_comp-min_comp)/(max_angle-min_angle))*(Angle-min_angle)+min_comp;
        return Compare;
    }
    
    int Theta2(float Angle)
    {
        int Compare;
        int max_comp=1300;
        int min_comp=7300;
        int min_angle=-90;
        int max_angle=90;
        Compare=((max_comp-min_comp)/(max_angle-min_angle))*(Angle-min_angle)+min_comp;
        return Compare;
    }
    
int main(void)
{
    float X=8.0; //Desired X postion of the end-effector in cm
    float Y=8.0; //Desired Y postion of the end-effector in cm
    float r1=0.0;
    float phi1=0.0;
    float phi2=0.0;
    float phi3=0.0;
    float a2=6.0;
    float a4=5.5;
    float T1=0.0;//T1 is theta 1 in radians
    float T2=0.0;//T2 is theta 2 in radians
    
    r1=sqrt(X*X+Y*Y);
    
    
    PWM_1_Start(); //Eq.1
    phi1=acos(((a4*a4)-(a2*a2)-(r1*r1))/(-2.0*a2*r1));//Eq.2
    phi2=atan(Y/X);//Eq.3
    T1=phi2-phi1;//Eq.4
    phi3=acos(((r1*r1)-(a2*a2)-(a4*a4))/(-2.0*a2*a4));//Eq.5
    T2=3.14159-phi3;//Eq.6
    
    for(;;)
    {   
       PWM_1_WriteCompare1(Theta1((T1/3.14159)*180.0)); //send servo 1 to clockwise position
       CyDelay(2000);
       PWM_1_WriteCompare2(Theta2((T2/3.14159)*180.0)); //Send servo 2 to counterclockwise position
       CyDelay(2000);
     // PWM_1_WriteCompare1(Theta1(180.0)); //Send servo 1 to counterclockwise position
  // CyDelay(2000);
////        
   //PWM_1_WriteCompare2(Theta2(90.0)); //send servo 2 to clockwise position
 // CyDelay(2000);
//PWM_1_WriteCompare2(Theta2(-90.0)); //Send servo 2 to counterclockwise position
  //     CyDelay(2000);
        
    }
}


