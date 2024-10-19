## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale
### 2.1 Refactoring Signs (Code Smells)
- Feature Envy: The `price_code` attribute is more frequently used by `Rental` than by `Movie`. `Rental` is the class that directly interacts with the `price_code` for pricing and rental points.
- Middle Man: The `Rental` class was calling methods on the `Movie` to access pricing information.
### 2.2 Design Principle
Single Responsibility Principle - According to SRP, a class should have only one responsibility.
  - The `Movie` class is responsible for holding information about the movie.
  - The `Rental` class is responsible for managing the rental process.

### 5.2 I choose to implement price_code_for_movie method in the PriceStrategy class for the following reasons:

  - Low Coupling: By placing this method here, it minimizes dependencies between the `Movie` and `Rental` classes. 
  - Single Responsibility Principle: The `PriceStrategy` class is responsible for defining price rules. By implementing the pricing logic here, we ensure that each class has a single responsibility.
  - High Cohesion: The `PriceStrategy` class is focused on pricing. By including the price code determination method here, we ensure that all price related functions are in the same class. 
