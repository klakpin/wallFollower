# Wall follower
*Ilya Kuznetsov*

## Project description
This is the robot that will follow the wall on the desired distance.
## Description of the work process
First of all I created scheme of my system and got something like that:
![](https://pp.userapi.com/c840235/v840235159/911fd/zuxSZvifjOI.jpg)
Then I began implementation. First, naive implementation was (and it's the final) with one ultrasonic sensor. The problem is that when robot rotates the values from sensor aren't really actual, because sensor isn't perpendicular to wall. Then I've tried to use servo, that would rotates with the robot, then I've tried use to sensors, but the geometric task, that should be solved for this was too hard for me and all my friends. So I've decided to use only one sensor and try do do at least something with it.

## Explanation of the result values
I got these results mostly by empirical way. I re-read slides from presentations, watched some videos about PID controllers and this is all. I began set up from P part, then when robot became somehow stable I was working with D part, then I was tuning them all. 
## Why these values are the best?
These values aren't best. I suppose if I could use Matlab for system simulation I could improve my results, but ev3 compatible addon for Matlab requires Matlab account.

## Youtube video
Video is available by the [link](https://youtu.be/R1cqX-7YcWc) 
 