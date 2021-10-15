"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 
Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.

"""
#time: O(n)
#space: O(1)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos_x, pos_y = 0, 0 
        pointing = 'N'
        
        step = {'N': (0,1),'L': (-1,0),'R': (1,0),'S': (0, -1)}
        rotate_left = {'N': 'L', 'L': 'S', 'S': 'R', 'R': 'N'}
        rotate_right = {'N': 'R', 'R': 'S', 'S': 'L', 'L': 'N'}
        
        for instruction in instructions:
            if instruction == 'L':
                pointing = rotate_left[pointing]
            elif instruction == 'R':
                pointing = rotate_right[pointing]
            elif instruction =='G':
                step_x, step_y = step[pointing]
                pos_x = pos_x + step_x
                pos_y = pos_y + step_y
                
        return (pos_x, pos_y) == (0,0) or pointing != 'N'
                            