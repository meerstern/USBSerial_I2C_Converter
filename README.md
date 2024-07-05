# USBシリアルI2C変換基板
USB Serial I2C Converter

## 概要 
  * USBシリアルをI2Cマスタに変換する基板です
  * シリアルCOMポートを介してPCやRPI等からI2Cデバイスを制御できます  
  * I2Cデバイスの動作確認やラピッドプロトタイピングに最適です  
  * シリアルCOM変換にPL2303GL、シリアルI2C変換に[SC18IM704][1]を使用しています(V2：現行モデル)  
  * シリアルCOM変換にPL2303SA、シリアルI2C変換にSC18IM700を使用しています(V1：旧モデル)  
  * TeratermやNode-Red、Unity、Python等からシリアルCOMポートを介して容易なコマンドでI2Cデバイスを制御できます  
  * I2CはGrove互換コネクタを搭載しています  
  * Grove互換コネクタの電源、プルアップ抵抗はスイッチ切り替えで5V/3.3Vに対応しています  
    ※USB、I2Cデバイスを接続する前に基板上のシルクを確認してから5V/3.3V切替してください  
    ※3.3V専用デバイスに5Vを加えないように注意してください  


## 詳細 
 * シリアルI2C変換SC18IM700/SC18IM704のコマンドは[データシート(PDF)][8]を参照してください  
 * シリアルI2C変換[SC18IM700/SC18IM704][1]のデフォルトボーレートは9600bpsです  
 * アドレスの異なる複数のデバイスを接続する場合は[I2Cハブ][7]を使用してください
 * 基板のピンヘッダを用いることでSC18IM700/SC18IM704単体の変換基板としても使用できます  
 * USB5V電源入力側に350mA定格のリセッタブルヒューズを搭載しています  
 * 給電可能な電流は3.3Vラインで最大150mA前後、5Vラインで最大350mAです
 * コマンドの応答がない場合はピンセット等でRSTピンとGNDピンを1秒程度短絡してリセットさせてください    

## USBドライバ
 * Windows版は[こちらからダウンロード][2]して使用してください  
 ※標準ドライバではNode-Redで動作不具合があるため、最新のドライバに更新し、再起動後に使用してください
 * Mac版は標準でドライバが読み込まれますが、必要に応じて[こちらからダウンロード][3]して使用してください  
 * Linux版はKernel 2.4.31以降、標準でドライバが組み込まれています  

## Node-Redサンプルフロー
 * シリアルポートフローを使用して[Grove温湿度センサSHT31][5]から温度、湿度を読み込む[サンプル][4]  
 * 温湿度センサ　SHT31、I2C接続LCD AQM1602、マルチ環境センサBME280、CO2センサ CCS811、リアルタイムクロック DS1307、AD変換 MCP3425、粒子センサ HM3301、赤外線グリッドセンサAMG8833、I2Cデバイス検索のサンプルコードがあります  
 ※詳細はサンプルコードをご確認ください  
 ※シリアルポートフローを使用する場合はオンプレミス版Node-Redを使用する必要があります。[こちらの記事][6]を参考にしてください  
 
<img src="https://raw.githubusercontent.com/meerstern/USBSerial_I2C_Converter/master/SampleNodeRedFlow/Node-Red_SHT31.jpg" width="360">

## Teratermサンプルマクロ
 * サンプルマクロを実行する際には必ず言語設定を「English」、「Default.lng」に設定してください。正しく送受信されません。  

## WebシリアルAPIツール
 * WebシリアルAPIを使用した[ツールを公開][9]しています  
 * EdgeもしくはChromeブラウザからアクセスすると簡単にI2Cデバイスと通信できます  
 * 対応デバイスは随時追加予定です  


## 変換基板
 * USBシリアルI2C変換基板の外観  

<img src="https://raw.githubusercontent.com/meerstern/USBSerial_I2C_Converter/master/img1.jpg" width="360">
<img src="https://raw.githubusercontent.com/meerstern/USBSerial_I2C_Converter/master/img2.jpg" width="360">
 
 ※上記写真は試作基板のため、量産版と異なる場合があります  
 
 ## 販売サイト
  * [スイッチサイエンス][10]
  
 ## 告知
  * SC18IM700、PL2303SAは生産完了のため、23年7月以降はそれぞれ後継機種のSC18IM704、PL2303GLを使用したv2.x基板に変更しました
  * SC18IM700/SC18IM704の基本的なI2Cコマンド等は互換性が維持されています
  * 生産完了に伴い、v1.xモデルの製造及び販売は終了しました  


# USB Serial I2C Converter
## Overview 

  * This is a board that converts USB serial to I2C master.
  * Can control I2C devices from PC, RPI, etc. via serial COM port
  * Ideal for I2C device operation verification and rapid prototyping
  * PL2303GL is used for serial COM conversion, and [SC18IM704][1] is used for serial I2C conversion (V2: current model)
  * Control I2C devices with easy commands via serial COM port from Teraterm, Node-Red, Unity, Python, etc.
  * I2C has Grove compatible connector  
  * Grove compatible connector power supply and pull-up resistor support 5V/3.3V by switching
  * Before connecting USB or I2C devices, please check the silk on the board and then switch 5V/3.3V.
  * Please be careful not to apply 5V to 3.3V only devices.

## Details 
  * For serial I2C conversion SC18IM700/SC18IM704 commands, please refer to [Datasheet (PDF)][8]
  * The default baud rate for serial I2C conversion [SC18IM700/SC18IM704][1] is 9600bps
  * When connecting multiple devices with different addresses, please use [I2C hub][7]
  * Can also be used as a conversion board for SC18IM700/SC18IM704 by using the pin header on the board
  * Equipped with a resettable fuse rated at 350mA on the USB5V power input side
  * The maximum current that can be supplied is around 150mA for 3.3V line, and 350mA for 5V line.
  * If there is no response to the command, short the RST pin and GND pin with tweezers for about 1 second to reset.

  ## USB Driver
  * For Windows version, please [download][2] from here.
  * The standard driver has a malfunction with Node-Red, so please update to the latest driver and use it after restarting.
  * The driver is loaded by default in the Mac version, but if necessary, please [download][3].
  * The Linux version has a built-in driver as standard since Kernel 2.4.31 

 ## Node-Red Sample Flow
  * Read temperature and humidity from [Grove temperature and humidity sensor SHT31][5] using serial port flow [sample][4]
  * Temperature and humidity sensor SHT31, I2C connection LCD AQM1602, multi-environment sensor BME280, CO2 sensor CCS811, real-time clock DS1307, AD conversion MCP3425, particle sensor HM3301, infrared grid sensor AMG8833, sample code for I2C device search is available
  * Please check the sample code for details.
  * If you want to use serial port flow, you need to use the on-premises version of Node-Red. Please refer to [this article(Japanese)][6]
 
<img src="https://raw.githubusercontent.com/meerstern/USBSerial_I2C_Converter/master/SampleNodeRedFlow/Node-Red_SHT31.jpg" width="360">

## Teraterm Sample Macro
 * When running the sample macro, be sure to set the language settings to "English" and "Default.lng". It will not be sent or received correctly.

 
## Web Serial API Tools
 * [Publishing tools][11] using Web Serial API
 * Easily communicate with I2C devices when accessed from Edge or Chrome browsers
 * Compatible devices will be added

 ## Announcement
  * Production of SC18IM700 and PL2303SA has been discontinued, so from July 2023 onwards, we have changed to v2.x boards using the successor models SC18IM704 and PL2303GL, respectively.
  * Compatibility of basic I2C commands etc. of SC18IM700/SC18IM704 is maintained.
  * Due to the completion of production, the manufacture and sale of v1.x model has ended.
  
 
[1]: https://www.nxp.jp/part/SC18IM704PW#/
[2]: https://www.prolific.com.tw/UserFiles/files/PL23XX_Prolific_DriverInstaller_v408.zip
[3]: https://www.prolific.com.tw/UserFiles/files/PL2303HXD_G_Mac%20Driver_v2_1_0_20210311.zip
[4]: https://github.com/meerstern/USBSerial_I2C_Converter/tree/master/SampleNodeRedFlow
[5]: https://www.switch-science.com/catalog/2853/
[6]: http://meerstern.seesaa.net/article/465007276.html
[7]: https://www.switch-science.com/catalog/796/
[8]: https://www.nxp.jp/docs/en/data-sheet/SC18IM704.pdf
[9]: https://meerstern.github.io/
[10]: https://www.switch-science.com/products/6214
[11]: https://meerstern.github.io/Web%20API%20Tools_En.html

MIT Lisense
