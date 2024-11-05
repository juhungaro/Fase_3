#include "DHTesp.h"

const int pinSensorUmidade = 15;
const int pinRele = 22;
const int pinBotaoPotassio = 23;
const int pinBotaoFosforo = 18;
const int pinLed = 21; 

// Constantes para o cálculo do pH
const int resistencia_ph4 = 0;  // Adicione o valor correto da resistência para pH 4
const int resistencia_ph7 = 1023;  // Adicione o valor correto da resistência para pH 7
const int pin_ph = 34;  // Pino para leitura do pH

DHTesp sensorUmidade;

// Gera um número aleatório dentro de um intervalo
int gerarNumeroAleatorio(int min, int max) {
  return random(min, max + 1);
}

void setup() {
  Serial.begin(115200);
  
  // Inicializa a semente do gerador de números aleatórios uma única vez
  randomSeed(analogRead(0));
  
  sensorUmidade.setup(pinSensorUmidade, DHTesp::DHT22);
  pinMode(pinRele, OUTPUT);
  pinMode(pinBotaoPotassio, INPUT);  // Corrigido para INPUT se for botão
  pinMode(pinBotaoFosforo, INPUT);   // Corrigido para INPUT se for botão
  pinMode(pinLed, OUTPUT); 
}

void loop() {
  // Lê a temperatura e umidade do sensor
  TempAndHumidity dados = sensorUmidade.getTempAndHumidity();
  
  // Verifica se a leitura foi bem-sucedida
  if (isnan(dados.temperature) || isnan(dados.humidity)) {
    Serial.println("Falha ao ler o sensor DHT!");
    delay(1000);
    return;
  }
  
  int valorFosforo = gerarNumeroAleatorio(1, 50);
  int valorPotassio = gerarNumeroAleatorio(1, 50);
  
  // Leitura do pH
  int valor_ldr = analogRead(pin_ph);
  float valor_ph = map(valor_ldr, resistencia_ph4, resistencia_ph7, 4, 7);

  // Impressão dos dados
  Serial.println("Temperatura: " + String(dados.temperature, 2) + "°C");
  Serial.println("Umidade: " + String(dados.humidity, 1) + "%");
  Serial.println("Fósforo: " + String(valorFosforo));  
  Serial.println("Potássio: " + String(valorPotassio));
  Serial.println("pH: " + String(valor_ph, 2));

  // Verifica as condições e aciona os dispositivos
  // Bomba: Acionada apenas se a umidade estiver abaixo de 20%
  if (dados.humidity < 20) {
    digitalWrite(pinRele, HIGH); // Liga a bomba
    digitalWrite(pinLed, HIGH);   // Liga o LED
    Serial.println("Bomba ativada: Umidade baixa detectada");
  } else {
    digitalWrite(pinRele, LOW);  // Desliga a bomba
    digitalWrite(pinLed, LOW);    // Desliga o LED
    Serial.println("Bomba desligada: Umidade suficiente");
  }

  // Verificação dos níveis de nutrientes
  if (valorPotassio < 38) {
    digitalWrite(pinBotaoPotassio, HIGH);
    Serial.println("Ativação de potássio");
  } else {
    digitalWrite(pinBotaoPotassio, LOW);
    Serial.println("Nível de potássio suficiente");
  }

  if (valorFosforo < 15) {
    digitalWrite(pinBotaoFosforo, HIGH);
    Serial.println("Ativação de fósforo");
  } else {
    digitalWrite(pinBotaoFosforo, LOW);
    Serial.println("Nível de fósforo suficiente");
  }

  delay(1000);
}
