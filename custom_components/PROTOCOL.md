# Danfoss Air CCM Native TCP Protocol

This document describes the native TCP protocol used by Danfoss Air CCM ventilation units.

The protocol has been reverse engineered from the official Danfoss PC Tool and packet captures.

> TCP Port **30046**

---

# Overview

Unlike Modbus, Danfoss Air CCM uses its own proprietary binary protocol.

Communication is completely local.

Features:

- Native TCP
- No cloud
- No Internet access
- Fixed packet size
- Very fast response
- Read and write support

---

# Connection

| Item | Value |
|------|------|
| Protocol | TCP |
| Port | 30046 |
| Endpoint | 1 |
| Packet Size | 63 bytes |
| Timeout | 5 seconds |

One TCP connection can remain open for multiple requests.

---

# Packet Layout

Every packet is exactly **63 bytes**.

## Read request

| Byte | Description |
|-----:|-------------|
| 0 | Endpoint |
| 1 | Command |
| 2 | Parameter High |
| 3 | Parameter Low |
| 4-62 | Reserved (0x00) |

Example:

```
01 04 15 61
```

Read parameter **5473** (Fan Step)

---

## Write request

| Byte | Description |
|-----:|-------------|
| 0 | Endpoint |
| 1 | Command |
| 2 | Parameter High |
| 3 | Parameter Low |
| 4 | Value |
| 5-62 | Reserved |

Example

```
01 06 15 61 05
```

Write value **5** to parameter **5473**

---

# Commands

| Value | Meaning |
|------:|---------|
| 0x04 | Read parameter |
| 0x06 | Write parameter |

No other commands are currently implemented.

---

# Responses

The controller always replies with a 63-byte packet.

For BYTE values:

```
Byte 0 = value
```

Example

```
05
```

means

```
5
```

---

For SHORT values

```
Byte0 Byte1
```

Example

```
09 D0
```

```
0x09D0 = 2512

2512 / 100 = 25.12 °C
```

Negative temperatures use signed 16-bit integers.

Example

```
FF 38

0xFF38 = -200

-2.00 °C
```

---

# Supported Data Types

## BYTE

Unsigned 8-bit value.

Examples

- Fan Step
- Boost Timer
- Supply Step

---

## SHORT

Signed 16-bit integer divided by 100.

Examples

- Outdoor Temperature
- Supply Temperature
- Extract Temperature
- Exhaust Temperature

---

## WORD

Unsigned 16-bit integer.

Examples

- Alarm Code

---

## BOOL

```
0 = False

1 = True
```

Examples

- Boost
- Bypass
- Boost Auto

---

## PERCENT

Humidity uses

```
value × 100 / 255
```

Example

```
158

158 × 100 / 255 = 61.96 %
```

---

# Example Frames

## Read Fan Step

Request

```
01 04 15 61
```

Response

```
03
```

Fan Step = 3

---

## Set Fan Step = 6

Request

```
01 06 15 61 06
```

---

## Read Outdoor Temperature

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

The protocol uses decimal parameter numbers.

Example

| Parameter | Hex |
|----------:|----:|
| 5138 | 0x1412 |
| 5160 | 0x1428 |
| 5184 | 0x1440 |
| 5234 | 0x1472 |
| 5424 | 0x1530 |
| 5473 | 0x1561 |
| 5891 | 0x1703 |
| 6017 | 0x1781 |

---

# Communication Notes

- All packets are exactly 63 bytes.
- Multiple requests may use the same TCP connection.
- The controller answers immediately.
- Values are returned in big-endian format.
- Unknown parameters usually return zero.
- Invalid writes are silently ignored.

## Write Dependencies

Some parameters are not independent.

For example, enabling **Boost** requires that the associated Boost configuration parameters are written first:

- Boost Maximum Step
- Boost Timer
- Boost Auto

The Danfoss controller may reject or ignore incomplete write sequences.


---

# Reverse Engineering

The protocol was reconstructed using:

- Official Danfoss PC Tool
- Wireshark packet captures
- dnSpy analysis
- Danfoss HRV Driver
- Native TCP traffic
- Live testing on Danfoss Air CCM
- Live testing on Danfoss W1A2

No official protocol documentation from Danfoss was available.

---

# Future Work

The following protocol features are currently under investigation:

- Weekly Scheduler
- Program Profiles
- Alarm Log
- Filter Reset
- Filter Fouling
- Resultant Fan Step
- Bypass Auto
- Night Cooling
- Operating State
- Device Discovery