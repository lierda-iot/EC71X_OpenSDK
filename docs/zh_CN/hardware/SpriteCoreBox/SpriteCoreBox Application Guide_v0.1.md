# Lierda 灵芯盒 应用指导_Rev0.1

{link_to_translation}`en:[English]`

[变更履历](变更履历.md)

> [!NOTE] 备注
> 请查看主板上的丝印型号和版本，以确认您的开发板版本能与应用指导文档对应。

本指南将帮助您快速上手**灵芯盒**，并提供该款开发板的详细信息。

**灵芯盒**是一款集语音识别、音频播放、智能交互于一体的嵌入式核心模块，专为智能玩具、教育设备及互动终端设计。该机芯内置主控芯片、音频系统及供电模块，可实现语音唤醒、对话交互、内容播放等功能。

![](assets/灵芯盒%20应用指导_Rev0.1/file-20260417171958736.png)

本指南包括如下内容：
- [入门指南](灵芯盒%20应用指导_Rev0.1.md#入门指南)：简要介绍了开发板和硬件、软件设置指南。
- [硬件参考](灵芯盒%20应用指导_Rev0.1.md#硬件参考)：详细介绍了开发板的硬件。
- [硬件版本](灵芯盒%20应用指导_Rev0.1.md#硬件版本)：介绍硬件历史版本和已知问题（如有）。
- [相关资源](灵芯盒%20应用指导_Rev0.1.md#相关资源)：列出了相关文档的链接。

## 入门指南

本小节将简要介绍**灵芯盒**，说明如何在**灵芯盒**上烧录固件及相关准备工作。

### 组件介绍

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%;">
  <thead>
    <!-- 表头：TOP区域列定义 -->
    <tr><th style="width: 40%;">主要器件 (TOP)</th><th>描述</th></tr>
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

【此处有PCBA照片】
L-CT4IT00-YP00W-03A_V04 (Main Board PCB)

【此处有PCBA照片】
L-CT4IT00-YP00W-02A_V01 (Dual Screen PCB)

【此处有PCBA照片】
L-CT4IT00-YP00W-03B_V02 (Key Extension PCB)

【此处有外壳照片】
xxxx (Enclosure)

【此处有电池照片】
103040A1 (Battery)

【此处有麦克风照片】
JMO-627BA283H-1AXD63 (Microphone)

【此处有】
2831NROOO-4P25D13H (Speaker)

### 主板介绍

L-CT4IT00-YP00W-03A_V04主要器件和接口介绍如下：
【此处有主板PCBA top/bot view】

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%;">
  <!-- 表头：TOP 面列标题 -->
  <thead>
    <tr>
      <th style="width: 23%;">主要器件 (TOP)</th>
      <th>描述</th>
    </tr>
  </thead>
  <tbody>
    <!-- ========== TOP 面器件列表 ========== -->
    <!-- 板载麦克风（预留） -->
    <tr><td>板载MIC(预留)</td><td>与麦克风连接器二选一即可</td></tr>
    <!-- 振动开关（预留） -->
    <tr><td>振动开关(预留)</td><td>作为振动传感器使用，晃动时SHAKE短接到GND</td></tr>
    <!-- 扬声器连接器 -->
    <tr><td>扬声器连接器</td><td>1.5mm/2PIN连接器座子，用于连接4Ω/3W喇叭</td></tr>
    <!-- 电池连接器，注意线序：+ NTC - -->
    <tr><td>电池连接器</td><td>1.5mm/3PIN连接器座子，适配电池103040A1，线序为<strong>+ NTC -</strong></td></tr>
    <!-- BOOT 测试点，用于强制下载模式 -->
    <tr><td>BOOT测试点</td><td>用于模组变砖时强制进入下载模式</td></tr>
    <!-- 电机/舵机连接器，提供 2 路 PWM / 电源 / H 桥差分输出 -->
    <tr><td>电机/舵机连接器</td><td>1.25mm/6PIN连接器座子，提供2路PWM/电源/H桥差分输出，按需使用</td></tr>
    <!-- 离线语音芯片 GX8006A -->
    <tr><td>GX8006A</td><td>离线语音芯片，具备本地AEC、自定义唤醒词能力</td></tr>
    <!-- 功放芯片 CST8302A -->
    <tr><td>CST8302A</td><td>AB/D类功放，建议使用AB类提升AEC效果</td></tr>
    <!-- 充电管理芯片 CL4056D -->
    <tr><td>CL4056D</td><td>充电管理芯片，适用4.2V电池，NTC建议使用 R<sub>25</sub>=100KΩ</td></tr>
    <!-- Nor Flash 存储器 -->
    <tr><td>Nor flash</td><td>Nor flash芯片，32Mbit，适用于3.3V系统</td></tr>
    <!-- USB Type-C 连接器 -->
    <tr><td>USB连接器</td><td>Type-C接口连接器，用于供电、充电、通信、下载</td></tr>
    <!-- 复位侧键 -->
    <tr><td>复位侧键</td><td>Reset，用于复位模组</td></tr>

    <!-- ========== BOT 面子表头（使用 <th> 作为分隔行） ========== -->
    <tr><th>主要器件 (BOT)</th><th>描述</th></tr>

    <!-- ========== BOT 面器件列表 ========== -->
    <!-- 天线座子，IPEX-1 代 -->
    <tr><td>天线座子</td><td>IPEX-1 代座子，适配</td></tr>
    <!-- 拓展按键连接器，可复用为串口 -->
    <tr><td>拓展按键连接器</td><td>1.25mm/6PIN连接器座子，提供PWRKEY和3个自定义按键(其中2个可复用为串口)</td></tr>
    <!-- Cat.1 模组 NT26F6D0 -->
    <tr><td>NT26F6D0模组</td><td>Cat.1模组，支持OPEN应用开发</td></tr>
    <!-- FPC 连接器，用于双目屏转接板 -->
    <tr><td>FPC 连接器</td><td>0.5mm/16PIN FPC连接器，用于连接双目屏转接板</td></tr>
    <!-- 麦克风连接器（外接驻极体麦克风） -->
    <tr><td>麦克风连接器</td><td>1.25mm/2PIN连接器座子，用于连接驻极体麦克风</td></tr>
    <!-- 开关机按键（Pwrkey） -->
    <tr><td>开关机按键</td><td>Pwrkey，用于模组开关机</td></tr>
    <!-- RGB 状态指示灯 -->
    <tr><td>RGB LED</td><td>RGB指示灯，指示模组工作状态</td></tr>
    <!-- 绿色充电完成指示灯 -->
    <tr><td>Green LED</td><td>充电完成指示灯，充满电时常亮</td></tr>
    <!-- 红色充电指示灯 -->
    <tr><td>Red LED</td><td>充电状态指示灯，充电中时常亮</td></tr>
    <!-- SIM 卡座 -->
    <tr><td>SIM 卡座</td><td>Nano-SIM卡座连接器，用于SIM卡读卡</td></tr>
  </tbody>
</table>

L-CT4IT00-YP00W-02A_V01关键物料和接口介绍如下：
![](assets/灵芯盒%20应用指导_Rev0.1/file-20260416142304176.png)

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%;">
  <thead>
	<!-- 表头 -->
    <tr><th style="width: 23%;">主要器件 (TOP)</th><th>描述</th></tr>
  </thead>
  <tbody>
    <!-- TOP 面器件 -->
    <tr><td>LCD</td><td>双目屏，可以单独使用</td></tr>
    <!-- BOT 面分隔行（作为子表头） -->
    <tr><th style="width: 23%;">主要器件 (BOT)</th><th>描述</th></tr>
    <!-- BOT 面器件 -->
    <tr><td>FPC 连接器</td><td>0.5mm/16PIN FPC 连接器，用于连接主板</td></tr>
  </tbody>
</table>

### 开始使用

上电前目视检查 L-CT4IT00-YP00W-03A_V04 PCBA 完好，无明显缺损。

#### 必备硬件

- L-CT4IT00-YP00W-03A_V04 PCBA
- USB数据线*
- 电脑（Windows、Linux 或 macOS）

> [!NOTE] 备注
> 部分 USB 数据线仅支持供电、充电，无法通信、下载，请确保使用的 USB 数据线可以下载固件。

#### 硬件设置

主板仅需要USB数据线供电、通信和烧录，使用USB数据线连接PC和L-CT4IT00-YP00W-03A_V04 PCBA，长按开关机按键3秒以上。

#### 安装驱动

驱动安装请参考[Lierda 移芯CAT.1模组USB驱动安装指导说明](https://alidocs.dingtalk.com/i/nodes/1zknDm0WRaMv5M2wHDj01Xwb8BQEx5rG?corpId=dingecd566d61b3ecc77a39a90f97fcb1e09&doc_type=wiki_doc&utm_medium=search_main&utm_source=search)，安装完成后可从设备管理器中看到Lierda的USB端口。

---

## 硬件参考

### 功能框图

灵芯盒功能框图如下所示。
![](assets/灵芯盒%20应用指导_Rev0.1/file-20260416142304187.png)

### 供电方式

主板上设计有电源切换电路，可通过以下方法为系统供电：
1. 通过`电池`供电
	设备内部集成3.7V锂电池，按下开关机按键3s开机即可。
2. 通过`Type-C口`供电
	将Type-C口的USB数据线插入USB接口，系统电源自动切换至Type-C供电，按下开关机按键3s开机即可。

### 充电电路

<figure align="center">
  <img src="assets/灵芯盒%20应用指导_Rev0.1/file-20260417102436335.png" alt="充电管理参考电路" width="75%">
  <figcaption>充电管理参考电路</figcaption>
</figure>
CL4056D最高充电电压4.2V，NTC建议选用R<sub>25</sub>=100KΩ的电池，可设计的充电范围为0~45℃，R<sub>25</sub>=10KΩ时可设计的充电范围为0~50℃。如参考电路所示，搭配103040A1电池（R<sub>25</sub>=10KΩ,B<sub>25/50</sub>=3435），设计的充电温度范围为0.46℃~50.22℃。具体计算方式见下表：[NTC计算工具](assets/灵芯盒%20应用指导_Rev0.1/NTC计算工具_V1.2.xlsx)(XLSX)

### USB接口

<figure align="center">
  <img src="assets/灵芯盒%20应用指导_Rev0.1/file-20260416145552696.png" alt="USB连接器参考电路" width="75%">
  <figcaption>USB连接器参考电路</figcaption>
</figure>

### SIM卡接口

<figure align="center">
  <img src="assets/灵芯盒%20应用指导_Rev0.1/file-20260417093604496.png" alt="SIM卡座参考电路" width="75%">
  <figcaption>SIM卡座参考电路</figcaption>
</figure>
除SIM卡座外，主板上还预留贴片SIM卡封装，两者在PCB上位置重叠，默认使用卡座，若需贴片SIM可拆除卡座后焊接。

### 按键拓展接口

<figure align="center">
  <img src="assets/灵芯盒%20应用指导_Rev0.1/file-20260417094134651.png" alt="按键拓展连接器参考电路" width="75%">
  <figcaption>按键拓展连接器参考电路</figcaption>
</figure>
**请注意，所有按键拓展的IO均存在特殊用法：**
1. PWRKEY基础用法是作为开关机按键，在开机后可以调整按下时长用作功能按键，如：短按对话、长按关机
2. KEY_FUNC是唯一可复用为wakeup的按键，中断优先级更高，也可以复用为AGPIO，在模组休眠时保持
3. IO1/IO2是普通IO，中断优先级偏低，可复用为串口方便调试

### 电机/舵机接口

<figure align="center">
  <img src="assets/灵芯盒%20应用指导_Rev0.1/file-20260417094406290.png" alt="电机/舵机连接器参考电路" width="75%">
  <figcaption>电机/舵机连接器参考电路</figcaption>
</figure>
模组提供了4路不同的PWM作为电机和舵机驱动，支持同时外接1个直流电机和2个舵机。

### 麦克风接口

<figure align="center">
  <img src="assets/灵芯盒%20应用指导_Rev0.1/file-20260417095314016.png" alt="麦克风连接器参考电路" width="75%">
  <figcaption>麦克风连接器参考电路</figcaption>
</figure>
灵芯盒内麦克风连接器已插入麦克风，如需外接其他驻极体麦克风请注意端子线序，正负极接反时无法驱动。

### RGB指示灯

<figure align="center">
  <img src="assets/灵芯盒%20应用指导_Rev0.1/file-20260417095125140.png" alt="RGB LED参考电路" width="75%">
  <figcaption>RGB LED参考电路</figcaption>
</figure>
RGB LED符合WS2812时序。

---

## 硬件版本

### L-CT4IT00-YP00W-03A_V04

- B系列模组后续不主推，修改为D系列（NT26F6D0）
- GX8006A pin18/pin20 原厂引脚名与实际复用功能存在歧义，根据复用功能修改

---

## 相关资源

- [SCH-PCB](assets/灵芯盒%20应用指导_Rev0.1/L-CT4IT00-YP00W-03A_V04_ref%20(2026-4-17%2016-00-31).zip)(ZIP)
- [BOM](assets/灵芯盒%20应用指导_Rev0.1/L-CT4IT00-YP00W-04_BOM.xlsx)(XLSX)
- [NTC计算工具](assets/灵芯盒%20应用指导_Rev0.1/NTC计算工具_V1.2.xlsx)(XLSX)