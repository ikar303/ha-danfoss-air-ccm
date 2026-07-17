# Danfoss Air CCM Native TCP Protocol

This document describes the native TCP protocol used by Danfoss Air CCM ventilation units.

The protocol has been reverse engineered using the official Danfoss PC Tool, dnSpy source code analysis and live TCP packet captures.

Whenever possible, protocol behaviour has been verified against the original Danfoss .NET source code.

> Native TCP Protocol (TCP Port **30046**)

---

# Overview

Unlike Modbus, Danfoss Air CCM uses its own proprietary binary protocol.

Communication is completely local.

Features:

- Native TCP protocol
- No cloud
- No Internet access
- Fixed packet size
- Persistent TCP connection
- Multiple protocol endpoints
- Read and write support
- Fast response time

---

# Connection

| Item | Value |
|------|------|
| Protocol | TCP |
| Port | 30046 |
| Default Endpoint | 1 |
| Packet Size | 63 bytes |
| Timeout | 5 seconds |

A single TCP connection may remain open indefinitely and can be reused for multiple requests.

---

# Endpoints

Unlike Modbus, the Danfoss protocol stores parameters on multiple logical endpoints.

| Endpoint | Purpose |
|---------:|---------|
|0|System information and runtime counters|
|1|Configuration and operating status|
|4|Live temperatures and actual fan speeds (RPM)|
|6|Scheduler, arrays, alarm log and Z-Wave|

---

# Packet Layout

Every packet is exactly **63 bytes**.

Unused bytes are filled with **0x00**.

---

## Read Request

| Byte | Description |
|-----:|-------------|
|0|Endpoint|
|1|Command|
|2|Parameter High|
|3|Parameter Low|
|4-62|Reserved (0x00)|

Example

```
01 04 17 81
```

Read parameter **6017** (Fan Step).

---

## Write Request

| Byte | Description |
|-----:|-------------|
|0|Endpoint|
|1|Command|
|2|Parameter High|
|3|Parameter Low|
|4|Value|
|5-62|Reserved (0x00)|

Example

```
01 06 17 81 05
```

Write Fan Step = **5**.

---

# Commands

| Value | Meaning |
|------:|---------|
|0x04|Read Parameter|
|0x06|Write Parameter|

No additional commands have been identified.

---

# Responses

The controller always returns a **63-byte** response packet.

Only the first bytes contain useful data depending on the parameter type.

---

## BOOL

```
0 = False
1 = True
```

Examples

- Boost
- Auto Boost
- Bypass
- Auto Bypass

---

## BYTE

Single unsigned byte.

Example

```
05
```

Result

```
5
```

---

## WORD

Unsigned 16-bit integer.

Example

```
02 BF
```

```
703
```

Used for:

- Alarm Code
- Supply Fan Speed (RPM)
- Extract Fan Speed (RPM)

---

## SHORT

Signed 16-bit integer stored in hundredths.

Example

```
09 D0
```

```
0x09D0 = 2512

25.12 °C
```

Negative values use signed 16-bit integers.

Example

```
FF 38

-200

-2.00 °C
```

---

## PERCENT

Relative Humidity and Filter Fouling use

```
value × 100 / 255
```

Example

```
158

158 × 100 / 255 = 61.96 %
```

---

## DATETIME

The official Danfoss driver stores timestamps as six bytes.

| Byte | Description |
|-----:|-------------|
|0|Second|
|1|Minute|
|2|Hour (bit 7 = DST)|
|3|Day + Day of Week|
|4|Month|
|5|Year - 2000|

Used by:

- Away Start Time
- Away End Time

---

# Example Frames

## Read Fan Step

Request

```
01 04 17 81
```

Response

```
03
```

Fan Step = **3**

---

## Set Fan Step = 6

Request

```
01 06 17 81 06
```

---

## Read Supply Fan Speed

Request

```
04 04 14 50
```

Parameter

```
5200
```

Response

```
02 BF
```

Result

```
703 RPM
```

---

## Read Extract Fan Speed

Request

```
04 04 14 51
```

Parameter

```
5201
```

---

## Read Outdoor Temperature

Request

```
01 04 14 72
```

Parameter

```
5234
```

Response

```
09 A6
```

```
2470

24.70 °C
```

---

## Enable Boost

Parameter

```
5424
```

Request

```
01 06 15 30 01
```

---

## Disable Boost

```
01 06 15 30 00
```

---

# Parameter Addressing

Parameters are addressed using decimal identifiers and transmitted as **big-endian unsigned 16-bit integers**.

| Parameter | Hex |
|----------:|----:|
|5138|0x1412|
|5160|0x1428|
|5184|0x1440|
|5200|0x1450|
|5201|0x1451|
|5234|0x1472|
|5235|0x1473|
|5236|0x1474|
|5237|0x1475|
|5424|0x1530|
|5891|0x1703|
|6017|0x1781|

---

# Communication Notes

- All packets are exactly **63 bytes**.
- One TCP connection may be reused for multiple requests.
- Parameters are transmitted using big-endian byte order.
- Responses are immediate.
- Unsupported parameters usually return zero.
- Invalid write operations are silently ignored.
- Different parameter groups may require different endpoints.

---

# Known Protocol Behaviour

The following behaviour has been verified against the official Danfoss software.

- Packets are always 63 bytes.
- One TCP connection is reused.
- Temperatures are stored as signed SHORT values divided by 100.
- Relative Humidity uses `value × 100 / 255`.
- Filter Fouling uses `value × 100 / 255`.
- Boost Auto uses inverted logic (`0 = enabled`, `1 = disabled`).
- Auto Bypass uses inverted logic.
- Boost Max Step is stored multiplied by 10.
- Supply Fan Speed (5200) is available only on endpoint **4**.
- Extract Fan Speed (5201) is available only on endpoint **4**.
- Official Danfoss PC Tool reads Outdoor Temperature from endpoint **0** (parameter **820**).
- Home Assistant integration reads Outdoor Temperature from endpoint **1** (parameter **5234**).

---

# Write Dependencies

Some parameters depend on other settings.

## Boost

Before enabling Boost (5424), the controller expects:

- Boost Max Step
- Boost Duration
- Auto Boost

to be configured first.

## Away Mode

Away mode is controlled by writing:

- Away Start Time
- Away End Time

The controller determines whether Away mode is active from the configured time interval.

---

# Reverse Engineering

The protocol was reconstructed using:

- Official Danfoss PC Tool
- Danfoss HRV .NET assemblies
- Decompiled official source code
- dnSpy analysis
- Wireshark packet captures
- Native TCP traffic
- Live testing on Danfoss Air CCM
- Live testing on Danfoss W1A2

No official protocol documentation from Danfoss has been published.

---

# Future Work

The following protocol features are currently under investigation.

- Weekly Scheduler
- Week Profiles
- Alarm Log
- Night Cooling
- Defrost
- Heating Surface
- Z-Wave
- Automatic controller discovery
- Firmware detection