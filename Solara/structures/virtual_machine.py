# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/03/17
# ------------------------------------------------------------
import sys
from structures.execution_block import executionBlock
from turtle import *

class virtualMachine:

    def __init__(self, quadQueue, mainMemory, funDir, programID):
        print('Initializing virtual machine....')
        self.mainMemory = mainMemory
        self.funDir = funDir
        self.mainMemory.malloc(self.funDir.search(programID)[4], self.funDir.search(programID)[5])
        print(self.mainMemory)
        self.pen = self.turtle_setup()
        self.execute(quadQueue.quadList)
        self.pen.getscreen()._root.mainloop()

    # Class variables
    currentParameters = []
    have_global_definitions_been_processed = False
    executionBlock = executionBlock()

    # stringTo methods

    def __str__(self):
        return ""

    def __unicode__(self):
        return ""

    def turtle_setup(self):
        pen = Pen()
        pen.screen.bgcolor('#94B3C6')
        pen.color('#f4425c')
        return pen

    def is_virtual_address_global(self, virtual_address):
        if self.mainMemory.is_virtual_address_global_or_constant(virtual_address):
            return True
        else:
            return False

    def execute(self, quadList):

        index = 0
        while index <= (len(quadList) - 1):

            # Multiplication operation
            if quadList[index][0] == "*":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    result = left_value * right_value
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    result = left_value * right_value
                    self.mainMemory.set_value(quadList[index][3], result)

            # Division operation
            elif quadList[index][0] == "/":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if right_value == 0:
                        self.error_division_by_zero()
                    result = left_value / right_value
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if right_value == 0:
                        self.error_division_by_zero()
                    result = left_value / right_value
                    self.mainMemory.set_value(quadList[index][3], result)

            # Addition operation
            elif quadList[index][0] == "+":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    result = left_value + right_value
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    result = left_value + right_value
                    self.mainMemory.set_value(quadList[index][3], result)

            # Subtraction operation
            elif quadList[index][0] == "-":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    result = left_value - right_value
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    result = left_value - right_value
                    self.mainMemory.set_value(quadList[index][3], result)

            # Less than operation
            elif quadList[index][0] == "<":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value < right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value < right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Less equal than operation
            elif quadList[index][0] == "<=":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value <= right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value <= right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Greater than operation
            elif quadList[index][0] == ">":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value > right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value > right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Greater equal than operation
            elif quadList[index][0] == ">=":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value >= right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value >= right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Or operation
            elif quadList[index][0] == "||":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value or right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value or right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # And operation
            elif quadList[index][0] == "&&":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value and right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value and right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Is equals operation
            elif quadList[index][0] == "==":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value == right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value == right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Mod operation
            elif quadList[index][0] == "%":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    result = left_value % right_value
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    result = left_value % right_value
                    self.mainMemory.set_value(quadList[index][3], result)

            # Assignation operation
            elif quadList[index][0] == "=":
                #print(str(index) + ": " + str(quadList[index][3]) + " = " + str(quadList[index][1]))
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        #print('global or constant')
                        value = self.mainMemory.get_value(quadList[index][1])
                        #print(value)
                        self.executionBlock.set_value(quadList[index][3], value)
                    else:
                        #print('local')
                        value = self.executionBlock.get_value(quadList[index][1])
                        #print(value)
                        self.executionBlock.set_value(quadList[index][3], value)
                else:
                    #print('global')
                    value = self.mainMemory.get_value(quadList[index][1])
                    #print(value)
                    self.mainMemory.set_value(quadList[index][3], value)

            # Negation operation
            elif quadList[index][0] == "!":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        value = self.executionBlock.get_value(quadList[index][1])

                    self.executionBlock.set_value(quadList[index][3], not value)
                else:
                    value = self.mainMemory.get_value(quadList[index][1])
                    self.mainMemory.set_value(quadList[index][3], not value)

            # GOTOF operation
            elif quadList[index][0] == "GOTOF":
                value = self.executionBlock.get_value(quadList[index][1])

                if not value:
                    index = (quadList[index][3] - 1)

            # GOTO operation
            elif quadList[index][0] == "GOTO":
                index = (quadList[index][3] - 1)

            # GOSUB operation
            elif quadList[index][0] == "GOSUB":
                if quadList[index][1] == "main":
                    self.have_global_definitions_been_processed = True
                    self.executionBlock.malloc(self.funDir.search('main')[3], self.funDir.search('main')[4], self.funDir.search('main')[5])
                    index = (quadList[index][3] - 1)
                else:
                    print()

            # PRINT operation
            elif quadList[index][0] == "PRINT":
                print('')

            # PARAMETER operation
            elif quadList[index][0] == "PARAMETER":
                if self.is_virtual_address_global(quadList[index][1]):
                    self.currentParameters.append(self.mainMemory.get_value(quadList[index][1]))
                else:
                    self.currentParameters.append(self.executionBlock.get_value(quadList[index][1]))

            # EXEC operation
            elif quadList[index][0] == "EXEC":
                if quadList[index][1] == "PRINT":
                    print(self.currentParameters[0])
                elif quadList[index][1] == "MOVE_UP":
                    self.pen.up()
                    self.pen.sety(self.currentParameters[0])
                    self.pen.down()
                elif quadList[index][1] == "MOVE_DOWN":
                    self.pen.up()
                    self.pen.sety(self.currentParameters[0])
                    self.pen.down()
                elif quadList[index][1] == "MOVE_RIGHT":
                    self.pen.up()
                    self.pen.setx(self.currentParameters[0])
                    self.pen.down()
                elif quadList[index][1] == "MOVE_LEFT":
                    self.pen.up()
                    self.pen.setx(self.currentParameters[0])
                    self.pen.down()
                elif quadList[index][1] == "DRAW_RECTANGLE":
                    self.pen.up()
                    self.pen.setposition(self.currentParameters[0], self.currentParameters[1])
                    self.pen.down()
                    self.pen.setx(self.currentParameters[3])
                    self.pen.sety(-self.currentParameters[2])
                    self.pen.setx(-self.currentParameters[3])
                    self.pen.sety(self.currentParameters[2])
                elif quadList[index][1] == "DRAW_LINE":
                    self.pen.up()
                    self.pen.setposition(self.currentParameters[0], self.currentParameters[1])
                    self.pen.down()
                    self.pen.setposition(self.currentParameters[2], self.currentParameters[3])
                elif quadList[index][1] == "DRAW_CIRCLE":
                    self.pen.up()
                    self.pen.setposition(self.currentParameters[0], self.currentParameters[1])
                    self.pen.down()
                    self.pen.circle(self.currentParameters[2])

                for param in self.currentParameters:
                    self.currentParameters.remove(param)

            index += 1

    # Error-handling functions for execution-time semantic analysis
    def error_division_by_zero(self):
        print('Error!')
        print('Division by 0 not possible!')
        sys.exit()