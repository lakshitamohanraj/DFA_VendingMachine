#### Design a DFA that describes the behavior of a vending machine which accepts 1 dollar and its quarter, and charges $1.25 per soda. Once the machine receives at least $1.25, the soda can be dispensed to the user. The machine will not dispense a soda until at least $1.25 has been deposited, and it will not accept more money once it has already received greater than or equal to $1.25
##### DFA States:
**State 0 ($0)**: Initial state where no money has been inserted.
**State 1 ($0.25)**: After 25 cents (one quarter) has been inserted.
**State 2 ($0.50)**: After 50 cents (two quarters) have been inserted.
**State 3 ($0.75)**: After 75 cents (three quarters) have been inserted.
**State 4 ($1.00)**: After $1.00 (four quarters or one dollar) has been inserted.
**State 5 ($1.25)**: After $1.25 has been inserted. This is the accepting state where the vending machine dispenses a soda.
#### Input Alphabet:
𝑞 :Insert a quarter (25 cents).
𝑑 :Insert a dollar ($1).
#### Transition Rules:

##### From State 0:
𝑞 → State 1 ($0.25)
𝑑 → State 4 ($1.00)
##### From State 1:
𝑞 → State 2 ($0.50)
𝑑 → State 5 ($1.25, soda dispensed)
##### From State 2:
𝑞 → State 3 ($0.75)
𝑑 → State 5 ($1.25, soda dispensed)
##### From State 3:
𝑞 → State 4 ($1.00)
𝑑 → State 5 ($1.25, soda dispensed)
##### From State 4:
𝑞 → State 5 ($1.25, soda dispensed)
𝑑 → State 5 ($1.25, soda dispensed)
##### From State 5:
Once the machine is in State 5, no further inputs (quarters or dollars) are accepted because the machine has received sufficient money to dispense a soda.
