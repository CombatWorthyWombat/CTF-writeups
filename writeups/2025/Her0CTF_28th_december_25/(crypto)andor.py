a_outputs = [0x4064004f230800551e0068201e24401023305130425f0020345514684412, 
    0x00014046214020451a3060200a152020026045202207591004033446604f, 
    0x404562226a083071132440640301481002605a1070133110010a100e000b,
    0x00014046214020451a3060200a152020026045202207591004033446604f,
    0x404562226a083071132440640301481002605a1070133110010a100e000b,
    0x4845702b28590051571046405534203111600b2030444010400c00684441,
    0x0000404d616930101b104c404f356c0000005600201a3810011c30084400,
    0x0004324d1a011031063444440e354c222140472002097120041600400459,
    0x406012621a3820044504224059040813235014300251001015543002205e,
    0x0820324941383024431000004a3528222140542010415930701f004c4447,
    0x4004306f0270005047346a401904400110204e1050022830155a20440055,
    0x480140222909205059006444190524001110132052131930711f040e2040]
    
o_outputs = [0x63ff7767b3b7df73fb7d7c6dfddf76fdbe7f7fb66e64ff7230b16ff73fff,
    0x6fb06e7677fbdfb3f97575fc3d7f7ffe7577dfbfefe47ffb36797e7ffd7f,
    0xfff97676f373fffff5f7fe6cb55f676d3c7fdffe7e74dff6fef7ff37fffd,
    0xebb1fee673375ff773f5b4fe7ddf7eeebdefff767e77df76feb57f37bf7f,
    0x6b72fe6ffbffdffbfd75b6fc77df676f7ef75f7e6f6dfff9f5737e3fffff,
    0x73fafe773b3f5f777df57c7fb75f66ecf4675f7f6ffefff1f0797efffd7d,
    0x7f327ffe77fb7ffbfbff37fe357f76ed746f7fbd6efdff7132f9fe77b5ff,
    0x67b86e7f737f5fff797d76fd3dfffeedffe77ff66ee77ffafe79efff37fd,
    0xe3fae7eefbb3fffb7b757f7e3dff6f7dbfe7dff56ee5dff6b739eefffdff,
    0x6b7166763f7bff3bfd777d6fb57f7e6cfcef5f74fe745f7db0b37f7777ff]

#===========================================================================# AND handling
def OR_chain(outputs):
    result = 0
    for value in outputs:
        result = result | value
    return hex(result)
#===========================================================================# OR handling
def AND_chain(outputs):
    byte_count = (o_outputs[0].bit_length() + 7) // 8
    result = int.from_bytes(b'\xff' * byte_count, 'big')
    for value in outputs:
        result = result & value
    return hex(result)
#===========================================================================# parsing
def readable(num):
    hex_str = num[2:]
    if len(hex_str) % 2 == 1:
        hex_str = "0" + hex_str
        
    return bytes.fromhex(hex_str)
    
if __name__ == "__main__":

    x1 = OR_chain(a_outputs)
    y1 = readable(x1)
    print(y1)
    
    x2 = AND_chain(o_outputs)
    y2 = readable(x2)
    print(y2)
