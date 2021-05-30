from random import choice
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
'Eyvah! En yakın arkadaşınla sevgilisini uygunsuz bi zamanda yakaladın. Durumu toparlamak için yapacağın ilk şey nedir?',
'Bu odada en kötü mizah anlayışı olan kim?\n', 'İlk ilişkin neden bitmişdi?\n', 'Birine verdiğin en kötü hediye neydi? (-)\n', 'Hiç yanlış bi söylendi veya dedikodu yaydın mı?\n', 'Hangisini tercih ederdin: sevmediğin biriyle çıkmak, yada seni sevmeyen biriyle çıkmak.\n', 'En son internette anonim bi şekilde birine hakaret etdiyinde ne zamandı?\n', 'Partnerim 100 kilo alsaydı yinede onunla birlikde olur muydun?\n', 'En son birini sevdiğin için huzursun hiss etdiyinde ne zamandı ve neden?\n', 'Hangisini tercih edersdin; bir vücut parçanı kayb etmek, yada Kardashianlardan biriyle evlenmek\n', 'Hiç birine karşı suç duyurusunda bulundun mu?\n', 'Hiç yanlışlıkla birinin mesajlaşmalarını okudun mu?\n', 'Online tanışma sitelerinde bi profilin var mı?\n', 'Sence senin bir gecelik fiyatın ne olmalı?\n', 'Bu odada kı hangi ikiliden en kötü çift olurdu?\n', 'En yakın arkadaşının en sevmediğin özelliği veya huyu\n', 'Bu odada seni en çok kim gıcık ediyor\n', 'Bu gece hiç yalan söyledin mi?\n', 'Gizlice sevdiğin ama söylemeye çekindiğin bu grup yada şarkıcı var mı?\n', 'Bu odada kı en kötü sır tutucu kim?\n', 'Sahip olduğun en kötü oyuncu ismi?\n', 'Söylemeye en utandığın önyargın var mı? Evetse kimlere ve neden?\n', 'Hiç birine fake hesapdan açıldın mı?\n', 'İsmini googlayarak bula bileceğin en utanç verici şey ne?\n', 'Kendi görünüşü 1-10 üzerinden puanlasan bu kaç olurdu?\n', 'Hiç hırsızlık yapdın mı? Ne çaldın? (-)\n', 'Hiç sarhoş olduğuna dair yalan söyledin mi?\n', 'Birine verdiğin en kaba lakab neydi?\n', 'İçerisinde bulunduğun en garip ortam hangisiydi?\n', 'Bu odada en yakışıklı babaya sahip olan kim?\n', 'Eğer partnerinin izini olsaydı, onu aldatır mıydın?\n', 'Bir kavgada gidicek olsaydın hangi tarafı seçerdin; haklı ama muhtemelen dayağı yiyecek olan taraf, yoksa haksız ama güçlü olan taraf mı?\n', 'Hiç profil fotoğrafını shopladın mı?\n', 'Beğendiğin için en çok utandığın film hangisi?\n', 'Söylediğin en son yalan neydi?\n', 'İlgini çeken birinde ilk kontrol etdiğin vücut parşası hangisi?\n', 'Hiç birine zorbalık yapdın mı?\n', 'Hiç duş almadan zaman geçirdiği en fazla süre ne kadardı?\n', 'Hiç birinin izinsizce fotoğrafını çekdin mi?\n', 'Kendi cinsinde dikkatini en çok çeken vücut parçası hangisi?\n', 'Bu odada 20 yaşında en başarı olacağını düşündüğün kişi kim?\n', 'Bu grupda en yönetici kişiliğe sahip kişi kim?\n', 'İsim vermeden bu grupdakı biri hakkında dürüst düşüncelerini söyle.'
]
def max():
  global sorular
  return len(sorular)
def soru18(hangisi):
  global sorular
  if hangisi == None:
    return choice (sorular)
  else:
    try:
      x=int(hangisi)
    except:
      return False
    if x > len (sorular):
      return False
    return sorular [x]