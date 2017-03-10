/*
  AUTHOR: Fernando Gonzalez
  DESCRIPTION:
    Programa de lectura sensor dht22 sobre node MCU
  DEPENDECIES:
    DHT.h
    NodeMCU ESP8266  
*/
//LIBRERIAS
//#################################################################################
//LIBRERIA PARA DHT22
#include "DHT.h"
//#################################################################################
//CONSTANTES y Vars GLOBALES

#define DHTPIN 2      //GPIO 2 NodeMCU (~D4)
#define DHTTYPE DHT22 //Seleccion de sensor DHT22 (tambien esta el DHT11)
DHT dht(DHTPIN, DHTTYPE); //Declaracion para leer el sensor

//ACTIVA EL MODO DEPURACION
//Con esta variable habilitamos la depuracion con mensajes por puerto serial
#define DEBUG

//################################################################################


void readTempHum(){
  
  float temp = dht.readTemperature(); 
  float hum = dht.readHumidity(); 

  #ifdef DEBUG
    Serial.print("Temperatura: ");
    Serial.print(temp);
    Serial.print("\t\t");
    Serial.print("Humedad: "); 
    Serial.print(hum);
  #endif
}

void setup() {
  #ifdef DEBUG
    Serial.begin(9600); //Comunicacion serial para depurar
  #endif
  dht.begin(); //Comunicacion con el sensor
}

void loop() {
  
  readTempHum();

  #ifdef DEBUG
    Serial.println(""); //Salto de linea
    delay(2000); //Se espera 2 segundos para seguir leyendo
  #endif
}
