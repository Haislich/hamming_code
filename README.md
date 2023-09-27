# Introduction

This is a Python implementation of the paper [Error detection and error correcting codes](https://ieeexplore.ieee.org/document/6772729).

We assume that information is handled in a binary form.
This assumption is made both for mathematical convenience and because a binary system is a natural form of representing open  and closed relays.
The paper utilizes systematic codes, codes in which each code has n binary digits, where $m$ digits contain information and the remaining $r$ are used for error detection and correction.

We also define $R = \frac{1}{m}$ as the redundancy, which informs us about the efficency of the code in regards to transmission of information.
