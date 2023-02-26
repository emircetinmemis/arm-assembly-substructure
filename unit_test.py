import colorama

class Led() :

    def __init__(self, led_id:int, content:str=None, mapping:str=None) -> None:
        
        self.led_id = led_id
        self.content = content
        self.mapping = mapping

        if not self.content and not self.mapping :
            self._map_default_attributes()
        elif self.content :
            self._map_via_content()
        elif self.mapping :
            self._map_via_mapping()

    def __str__(self) -> str:
        
        template = "\n".join(self.layerize_led())    
    
        return template
    
    def layerize_led(self) :

        bg_color = colorama.Fore.BLACK
        on_color = colorama.Fore.GREEN
        off_color = colorama.Fore.RED
        term_color = ""

        char = "|"
        layer1 = term_color+bg_color+"   "+(on_color if self.mapping["A"] else off_color)+(char*5)+bg_color+"   "
        layer2 = bg_color+" "+(on_color if self.mapping["F"] else off_color)+(char*2)+bg_color+(" "*5)+(on_color if self.mapping["B"] else off_color)+(char*2)+bg_color+" "
        layer3 = bg_color+" "+(on_color if self.mapping["F"] else off_color)+(char*2)+bg_color+(" "*5)+(on_color if self.mapping["B"] else off_color)+(char*2)+bg_color+" "
        layer4 = term_color+bg_color+"   "+(on_color if self.mapping["G"] else off_color)+(char*5)+bg_color+"   "
        layer5 = bg_color+" "+(on_color if self.mapping["E"] else off_color)+(char*2)+bg_color+(" "*5)+(on_color if self.mapping["C"] else off_color)+(char*2)+bg_color+" "
        layer6 = bg_color+" "+(on_color if self.mapping["E"] else off_color)+(char*2)+bg_color+(" "*5)+(on_color if self.mapping["C"] else off_color)+(char*2)+bg_color+" "
        layer7 = term_color+bg_color+"   "+(on_color if self.mapping["D"] else off_color)+(char*5)+bg_color+"   "

        return [layer1,layer2,layer3,layer4,layer5,layer6,layer7]

    def _map_default_attributes(self) -> None:
        self.mapping = {"A":False, "B":False, "C":False, "D":False, "E":False, "F":False, "G":False}

    def _map_via_content(self) -> None:
        segment_map = {
            "0": {"A":True, "B":True, "C":True, "D":True, "E":True, "F":True, "G":False},
            "1": {"A":False, "B":True, "C":True, "D":False, "E":False, "F":False, "G":False},
            "2": {"A":True, "B":True, "C":False, "D":True, "E":True, "F":False, "G":True},
            "3": {"A":True, "B":True, "C":True, "D":True, "E":False, "F":False, "G":True},
            "4": {"A":False, "B":True, "C":True, "D":False, "E":False, "F":True, "G":True},
            "5": {"A":True, "B":False, "C":True, "D":True, "E":False, "F":True, "G":True},
            "6": {"A":True, "B":False, "C":True, "D":True, "E":True, "F":True, "G":True},
            "7": {"A":True, "B":True, "C":True, "D":False, "E":False, "F":False, "G":False},
            "8": {"A":True, "B":True, "C":True, "D":True, "E":True, "F":True, "G":True},
            "9": {"A":True, "B":True, "C":True, "D":True, "E":False, "F":True, "G":True},
            "A": {"A":True, "B":True, "C":True, "D":False, "E":True, "F":True, "G":True},
            "B": {"A":False, "B":False, "C":True, "D":True, "E":True, "F":True, "G":True},
            "C": {"A":True, "B":False, "C":False, "D":True, "E":True, "F":True, "G":False},
            "D": {"A":False, "B":True, "C":True, "D":True, "E":True, "F":False, "G":True},
            "E": {"A":True, "B":False, "C":False, "D":True, "E":True, "F":True, "G":True},
            "F": {"A":True, "B":False, "C":False, "D":False, "E":True, "F":True, "G":True},
            "G": {"A":True, "B":True, "C":True, "D":True, "E":True, "F":False, "G":True},
            "H": {"A":False, "B":True, "C":True, "D":False, "E":True, "F":True, "G":True},
            "I": {"A":False, "B":True, "C":True, "D":False, "E":False, "F":False, "G":False},
            "J": {"A":False, "B":True, "C":True, "D":True, "E":True, "F":False, "G":False},
            "K": {"A":False, "B":True, "C":True, "D":False, "E":True, "F":True, "G":True},
            "L": {"A":False, "B":False, "C":False, "D":True, "E":True, "F":True, "G":False},
            "M": {"A":False, "B":True, "C":True, "D":False, "E":True, "F":True, "G":True},
            "N": {"A":False, "B":True, "C":True, "D":False, "E":True, "F":True, "G":True},
            "O": {"A":True, "B":True, "C":True, "D":True, "E":True, "F":True, "G":False},
            "P": {"A":True, "B":True, "C":False, "D":False, "E":True, "F":True, "G":True},
            "Q": {"A":True, "B":True, "C":True, "D":False, "E":False, "F":True, "G":True},
            "R": {"A":False, "B":True, "C":False, "D":False, "E":True, "F":True, "G":True},
            "S": {"A":True, "B":False, "C":True, "D":True, "E":False, "F":True, "G":True},
            "T": {"A":False, "B":False, "C":False, "D":True, "E":True, "F":True, "G":True},
            "U": {"A":False, "B":True, "C":True, "D":True, "E":True, "F":True, "G":False},
            "V": {"A":False, "B":True, "C":True, "D":True, "E":True, "F":True, "G":False},
            "W": {"A":False, "B":True, "C":True, "D":True, "E":True, "F":True, "G":False},
            "X": {"A":False, "B":True, "C":True, "D":False, "E":True, "F":True, "G":True},
            "Y": {"A":False, "B":True, "C":True, "D":True, "E":False, "F":True, "G":True},
            "Z": {"A":True, "B":True, "C":False, "D":True, "E":True, "F":False, "G":True},
            "_": {"A":False, "B":False, "C":False, "D":False, "E":False, "F":False, "G":True},
            "-": {"A":False, "B":False, "C":False, "D":False, "E":False, "F":False, "G":True},
            "|": {"A":False, "B":False, "C":False, "D":False, "E":False, "F":False, "G":False},
            " ": {"A":False, "B":False, "C":False, "D":False, "E":False, "F":False, "G":False},
        }
        self.mapping = segment_map[self.content]

    def _map_via_mapping(self) -> None:

        temporary_mapping = {"A":False, "B":False, "C":False, "D":False, "E":False, "F":False, "G":False}
        for segment in self.mapping :
            temporary_mapping[segment] = True
        self.mapping = temporary_mapping

if __name__ == "__main__":
    led_count = 9

    rows = 7
    columns = led_count+1
    layer_matrix = [["" for x in range(columns)] for y in range(rows)]

    for current_led_id in range(led_count+1):
        
        led = Led(led_id=current_led_id, content=str(current_led_id))

        current_led_layers = led.layerize_led()

        for current_layer in range(len(current_led_layers)):
            layer_matrix[current_layer][current_led_id] = current_led_layers[current_layer]
        
    display = "\n".join(["".join(row) for row in layer_matrix])

    print(display)