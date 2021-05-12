# Jason's Generator - Simple Open-source Generator
A Basic Number Printer, Useful for generating passwords, keys, sequences of numbers, and more.

## Installation
[Download and setup python](https://www.python.org/downloads/) if you haven't already.

Then, after [downloading the newest release](https://github.com/JasonDerulo1259/NumberPrinter-RandEvenConsecOdd/releases) of the number printer, follow the instructions on the program. (explained below)

## Usage
The first thing you see when you open the python program (assuming it was installed correctly) is something similar to this
(screenshot taken on version 0.3)

![Screenshot of first output from program](https://i.imgur.com/B5FHjGi.png)

This is where you can choose what to output.

The current options are Even numbers, Odd numbers, Consecutive numbers, Random numbers, non repeating password and repeating password.

To choose one you put in the letter that corresponds to it.
```python
e="Even", o="Odd", c="Consecutive", r="Random", p="Password (without repeating)", pr="Password (with repeating)"
```
Next, It will ask you how many times/strings to print. [image here](https://i.imgur.com/rIYxWV5.png)

Here, Just input any number you want, and it will print that many strings of It

For example. If you chose consecutive, And put `25`, 
It would print something similar to this **depending on the settings chosen after this point**

![Example Of Consecutive Output](https://i.imgur.com/dlFIE0t.png)

Anyway, After it asks you what the amount you want to print out is, It will then show output another option, that says [this](https://i.imgur.com/nWjp7WY.png)

`What speed should it print`
And it will go on to tell you to answer in seconds. And that 0.02 is a "Normal-ish" Speed.

This is where you choose the time between each string. 

The example below compares printing 100 numbers at 0.02 compared to 1

![Speed Comparison Part 1](https://i.imgur.com/UJUzBYG.gif) *A string every second ^*
![Speed Comparison Part 2](https://i.imgur.com/DaWzblC.gif) *A string every 0.02 seconds ^*

As you can see, changing the the time between each string is important.

Next up then, it will ask you what to put inbetween each string. 
Below is an example of two different ones.

![Inbetween Comparison Part1](https://i.imgur.com/heykgJU.png) ![Inbetween Comparison Part 2](https://i.imgur.com/PQsATPn.png)

Shown above is a comparison of spaces and commas inbetween, However, you can choose much more than that.

You can choose between [Spaces](https://i.imgur.com/heykgJU.png), [Commas](https://i.imgur.com/PQsATPn.png), [Newlines](https://i.imgur.com/m5Ap9xN.png), [Or Litterally any other string](https://i.imgur.com/3ATHUY0.png)

After this, it will tell you what your final number will be. (Unless random or password)

It will also ask you to confirm it with y/n. If you type `y`, it will continue, If you type `n`, it will exit.

### Situation Specific Usage
###### Random Specific Outputs:

There are some options in the program that will elicit some extra options

For example, If you choose it to output random numbers at the beggining, it will ask what the highest and lowest numbers should be

![Example of high/low cap for random](https://i.imgur.com/0nKZkSG.png)

It will also output a slightly different confirmation message

![Example of random confirmation](https://i.imgur.com/Rzt26jh.png)

###### Password Specific Outputs:

When generating passwords, It will ask how many letters it will have, With the `"Password (without repeating)"` option showing an extra 'max letters' message

![Password Message 1](https://i.imgur.com/rSlhghb.png)
![Password Message 2](https://i.imgur.com/JitmXBs.png)

Finally, It also shows a slightly different confirmation message for Each.

![Password Confirmation 1](https://i.imgur.com/S2HBZw3.png)
![Password Confirmation 2](https://i.imgur.com/XCfEBll.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact

Feel free to contact me on discord - 'ScrotumBasher#4316' - (although my tag changes a bit.) Or email me here : molopolo1259@gmail.com

## License

MIT License

Copyright (c) 2020/2021 JasonDerulo1259

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
