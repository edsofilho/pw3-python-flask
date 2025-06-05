from flask import render_template, request

# Array de objetos
placaslist = [
    {'Nome': 'Arduino Uno', 'Codigo': 'A8-009', 'Valor': '68.99'},
    {'Nome': 'Arduino Mega 2560', 'Codigo': 'A8-010', 'Valor': '95.50'},
    {'Nome': 'ESP32 DevKit', 'Codigo': 'A8-011', 'Valor': '82.40'},
    {'Nome': 'ESP8266 NodeMCU', 'Codigo': 'A8-012', 'Valor': '48.90'},
    {'Nome': 'Raspberry Pi 4 - 4GB', 'Codigo': 'A8-013', 'Valor': '379.99'},
    {'Nome': 'Raspberry Pi Pico', 'Codigo': 'A8-014', 'Valor': '35.00'},
    {'Nome': 'BeagleBone Black', 'Codigo': 'A8-015', 'Valor': '250.00'},
    {'Nome': 'STM32 Blue Pill', 'Codigo': 'A8-016', 'Valor': '44.90'},
    {'Nome': 'Teensy 4.0', 'Codigo': 'A8-017', 'Valor': '130.00'},
    {'Nome': 'ATtiny85 Digispark', 'Codigo': 'A8-018', 'Valor': '22.50'}
]

componenteslist = [
    {'Nome': 'Led 3v', 'Codigo': 'C1-001', 'Valor': '2.99'},
    {'Nome': 'Resistor 220Ω', 'Codigo': 'C1-002', 'Valor': '0.10'},
    {'Nome': 'Resistor 10kΩ', 'Codigo': 'C1-003', 'Valor': '0.10'},
    {'Nome': 'Capacitor Cerâmico 100nF', 'Codigo': 'C1-004', 'Valor': '0.30'},
    {'Nome': 'Capacitor Eletrolítico 10uF', 'Codigo': 'C1-005', 'Valor': '0.50'},
    {'Nome': 'Transistor BC547', 'Codigo': 'C1-006', 'Valor': '0.80'},
    {'Nome': 'Diodo 1N4007', 'Codigo': 'C1-007', 'Valor': '0.20'},
    {'Nome': 'Push Button', 'Codigo': 'C1-008', 'Valor': '0.90'},
    {'Nome': 'Potenciômetro 10k', 'Codigo': 'C1-009', 'Valor': '1.50'},
    {'Nome': 'Protoboard 830 pontos', 'Codigo': 'C1-010', 'Valor': '18.00'},
    {'Nome': 'Jumpers macho-macho (kit 65)', 'Codigo': 'C1-011', 'Valor': '5.00'},
    {'Nome': 'Display 7 segmentos', 'Codigo': 'C1-012', 'Valor': '3.90'}
]

sensoreslist = [
    {'Nome': 'Sensor RF 433MHz', 'Codigo': 'S1-001', 'Valor': '12.90'},
    {'Nome': 'Sensor Ultrassônico HC-SR04', 'Codigo': 'S1-002', 'Valor': '9.50'},
    {'Nome': 'Sensor de Temperatura LM35', 'Codigo': 'S1-003', 'Valor': '6.90'},
    {'Nome': 'Sensor de Chuva YL-83', 'Codigo': 'S1-004', 'Valor': '8.30'},
    {'Nome': 'Sensor de Gás MQ-2', 'Codigo': 'S1-005', 'Valor': '17.00'},
    {'Nome': 'Sensor de Luminosidade LDR', 'Codigo': 'S1-006', 'Valor': '1.50'},
    {'Nome': 'Sensor Infravermelho IR', 'Codigo': 'S1-007', 'Valor': '4.20'},
    {'Nome': 'Sensor de Movimento PIR', 'Codigo': 'S1-008', 'Valor': '13.40'},
    {'Nome': 'Sensor de Chama', 'Codigo': 'S1-009', 'Valor': '7.80'},
    {'Nome': 'Sensor de Umidade e Temperatura DHT11', 'Codigo': 'S1-010', 'Valor': '12.00'},
    {'Nome': 'Sensor de Toque Capacitivo TTP223', 'Codigo': 'S1-011', 'Valor': '3.70'}
]


def init_app(app):
    # Criando a rota principal do site
    @app.route('/')
    @app.route('/index', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')

    @app.route('/estoque', methods=['GET', 'POST'])
    def estoque():
        return render_template('estoque.html',
                               componenteslist=componenteslist,
                               sensoreslist=sensoreslist,
                               placaslist=placaslist)

    @app.route('/cadplacas', methods=['GET', 'POST'])
    def cadplacas():
        if request.method == 'POST':
            nome = request.form.get('nome')
            codigo = request.form.get('codigo')
            valor = request.form.get('valor')
        
        # Verifique se todos os campos foram preenchidos
            if nome and codigo and valor:
               placaslist.append({'Nome': nome, 'Codigo': codigo, 'Valor': valor})
               
        return render_template('cadplacas.html', placaslist=placaslist)

    @app.route('/cadcomponentes', methods=['GET', 'POST'])
    def cadcomponentes():
        if request.method == 'POST':
            nome = request.form.get('nome')
            codigo = request.form.get('codigo')
            valor = request.form.get('valor')
            
            # Verifique se todos os campos foram preenchidos
            if nome and codigo and valor:
                componenteslist.append({'Nome': nome, 'Codigo': codigo, 'Valor': valor})
        
        return render_template('cadcomponentes.html', componenteslist=componenteslist)

    @app.route('/cadsensores', methods=['GET', 'POST'])
    def cadsensores():
        if request.method == 'POST':
            nome = request.form.get('nome')
            codigo = request.form.get('codigo')
            valor = request.form.get('valor')
        
        # Verifique se todos os campos foram preenchidos
            if nome and codigo and valor:
                sensoreslist.append({'Nome': nome, 'Codigo': codigo, 'Valor': valor})
    
        return render_template('cadsensores.html', sensoreslist=sensoreslist)