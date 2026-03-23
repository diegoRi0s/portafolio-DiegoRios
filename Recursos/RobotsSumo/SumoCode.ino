#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

// Pines de los motores
int motor1A = 12; 
int motor1B = 13;
int motor2A = 14;
int motor2B = 27;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("Sumo_ESP32_Robot"); // Nombre que veras en tu celular
  
  pinMode(motor1A, OUTPUT);
  pinMode(motor1B, OUTPUT);
  pinMode(motor2A, OUTPUT);
  pinMode(motor2B, OUTPUT);
}

void loop() {
  if (SerialBT.available()) {
    char command = SerialBT.read();
    Serial.println(command); // Para debug en el monitor serie

    switch (command) {
      case 'F': moverAdelante();  break;
      case 'B': moverAtras();     break;
      case 'L': girarIzquierda(); break;
      case 'R': girarDerecha();   break;
      case 'S': detener();        break; 
    }
  }
}

// Ejemplo de una de las funciones
void moverAdelante() {
  digitalWrite(motor1A, HIGH);
  digitalWrite(motor1B, LOW);
  digitalWrite(motor2A, HIGH);
  digitalWrite(motor2B, LOW);
}

void moverAtras() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, HIGH);
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, HIGH);
}

void girarIzquierda() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, HIGH);
  digitalWrite(motor2A, HIGH);
  digitalWrite(motor2B, LOW);
}

void girarDerecha() {
  digitalWrite(motor1A, HIGH);
  digitalWrite(motor1B, LOW);
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, HIGH);
}

void detener() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, LOW);
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, LOW);
}

