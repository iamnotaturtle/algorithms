/**
 * Taken from Writing a Compiler in Go
 * @param {[]} program array of string instructions and integer values
 */
const virtualMachine = (program) => {
    const stack = [];
    let stackPointer = 0;
    let programCounter = 0;
    let right, left;


    while (programCounter < program.length) {
        let currentInstruction = program[programCounter];

        switch(currentInstruction) {
            case 'PUSH':
                stack[stackPointer] = program[programCounter + 1];
                stackPointer += 1;
                programCounter += 1;
                break;
            case 'ADD':
                right = stack[stackPointer - 1];
                stackPointer -= 1;
                left = stack[stackPointer - 1];
                stackPointer -= 1;
                stack[stackPointer] = right + left;
                stackPointer += 1;
                break;
            case 'SUB':
                right = stack[stackPointer - 1];
                stackPointer -= 1;
                left = stack[stackPointer - 1];
                stackPointer -= 1;
                stack[stackPointer] = left - right;
                stackPointer += 1;
                break;
        }
        programCounter += 1;
    }

    console.log("stacktop: ", stack[stackPointer-1]);
};

const program = [
    'PUSH', 3,
    'PUSH', 4,
    'ADD',
    'PUSH', 5,
    'SUB',
  ];
virtualMachine(program);