# Genetic Determinants
This is a genetic algorithm which can be used to find scalar coefficients for vectors in a matrix, in order to identify the linear combination which describes the determinant as null.

![Graph](https://github.com/paubric/python-genetic-determinants/blob/master/Figure.png)

## Background

In mathematics, a matrix is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns.

![eq1](https://github.com/paubric/python-genetic-determinants/blob/master/eq2.gif)

A linear combination is an expression constructed from a set of terms by multiplying each term by a constant and adding the results (e.g. a linear combination of x and y would be any expression of the form ax + by, where a and b are constants). The concept of linear combinations is central to linear algebra and related fields of mathematics. 

![eq2](https://github.com/paubric/python-genetic-determinants/blob/master/eq1.gif)

The determinant is a value that can be computed from the elements of a square matrix. It can be viewed as the scaling factor of the transformation described by the matrix. The algorithm can determine the _c_ coefficients from the upper figure.

## Method

In a genetic algorithm, a population of candidate solutions (called individuals) to an optimization problem is evolved toward better solutions. Each candidate solution has a set of properties (in this case an n-tuple describing the vector scaling factors) which can be mutated and altered. 

Initially, the whole generation is created randomly. The population array has `population_size` lines and `n` columns. Then, every epoch, the individuals are sorted by fitness and only a `survival_rate` fraction of the fittest survive, performing crossover. Additionally, every generation is the subject of a mutation through a standard distribution with  `mutation_magnitude` variance. The fitness of an individual is determined by the mean absolute error of the matrix row sums scaled with the individuals' coefficients.

Finally, we pick the fittest individual from the fittest generation as a result.

## TODO

- Normalize/denormalize matrix values for faster convergence
- Try mean squared error as fitness function

