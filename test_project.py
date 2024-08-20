from project import inputNum,equal,clear,phy,click
from project import emc,w,F,P,Eh,wk,pw,wv

import pytest

def test_equal():
    assert equal()==""

def test_inputNum():
    assert inputNum("123")=="123"

def test_clear():
    assert clear()==""

def test_phy():
    assert phy()==0


def test_click():
    assert click()=="1"

def test_emc():
     assert emc()=="E = mc²(Joules)\nc = 3x10^8 ms^-1\nInput a value for mass in kilogram(kg):"

def test_w():
    assert w()=="W = mg(Newton)\ng = 9.81 ms^-2\nInput a value for mass in kilogram(kg):"


def test_F():
    assert F()=="F = ma(Newton)\na = Acceleration (ms^-2)\nm = mass (kg)\nInput values for mass in kilogram(kg) and acceleration in (ms^-2):"

def test_P():
    assert P()=="P = m/v (kgm^-3)\nm = mass (kg)\nv = volume (m^3) \nInput values for mass in kilogram(kg) and volume in cubic metre(m^3):"

def test_Eh():
    assert Eh()=="E = mgh(Joules)\ng = 9.81 ms^-2\nInput value for mass in kilogram(kg) and height in meters(m):"

def test_wk():
    assert wk()=="ΔW = FΔS(Joules)\nF = Force (ms^-2)\nΔS =Δdistance (m)\nInput values for foce in Newton(kgms^-2) and distance in meters(m):"
def test_pw():
    assert pw()=="P = W/t (Watt)\nW = work done (Joules)\nt = time (s)\nInput values for work done in Joules(J) and time in second(s):"
def test_wv():
    assert wv()=="V = fλ (speed)\nf = frequency (Hertz)\nλ = wavelength (m)\nInput values for fequency in Hertz(Hz) and wavelength in meters(m):"
