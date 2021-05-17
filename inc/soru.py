import random
def soru18(num):
  sorular = [
    'Yeni tanıdığın biriyle ne kadar ileri gide bilirsin?',
    'Daha önce hiç karşı cinsten biri için iç çamaşırı aldın mı?',
    'Orgazm sırasında hiç ağladı mı?',
    'Hiç arabada yaramazlık yapdın mı?',
    'Hiç striptiz clubuna gittin mi?',
    'Kusursuz bir flört ile ilgili ilk düşüncelerin neler?',
    'Seni eski sevgilinle bir araya getirecek şeyler neler?',
    'Daha önce hiç partnerinize ilişki sırasında veya öncesinde başka insanlarla beraber olma konusunda yalan söylediniz mi?',
    'Redtube, YouPorn veya PornHub? Hangisi ve neden?',
    'Daha önce hiç arkadaşınızın kardeşini öpdünüz mü?',
    'Çıplak uyur musun?',
    'Tamamiyle giyinik olduğun bir zaman hiç orgazm oldunuz mu?',
    'Daha önce hiç annenle babanı sevişirken yakalandın mı?',
    'En çok cinsel istek duyduğun şey nedir?',
    'Büyüklük senin için önemli mi?',
    'En kötü öpüşmen hangisiydi?',
    'En çok hangi tarz müzikle seks yapmayı seversin?',
    'Şu an ne kadar istekli olduğunu 1-10 arasında puanla.',
    'Favori porno siten hangisidir?',
    'İlk aşkınızın ismi neydi?',
    'En utanç verici cinsel deneyimin nedir?',
    'Eğer eski sevgililerinden biriyle bir gece geçirecek olsan kimi seçerdin?',
    'Şimdiye kadar işediğin en garip yer neresiydi?',
    'Aynı cinsten biriyle çıkma cesaretini gösterirmiydin?',
    'Daha önce hiç strip poker oynadın mı?',
    'Şu ana kadar en acı verici ayrılığı anlat.',
    'Hiç bahis oynadın mı? Kayb etdiğin en büyük meblağ neydi?',
    'striptizci mi porno yıldızı mı olmayı tercih edersin?',
    'Cinsellikte sığ olduğun konular nelerdir?',
    'Asla denemem bile diyeceğin pozisyon?',
    'İlk kiminle öpüştün?',
    'Daha önce gördüğün en açık saçık rüya hangisiydi? Detaylıca açıkla!',
    'Daha önce hiç hafif uyuşdurucu kullandın mı?',
    'Daha önce hiç tutuklandın mı?',
    'Daha önce hiç birinin çıplak fotoğrafını çekmesine izin verdin mi? Vermediysen, verir miydin?',
    'Aldatmayı hiç ciddi ciddi düşündüğün oldu mu?',
    'Üzerinde prezervatif taşıyor musun?',
    'Eğer gay deilsen, bu oda da seni gay yapabilmesi en muhtemel kişi kim?',
    'Daha önce hiç uyuşturucu almayı düşündüğün fakat cesaret edemediyin oldu mu?',
    'Daha önce hiç BDSM denediğiniz veya denemek istediğiniz oldu mu?',
    'Ne çeşit bu "sarhoşsun": mutlu, sosyal, herkesi seven, kaba, saldırgan, aşırı samimi, cinsel istekli, sessiz ve sakin veya sinsi?',
    'Daha önce hiç toplum içinde çıplak duş aldın mı?',
    'Bakir/bakireliğini nerde kaybetdin?',
    'Daha önce hiç telefonda seks yapdın mı?',
    'Bu oda da biriyle ne kadar ileriye gidebilirsin?',
    'En derin, karanlık fantazin nedir?',
    'Sarhoşken yapdığın en aptalca şey nedir?',
    'Hiç aromalı bir prezervatif kullandın mı?',
    'Orgazm olduğun en kısa süre nedir?',
    'İznin olmayan (+18) bir film veya TV şovunu izlendin mi?',
    'Sence nasıl bir hata ilişkinin bitmesi için yeterlidir?',
    'Seçmek zorunda olsan kız/erkek arkadaşının yerini alması için bu odadan kimi seçerdin?',
    'Bu odadan hangi kız veya erkeği ailen ile tanışdırsan çıldırırlardı?',
    'Sana karşı yapılmış fakat aff etdiğin en büyük kötülük neydi? Şu an olsa yine aff edermiydin?',
    'Yaşın hakkında yalan söylediğin halde en uzun süre devam eden ilişkin hangisiydi? Yakalanmadan ne kadar sürdürdün?',
    "Hiç ex'nin akrabasıyla sevgili oldun mu? Cevabın evetse, ne kadar yakın akrabasıydı?",
    'Eyvah! En yakın arkadaşınla sevgilisini uygunsuz bi zamanda yakaladın. Durumu toparlamak için yapacağın ilk şey nedir?'
    ]
  try:
    sayı=int(num)
  except:
    sayı=False
  if num=="random":
    return random.choice(sorular)
  elif sayı:
    try:
      return sorular[int(num)]
    except:
      return "bu numarada soru yok"
  else:
    return "soru numarası sayı olmalıdır"