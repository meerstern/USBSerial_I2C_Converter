# USBSerial_I2C_Converter
USB Serial I2C Converter

## 概要 
  * USBシリアルをI2Cマスタに変換する基板です
  * シリアルCOMポートを介してI2Cデバイスを制御できます  
  * シリアルCOM変換にPL2303SA、シリアルI2C変換に[SC18IM700][1]を使用しています  
  * シリアルI2C変換[SC18IM700][1]のデフォルトボーレートは9600bpsです  
  * TeratermやNode-Red、Unity等からシリアルCOMポートを介して容易なコマンドでI2Cデバイスを制御できます  
  * シリアルI2C変換SC18IM700のコマンドは[データシート(PDF)][8]を参照してください  
  * I2CはGrove互換コネクタを搭載しています  
  * Grove互換コネクタの電源、プルアップ抵抗はスイッチ切り替えで5V/3.3Vに対応しています  
  * 基板のピンヘッダを用いることでSC18IM700単体の変換基板としても使用できます  
  * アドレスの異なる複数のデバイスを接続する場合は[I2Cハブ][7]を使用してください
  
  
## USBドライバ
 * Windows版は[こちらからダウンロード][2]して使用してください  
 ※標準ドライバではNode-Redで動作不具合があるため、最新のドライバに更新し、再起動後に使用してください
 * Mac版は[こちらからダウンロード][3]して使用してください  

## Node-Redサンプルフロー
 * シリアルポートフローを使用して[Grove温湿度センサSHT31][5]から温度、湿度を読み込む[サンプル][4]  
 * 温湿度センサ　SHT31、I2C接続LCD AQM1602、マルチ環境センサBME280、CO2センサ CCS811、リアルタイムクロック DS1307、AD変換 MCP3425、粒子センサ HM3301、I2Cデバイス検索のサンプルコードがあります  
 ※詳細はサンプルコードをご確認ください  
 ※シリアルポートフローを使用する場合はオンプレミス版Node-Redを使用する必要があります。[こちらの記事][6]を参考にしてください  
 
<img src="https://raw.githubusercontent.com/meerstern/USBSerial_I2C_Converter/master/SampleNodeRedFlow/Node-Red_SHT31.jpg" width="360">

## Teratermサンプルマクロ
 * サンプルマクロを実行する際には必ず言語設定を「English」、「Default.lng」に設定してください。正しく送受信されません。  


## 変換基板
 * USBシリアルI2C変換基板の外観  

<img src="https://raw.githubusercontent.com/meerstern/USBSerial_I2C_Converter/master/img1.jpg" width="360">
<img src="https://raw.githubusercontent.com/meerstern/USBSerial_I2C_Converter/master/img2.jpg" width="360">

   
[1]: https://www.nxp.com/products/peripherals-and-logic/signal-chain/bridges/master-ic-bus-controller-with-uart-interface:SC18IM700IPW
[2]: http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=225&pcid=41
[3]: http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=229&pcid=41
[4]: https://github.com/meerstern/USBSerial_I2C_Converter/tree/master/SampleNodeRedFlow
[5]: https://www.switch-science.com/catalog/2853/
[6]: http://meerstern.seesaa.net/article/465007276.html
[7]: https://www.switch-science.com/catalog/796/
[8]: https://www.nxp.com/docs/en/data-sheet/SC18IM700.pdf

MIT Lisense
