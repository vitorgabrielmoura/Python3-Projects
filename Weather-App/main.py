import requests
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.QtGui import QPixmap, QIcon
from design import Ui_MainWindow
import sys
from datetime import datetime, timedelta

class Janela(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowIcon(QIcon('resources\Icon2.ico'))
        self.setFixedSize(412, 388)

        self.btnInfo.setIcon(QIcon('resources\info.png'))
        self.pushButton_2.setIcon(QIcon('resources\info2.png'))

        self.inputCidade.returnPressed.connect(self.acessa)

        self.btn_enviar.clicked.connect(self.acessa)
        self.btnInfo.clicked.connect(lambda i: QMessageBox.information(self, 'Sobre', 'Aplicativo feito por Vitu - copyright ©\nNão possuí fins lucrativos, somente educacionais\n\nVersão atual: 1.0'))
        self.pushButton_2.clicked.connect(lambda i: QMessageBox.information(self, '?', 'Esse botão ainda não faz nada.'))


        self.btn_enviar.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 15px")


    def acessa(self):
        api_key = '3ea6cb06e99531b888534f5b26da79fc'
        idioma = 'pt_br'
        city_name = self.inputCidade.text()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang={idioma}'
        try:
            response = requests.get(url)
            x = response.json()

            if x["cod"] != 404:
                t = x['main']

                timenow = datetime.utcnow()
                hours_away = int(x['timezone']) /60 /60
                hours = timenow + timedelta(hours=hours_away)
                hora = hours.hour


                name = x['name']
                pais = x['sys']['country']

                sens = t['feels_like'] - 273
                current_temp = int(t['temp']) - 273
                min_temp = t['temp_min'] - 273
                max_temp = t['temp_max'] - 273
                sit = x['weather'][0]['description']

                self.label_min.setText("Min:")
                self.label_max.setText("Max:")
                self.label_city.setText(f'{name} - {pais}')
                self.label_temp.setText(str(f'{current_temp}°C'))
                self.label_desc.setText(str(sit).capitalize())
                self.label_tempmin.setText(str(f'{min_temp:.1f}°C'))
                self.label_tempmax.setText(str(f'{max_temp:.1f}°C'))
                self.label_time.setText(hours.strftime('%d/%m/%Y\n%H:%M:%S'))
                self.label_stermica.setText('S. Térm:')
                self.label_stermica2.setText(f'{sens:.1f}°C')

                if sit == 'céu limpo':
                    if 18 > hora > 6:
                        self.label_img.setPixmap(QPixmap('resources\sunny2.png'))
                    else:
                        self.label_img.setPixmap(QPixmap('resources\sunny3.png'))
                if sit == 'nuvens dispersas' or sit == 'nublado' or sit == 'algumas nuvens':
                    if 18 > hora > 6:
                        self.label_img.setPixmap(QPixmap('resources\cloudy3.png'))
                    else:
                        self.label_img.setPixmap(QPixmap('resources\cloudy2.png'))
                if sit == 'névoa' or sit == 'neblina':
                    self.label_img.setPixmap(QPixmap(r'resources\fog.png'))
                if sit == 'chuva moderada' or sit == 'chuva forte' or sit == 'chuva leve' or sit == 'chuviscos moderados':
                    self.label_img.setPixmap(QPixmap(r'resources\rain1.png'))
            else:
                pass
        except Exception as e:
            self.messagebox = QMessageBox.critical(self, 'Erro', f'Não consegui achar essa cidade.\nVerifique se digitou corretamente e tente novamente.\n\n{e} - {type(e)}')


if __name__ == '__main__':
    qtt = QApplication(sys.argv)
    app = Janela()
    app.show()
    sys.exit(qtt.exec_())
