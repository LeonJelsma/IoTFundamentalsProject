<h1>IoT Fundamentals final project</h1>

This repository serves as public version of our private project without sensitive information (and commit messages).
The following pieces of information have been excluded from this repository:

<ul>
  <li>Github workflows & Azure pipelines</li>
  <li>SSiDs</li>
  <li>Passwords</li>
  <li>Certificates</li>
  <li>Pretty much everything that shouldn't be in a repository in the first place</li>
</ul>

<h2>Sensor setup</h2>

<ol>
  <li>pip install esptool</li>
  <li>esptool --chip esp32 -p <b>COM PORT</b> erase_flash</li>
  <li>esptool --chip esp32 -p <b>COM PORT</b> write_flash -z 0x1000 <b>Project Dir</b>/Sensor/setup/esp32-idf3-20200902-v1.13.bin</li>
  <li>Load Sensor project using Pycharm + MicroPython plugin and flash the ESP32
</ol>

<h3> ESP32 & BM280 Wiring</h3>

![Wiring Schematic](https://github.com/LeonJelsma/IoTFundamentalsProject/blob/master/Sensor/setup/SensorSchematic.png)

![Wiring Schematic](https://github.com/LeonJelsma/IoTFundamentalsEndProject/blob/feature/sensor-setup/Sensor/setup/SensorSchematic.png)
