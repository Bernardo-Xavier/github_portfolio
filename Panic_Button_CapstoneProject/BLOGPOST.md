# Building a Panic Button System: My Capstone Project

## Introduction
As part of my Electrical Engineering degree, I developed a **"Panic Button"** system. This project combines hardware and software to create a safety device that sends an SMS alert in emergency situations. In this blog post, I’ll walk you through the design, implementation, and challenges of this project.

## The Problem
In emergency situations, quick communication can save lives. Traditional methods like calling for help may not always be feasible. My goal was to create a simple, reliable device that could send an alert with the press of a button.

## The Solution
The **Botão de Pânico** system uses a PIC16F877A microcontroller and a GSM module to send SMS alerts. Here’s how it works:
1. **Panic Button**: When pressed, it triggers the microcontroller.
2. **Microcontroller**: Prepares and sends an AT command to the GSM module.
3. **GSM Module**: Sends an SMS to a predefined phone number.

## Key Features
- **Simple Design**: Easy to assemble and use.
- **Customizable**: The phone number and message can be changed in the code.
- **Visual Feedback**: LEDs indicate the system’s status.

## Challenges
1. **GSM Module Configuration**: Configuring the GSM module to send SMS was tricky. I had to ensure the correct AT commands were sent at the right time.
2. **Power Management**: The GSM module required a stable power supply, which added complexity to the circuit design.
3. **Assembly Programming**: Writing efficient assembly code for the PIC microcontroller was challenging but rewarding.

## Results
The system works as intended! When the panic button is pressed, an SMS is sent within seconds. The LEDs provide clear feedback, making it easy to understand the system’s status.

## Future Improvements
- **Battery Backup**: Add a battery for portable use.
- **Multiple Recipients**: Send alerts to multiple phone numbers.
- **IoT Integration**: Integrate with IoT platforms for advanced monitoring.

## Conclusion
This project was a great learning experience. It combined my knowledge of hardware design, assembly programming, and problem-solving. I’m excited to see how this project can be improved and applied in real-world scenarios.

---

**Bernardo Xavier da Silva**  
Electrical Engineer | Data Scientist  
[LinkedIn](https://www.linkedin.com/in/bernardo-xavier-da-silva/) | [GitHub](https://github.com/Bernardo-Xavier)