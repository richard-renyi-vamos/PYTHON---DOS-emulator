## A Simple Conceptual CPU Emulator

class SimpleEmulator:
    """
    A simple conceptual CPU emulator to demonstrate the core principles.
    This is not a functional DOS emulator but illustrates the fetch-decode-execute cycle.
    """
    def __init__(self):
        # 256 bytes of memory
        self.memory = [0] * 256
        # Registers: A, B, and the Instruction Pointer (IP)
        self.registers = {'A': 0, 'B': 0, 'IP': 0}
        # Flag to halt execution
        self.halted = False
        print("Emulator initialized.")
        
    def load_program(self, program):
        """Loads a program (list of integers) into memory."""
        for i, instruction in enumerate(program):
            if i < len(self.memory):
                self.memory[i] = instruction
            else:
                break
        print(f"Program loaded. Size: {len(program)} bytes.")

    def run(self):
        """Starts the main execution loop."""
        print("Starting execution...")
        while not self.halted:
            self.execute_next_instruction()
        print("Execution halted.")

    def execute_next_instruction(self):
        """Fetches, decodes, and executes the next instruction."""
        ip = self.registers['IP']
        if ip >= len(self.memory):
            print("Error: Instruction Pointer out of bounds.")
            self.halted = True
            return

        opcode = self.memory[ip]
        self.registers['IP'] += 1

        print(f"IP: {ip}, Opcode: 0x{opcode:02X}", end=" ")

        # Decode and execute based on opcode
        if opcode == 0x01:  # LOAD_A_IMMEDIATE: Load next byte into register A
            value = self.memory[self.registers['IP']]
            self.registers['A'] = value
            self.registers['IP'] += 1
            print(f"-> LOAD A, #{value}")

        elif opcode == 0x02:  # ADD_B_TO_A: Add register B to A, store in A
            self.registers['A'] += self.registers['B']
            print("-> ADD A, B")

        elif opcode == 0x03:  # PRINT_A: Print the value of register A
            print(f"-> PRINT A: {self.registers['A']}")

        elif opcode == 0x04:  # LOAD_B_IMMEDIATE: Load next byte into register B
            value = self.memory[self.registers['IP']]
            self.registers['B'] = value
            self.registers['IP'] += 1
            print(f"-> LOAD B, #{value}")

        elif opcode == 0xFF:  # HALT: Stop the emulator
            print("-> HALT")
            self.halted = True

        else:
            print(f"-> UNKNOWN OPCODE: 0x{opcode:02X}")
            self.halted = True

# --- Example Usage ---
if __name__ == "__main__":
    emulator = SimpleEmulator()

    # A simple program:
    # 1. Load the value 10 into register A
    # 2. Load the value 5 into register B
    # 3. Add B to A (Result: A = 15)
    # 4. Print the result
    # 5. Halt
    program_to_run = [
        0x01, 10,  # LOAD_A_IMMEDIATE 10
        0x04, 5,   # LOAD_B_IMMEDIATE 5
        0x02,      # ADD_B_TO_A
        0x03,      # PRINT_A
        0xFF       # HALT
    ]
    
    emulator.load_program(program_to_run)
    emulator.run()
