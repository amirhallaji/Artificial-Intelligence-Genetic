<p align='center'>
    <h2 align='center'>Jay Leno Garage</h2>
    <img src="../icons/jayleno.jpg"></img>
</p>

This problem gives us some input as **price** and **value** and wants the best case in which the **value** is maximized. One important thing is that the money of the buyer should be much enough to buy the cars and this issue is checked in the code.

### Initial Population
Depending on the number of inputs, I produce binary values(0 and 1) which are the final answers of our problem. **1** means **buy** and **0** means **don't buy**.
If the length of the input is **n**, I produce **2^(N-1)** binary values randomly as our **genes**.

### Crossover
For crossover, I chose 1-point crossover. The parents are selected randomly. The first half of the gene of the child is for father and the other half is from mother and new offsprings are generated in this way.

### Mutation
For this, I chose Bit-Flipping, in which **1/n** genes of the population are selected and one of their bits are toggled randomly.

### Fitness function
In this part, I gave each string of genes a score which is the value of the final cars in the garage. Addition to this, the budget of the buyer is checked here.

### Choosing Survivals
Now we have a list of genes with their score around them. For the next generation, I remove the last **20%** of the population, those with the least score.

**This process is repeated for N generations, which N is the length of the chromosome.**

### Output
The output is the list of **1s and 0s** which is the best case for buying the cars.