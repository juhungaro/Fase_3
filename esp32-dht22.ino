#include "DHTesp.h"

const int PIN_DO_SENSOR_UMIDADE = 15;
const int PIN_DO_RELE = 22;
const int pinoBotaoPotassio = 23;
const int pinoBotaoFosforo = 18;
//const int pinoBomba = 21;
const int pinoLed = 21; 

DHTesp sensorUmidade;

// Gera um número aleatório dentro de um intervalo
int gerarNumeroAleatorio(int min, int max) {
  randomSeed(analogRead(0));
  return random(min, max + 1);
}

void setup() {
  Serial.begin(115200);
  sensorUmidade.setup(PIN_DO_SENSOR_UMIDADE, DHTesp::DHT22);
  pinMode(PIN_DO_RELE, OUTPUT);
  pinMode(pinoBotaoPotassio, OUTPUT);
  pinMode(pinoBotaoFosforo, OUTPUT);
  pinMode(pinoLed, OUTPUT); 
}

void loop() {
  // Lê a temperatura e umidade do sensor
  TempAndHumidity dados = sensorUmidade.getTempAndHumidity();
  int valorFosforo = gerarNumeroAleatorio(1, 50);
  int valorPotassio = gerarNumeroAleatorio(1, 50);

  Serial.println("Temperatura: " + String(dados.temperature, 2) + "°C");
  Serial.println("Umidade: " + String(dados.humidity, 1) + "%");
  Serial.println("Fósforo: " + String(valorFosforo));  
  Serial.println("Potássio: " + String(valorPotassio));


  // Verifica as condições e aciona os dispositivos
  // Bomba: Acionada apenas se a umidade estiver abaixo de 20%
  if (dados.humidity < 20) {
    digitalWrite(PIN_DO_RELE, HIGH); // Liga a bomba
    digitalWrite(pinoLed, HIGH);   // Liga o LED
    Serial.println("Bomba ativada: Umidade baixa detectada");
  } else {
    digitalWrite(PIN_DO_RELE, LOW);  // Desliga a bomba
    digitalWrite(pinoLed, LOW);    // Desliga o LED
    Serial.println("Bomba desligada: Umidade suficiente");
  }

  //Potassio: Média da cultura da soja é de 38 kg de K₂O para cada tonelada de grãos.
  // e o teor de fósforo é 15,5 mg/dm3
  // Botões: Acionados de acordo com os níveis de fósforo e potássio  

  if (valorPotassio < 38) {
    digitalWrite(pinoBotaoPotassio, HIGH); // Liga o botão de potássio
    Serial.println("Ativação de potássio");
  } else {
    digitalWrite(pinoBotaoPotassio, LOW); // Desliga o botão de potássio
    Serial.println("Nível de potássio suficiente");
  }

  if (valorFosforo < 15) {
    digitalWrite(pinoBotaoFosforo, HIGH); // Liga o botão de fósforo
     Serial.println("Ativação de fósforo");
  } else {
    digitalWrite(pinoBotaoFosforo, LOW); // Desliga o botão de fósforo
    Serial.println("Nível de fósforo suficiente");
  }

  delay(5000);
}