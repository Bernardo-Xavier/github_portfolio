# Panic Button - Capstone Project

## Overview
This project, titled **"Panic Button"**, is a safety device designed to detect emergency situations and send an alert via SMS using a GSM module. The system is built around the **PIC16F877A microcontroller** and integrates hardware and software components to achieve its functionality.

## Features
- **Emergency Detection**: Detects a panic button press to trigger an alert.
- **SMS Notification**: Sends an SMS to a predefined phone number using a GSM module.
- **LED Indicators**: Visual feedback for system status (e.g., waiting for button press, sending SMS).
- **Configurable**: Phone number and message content can be customized in the code.

## Hardware Components
- Microcontroller: PIC16F877A
- GSM Module: SIM800L or similar
- Panic Button: Momentary push button
- LEDs: Status indicators
- Power Supply: 5V DC
- Resistors, Capacitors, and other passive components

## Software
- **Programming Language**: Assembly (MPASM)
- **IDE**: MPLAB X
- **Key Libraries**: None (pure assembly)

## How It Works
1. The system initializes and waits for the panic button to be pressed.
2. When the button is pressed, the microcontroller prepares the GSM module for SMS transmission.
3. The GSM module sends an SMS with a predefined message to a specified phone number.
4. LEDs provide visual feedback on the system's status.

## Setup Instructions
1. **Hardware Setup**: Assemble the circuit as per the schematic provided in the `Schematics/` folder.
2. **Software Setup**:
   - Open the `Main_Code.asm` file in MPLAB X.
   - Compile and upload the code to the PIC16F877A microcontroller.
3. **Testing**:
   - Power on the system and wait for the initialization to complete.
   - Press the panic button to trigger an SMS alert.

## License
This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.

## Author
**Bernardo Xavier da Silva**  
Electrical Engineer | Data Scientist  
[LinkedIn](https://www.linkedin.com/in/bernardo-xavier-da-silva/) | [GitHub](https://github.com/Bernardo-Xavier)
