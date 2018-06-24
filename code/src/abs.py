#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-24 15:09:46
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

print('//-------------------');
print('Return the absolute value of a number:');
print("-9 ads is %d" %(abs(-9)));
print("5 ads is %d" %(abs(5)));
print('-------------------//');

print('//-------------------');
print('Return the absolute value of a floating point number:');
print("1.8 ads is %.1f" %(abs(1.8)));
print("0.8 ads is %.1f" %(abs(0.8)));
print("-0.8 ads is %.1f" %(abs(-0.8)));
print('-------------------//');

print('//-------------------');
print('Return the absolute value of a complex number:');
print("5j ads is %f" %(abs(5j)));
print("1+5j ads is %f" %(abs(1+5j)));
print("3+5j ads is %f" %(abs(3+5j)));
print('-------------------//');