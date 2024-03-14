# criando uma tabela  de produtos em estoques
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QTableWidget,QTableWidgetItem,QHBoxLayout,QVBoxLayout,QPushButton,QComboBox

class Janela(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setGeometry(5,50,1580,800)
        self.setWindowTitle("Tabela de Estoque")
        
    #    criando o layout principal com distribuiçao vertical
    
        layout_principal = QVBoxLayout()
        
        # criar4 labels pra colocar na janela
        
        label_superio = QLabel()
        label_meio = QLabel()
        label_tabela = QLabel()
        label_rodape = QLabel()
        
        
        
        # aplicaçao de estilos de cor e ajuste da altura de cada label 
        
        label_superio.setStyleSheet("QLabel{background-color:yellow}")
        label_superio.setFixedHeight(300)
        
        label_meio.setStyleSheet("QLabel{background-color:red}")
        label_meio.setFixedHeight(60)
        
        
        label_tabela.setStyleSheet("QLabel{background-color:blue}")
        label_tabela.setFixedHeight(400)
        
        
        label_rodape.setStyleSheet("QLabel{background-color :brown}")
        label_rodape.setFixedHeight(100)

        # adicionar as labels horizontais ao layout principal 
        
        layout_principal.addWidget(label_superio) 
        layout_principal.addWidget(label_meio)
        layout_principal.addWidget(label_tabela)
        layout_principal.addWidget(label_rodape)
        
        # vms criar um layout horizontal  para distribuir as 3 colunas na parte superior do layout 
        #  as 3 colunas serao criadas com label e adicionadas o layout horizontal 
        
        layout_hor_lb_superior = QHBoxLayout()
        
        label_col_esquerda = QLabel()
        label_col_meio = QLabel()
        label_col_direita = QLabel()
        
        
         
        
        label_col_esquerda.setStyleSheet("QLabel{background-color:blue}")
        label_col_meio.setStyleSheet("QLabel{background-color:red}")
        label_col_direita.setStyleSheet("QLabel{background-color:blue}")  
        
        
        layout_hor_lb_superior.addWidget(label_col_esquerda)  
        layout_hor_lb_superior.addWidget(label_col_meio)
        layout_hor_lb_superior.addWidget(label_col_direita)    
        
        
        label_superio.setLayout(layout_hor_lb_superior) 
        
        # *******************************************************************************
        
        layout_ver_col_esquerda = QVBoxLayout()
        
        label_estabelecimento = QLabel("estabelecimento")
        label_estabelecimento.setStyleSheet("QLabel{font-size:15pt;color:white}")
        combo_estabelecimento = QComboBox()
        combo_estabelecimento.setStyleSheet("QComboBox{padding: 10px; font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_estabelecimento)
        layout_ver_col_esquerda.addWidget(combo_estabelecimento)
        label_col_esquerda.setLayout(layout_ver_col_esquerda)
        
        # *****************************************************************************************************
        
        
        label_Documento = QLabel("Documento")
        label_Documento.setStyleSheet("QLabel{font-size:15pt;color:white}")
        combo_documento =QComboBox()
        combo_documento.setStyleSheet("QComboBox{padding: 10px; font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_Documento)
        layout_ver_col_esquerda.addWidget(combo_documento)
        label_col_esquerda.setLayout(layout_ver_col_esquerda)
        
        label_grupo = QLabel("Grupo")
        label_grupo.setStyleSheet("QLabel{font-size:15pt;color:white}")
        combo_Grupo =QComboBox()
        combo_Grupo.setStyleSheet("QComboBox{padding: 10px; font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_grupo)
        layout_ver_col_esquerda.addWidget(combo_Grupo)
        label_col_esquerda.setLayout(layout_ver_col_esquerda)
        
        
        
        
        self.setLayout(layout_principal)
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
app = QApplication(sys.argv)
tela=Janela()
tela.show()
app.exec_()
       
        