#include "DHTesp.h" // Inclusao da biblioteca

//Definição dos PIN´s
#define pinUmidade 15
#define pinBotaoFosforo 18
#define pinLed 21
#define pinRele 22
#define pinBotaoPotassio 23


int valorFosforo = 0; // Definição de Fosforo se botão não acionado
int btnStateP;
int valorPotassio = 0; // Definição de Potássio se botão não acionado
int btnStateK;

// Define constantes para calibração do sensor de pH
const int resistencia_ph4 = 0;  
const int resistencia_ph7 = 1023;  
const int pin_ph = 34;  

DHTesp sensorUmidade; 

// Gera um número aleatório dentro de um intervalo para K e P
int gerarNumeroAleatorio(int min, int max) {
  return random(min, max + 1);
}

void setup() {
  Serial.begin(115200); //Inicia comunicação serial
  
  // Inicializa a geração de números aleatórios uma única vez
  randomSeed(analogRead(0));
  
  sensorUmidade.setup(pinUmidade, DHTesp::DHT22); //Configura o sensor DHT22

  //Define os modos dos pinos (entrada/saída)
  pinMode(pinRele, OUTPUT);
  pinMode(pinBotaoPotassio, INPUT_PULLUP);  
  pinMode(pinBotaoFosforo, INPUT_PULLUP);   
  pinMode(pinLed, OUTPUT); 
}

void loop() {
  // Leitura da temperatura e umidade do sensor
  TempAndHumidity dados = sensorUmidade.getTempAndHumidity();
  
  //Pressionando o botão azul verifica o valor do Potassio  
  btnStateK = digitalRead(pinBotaoPotassio);
  if (btnStateK == LOW){
    valorPotassio = gerarNumeroAleatorio(1,50); //Gera valores aleatórios para Potássio
  }

  //Pressionando o botão verde verifica o valor do Fosforo  
  btnStateP = digitalRead(pinBotaoFosforo);
  if (btnStateP == LOW){
    valorFosforo = gerarNumeroAleatorio(1,50); //Gera valores aleatórios para Fosfóro
  }

  int valor_ldr = analogRead(pin_ph); // Leitura do valor analógico do sensor de pH
  float valor_ph = map(valor_ldr, resistencia_ph4, resistencia_ph7, 4, 7); //Mapeia o valor para a escala de pH (4 a 7)

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

  delay(1000);
}
