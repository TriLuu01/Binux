# Binux
An 8-bit architecture CPU using a self-defined machine code to generate image files
Binux architecture is currently an elementary type of CPU. Currently, it is only capable of
performing 2 arithmetic operations: add and (instruction and). At the time, it can also load an
element from a register, with an immediate number as its offset. Lastly, it can run an empty
function that does not do anything called nop. However, the CPU can not store values back to
memory, as it is limited to the fact that each instruction only uses 8 bits or 1 byte.
The CPU design has 4 general-purpose registers: ×O,x1,×2,3, an instruction memory, and data
memory.
## Instructions:
Binux assembly is similar to other assembly languages, the exact syntax of the instruction is very
minimalist. Before discussing the syntax of the Or assembly language the table below introduces
each instruction and what it performs.
LDR Loads a value using operand register 1 as an address, which is then added by
an offset. The value found after adding the offset is then placed into a target
register.


and Compares the bits of register 1 and register 2, each bit is compared ( 1&1=1
anything else 0), the resulting bits are concatenated and placed into the target
register

add Adds register 1 and register 2 and places the total into target register

пор Is an empty instruction that does not write back any value to the registers
## Instructions to CPU:
To understand how the Ori CPU works. We first write our instructions into toTranslate. txt,
compile our instructions and load them into the CPU by loading translated. file into the
instruction memory. Those corresponding values must then be added to data memory manually.
After that, we can start running the program. The CPU will split up all the bits from instruction
memory, as shown in Table 4. Each of these bits is then used, in identifying which registers are
going to be used and where the output will be stored. The Alu opcode will be used to identify
whether we are using an immediate number or not, which operation we will doing, and if we are
writing back to memory. These are passed through multiplexors as control signals. If we are
loading for memory, then the outputs from instruction add and instruction and are disregarded,
only accepting the load instruction since the control signal will indicate the multiplexor to choose
the load value. These same principles can be applied to all the other instructions except we
would disregard the value from memory since the values for instructions and, and instruction add
are found in the registers. After the instruction is processed, on the rising edge of the clock cycle
of the next instruction, the value is stored.
