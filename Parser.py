from Node import Node


class Parser:

    def __init__(self, tokens, text):
        self.tokens = tokens
        self.text = text

    def nextToken(self):
        if len(self.tokens) == 0:
            return ['', '', 0, 0]
        else:
            aux = self.tokens[0]
            self.tokens = self.tokens[1:]
            return aux

    def nextTempToken(self):
        if len(self.tokens) == 0:
            return ['', '', 0, 0]
        else:
            aux = self.tokens[0]
            return aux

    def parse(self):
        docu = Node('document')
        docu.addChild(self.modelInfo())
        docu.addChild(self.modelInputs())
        docu.addChild(self.modelOutputs())
        docu.addChild(self.model())
        return [docu, len(self.tokens)]

    def modelInfo(self):
        node = Node('ModelInfo')
        node.addChild(self.modelName())
        node.addChild(self.modelType())
        return node

    def modelName(self):
        node = Node('ModelName')
        fine = False
        mod_name = self.nextToken()
        colon_sym = self.nextToken()
        free_text = self.nextToken()
        node.addChild(Node(mod_name[0]))
        node.addChild(Node(colon_sym[0]))
        node.addChild(Node(free_text[0]))
        if mod_name[1] == 'Model_Name_Token' and colon_sym[1] == 'Colon_Token' and free_text[1] == 'FreeText_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Module_Name attribute")
        return node

    def modelType(self):
        node = Node('ModelType')
        fine = False
        mod_type = self.nextToken()
        colon_sym = self.nextToken()
        type_option = self.nextToken()
        node.addChild(Node(mod_type[0]))
        node.addChild(Node(colon_sym[0]))
        node.addChild(Node(type_option[0]))
        if mod_type[1] == 'Model_Type_Token' and colon_sym[1] == 'Colon_Token' and type_option[1] == 'Model_Type_Options_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Module_Type attribute")
        return node

    def modelInputs(self):
        node = Node('ModelInputs')
        fine = False
        inputs = self.nextToken()
        node.addChild(Node(inputs[0]))
        l_brack = self.nextToken()
        node.addChild(Node(l_brack[0]))
        node.addChild(self.inputs())
        r_brack = self.nextToken()
        node.addChild(Node(r_brack[0]))
        if inputs[1] == 'Inputs_Token' and l_brack[1] == 'LeftBracket_Token' and r_brack[1] == 'RightBracket_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Inputs section")
        return node

    def inputs(self):
        node = Node('Inputs')
        node.addChild(self.input())
        inp_tok = self.nextTempToken()
        if inp_tok[1] == 'Input_Token':
            node.addChild(self.inputs())
        return node

    def input(self):
        node = Node('Input')
        fine = False
        inp_tok = self.nextToken()
        node.addChild(Node(inp_tok[0]))
        l_brack = self.nextToken()
        node.addChild(Node(l_brack[0]))
        node.addChild(self.inputName())
        node.addChild(self.inputType())
        r_brack = self.nextToken()
        node.addChild(Node(r_brack[0]))
        if inp_tok[1] == 'Input_Token' and l_brack[1] == 'LeftBracket_Token' and r_brack[1] == 'RightBracket_Token':
            fine = True
        if not fine:
            raise Exception("Error in an Input section")
        return node

    def inputName(self):
        node = Node('InputName')
        fine = False
        inp_name = self.nextToken()
        colon_sym = self.nextToken()
        free_text = self.nextToken()
        node.addChild(Node(inp_name[0]))
        node.addChild(Node(colon_sym[0]))
        node.addChild(Node(free_text[0]))
        if inp_name[1] == 'Input_Name_Token' and colon_sym[1] == 'Colon_Token' and free_text[1] == 'FreeText_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Input_Name attribute")
        return node

    def inputType(self):
        node = Node('InputType')
        fine = False
        inp_type = self.nextToken()
        colon_sym = self.nextToken()
        type_options = self.nextToken()
        node.addChild(Node(inp_type[0]))
        node.addChild(Node(colon_sym[0]))
        node.addChild(Node(type_options[0]))
        if inp_type[1] == 'Input_Type_Token' and colon_sym[1] == 'Colon_Token' and type_options[1] == 'Type_Options_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Input_Type attribute")
        return node

    def modelOutputs(self):
        node = Node('ModelOutputs')
        fine = False
        outputs = self.nextToken()
        node.addChild(Node(outputs[0]))
        l_brack = self.nextToken()
        node.addChild(Node(l_brack[0]))
        node.addChild(self.outputs())
        r_brack = self.nextToken()
        node.addChild(Node(r_brack[0]))
        if outputs[1] == 'Outputs_Token' and l_brack[1] == 'LeftBracket_Token' and r_brack[1] == 'RightBracket_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Outputs section")
        return node

    def outputs(self):
        node = Node('Outputs')
        node.addChild(self.output())
        out_tok = self.nextTempToken()
        if out_tok[1] == 'Output_Token':
            node.addChild(self.outputs())
        return node

    def output(self):
        node = Node('Output')
        fine = False
        out_tok = self.nextToken()
        node.addChild(Node(out_tok[0]))
        l_brack = self.nextToken()
        node.addChild(Node(l_brack[0]))
        node.addChild(self.outputName())
        node.addChild(self.outputType())
        r_brack = self.nextToken()
        node.addChild(Node(r_brack[0]))
        if out_tok[1] == 'Output_Token' and l_brack[1] == 'LeftBracket_Token' and r_brack[1] == 'RightBracket_Token':
            fine = True
        if not fine:
            raise Exception("Error in an Output section")
        return node

    def outputName(self):
        node = Node('OutputName')
        fine = False
        out_name = self.nextToken()
        colon_sym = self.nextToken()
        free_text = self.nextToken()
        node.addChild(Node(out_name[0]))
        node.addChild(Node(colon_sym[0]))
        node.addChild(Node(free_text[0]))
        if out_name[1] == 'Output_Name_Token' and colon_sym[1] == 'Colon_Token' and free_text[1] == 'FreeText_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Output_Name attribute")
        return node

    def outputType(self):
        node = Node('OutputType')
        fine = False
        out_type = self.nextToken()
        colon_sym = self.nextToken()
        type_options = self.nextToken()
        node.addChild(Node(out_type[0]))
        node.addChild(Node(colon_sym[0]))
        node.addChild(Node(type_options[0]))
        if out_type[1] == 'Output_Type_Token' and colon_sym[1] == 'Colon_Token' and type_options[1] == 'Type_Options_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Output_Type attribute")
        return node

    def model(self):
        node = Node('Model')
        fine = False
        mod = self.nextToken()
        node.addChild(Node(mod[0]))
        l_brack = self.nextToken()
        node.addChild(Node(l_brack[0]))
        node.addChild(self.modelLayers())
        r_brack = self.nextToken()
        node.addChild(Node(r_brack[0]))
        if mod[1] == 'Model_Token' and l_brack[1] == 'LeftBracket_Token' and r_brack[1] == 'RightBracket_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Model section")
        return node

    def modelLayers(self):
        node = Node('ModelLayers')
        fine = False
        layers = self.nextToken()
        node.addChild(Node(layers[0]))
        l_brack = self.nextToken()
        node.addChild(Node(l_brack[0]))
        node.addChild(self.layers())
        r_brack = self.nextToken()
        node.addChild(Node(r_brack[0]))
        if layers[1] == 'Layers_Token' and l_brack[1] == 'LeftBracket_Token' and r_brack[1] == 'RightBracket_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Layers section")
        return node

    def layers(self):
        node = Node('Layers')
        node.addChild(self.layer())
        layer_tok = self.nextTempToken()
        if layer_tok[1] == 'Layer_Token':
            node.addChild(self.layers())
        return node

    def layer(self):
        node = Node('Layer')
        fine = False
        layer_tok = self.nextToken()
        node.addChild(Node(layer_tok[0]))
        l_brack = self.nextToken()
        node.addChild(Node(l_brack[0]))
        node.addChild(self.layerName())
        node.addChild(self.layerParams())
        r_brack = self.nextToken()
        node.addChild(Node(r_brack[0]))
        if layer_tok[1] == 'Layer_Token' and l_brack[1] == 'LeftBracket_Token' and r_brack[1] == 'RightBracket_Token':
            fine = True
        if not fine:
            raise Exception("Error in a Layer section")
        return node

    def layerName(self):
        node = Node('LayerName')
        fine = False
        layer_name = self.nextToken()
        colon_sym = self.nextToken()
        free_text = self.nextToken()
        node.addChild(Node(layer_name[0]))
        node.addChild(Node(colon_sym[0]))
        node.addChild(Node(free_text[0]))
        if layer_name[1] == 'Layer_Name_Token' and colon_sym[1] == 'Colon_Token' and free_text[1] == 'FreeText_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Layer_Name attribute")
        return node

    def layerParams(self):
        node = Node('LayerParams')
        fine = False
        layer_par = self.nextToken()
        node.addChild(Node(layer_par[0]))
        colon_sym = self.nextToken()
        node.addChild(Node(colon_sym[0]))
        l_square = self.nextToken()
        node.addChild(Node(l_square[0]))
        node.addChild(self.numArray())
        r_square = self.nextToken()
        node.addChild(Node(r_square[0]))
        if layer_par[1] == 'Layer_Params_Token' and colon_sym[1] == 'Colon_Token' and l_square[1] == 'LeftSquare_Token' and r_square[1] == 'RightSquare_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Layer_Params attribute")
        return node

    def numArray(self):
        node = Node('NumericArray')
        node.addChild(self.num())
        nums_tok = self.nextTempToken()
        if nums_tok[1] == 'Comma_Token':
            comma_sym = self.nextToken()
            node.addChild(Node(comma_sym[0]))
            node.addChild(self.numArray())
        return node

    def num(self):
        node = Node('Number')
        fine = False
        number = self.nextToken()
        node.addChild(Node(str(number[0])))
        if number[1] == 'Int_Token' or number[1] == 'Float_Token':
            fine = True
        if not fine:
            raise Exception("Error in the Layer_Params2 attribute")
        return node
