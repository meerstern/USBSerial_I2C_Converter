# USBSerial_I2C_Converter
USB Serial I2C Converter

## 概要 
  * USBシリアルをI2Cマスタに変換する基板です
  * シリアルCOMポートを介してI2Cデバイスを制御できます  
  * シリアルCOM変換にPL2303SA、シリアルI2C変換に[SC18IM700][1]を使用しています  
  * TeratermやNode-Red等から簡単なコマンドを使用してI2Cデバイスを制御できます  
  * I2CはGrove互換コネクタを搭載しており、5V/3.3Vの両電源の切り替えに対応しています  
  
## USBドライバ
 * Windows版は[こちらからダウンロード][2]して使用してください  
 ※標準ドライバではNode-Redで動作不具合があるため、最新のドライバに更新し、再起動後に使用してください
 * Mac版は[こちらからダウンロード][3]して使用してください  

## Node-Redサンプルフロー
 * [Grove温湿度センサSHT31][5]を接続して温度、湿度を読み込んだ[サンプル][4]  
 ※詳細はサンプルコードをご確認ください  
 
<img src="https://raw.githubusercontent.com/meerstern/USBSerial_I2C_Converter/master/SampleNodeRedFlow/SHT31_Node-Red.jpg" width="360">
 
   
 
<img src="https://raw.githubusercontent.com/meerstern/USBSerial_I2C_Converter/master/PCB/img1.jpg" width="360">
<img src="https://raw.githubusercontent.com/meerstern/USBSerial_I2C_Converter/master/PCB/img2.jpg" width="360">
  
    
[1]: https://www.nxp.com/products/peripherals-and-logic/signal-chain/bridges/master-ic-bus-controller-with-uart-interface:SC18IM700IPW
[2]: http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=225&pcid=41
[3]: http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=229&pcid=41
[4]: https://github.com/meerstern/USBSerial_I2C_Converter/tree/master/SampleNodeRedFlow
[5]: https://www.switch-science.com/catalog/2853/
MIT Lisense
