# Drinkser 

![IMG_0381](https://user-images.githubusercontent.com/39228801/145053162-31a25fd9-dfc3-4644-8245-2f63b4ebcae6.jpg)


## IDD Final Project

Team Member: <br>
Jiacheng Peng (jp948)<br>
Wenlan Wei (ww367)<br>
Xingyu Tao (xt75)<br>

## Project Overview

Our project is called Drinkser, it is a cocktail dispenr that automatically mix differernt alcohol or drinks for you. All you have to do is place your empty bottle in front the machine, and press the drink you would like to have on the touch screen. Drinkser will make the drink for you.

## How to use it
First, place your empty cup under the tap in fornt of the machine. There will be selections of different cocktails/drinks shown on the touch screen. You will make your selection, and the machine will suck the liquid needed from the side to make your drink. 

## Parts needed
Raspberry pi 4 <br>
12V pumps <br> 
thing silicon tubing <br>
touch screen for Raspberry pi <br>
motors <br>
bread board <br>
battery box <br>
motor controller <br>

## Design
Below is a picture of the general idea. <br>
<img width="884" alt="Screen Shot 2021-12-07 at 12 21 17 AM" src="https://user-images.githubusercontent.com/39228801/144971227-61becb18-6140-469d-b94d-5ad33fcb45e4.png">

## Demo

[<img width="1138" alt="Screen Shot 2021-12-07 at 10 35 28 AM" src="https://user-images.githubusercontent.com/39228801/145059752-b644615d-5fc9-470c-9ce9-645721a4bf6c.png">](https://www.youtube.com/watch?v=HgxsOgSMFxE)

## Design Process

When we first start thinking about this idea, we were thinking about using motors to control the lid of a bottle for dispensing the drinks. But we found this is extremely hard to do. Instead we brought some pumps from Amazon, so that the pump could directly draw the liquid from the bottle. But there are no drivers or phiscal switch for the pump. The pump begins to work once its being connected to the current. We've tried using transisters to control the current. But the transister would cause a decrease of voltage and would not be able to actually starts the pump. Our solution is to tie the circuit on the tip of the motors. And we can contorl the motor for a indirect control of the pump. We use a battery pack for the power source of the pumps. Therefore the pumps would intiate sequentially instead of simultaneously. This could be avoid by using individual battery packs for each pump.
