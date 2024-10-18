from smartphone import Smartphone


Iphone = Smartphone('iPhone', '15', '+79150061234')
Oppo = Smartphone('Oppo', 'X2', '+79234567890')
Samsung = Smartphone('Samsung', 'Note 5', '+79522341232')
Huawei = Smartphone('Huawei', 'Mate X3', '+79456543289')
Honor = Smartphone('Honor', 'Band 6', '+79898765672')
Pixel = Smartphone('Pixel', '7 Pro', '+79654321223')
catalog = [Iphone, Oppo, Samsung, Huawei, Honor, Pixel]
for catalogs in catalog:
    catalogs.SayAll()
