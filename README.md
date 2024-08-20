Formula calculator
#### Video Demo:  <https://youtu.be/6rMmBv0t1BcE>
Description:
Being a student with great interests in physics, but in this subject,repetitively putting values of long digits constand into calculator is a cumbersome process. Therefore, I made a simple physics formula calculator,which I insert several basic physics formula into it.So we don't have to type again and again the constant in formula into our calculator.In addtion, this calculator also reminds us the units for variables in the formula.

Firstly,the main and only package in my project is tkinter.This GUI allows me to initialize my calculator screen size and headings by methods and functions: geometry(), title(), Label(),Entry() and Message(). I set up two screens,one for calcution and another for display physics formula.By putting arguments into functions Entry() and Message(), I adjusted the size of screens so they can fit into the window.

Secondly, I set up my buttons for numbers and operation character by using the function Button(), besides, I used differnt colors for each type of buttons. For example, I used gainsboro for number buttons and DarkSeaGreen4 for equal button.After I have set up the UI, I named a function called inputNum(i),which get value and store it by method get(), so the input numbers won't cover each other.Then, I defined a function called main(), which allows calculator to operate after press "=" button.

After I have completed the operation for calculations and the design of number buttons, I add a new button called Phy, the window is expanded and show more functions when the button is clicked and it will be reduced into original size if click again. In order to achieve this, I made an empty list and a function called click() which append integer 1 into the empty list every time you click the "Phy" button, then the function click() automatically operate another function called Phy(). The Phy() function calculate the remainder of sum of the integers in the list. If the sum is odd number, the window will unfold, if the sum is even number, the extra window will close.

Eventually, I defined some new functions and designed new buttons to display the physics formula in the upper screen, the constant in formula is automatically insert into the lower screen which is used for calculation.For some formula without constant, their variable is declared and units is showed.


