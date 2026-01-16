# Spore Game Simulation

The assignment is inspired by the 2008 life simulation RTS game [Spore](https://www.spore.com/). Spore allows you to evolve creatures with different characteristics such as claws, sharp teeth, wings, and many many more.

The implementation provides the simulation of the interaction between two creatures as follows

Evolution phase:

- Evolve a random creature at a 0 location (log characteristics)
  This creature will play the role of the predator in the simulation

- Evolve a random creature at a random location between 0 and 1000 (log characteristics)
  This creature will play the role of the pray in the simulation

Chase Phase:

- Predator chases pray, pray runs away until:
  * Predator runs out of `stamina`. (log message: "Pray ran into infinity")
  * Predator catches pray. In this case, they enter the fight

Fight Phase:

- In the fight, both creatures attack until:
  * Predator runs out of `health`. (log message: "Pray ran into infinity")
  * Pray runs out of `health`. (log message: "Some R-rated things have happened") :D