import mcp3208

CE = 0 #SPIデバイスの指定
SPEED = 1000000 #通信速度Hz（1MHzを指定．1秒間に100万bitを転送）
Vref = 3.307 #基準電圧（Raspberry Piの3.3V端子の電圧を測定し，その値を記入する）
CH = 0 #アナログ入力チャンネルの指定

mcp3208.Setup(CE, SPEED) #初期設定（1回だけ実行すればよい）

#値の取得用

def Rotation():
        data, volt = mcp3208.ReadData(CE, CH, Vref)

        if data > 4080:
            data = 4080
            
        data = int((data/4080)*100)

        return data

