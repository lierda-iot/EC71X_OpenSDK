# Lierda SpriteCoreBox Application Guide_v0.1

{link_to_translation}`zh_CN:[Chinese]`

[ChangeList](ChangeList.md)

> [!NOTE]
> Please check the silkscreen model and version on the main board to confirm that your development board version matches this application guide.

This guide will help you quickly get started with the **SpriteCoreBox** and provide detailed information about this development board.

**SpriteCoreBox** is an embedded core module integrating voice recognition, audio playback, and intelligent interaction, specifically designed for smart toys, educational devices, and interactive terminals. This core module features a built-in main control chip, audio system, and power supply module, enabling functions such as voice wake-up, conversational interaction, and content playback.

![](_images/灵芯盒%20应用指导_Rev0.1/file-20260417171958736.png)

This guide includes the following sections:
- [Getting Started](#getting-started): Briefly introduces the development board and hardware/software setup.
- [Hardware Reference](#hardware-reference): Detailed hardware description.
- [Hardware Versions](#hardware-versions): Lists historical hardware versions and known issues (if any).
- [Related Resources](#related-resources): Provides links to relevant documents.

## Getting Started

This section briefly introduces the **SpriteCoreBox** and explains how to flash firmware onto it and prepare necessary items.

### Component List

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%;">
  <thead>
    <!-- Header: TOP region column definition -->
    <tr><th style="width: 40%;">Main Component (TOP)</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td>L-CT4IT00-YP00W-03A_V04</td><td>Main Board PCB</td></tr>
    <tr><td>L-CT4IT00-YP00W-02A_V01</td><td>Dual Screen PCB</td></tr>
    <tr><td>L-CT4IT00-YP00W-03B_V02</td><td>Key Extension PCB</td></tr>
    <tr><td>xxxx</td><td>Enclosure</td></tr>
    <tr><td>103040A1</td><td>Battery</td></tr>
    <tr><td>JMO-627BA283H-1AXD63</td><td>Microphone</td></tr>
    <tr><td>2831NROOO-4P25D13H</td><td>Speaker</td></tr>
  </tbody>
</table>

【PCBA photo here】
L-CT4IT00-YP00W-03A_V04 (Main Board PCB)

[PCBA photo here]
L-CT4IT00-YP00W-02A_V01 (Dual Screen PCB)

[PCBA photo here]
L-CT4IT00-YP00W-03B_V02 (Key Extension PCB)

[Enclosure photo here]
xxxx (Enclosure)

[Battery photo here]
103040A1 (Battery)

[Microphone photo here]
JMO-627BA283H-1AXD63 (Microphone)

[Speaker photo here]
2831NROOO-4P25D13H (Speaker)

### Main Board Introduction

The main components and interfaces of the L-CT4IT00-YP00W-03A_V04 are described below:

【Main board PCBA top/bot view here】
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%;">
  <!-- Header: TOP side column titles -->
  <thead>
    <tr>
      <th style="width: 23%;">Main Components (TOP)</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <!-- ========== TOP Side Component List ========== -->
    <!-- On-board MIC (Reserved) -->
    <tr><td>On-board MIC (Reserved)</td><td>Choose either this or the external MIC connector</td></tr>
    <!-- Vibration Switch (Reserved) -->
    <tr><td>Vibration Switch (Reserved)</td><td>Functions as a vibration sensor; SHAKE pin shorts to GND when shaken</td></tr>
    <!-- Speaker Connector -->
    <tr><td>Speaker Connector</td><td>1.5mm/2-pin socket, for connecting a 4Ω/3W speaker</td></tr>
    <!-- Battery Connector, note pinout: + NTC - -->
    <tr><td>Battery Connector</td><td>1.5mm/3-pin socket, compatible with 103040A1 battery, pinout: <strong>+ NTC -</strong></td></tr>
    <!-- BOOT test point, for forced download mode -->
    <tr><td>BOOT Test Point</td><td>Forces download mode if the module becomes unresponsive/bricked</td></tr>
    <!-- Motor/Servo Connector, provides 2x PWM/Power/H-bridge differential outputs -->
    <tr><td>Motor/Servo Connector</td><td>1.25mm/6-pin socket, provides 2x PWM/Power/H-bridge differential outputs, use as needed</td></tr>
    <!-- Offline Voice Chip GX8006A -->
    <tr><td>GX8006A</td><td>Offline voice chip with local AEC and custom wake-word support</td></tr>
    <!-- Audio Amplifier Chip CST8302A -->
    <tr><td>CST8302A</td><td>Class-AB/Class-D audio amplifier; Class-AB is recommended for better AEC performance</td></tr>
    <!-- Charging Management Chip CL4056D -->
    <tr><td>CL4056D</td><td>Battery charging management IC, for 4.2V batteries; NTC recommendation: R<sub>25</sub>=100KΩ</td></tr>
    <!-- NOR Flash Memory -->
    <tr><td>NOR Flash</td><td>NOR flash chip, 32Mbit, compatible with 3.3V systems</td></tr>
    <!-- USB Type-C Connector -->
    <tr><td>USB Connector</td><td>Type-C port for power supply, charging, communication, and firmware download</td></tr>
    <!-- Reset Side Button -->
    <tr><td>Reset Side Button</td><td>Reset button, used to restart the module</td></tr>

    <!-- ========== BOT Side Sub-header (using <th> as separator row) ========== -->
    <tr><th>Main Components (BOT)</th><th>Description</th></tr>

    <!-- ========== BOT Side Component List ========== -->
    <!-- Antenna Connector, IPEX-1 Generation -->
    <tr><td>Antenna Connector</td><td>IPEX-1 generation socket, for external antenna connection</td></tr>
    <!-- Extension Button Connector, multiplexable as UART -->
    <tr><td>Extension Button Connector</td><td>1.25mm/6-pin socket, provides PWRKEY and 3 custom buttons (2 can be multiplexed as UART/serial)</td></tr>
    <!-- Cat.1 Module NT26F6D0 -->
    <tr><td>NT26F6D0 Module</td><td>Cat.1 cellular module, supports OPEN application development</td></tr>
    <!-- FPC Connector, for dual-display adapter board -->
    <tr><td>FPC Connector</td><td>0.5mm/16-pin FPC socket, for connecting the dual-display adapter board</td></tr>
    <!-- MIC Connector (external electret microphone) -->
    <tr><td>MIC Connector</td><td>1.25mm/2-pin socket, for connecting an external electret microphone</td></tr>
    <!-- Power On/Off Button (Pwrkey) -->
    <tr><td>Power Button</td><td>Pwrkey, used to power on/off the module</td></tr>
    <!-- RGB Status Indicator -->
    <tr><td>RGB LED</td><td>RGB status indicator, shows module operating state</td></tr>
    <!-- Green Charging Complete Indicator -->
    <tr><td>Green LED</td><td>Charging complete indicator, solid on when fully charged</td></tr>
    <!-- Red Charging Indicator -->
    <tr><td>Red LED</td><td>Charging status indicator, solid on during charging</td></tr>
    <!-- SIM Card Slot -->
    <tr><td>SIM Card Slot</td><td>Nano-SIM card socket for SIM card reading</td></tr>
  </tbody>
</table>

The key components and interfaces of the L-CT4IT00-YP00W-02A_V01 are as follows:
![](_images/灵芯盒%20应用指导_Rev0.1/file-20260416142304176.png)

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%;">
  <thead>
	<!-- Header -->
    <tr><th style="width: 23%;">Main Components (TOP)</th><th>Description</th></tr>
  </thead>
  <tbody>
    <!-- TOP Side Components -->
    <tr><td>LCD</td><td>Dual-screen display, can be used independently</td></tr>
    <!-- BOT Side Separator (as sub-header) -->
    <tr><th style="width: 23%;">Main Components (BOT)</th><th>Description</th></tr>
    <!-- BOT Side Components -->
    <tr><td>FPC Connector</td><td>0.5mm/16-pin FPC connector, used to connect to the main board</td></tr>
  </tbody>
</table>

### Getting Started

Before powering on, visually inspect the L-CT4IT00-YP00W-03A_V04 PCBA to ensure it is intact with no obvious damage.

#### Required Hardware

- L-CT4IT00-YP00W-03A_V04 PCBA
- USB data cable*
- Computer (Windows, Linux, or macOS)

> [!NOTE]
> Some USB cables only support power supply and charging, not communication or downloading. Ensure the USB cable you use supports firmware download.

#### Hardware Setup

The main board only requires a USB data cable for power, communication, and flashing. Connect the USB cable between the PC and the L-CT4IT00-YP00W-03A_V04 PCBA, then press and hold the power button for more than 3 seconds.

#### Driver Installation

For driver installation, please refer to [Lierda Cat.1 Module USB Driver Installation Guide](https://alidocs.dingtalk.com/i/nodes/1zknDm0WRaMv5M2wHDj01Xwb8BQEx5rG?corpId=dingecd566d61b3ecc77a39a90f97fcb1e09&doc_type=wiki_doc&utm_medium=search_main&utm_source=search). After installation, you should see Lierda USB ports in the Device Manager.


---

## Hardware Reference

### Functional Block Diagram

The functional block diagram of the SpriteCoreBox is shown below.
![](_images/灵芯盒%20应用指导_Rev0.1/file-20260416142304187.png)

### Power Supply Methods

The main board has a power switching circuit. The system can be powered in the following ways:
1. **Battery power supply**: The device integrates a 3.7V lithium battery. Press and hold the power button for 3 seconds to power on.
2. **Type-C port power supply**: Insert a USB data cable into the Type-C port; the system will automatically switch to Type-C power. Press and hold the power button for 3 seconds to power on.

### Charging Circuit

<figure align="center">
  <img src="_images/灵芯盒%20应用指导_Rev0.1/file-20260417102436335.png" alt="Charging reference circuit" width="75%">
  <figcaption>Charging reference circuit</figcaption>
</figure>
The CL4056D has a maximum charging voltage of 4.2V. NTC is recommended with R<sub>25</sub>=100KΩ for a charging range of 0~45°C, or R<sub>25</sub>=10KΩ for 0~50°C. As shown in the reference circuit, with the 103040A1 battery (R<sub>25</sub>=10KΩ, B<sub>25/50</sub>=3435), the designed charging temperature range is 0.46°C~50.22°C. See the [NTC calculation tool](_images/灵芯盒%20应用指导_Rev0.1/NTC计算工具_V1.2.xlsx)(XLSX) for details.

### USB Interface
<figure align="center">
  <img src="_images/灵芯盒%20应用指导_Rev0.1/file-20260416145552696.png" alt="USB connector reference circuit" width="75%">
  <figcaption>USB connector reference circuit</figcaption>
</figure>

### SIM Card Interface
<figure align="center">
  <img src="_images/灵芯盒%20应用指导_Rev0.1/file-20260417093604496.png" alt="SIM card socket reference circuit" width="75%">
  <figcaption>SIM card socket reference circuit</figcaption>
</figure>
In addition to the SIM card socket, the main board also reserves a solder pad for a SMD SIM card. The two overlap on the PCB; the socket is used by default. If a SMD SIM is needed, remove the socket before soldering.

### Key Expansion Interface
<figure align="center">
  <img src="_images/灵芯盒%20应用指导_Rev0.1/file-20260417094134651.png" alt="Key expansion connector reference circuit" width="75%">
  <figcaption>Key expansion connector reference circuit</figcaption>
</figure>
**Note the special uses of all key expansion IOs:**
1. PWRKEY is primarily used as the power on/off button. After power-on, the press duration can be used for different functions, e.g., short press for conversation, long press for shutdown.
2. KEY_FUNC is the only key that can be reused as a wakeup source, with higher interrupt priority. It can also be reused as AGPIO and remains active during module sleep.
3. IO1/IO2 are general-purpose IOs with lower interrupt priority, can be reused as UART for debugging.

### Motor/Servo Interface
<figure align="center">
  <img src="_images/灵芯盒%20应用指导_Rev0.1/file-20260417094406290.png" alt="Motor/servo connector reference circuit" width="75%">
  <figcaption>Motor/servo connector reference circuit</figcaption>
</figure>
The module provides 4 different PWM channels for motor and servo driving, supporting connection of one DC motor and two servos simultaneously.

### Microphone Interface
<figure align="center">
  <img src="_images/灵芯盒%20应用指导_Rev0.1/file-20260417095314016.png" alt="Microphone connector reference circuit" width="75%">
  <figcaption>Microphone connector reference circuit</figcaption>
</figure>
The SpriteCoreBox's microphone connector is already fitted with a microphone. If you need to connect an external electret microphone, pay attention to the terminal wire sequence; reverse polarity will not drive the microphone.

### RGB Indicator LED
<figure align="center">
  <img src="_images/灵芯盒%20应用指导_Rev0.1/file-20260417095125140.png" alt="RGB LED reference circuit" width="75%">
  <figcaption>RGB LED reference circuit</figcaption>
</figure>
The RGB LED follows the WS2812 timing.

---
## Hardware Versions

### L-CT4IT00-YP00W-03A_V04

- Series B modules are no longer recommended; changed to Series D (NT26F6D0).
- For GX8006A pins 18/20, there was ambiguity between the original factory pin names and the actual multiplexed functions; modified according to the multiplexed functions.

---

## Related Resources

- [SCH-PCB](_images/灵芯盒%20应用指导_Rev0.1/L-CT4IT00-YP00W-03A_V04_ref%20(2026-4-17%2016-00-31).zip) (ZIP)
- [BOM](_images/灵芯盒%20应用指导_Rev0.1/L-CT4IT00-YP00W-04_BOM.xlsx) (XLSX)
- [NTC Calculation Tool](_images/灵芯盒%20应用指导_Rev0.1/NTC计算工具_V1.2.xlsx) (XLSX)