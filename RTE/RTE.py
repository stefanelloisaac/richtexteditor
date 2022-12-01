import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import *

class RTE(QMainWindow):
    def __init__(self):
        super(RTE, self).__init__()
        self.editor = QTextEdit()
        self.fontSizeBox = QSpinBox()           #caixa para alterar tamanho da fonte

        font = QFont('Times', 24)
        self.editor.setFont(font)
        self.path = ""
        self.setCentralWidget(self.editor)      #mostrar o campo de texto
        self.setWindowTitle('Rich Text Editor') #nome da janela
        self.showMaximized()                    #iniciar maximizado
        self.barra_de_ferramentas()             #iniciar barra de ferramentas
        self.editor.setFontPointSize(24)


    def barra_de_ferramentas(self):
        ferramentas = QToolBar()

        salvar = QAction(QIcon('save.png'), 'Salvar', self)
        salvar.triggered.connect(self.saveFile)
        ferramentas.addAction(salvar)

        desfazer = QAction(QIcon('undo.png'), 'Desfazer', self)
        desfazer.triggered.connect(self.editor.undo)
        ferramentas.addAction(desfazer)

        refazer = QAction(QIcon('redo.png'), 'Refazer', self)
        refazer.triggered.connect(self.editor.redo)
        ferramentas.addAction(refazer)

        copiar = QAction(QIcon('copy.png'), 'Copiar', self)
        copiar.triggered.connect(self.editor.copy)
        ferramentas.addAction(copiar)

        recortar = QAction(QIcon('cut.png'), 'Recortar', self)
        recortar.triggered.connect(self.editor.cut)
        ferramentas.addAction(recortar)

        colar = QAction(QIcon('paste.png'), 'Colar', self)
        colar.triggered.connect(self.editor.paste)
        ferramentas.addAction(colar)

        self.fontBox = QComboBox(self)
        self.fontBox.addItems(['Helvetica', 'Arial', 'Courier Std', 'Times', 'Monospace'])
        self.fontBox.activated.connect(self.setFont)
        ferramentas.addWidget(self.fontBox)

        self.fontSizeBox.setValue(24)
        self.fontSizeBox.valueChanged.connect(self.setFontSize)
        ferramentas.addWidget(self.fontSizeBox)

        right_align = QAction(QIcon('alignright.png'), 'Alinhar à direita', self)
        right_align.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
        ferramentas.addAction(right_align)

        left_align = QAction(QIcon('alignleft.png'), 'Alinhar à esquerda', self)
        left_align.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
        ferramentas.addAction(left_align)

        center_align = QAction(QIcon('aligncenter.png'), 'Alinhar ao centro', self)
        center_align.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignHCenter))
        ferramentas.addAction(center_align)

        justify_align = QAction(QIcon('alignjustify.png'), 'Justificado', self)
        justify_align.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignJustify))
        ferramentas.addAction(justify_align)

        ferramentas.addSeparator()

        negrito = QAction(QIcon('bold.png'), 'Negrito', self)
        negrito.triggered.connect(self.textoNegrito)
        ferramentas.addAction(negrito)

        sublinhado = QAction(QIcon('underline.png'), 'Sublinhado', self)
        sublinhado.triggered.connect(self.textoSublinhado)
        ferramentas.addAction(sublinhado)

        italico = QAction(QIcon('italic.png'), 'Itálico', self)
        italico.triggered.connect(self.textoItalico)
        ferramentas.addAction(italico)

        ferramentas.addSeparator()

        # imprimir = QAction(QIcon("print.png"), "Imprimir", self)
        # imprimir.triggered.connect(self.print)
        # ferramentas.addAction(imprimir)


        self.addToolBar(ferramentas)


    def setFontSize(self):
        value = self.fontSizeBox.value()
        self.editor.setFontPointSize(value)

    def setFont(self):
        font = self.fontBox.currentText()
        self.editor.setCurrentFont(QFont(font))

    def textoNegrito(self):
        if self.editor.fontWeight != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)
            return
        self.editor.setFontWeight(QFont.Normal)

    def textoSublinhado(self):
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not(state))

    def textoItalico(self):
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not(state))

    def saveFile(self):
        print(self.path)
        if self.path == '':
            self.file_saveas()
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def file_saveas(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt)")
        if self.path == '':
            return
        text = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)


app = QApplication(sys.argv)
window = RTE()
window.show()
sys.exit(app.exec_())

