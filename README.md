\# Design Patterns – Free University of Tbilisi



This repository contains university projects developed as part of coursework focused on

object-oriented programming principles and design patterns.



\## Projects

\- \*\*Spore Game Simulation\*\*

\- \*\*Health App Backend API\*\*

\- \*\*Weather Monitoring System\*\*



Each project includes its own README with details.



All projects are implemented with Python 3.13







\# Health App Backend API



RESTful backend service for a Smart Habit Tracker application.



🧩 Core Features

1\. Manage Habits



Users are be able to:



Create new habits (like “Drink 8 glasses of water” or “Meditate for 10 minutes”)



View all their habits



Update or delete them when needed



Each habit has:



A name



A short description



A category (e.g., Health, Learning, Productivity)



A type (some habits are yes/no; others measure numbers like pages read or minutes exercised)



A goal or target value (optional)



The date it was created



2\. Organize Habits



Many users follow routines that consist of multiple smaller habits.

For example, “Morning Routine” could include “Stretch”, “Meditate”, and “Drink water”.



3\. Track Progress



Every day, users record their progress:



For yes/no habits: whether they did it or not



For measurable habits: how much they did



4\. Show Statistics



Users can see:



Total completions or progress



Current streaks (e.g., “5 days in a row!”)



Average performance over time









\# Spore Game Simulation



The assignment is inspired by the 2008 life simulation RTS game \[Spore](https://www.spore.com/). Spore allows you to evolve creatures with different characteristics such as claws, sharp teeth, wings, and many many more.



The implementation provides the simulation of the interaction between two creatures as follows



Evolution phase:



\- Evolve a random creature at a 0 location (log characteristics)

&nbsp; This creature will play the role of the predator in the simulation



\- Evolve a random creature at a random location between 0 and 1000 (log characteristics)

&nbsp; This creature will play the role of the pray in the simulation



Chase Phase:



\- Predator chases pray, pray runs away until:

&nbsp; \* Predator runs out of `stamina`. (log message: "Pray ran into infinity")

&nbsp; \* Predator catches pray. In this case, they enter the fight



Fight Phase:



\- In the fight, both creatures attack until:

&nbsp; \* Predator runs out of `health`. (log message: "Pray ran into infinity")

&nbsp; \* Pray runs out of `health`. (log message: "Some R-rated things have happened") :D







\# Weather Monitoring System



\## Description

A simple implementation for a \*\*Weather Monitoring System\*\* that helps us keep track of weather conditions like temperature, humidity, and wind speed. The system allows various parts of the system to respond automatically when the weather changes(changes are random). For example, if the temperature gets too hot, an alert might be triggered.

