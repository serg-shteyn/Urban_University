class Pol:
    alfa=0.2
    podvod=0
    zapas=1.0
    def __init__(self):
        '''a,b - стороны комнаты,
        step - шаг
        alfa - отступ от стен
        '''
        
        print('Рассчет труб водяного теплого пола')
        print('-'*35)
        print('Пример ввода: a,b,c,d=0.2,e=0')
        print('a,b - размеры помещения')
        print('c - шаг , d - отступ')
        print('e - расстояние до подключения')
        print('-'*35)
        self.next()
        
    def my_init(self):
        demp=(self.a+self.b)*2
        sq=(self.a*self.b)
        self.sq=round(sq,3)
        self.demp=round(demp,3)
            
    def next(self):
        self.enter()
        self.my_init()
        self.sector()
        self.get_sectors_per()
        self.test()
        while(not self.t=='0'):
            self.new_step()
            self.sector()
            self.get_sectors_per()
            self.test()
        
    def new_step(self):
        ent=input('Введите другой шаг:')
        while (not self.check_step(ent)):
            ent=input('ошибка ввода! Введите размеры,м:')
        ent=float(ent)
        del self.step
        self.step=ent
        del self.sectors
            
    def check_step(self,s):
        if float(s):
            return True
        else:
            return False
            
        
    def min(self,a,b):
       if float(a)<float(b):
           self.a=float(a)
           self.b=float(b)
       else:
           self.a=float(b)
           self.b=float(a)
           
    def enter(self):
        ent=input('Введите размеры,м:')
        ent=ent.split(',')
        while (not self.check(ent)):
            ent=input('ошибка ввода! Введите размеры,м:')
            ent=ent.split(',')
        self.min(ent[0],ent[1])
        self.step=float(ent[2])
        if len(ent)>3:
            self.podvod=float(ent[3])
        if len(ent)>4:
            self.alfa=float(ent[4])
        
            
    def check(self,ent):
        if len(ent)<3 or len(ent)>5:
            return False
        for i in ent:
            try:
                float(i)
            except:
                return False
        return True
        
    def sector(self):
        a=self.a
        b=self.b
        sectors=[]
        a=round((a-self.alfa*2),3)
        b=round((b-self.alfa*2),3)
        while (a>(self.step*2)):
            sectors.append([a,b])
            a=round((a-self.step*2),3)
            b=round((b-self.step*2),3)
        sectors.append([a,b])
        self.sectors=sectors
        
        
        
    def per(self,A):
        per=A[0]*2+A[1]*2
        return round(per,3)
        
    def get_sectors_per(self):
        self.sectors_per=[]
        for i in self.sectors:
            self.sectors_per.append(self.per(i))
        
    def get_long(self):
        N=len(self.sectors_per)
        L=0
        for s in range(0,N):
            if s==0:
                dop=self.alfa*2
            elif s==N-1:
                dop=-self.step
            else:
                dop=0
            sector=round((self.sectors_per[s]+dop),5)
            L=(L+sector) 
        self.L0=round(L,2)
        self.L1=round((L*self.zapas),3)
        self.L2=round((self.L1+self.podvod*2),3)
            
            
            
            
    def test(self):
        print('='*38)
        print('Размеры помещения:',self.a,'x',self.b)
        print(f'Потребуется демпферной ленты - {self.demp} п.м.')
        print(f'Площадь помещения - {self.sq} м.кв.')
        print('-'*28)
        print('шаг,отступ,подвод в м.:',self.step,',',self.alfa,',',self.podvod)
        print('-'*38)
        print('размеры секторов, м.')
        for i in self.sectors:
            print(i[0],'x',i[1])
        self.get_long()
        print('Длина трубы без подвода:')
        print(self.L0,'м.')
        print(f'Длина трубы с запасом {round(((self.zapas*100)-100),2)}%:')
        print(self.L1,'м.')
        print(f'Длина трубы с подводом, {self.podvod}м.')
        print(self.L2,'м.')
        print('-'*28)
        self.t=input('Попробовать с другим шагом?')
Pol()
        