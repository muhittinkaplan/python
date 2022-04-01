from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

from mplcursors import cursor

from PyQt5.Qt import *
import pandas as pd

import os
import sys
import pickle

class MapClass(QDialog):#sınıf pyqt qdialog dan kalıtım alıyor
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fig = plt.figure('map', facecolor='Silver')#type:Figure #matplotlib figure oluşturuyoruz type ile yapılan işleme dikkat
        self.canvas = FigureCanvas(self.fig)#matplotlib canvas oluşturuyoruz
        self.ax = plt.axes()#type:plt.Axes #matplotlib Ax oluşturuyoruz.type ile yapılan işleme dikkat
        self.ax.set_facecolor('LightCyan')
        self.ax.format_coord=self.informationCoordType#matplotlib penceresinde sağ üstte bulunan cursor bilgilerini düzenlemek için kullanılıyor
        self.cursorX=0#cursorun bilgisini tutuyor
        self.cursorY=0#cursorun bilgisini tutuyor
        self.toolbar=NavigationToolbar(self.canvas,self)#matplotlib için toolbar oluşturuluyor.
        self.editWidgetOnEarthToolbar(self.toolbar)#toolbar a buton eklemek için kullanılan fonksiyon
        self.centerLayout=QVBoxLayout(self)#vertical layout oluşturuluyor
        self.centerLayout.addWidget(self.toolbar)#layout a toolbar ekleniyor
        self.centerLayout.addWidget(self.canvas)#layout a matplotlib canvas ı ekleniyor
        self.setLayout(self.centerLayout)#pyqt diyalog penceresi (sınıfın kalıtım aldığı)
        self.earthMap=self.createMAP("high","ocean.png")#harita createMap metodu ile oluşturuluyor, Basemap tipinde dönüyor.
        self.eventConnect()#Matplotlib olayları ile fonksiyonlar bağlanıyor
        self.setGeometry(0,0,800,700)
        self.setWindowTitle("AllInOne")
        self.show()

    def earthMapScroolEvent(self, event):
        if event.step == 1:
            minXlim = self.ax.get_xlim()[0]
            maxXlim = self.ax.get_xlim()[1]
            ratioX = (maxXlim - minXlim) * 0.2

            minYlim = self.ax.get_ylim()[0]
            maxYlim = self.ax.get_ylim()[1]
            ratioY = (maxYlim - minYlim) * 0.2

            newXlim = ((minXlim + ratioX), (maxXlim - ratioX))
            newYlim = ((minYlim + ratioY), (maxYlim - ratioY))

            self.ax.set_xlim(newXlim)
            self.ax.set_ylim(newYlim)

            self.canvas.draw()
        else:

            minXlim = self.ax.get_xlim()[0]
            maxXlim = self.ax.get_xlim()[1]
            ratioX = (maxXlim - minXlim) * 0.2

            minYlim = self.ax.get_ylim()[0]
            maxYlim = self.ax.get_ylim()[1]
            ratioY = (maxYlim - minYlim) * 0.2

            newXlim = ((minXlim - ratioX), (maxXlim + ratioX))
            newYlim = ((minYlim - ratioY), (maxYlim + ratioY))

            self.ax.set_xlim(newXlim)
            self.ax.set_ylim(newYlim)

            self.canvas.draw()
            #self.fig.canvas.flush_events()

    #overloading format_coord

    def informationCoordType(self, x, y):
        originLon, originLat = (self.earthMap(self.cursorX, self.cursorY, inverse=True))#kartezyen verilen bilgiyi lon,lat a çeviriyor
        return ('Lon %f  Lat %f' % (originLon, originLat))

    def earthMapOnMoveEvent(self, event):
        '''
        mouse x y durumunu verir.
        :param event:
        :return:
        '''
        if not event.inaxes:
            self.inaxes=True
            return
        else:
            self.cursorX = event.xdata
            self.cursorY = event.ydata
            self.inaxes=False

    def eventConnect(self):
        self.canvas.mpl_connect('motion_notify_event', self.earthMapOnMoveEvent)#mouseMove
        self.canvas.mpl_connect('scroll_event', self.earthMapScroolEvent)#tekerlek ileri geri

    def editWidgetOnEarthToolbar(self,toolbar):
        btn=QPushButton("Çiz")#buton oluşturuluyor
        btn.clicked.connect(self.drawShapes)#butona click metodu için fonksiyon atanıyor
        btn2 = QPushButton()#buton oluşturuluyor
        toolbar.addWidget(btn)#toolbar a buton ekleniyor
        toolbar.addWidget(btn2)#toolbar a buton ekleniyor

    def formatterCursor(self, index):
        label=['Kırmızı Nokta','Yeşil Nokta','Mavi Nokta','Mor Nokta']
        print(index)
        return ("{} index Numaralı {} ".format(index,label[index]))

    def setUserPointOnEarthMap(self,ax:plt.Axes,earthMap:Basemap,userPoinFile:str)->Basemap:
        _userPoints = pd.read_csv(userPoinFile)
        _coordinatesTocartesian = []
        #Koordinatlara Şekil Koy ve yaz

        for i in range(len(_userPoints)):
            _lat=_userPoints['lat'].tolist()[i]
            _lon=_userPoints['lon'].tolist()[i]

            _marker=_userPoints['marker'].tolist()[i]
            _markerColor=_userPoints['markercolor'].tolist()[i]
            _markerSize=_userPoints['markersize'].tolist()[i]

            _name=_userPoints['name'].tolist()[i]
            _fontSize=_userPoints['fontsize'].tolist()[i]
            _nameColor=_userPoints['namecolor'].tolist()[i]

            x, y = earthMap(_lon,_lat)

            earthMap.scatter(x, y, zorder=11, marker=_marker,color=_markerColor,s=_markerSize)
            self.ax.text(x,y,_name,fontsize=_fontSize,color=_nameColor)
            _coordinatesTocartesian.append([x,y])#polygon için koordinatları tutuyor

        _patches = []
        _patches.append(Polygon(_coordinatesTocartesian))
        self.ax.add_collection(
            PatchCollection(patches=_patches, facecolors='lightgreen', edgecolors='k', linewidths=1.5, alpha=0.5))

        #forCursor = earthMap.scatter(_userPoints['lon'].tolist(), _userPoints['lat'].tolist(), latlon=True, alpha=0.0)

        plotForCursorColor=['r','g','b','m']
        plotForCursor=earthMap.scatter([25.00,26.00,27.00,28.00],[45.00,45.00,45.00,45.0],
                                       latlon=True,c=plotForCursorColor,marker="o",s=10)

        myHoverCursor = cursor(plotForCursor, multiple=True).\
            connect("add", lambda sel: sel.annotation.
                set_text(self.formatterCursor(sel.target.index)))  # scatterlara tıklandığında balon göster

        return earthMap

    def setResolutionAndCreateBaseMap(self,mapRes='coarse')->Basemap:
        '''

        :param mapRes:
        :return:

        Basemap oluştururken, daha hızlı olması açısından, önceden oluşturulmulmuş ve pickle modülü ile serialize edilmiş
        basemap haritası okunuyor, eğer bu dosyalar yoksa her defasında tekrar tekrar oluşturmak gerekecek, dolayısıyla
        performans düşecekti.

        '''
        if mapRes == 'high':
            mapFile,mapFileType = 'mapHighRes.pickle','h'
        else:  # coarse
            mapFile,mapFileType = 'mapCoarseRes.pickle','c'

        if os.path.exists(mapFile):  #pickle dosyası orada duruyormu ?
            earthMap = pickle.load(open(mapFile, 'rb'))
        else:
            earthMap = Basemap(projection='mill', llcrnrlat=31, urcrnrlat=44, llcrnrlon=21, urcrnrlon=52,
                             resolution=mapFileType, epsg=5254)  # epsg 5254 epsg=4326 2boyutluMap, 5253-5259 3Deg,
            pickle.dump(earthMap, open(mapFile, 'wb'), -1)  #pickle modülü ile serialize et.

        return earthMap

    def setImageToEarthMap(self,earthMap:Basemap,imagePath=None)->Basemap:

        if (imagePath !=None):
            earthMap.imshow(plt.imread(imagePath), origin='upper',interpolation='nearest')

        else:
            earthMap.fillcontinents(zorder=1, color='#efebe7')
            earthMap.drawmapboundary(zorder=0)

        return earthMap

    def createMAP(self,mapRes:str='coarse',bgImage:str=None)->Basemap:


        earthMap=self.setResolutionAndCreateBaseMap(mapRes=mapRes)

        earthMap=self.setImageToEarthMap(earthMap=earthMap,imagePath=bgImage)

        earthMap.drawcoastlines(linewidth=0.1, linestyle='solid', color='k', antialiased=1,ax=self.ax,zorder=9)
        earthMap.drawcountries(linewidth=0.1, linestyle='solid', color='k', antialiased=1,ax=self.ax,zorder=10)
        earthMap.drawstates(color='#A0A0A0')
        earthMap.drawparallels(circles=[33, 36, 39, 42, 45], color='gray', textcolor='gray', linewidth=0.5, labels=[1, 0, 0, 0])
        earthMap.drawmeridians(meridians=[23, 26, 29, 32, 35, 38, 41, 44, 47], color='gray', textcolor='gray', linewidth=0.5,
                             labels=[1, 0, 0, 1])  # label left right up bottom

        self.fig.tight_layout()#en geniş halde ayarla
        self.ax.text(0,1,'Noktaların Üzerine Tıkla !!',
                     fontsize=15,
                     color='DarkSlateGray',
                     ha='left',va='top',
                     transform=self.ax.transAxes)



        self.setUserPointOnEarthMap(ax=self.ax,earthMap=earthMap,userPoinFile="userpointlist.csv")

        return earthMap


    def drawShapes(self):
        lon1=23.132620121470136
        lat1=33.34624901509963
        lon2=45.65072916000131
        lat2=42.45794055728087


        self.earthMap.drawgreatcircle(lon1=lon1, lat1=lat1,lon2=lon2, lat2=lat2)#küre dünyaya göre çizgi çiziyor
        _x1,_y1=self.earthMap(lon1,lat1)#latlon degerlerini X ve Y degerine çeviriyor.
        _x2, _y2 = self.earthMap(lon2, lat2)
        self.earthMap.plot([_x1,_x2],[_y1,_y2],color='red',alpha=0.5)#düz çizgi çiziyor
        self.earthMap.scatter([_x1,_x2],[_y1, _y2], zorder=12, marker='*',color='blue',s=100,alpha=0.5)#nokta dağılım oluşturuyor
        self.canvas.draw()#canvas i çiz

if __name__ == '__main__':

    uygulama = QApplication(sys.argv)
    uygulama.setStyle(QStyleFactory.create('Fusion'))
    pencere =MapClass()

    uygulama.exec_()
