// Otimizações propostas resultam em redução do uso de RAM, melhor utilização da memória flash, operações mais eficientes e menor fragmentação de memória
// Link para o wokwi https://wokwi.com/projects/413103691995388929


#include "DHTesp.h" // Inclusao da biblioteca

// Definição dos PINs usando uint8_t (1 byte) ao invés de int (4 bytes)
static const uint8_t pinUmidade = 15;
static const uint8_t pinBotaoFosforo = 18;
static const uint8_t pinLed = 21;
static const uint8_t pinRele = 22;
static const uint8_t pinBotaoPotassio = 23;

// Utilização de uint8_t para valores que não excedem 255 e não serão negativos. Redução de 4 bytes (int) para 1 byte

// Definição de Fosforo se botão não acionado
uint8_t valorFosforo = 0; 

// Definição de Potássio se botão não acionado
uint8_t  valorPotassio = 0; 

 // Utilização de bool (1 byte) ao invés de int (4 bytes) para os botões
 bool btnStateP;
 bool btnStateK;

 // Constantes para calibração do sensor de pH
 // Utilização de uint16_t (2 bytes) ao invés de int (4 bytes) para valores até 1023

 // Definição da calibração do sensor de pH
 static const uint16_t resistencia_ph4 = 0;  
 static const uint16_t resistencia_ph7 = 1023;  
 static const uint8_t pin_ph = 34;  

 // Declarado como static para limitar escopo
 static DHTesp sensorUmidade; 

 // Gera um número aleatório dentro de um intervalo para K e P
 // Parâmetros alterados para uint8_t já que os valores são pequenos (1-50)
 uint8_t  gerarNumeroAleatorio(uint8_t  min, uint8_t  max) {
 return random(min, max + 1);
 }

 void setup() {
 Serial.begin(115200); //Inicia comunicação serial
  
 // Inicializa a geração de números aleatórios uma única vez
 randomSeed(analogRead(36));
  
 sensorUmidade.setup(pinUmidade, DHTesp::DHT22); //Configura o sensor DHT22

 //Definição dos modos dos pinos (entrada/saída)
 pinMode(pinRele, OUTPUT);
 pinMode(pinBotaoPotassio, INPUT_PULLUP);  
 pinMode(pinBotaoFosforo, INPUT_PULLUP);   
 pinMode(pinLed, OUTPUT); 
 }

 void loop() {
 // Leitura da temperatura e umidade do sensor, Struct TempAndHumidity otimizada pela biblioteca
 TempAndHumidity dados = sensorUmidade.getTempAndHumidity();

 // Leitura dos botões com debounce simplificado,invertido para economizar operação
  
 //Pressionando o botão azul verifica o valor do Potassio 
 btnStateK = digitalRead(pinBotaoPotassio); 
 if (btnStateK == LOW){
 valorPotassio = gerarNumeroAleatorio(1,50); 
 } else {
        valorPotassio = 0; // Retorna para 0 quando o botão é solto
    }

 //Pressionando o botão verde verifica o valor do Fosforo  
 btnStateP = digitalRead(pinBotaoFosforo);
 if (btnStateP == LOW){
 valorFosforo = gerarNumeroAleatorio(1,50); //Gera valores aleatórios para Fosfóro
 } else {
        valorFosforo = 0; // Retorna para 0 quando o botão é solto
    }
    
 // Usando uint16_t para leitura analógica (0-4095 no ESP32)
 uint16_t  valor_ldr = analogRead(pin_ph); // Leitura do valor analógico do sensor de pH
  
 //Mapeia o valor para a escala de pH (4 a 7)
 float valor_ph = map(valor_ldr, resistencia_ph4, resistencia_ph7, 40, 70) /10.0f;

 // Buffer estático para formatar strings
 static char buffer[50];

 // Impressão dos dados, utilização de snprintf para otimizar o uso de memória na formatação
 snprintf(buffer, sizeof(buffer), "Temperatura: %.2f°C", dados.temperature);
 Serial.println(buffer);
  
 snprintf(buffer, sizeof(buffer), "Umidade: %.1f%%", dados.humidity);
 Serial.println(buffer);

 snprintf(buffer, sizeof(buffer), "Fósforo: %u", valorFosforo);
 Serial.println(buffer);
    
 snprintf(buffer, sizeof(buffer), "Potássio: %u", valorPotassio);
 Serial.println(buffer);
    
 snprintf(buffer, sizeof(buffer), "pH: %.2f", valor_ph);
 Serial.println(buffer);


 // Verifica as condições e aciona os dispositivos
 // Bomba: Acionada apenas se a umidade estiver abaixo de 20%
 bool bomba_estado = (dados.humidity < 20);
 digitalWrite(pinRele, bomba_estado);
 digitalWrite(pinLed, bomba_estado);
   
 Serial.println(bomba_estado ? "Bomba ativada: Umidade baixa detectada"
                : "Bomba desligada: Umidade suficiente");
  

  delay(1000);
}
