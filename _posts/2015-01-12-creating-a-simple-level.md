---
title: 'Creating a Simple Level Flowchart System'
date: 2015-01-12 00:00:00
description: 
featured_image: '/images/blog/creating-a-flowchart-system/creating-a-flowchart-system-square.jpg'
tags: ['level design', 'flowchart', 'guide']
---

A level flowchart is like a roadmap that shows the player’s journey and actions in a level. It includes all the possible paths, triggers, and events. Designers use this to plan and visualise the player’s experience, making sure it’s logical and engaging. It can also help find any issues with flow or pacing, reveal bugs or unexpected player behaviour, and figure out the difficulty and balance of the level by seeing the challenges and rewards. It’s also a great way to share design ideas with the team.

#### Scenario

The player has to find a key in order to unlock the locked chest. In the locked chest, they find a sword which they can use to beat the defence timer section. Finishing it unlocks the door, allowing them to progress to the next level.

#### Steps

1. Break down the scenario into actions:
    - **Find** a key
    - **Unlock** chest
    - **Find** sword
    - **Defeat** defence timer
    - **Unlock** door
    - **Progress** to next level
2. Establish a legend (grouping and categorising the actions):
    - Exit/ Enter
    - An action
    - Mechanics (such as picking up a key, unlocking a door, race timer begin/ finish)
    - Getting an item
    - Has a fail state
3. Map out the level on some paper.
4. (Optional) Transfer the final design to diagram software like [draw.io](https://app.diagrams.net/).
6. Refine.

#### Example

<div class="gallery" data-columns="2">
    <img src='/images/blog/creating-a-flowchart-system/notes-1.jpg' />
    <img src='/images/blog/creating-a-flowchart-system/notes-2.jpg' />
</div>

#### Refinement

<img src='/images/blog/creating-a-flowchart-system/flowchart-version-1.jpg'/>

I added checks to see if the player has picked up the sword. They might just leave it in the chest. I also coloured the lines to make it easier to read. Green means they got it, red means they failed, and black means they just moved on to the next thing without any issues.

Looking at the cleaned-up draft, I can see some areas where my approach could be improved. It’s a bit tricky to follow all the lines, and there’s a lot of unnecessary information. Let’s refine the chart and remove any unnecessary details.

<img src='/images/blog/creating-a-flowchart-system/flowchart-version-2.jpg'/>

 
Now only fails that result in death are shown, otherwise it’s assumed that they lead back to the “explore” option. I removed the conditionals for picking up objects since having a fail doesn’t really add anything new. It's fine at this stage but I could refine it a little bit more.

<img src='/images/blog/creating-a-flowchart-system/flowchart-version-3.jpg'/>

I removed the fail states for simple conditionals (e.g. don't have key which leads to failure), and only included the successful paths.

#### Conclusion

As you can see, creating a detailed flowchart for level design is a must-do to make a player’s experience awesome. It helps find any design flaws, pacing issues, or ways to keep players engaged. By drawing out all the possible actions and outcomes, designers can make sure the gameplay is balanced and fun. Through refinement, they can remove any unnecessary complexity, leaving a clear roadmap that guides both the development team and the player through a logical and enjoyable journey. This iterative process not only makes the game better but also helps the design team talk to each other more effectively.