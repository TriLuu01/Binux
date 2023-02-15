# Binux
An 8-bit architecture CPU using a self-defined machine code to generate image files
Binux architecture is currently an elementary type of CPU. Currently, it is only capable of
performing 2 arithmetic operations: add and (instruction and). At the time, it can also load an
element from a register, with an immediate number as its offset. Lastly, it can run an empty
function that does not do anything called nop. However, the CPU can not store values back to
memory, as it is limited to the fact that each instruction only uses 8 bits or 1 byte.
The CPU design has 4 general-purpose registers: ×0,x1,×2,×3, an instruction memory, and data
memory.
Instructions:
Binux assembly is similar to other assembly languages, the exact syntax of the instruction is very
minimalist. Before discussing the syntax of the Or assembly language the table below introduces
each instruction and what it performs.
(Table 1)
Instruction Action
LDR Loads a value using operand register 1 as an address, which is then added by
an offset. The value found after adding the offset is then placed into a target
register.
and Compares the bits of register 1 and register 2, each bit is compared (1&1=1
anything else 0), the resulting bits are concatenated and placed into the target
register
add Adds register 1 and register 2 and places the total into target register
пор Is an empty instruction that does not write back any value to the registers
The and, add, and nop instruction all share a similar format when they are written in the Ori
assembly language. The only difference LDR has is that it uses an immediate number to
calculate an offset. Before writing Or assembly language some basic facts the user should know.
Capitalization and the number of spaces does not matter, however, commas must be in their
correct place, and each instruction must be written in one line and separately. Instructions can not
use registers above ×3, and cannot use a negative number as a register number. The amount of
