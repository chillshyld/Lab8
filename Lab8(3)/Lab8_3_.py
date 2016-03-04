def paintEvent(self, e):
    p = Qpainter()
    p.begin(self)
    
    p.setPen(QColor(0,0,0))
    p.setBrush(QColor(0, 127, 0))
    p.drawPolygon()