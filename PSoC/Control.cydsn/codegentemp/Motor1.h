/*******************************************************************************
* File Name: Motor1.h  
* Version 2.20
*
* Description:
*  This file contains Pin function prototypes and register defines
*
* Note:
*
********************************************************************************
* Copyright 2008-2015, Cypress Semiconductor Corporation.  All rights reserved.
* You may use this file only in accordance with the license, terms, conditions, 
* disclaimers, and limitations in the end user license agreement accompanying 
* the software package with which this file was provided.
*******************************************************************************/

#if !defined(CY_PINS_Motor1_H) /* Pins Motor1_H */
#define CY_PINS_Motor1_H

#include "cytypes.h"
#include "cyfitter.h"
#include "cypins.h"
#include "Motor1_aliases.h"

/* APIs are not generated for P15[7:6] */
#if !(CY_PSOC5A &&\
	 Motor1__PORT == 15 && ((Motor1__MASK & 0xC0) != 0))


/***************************************
*        Function Prototypes             
***************************************/    

/**
* \addtogroup group_general
* @{
*/
void    Motor1_Write(uint8 value);
void    Motor1_SetDriveMode(uint8 mode);
uint8   Motor1_ReadDataReg(void);
uint8   Motor1_Read(void);
void    Motor1_SetInterruptMode(uint16 position, uint16 mode);
uint8   Motor1_ClearInterrupt(void);
/** @} general */

/***************************************
*           API Constants        
***************************************/
/**
* \addtogroup group_constants
* @{
*/
    /** \addtogroup driveMode Drive mode constants
     * \brief Constants to be passed as "mode" parameter in the Motor1_SetDriveMode() function.
     *  @{
     */
        #define Motor1_DM_ALG_HIZ         PIN_DM_ALG_HIZ
        #define Motor1_DM_DIG_HIZ         PIN_DM_DIG_HIZ
        #define Motor1_DM_RES_UP          PIN_DM_RES_UP
        #define Motor1_DM_RES_DWN         PIN_DM_RES_DWN
        #define Motor1_DM_OD_LO           PIN_DM_OD_LO
        #define Motor1_DM_OD_HI           PIN_DM_OD_HI
        #define Motor1_DM_STRONG          PIN_DM_STRONG
        #define Motor1_DM_RES_UPDWN       PIN_DM_RES_UPDWN
    /** @} driveMode */
/** @} group_constants */
    
/* Digital Port Constants */
#define Motor1_MASK               Motor1__MASK
#define Motor1_SHIFT              Motor1__SHIFT
#define Motor1_WIDTH              1u

/* Interrupt constants */
#if defined(Motor1__INTSTAT)
/**
* \addtogroup group_constants
* @{
*/
    /** \addtogroup intrMode Interrupt constants
     * \brief Constants to be passed as "mode" parameter in Motor1_SetInterruptMode() function.
     *  @{
     */
        #define Motor1_INTR_NONE      (uint16)(0x0000u)
        #define Motor1_INTR_RISING    (uint16)(0x0001u)
        #define Motor1_INTR_FALLING   (uint16)(0x0002u)
        #define Motor1_INTR_BOTH      (uint16)(0x0003u) 
    /** @} intrMode */
/** @} group_constants */

    #define Motor1_INTR_MASK      (0x01u) 
#endif /* (Motor1__INTSTAT) */


/***************************************
*             Registers        
***************************************/

/* Main Port Registers */
/* Pin State */
#define Motor1_PS                     (* (reg8 *) Motor1__PS)
/* Data Register */
#define Motor1_DR                     (* (reg8 *) Motor1__DR)
/* Port Number */
#define Motor1_PRT_NUM                (* (reg8 *) Motor1__PRT) 
/* Connect to Analog Globals */                                                  
#define Motor1_AG                     (* (reg8 *) Motor1__AG)                       
/* Analog MUX bux enable */
#define Motor1_AMUX                   (* (reg8 *) Motor1__AMUX) 
/* Bidirectional Enable */                                                        
#define Motor1_BIE                    (* (reg8 *) Motor1__BIE)
/* Bit-mask for Aliased Register Access */
#define Motor1_BIT_MASK               (* (reg8 *) Motor1__BIT_MASK)
/* Bypass Enable */
#define Motor1_BYP                    (* (reg8 *) Motor1__BYP)
/* Port wide control signals */                                                   
#define Motor1_CTL                    (* (reg8 *) Motor1__CTL)
/* Drive Modes */
#define Motor1_DM0                    (* (reg8 *) Motor1__DM0) 
#define Motor1_DM1                    (* (reg8 *) Motor1__DM1)
#define Motor1_DM2                    (* (reg8 *) Motor1__DM2) 
/* Input Buffer Disable Override */
#define Motor1_INP_DIS                (* (reg8 *) Motor1__INP_DIS)
/* LCD Common or Segment Drive */
#define Motor1_LCD_COM_SEG            (* (reg8 *) Motor1__LCD_COM_SEG)
/* Enable Segment LCD */
#define Motor1_LCD_EN                 (* (reg8 *) Motor1__LCD_EN)
/* Slew Rate Control */
#define Motor1_SLW                    (* (reg8 *) Motor1__SLW)

/* DSI Port Registers */
/* Global DSI Select Register */
#define Motor1_PRTDSI__CAPS_SEL       (* (reg8 *) Motor1__PRTDSI__CAPS_SEL) 
/* Double Sync Enable */
#define Motor1_PRTDSI__DBL_SYNC_IN    (* (reg8 *) Motor1__PRTDSI__DBL_SYNC_IN) 
/* Output Enable Select Drive Strength */
#define Motor1_PRTDSI__OE_SEL0        (* (reg8 *) Motor1__PRTDSI__OE_SEL0) 
#define Motor1_PRTDSI__OE_SEL1        (* (reg8 *) Motor1__PRTDSI__OE_SEL1) 
/* Port Pin Output Select Registers */
#define Motor1_PRTDSI__OUT_SEL0       (* (reg8 *) Motor1__PRTDSI__OUT_SEL0) 
#define Motor1_PRTDSI__OUT_SEL1       (* (reg8 *) Motor1__PRTDSI__OUT_SEL1) 
/* Sync Output Enable Registers */
#define Motor1_PRTDSI__SYNC_OUT       (* (reg8 *) Motor1__PRTDSI__SYNC_OUT) 

/* SIO registers */
#if defined(Motor1__SIO_CFG)
    #define Motor1_SIO_HYST_EN        (* (reg8 *) Motor1__SIO_HYST_EN)
    #define Motor1_SIO_REG_HIFREQ     (* (reg8 *) Motor1__SIO_REG_HIFREQ)
    #define Motor1_SIO_CFG            (* (reg8 *) Motor1__SIO_CFG)
    #define Motor1_SIO_DIFF           (* (reg8 *) Motor1__SIO_DIFF)
#endif /* (Motor1__SIO_CFG) */

/* Interrupt Registers */
#if defined(Motor1__INTSTAT)
    #define Motor1_INTSTAT            (* (reg8 *) Motor1__INTSTAT)
    #define Motor1_SNAP               (* (reg8 *) Motor1__SNAP)
    
	#define Motor1_0_INTTYPE_REG 		(* (reg8 *) Motor1__0__INTTYPE)
#endif /* (Motor1__INTSTAT) */

#endif /* CY_PSOC5A... */

#endif /*  CY_PINS_Motor1_H */


/* [] END OF FILE */
