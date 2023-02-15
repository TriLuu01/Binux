from array import*
import os.path
class Translator:
    two_Bits = ["00", "01", "10", "11"]
    address = ["00:", "10:", "20:", "30:", "40:", "50:", "60:", "70:", "80:", "90:", "a0:", "b0:", "c0:", "d0:", "e0:", "f0:"]
    hexAddress = Matrix = [[0 for x in range(16)] for y in range(16)] 
    instructions =  []
    
    def initalize(self) :
        i = 0
        while (i < len(self.hexAddress)) :
            j = 0
            while (j < len(self.hexAddress[i])) :
                self.hexAddress[i][j] = "00"
                j += 1
            i += 1
    
    def  ImmediateToBinary(self,num) :
        num = int(num)
        if (num == -2) :
            return self.two_Bits[2]
        elif(num == -1) :
            return self.two_Bits[3]
        elif(num == 0) :
            return self.two_Bits[0]
        else :
            return self.two_Bits[1]
    
    def  AluOpToBinary(self,aluOp_Translate) :
        if (aluOp_Translate.lower() == ("ldr").lower()) :
            return self.two_Bits[3]
        elif(aluOp_Translate.lower() == ("add").lower()) :
            return self.two_Bits[1]
        elif(aluOp_Translate.lower() == ("and").lower()) :
            return self.two_Bits[2]
        elif(aluOp_Translate.lower() == ("nop").lower()) :
            return self.two_Bits[0]
        else :
            return self.two_Bits[0]
    
    def  RegisterToBinary(self,reg_Translate) :
        #convert num from register to binary
        crop = "" + str(reg_Translate[1])
       
        num = int(crop)
        return self.two_Bits[num]
    
    def BinaryToHex(self) :
        #Convert binary to hex
        index_counter = -1
        output = ""
        for it in self.instructions :
            each = it.replace("\\s","")
            split_Each = each.split(",",4)
            output += self.AluOpToBinary(split_Each[0])
            if (output==self.two_Bits[3]) :
                output += self.ImmediateToBinary(split_Each[0])
                output += self.RegisterToBinary(split_Each[1])
                output += self.RegisterToBinary(split_Each[2])
            else :
                output += self.RegisterToBinary(split_Each[0])
                output += self.RegisterToBinary(split_Each[1])
                output += self.RegisterToBinary(split_Each[2])
            
            i = 0
            for i in range(0,len(self.hexAddress)):
                j = 0
                for j in range (0,len(self.hexAddress[i])) :
                    if (self.hexAddress[i][j]=="00" and ((i * 16) + j) > index_counter) :
                        self.hexAddress[i][j] = self.helper_BinaryToHex(output)
                        flag = True 
                        break
                if (flag == True) :
                    break    
            index_counter += 1
            output = ""
    def  helper_BinaryToHex(self,binary) :
        num = (int)(binary,2)
        hexConvert = str(hex(num))
        if (len(hexConvert) == 1) :
            append_zero_beginning = binary[0:4]
            append_zero_ending = binary[4:len(binary)]
            if (append_zero_beginning=="0000") :
                hexConvert = "0" + hexConvert
            elif(append_zero_ending=="0000") :
                hexConvert += "0"
        return hexConvert
    def Writeback(self,path) :
        file = None
        mycontent = ""
        file = open(path, "w")
        file.write("v3.0 hex words addressed\r\n")
        i = 0
        while (i < len(self.hexAddress)) :
            mycontent += self.address[i] + " "
            j = 0
            while (j < len(self.hexAddress[i])) :
                if (j == 15) :
                    mycontent += self.hexAddress[i][j] + "\r\n"
                else :
                    mycontent += self.hexAddress[i][j] + " "
                j += 1
            file.write(mycontent)
            mycontent = ""
            i += 1
    
        file.close()

    def main(self) :
        path = "toTranslate.txt"
        # sets up matrix
        self.initalize()
        self.Writeback(path)
        file_read = open(path, 'r')
        lines = file_read.readlines()
        for i in lines:
            self.instructions.append(i.strip())
        self.BinaryToHex()
        self.Writeback(path)
        print("Image created for instruction memory")
newClass = Translator
newClass.main("toTranslate.txt")
