

import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import Token

bot = Bot(token=Token)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Assalomu alaykum\nNa gap?')

@dp.message(Command('salom')) # /salom
async def cmd_salom(message: Message):
    await message.reply('Vaaleykum Assalom!')

@dp.message(F.text == 'Assalomu alaykum')
async def cmd_na_gap(message: Message):
    await message.reply('Valeykum Assalom!')

@dp.message(F.photo)
async def photo(message: Message):
    await message.answer(f'Foto ID si: {message.photo[-1].file_id}')

@dp.massage(F.text == 'yordam kerak')
async def yordam(message:Message):
    await message.reply('qanday yordam bera olaman')

@dp.message(F.text == 'nima funksiyang bor ozi?')
async def funksiyasi(message:Message):
    await message.reply('men senga ranglar haqida malumot beraman va hayvonlar')

@dp.message(F.text == 'sariq rangi haqida malumot')
async def sariq(message:Message):
    await message.reply('Sariq rang — quvonch, quvvat, umid, va ijodkorlik ramzi hisoblanadi.Quyosh, limon, asalari, banan kabi narsalar sariq rangda bo‘ladi')

@dp.message(F.text == 'yashil rang haqida malumot')
async def yashil(message:Message):
    await message.reply('Yashil rang — tabiat, hayot, baraka, osoyishtalik va yangilanish ramzi hisoblanadi')

@dp.message(F.text == 'qora rangi haqida malumot')
async def qora(message:Message):
    await message.reply('Qora rang ko‘plab ma’nolarni ifodalaydi, ular ijobiy ham, salbiy ham bo‘lishi mumkin')

@dp.message(F.text == 'oq rangi haqida malumot')
async def oq(message:Message):
    await message.reply('')

@dp.message(F.text == 'ko‘k rang haqida malumot')
async def kok(message: Message):
    await message.reply("Ko‘k rang — ishonch, osoyishtalik va osmon ramzi. Professional va taskin beruvchi rang.")

@dp.message(F.text == 'qizil rang haqida malumot')
async def qizil(message: Message):
    await message.reply("Qizil rang — sevgi, ehtiros, xavf va kuch timsoli.")

@dp.message(F.text == 'pushti rang haqida malumot')
async def pushti(message: Message):
    await message.reply("Pushti rang — nafislik, mehr, g‘amxo‘rlik va noziklik ifodasidir.")

@dp.message(F.text == 'jigarrang rang haqida malumot')
async def jigarrang(message: Message):
    await message.reply("Jigarrang — yer, barqarorlik va ishonch timsoli bo‘lib, tabiiylikni ifodalaydi.")

@dp.message(F.text == 'kulrang rang haqida malumot')
async def kulrang(message: Message):
    await message.reply("Kulrang — neytral va jiddiy rang bo‘lib, ko‘pincha professional dizaynda ishlatiladi.")

@dp.message(F.text == 'oltin rang haqida malumot')
async def oltin(message: Message):
    await message.reply("Oltin rang — boylik, hashamat va muvaffaqiyat ramzi.")

@dp.message(F.text == 'moviy rang haqida malumot')
async def moviy(message: Message):
    await message.reply("Moviy rang — tinchlik va osoyishtalik ramzi, ko‘plab madaniyatlarda ilohiylikni ifodalaydi.")

@dp.message(F.text == 'siyoh rang haqida malumot')
async def siyoh(message: Message):
    await message.reply("Siyoh rang — chuqurlik, sirli va jiddiylik ramzi.")

@dp.message(F.text == 'turkuaz rang haqida malumot')
async def turkuaz(message: Message):
    await message.reply("Turkuaz rang — yangilanish va o‘sishni ifodalaydi, tabiiy va tinchlantiruvchi rang.")

@dp.message(F.text == 'binafsha rang haqida malumot')
async def binafsha(message: Message):
    await message.reply("Binafsha rang – sirli, jozibali va ruhiy energiya ramzi hisoblanadi.")

@dp.message(F.text == 'bezak rang haqida malumot')
async def bezak(message: Message):
    await message.reply("Bezak rang – bezaklarda ishlatiladigan har xil yorqin va qiziqarli ranglar to‘plami.")

@dp.message(F.text == 'sher haqida malumot')
async def sher(message: Message):
    await message.reply("Sher — o‘rmon podshosi. Kuchli, jasur va ijtimoiy hayvon.")

@dp.message(F.text == 'mushuk haqida malumot')
async def mushuk(message: Message):
    await message.reply("Mushuk — mustaqil va toza uy hayvoni. Ular tinch va ko‘p uxlaydi.")

@dp.message(F.text == 'it haqida malumot')
async def it(message: Message):
    await message.reply("It — insonning sodiq do‘sti. Ular sadoqatli va ko‘plab vazifalarda foydali.")

@dp.message(F.text == 'fil haqida malumot')
async def fil(message: Message):
    await message.reply("Fil — eng katta quruqlik hayvoni. Ular aqlli va mehribon.")

@dp.message(F.text == 'qushlar haqida malumot')
async def qushlar(message: Message):
    await message.reply("Qushlar — qanotli, tuxum qo‘yuvchi va aksari ucha oladigan hayvonlar.")

@dp.message(F.text == 'maymun haqida malumot')
async def maymun(message: Message):
    await message.reply("Maymunlar aqlli, faol va ijtimoiy hayvonlardir.")

@dp.message(F.text == 'kapalak haqida malumot')
async def kapalak(message: Message):
    await message.reply("Kapalak — go‘zal, rang-barang qanotli hasharot bo‘lib, yengillik ramzi hisoblanadi.")

@dp.message(F.text == 'ilon haqida malumot')
async def ilon(message: Message):
    await message.reply("Ilon — sudralib yuradigan, ba'zilari zaharli bo‘lgan hayvon.")

@dp.message(F.text == 'quyon haqida malumot')
async def quyon(message: Message):
    await message.reply("Quyon — yumshoq tukli va tez yuguradigan o‘txo‘r hayvon.")

@dp.message(F.text == 'tulki haqida malumot')
async def tulki(message: Message):
    await message.reply("Tulki — ayyor, chaqqon va yovvoyi hayvon sifatida tanilgan.")

@dp.message(F.text == 'bo‘ri haqida malumot')
async def bori(message: Message):
    await message.reply("Bo‘ri — to‘da bilan yashovchi, kuchli yirtqich hayvon.")

@dp.message(F.text == 'zebra haqida malumot')
async def zebra(message: Message):
    await message.reply("Zebra — qora-oq chiziqli o‘txo‘r hayvon, Afrikada yashaydi.")

@dp.message(F.text == 'jirafa haqida malumot')
async def jirafa(message: Message):
    await message.reply("Jirafa — dunyodagi eng bo‘yi baland hayvon, daraxt barglarini yeydi.")

@dp.message(F.text == 'ayiq haqida malumot')
async def ayiq(message: Message):
    await message.reply("Ayiq — kuchli yovvoyi hayvon, ammo ba'zida osoyishta va yolg‘onchi ko‘rinadi.")

@dp.message(F.text == 'burgut haqida malumot')
async def burgut(message: Message):
    await message.reply("Burgut — baland uchuvchi va kuchli yirtqich qush.")

@dp.message(F.text == 'lochin haqida malumot')
async def lochin(message: Message):
    await message.reply("Lochin — tez uchuvchi va o'tkir ko‘zli yirtqich qush.")

@dp.message(F.text == 'to‘tiqush haqida malumot')
async def totiqush(message: Message):
    await message.reply("To‘tiqush — rangli patli va gapni taqlid qiluvchi qush.")

@dp.message(F.text == 'sigir haqida malumot')
async def sigir(message: Message):
    await message.reply("Sigir — sut beruvchi chorva hayvoni.")

@dp.message(F.text == 'ot haqida malumot')
async def otminish(message: Message):
    await message.reply("Ot — qadimdan odamlar tomonidan transport va ishlash uchun ishlatilgan hayvon.")

@dp.message(F.text == 'eshak haqida malumot')
async def eshakhaqida(message: Message):
    await message.reply("Eshak — chidamli va kam talabi bor hayvon, yuk tashishda foydali.")

@dp.message(F.text == 'parrandalar haqida malumot')
async def parrandalar(message: Message):
    await message.reply("Parrandalar — uylarda boqiladigan qanotli hayvonlar, tuxum beradi va go‘shti uchun saqlanadi.")

@dp.message(F.text == 'tovuq haqida malumot')
async def tovuq(message: Message):
    await message.reply("Tovuq — uyda boqiladigan qush, tuxum va go‘shti uchun yetishtiriladi.")

@dp.message(F.text == 'quyon haqida malumot')
async def quyon(message: Message):
    await message.reply("Quyon — yumshoq tukli, tez yuguradigan uy hayvoni.")

@dp.message(F.text == 'quyosh nima?')
async def handler1(message: Message):
    await message.reply("Quyosh — Quyosh tizimining markaziy yulduzi.")

@dp.message(F.text == 'dinozavrlar qachon yashagan?')
async def handler2(message: Message):
    await message.reply("Dinozavrlar taxminan 230 million yil avval yashagan.")

@dp.message(F.text == 'everest cho‘qqisi qayerda?')
async def handler3(message: Message):
    await message.reply("Everest cho‘qqisi Nepal va Xitoy chegarasida joylashgan.")

@dp.message(F.text == 'internet nima?')
async def handler4(message: Message):
    await message.reply("Internet — global kompyuter tarmog‘i bo‘lib, milliardlab qurilmalarni bog‘laydi.")

@dp.message(F.text == 'monaliza kim tomonidan chizilgan?')
async def handler5(message: Message):
    await message.reply("Monaliza — Leonardo da Vinci tomonidan chizilgan mashhur portret.")

@dp.message(F.text == 'yer necha yoshda?')
async def handler6(message: Message):
    await message.reply("Yerning yoshi taxminan 4.5 milliard yil.")

@dp.message(F.text == 'kitlar nima bilan nafas oladi?')
async def handler7(message: Message):
    await message.reply("Kitlar o‘pka orqali nafas oladi, ular baliq emas.")

@dp.message(F.text == 'nil daryosi qayerda?')
async def handler8(message: Message):
    await message.reply("Nil daryosi Afrikada joylashgan va eng uzun daryolardan biridir.")

@dp.message(F.text == 'robot nima?')
async def handler9(message: Message):
    await message.reply("Robot — avtomatik ishlovchi mashina yoki mexanik tizim.")

@dp.message(F.text == 'futbol nechta o‘yinchi bilan o‘ynaladi?')
async def handler10(message: Message):
    await message.reply("Futbol jamoasida 11 nafar o‘yinchi bo‘ladi.")

@dp.message(F.text == 'kuchukcha haqida malumot')
async def kuchukcha(message: Message):
    await message.reply("Kuchukcha — insonning eng sodiq do‘sti, himoya va do‘stlik uchun boqiladi.")

@dp.message(F.text == 'mushukcha haqida malumot')
async def mushukcha(message: Message):
    await message.reply("Mushukcha — mustaqil va o‘yinchoq uy hayvoni, ko‘p uxlashni yoqtiradi.")

@dp.message(F.text == 'gerbil haqida malumot')
async def gerbil(message: Message):
    await message.reply("Gerbil — kichik va faol kemiruvchi uy hayvoni, asosan qulay sharoitlarda boqiladi.")

@dp.message(F.text == 'baliq haqida malumot')
async def baliq(message: Message):
    await message.reply("Baliq — suvda yashovchi uy hayvoni, akvariumlarda boqiladi va tinchlantiruvchi effekt beradi.")

@dp.message(F.text == 'xoroz haqida malumot')
async def xoroz(message: Message):
    await message.reply("Xoroz — tovuq oilasidan bo‘lib, o‘zining qo‘ng‘iroq qilish ovozi bilan mashhur.")

@dp.message(F.text == 'kanareyka haqida malumot')
async def kanareyka(message: Message):
    await message.reply("Kanareyka — kichik va chiroyli qush, juda yaxshi kuylaydi.")

@dp.message(F.text == 'musika nima?')
async def handler11(message: Message):
    await message.reply("Musika — tovushlar orqali ifodalanadigan san’at turi.")

@dp.message(F.text == 'ko‘k qurbaqalar zaharlimi?')
async def handler12(message: Message):
    await message.reply("Baʼzi ko‘k qurbaqalar juda kuchli zaharga ega.")

@dp.message(F.text == 'kompyuter nima?')
async def handler13(message: Message):
    await message.reply("Kompyuter — ma’lumotlarni qayta ishlovchi elektron qurilma.")

@dp.message(F.text == 'chempionlar ligasi nima?')
async def handler14(message: Message):
    await message.reply("Chempionlar Ligasi — Yevropaning eng kuchli klublariga mo‘ljallangan futbol musobaqasi.")

@dp.message(F.text == 'qor qanday hosil bo‘ladi?')
async def handler15(message: Message):
    await message.reply("Qor suv bug‘ining muz kristallariga aylanishi natijasida hosil bo‘ladi.")

@dp.message(F.text == 'astronomiya fani nimani o‘rganadi?')
async def handler16(message: Message):
    await message.reply("Astronomiya — yulduzlar, sayyoralar va koinotni o‘rganadigan fan.")

@dp.message(F.text == 'tiger hayvoni qayerda yashaydi?')
async def handler17(message: Message):
    await message.reply("Tiger asosan Osiyoda, Hindiston, Bangladesh va Rossiyada uchraydi.")

@dp.message(F.text == 'amerika qit’asi nechta davlatdan iborat?')
async def handler18(message: Message):
    await message.reply("Shimoliy va Janubiy Amerikani qo‘shib hisoblaganda 35 dan ortiq davlat mavjud.")

@dp.message(F.text == 'oyda havo bormi?')
async def handler19(message: Message):
    await message.reply("Oyda atmosfera yo‘q, shuning uchun havo ham yo‘q.")

@dp.message(F.text == 'neon nima?')
async def handler20(message: Message):
    await message.reply("Neon — kimyoviy element, ko‘pincha reklama chiroqlarida ishlatiladi.")

@dp.message(F.text == 'qushlar nega uchadi?')
async def handler21(message: Message):
    await message.reply("Qushlar qanotlari va yengil skeleti tufayli uchishga moslashgan.")

@dp.message(F.text == 'dunyo aholisining eng ko‘p mamlakati?')
async def handler22(message: Message):
    await message.reply("Xitoy — dunyodagi eng ko‘p aholiga ega mamlakat.")

@dp.message(F.text == 'musiqa notasi nima?')
async def handler23(message: Message):
    await message.reply("Nota — musiqiy tovushlarni yozma ifodalash usuli.")

@dp.message(F.text == 'vulkan qanday portlaydi?')
async def handler24(message: Message):
    await message.reply("Vulkan yer osti bosimi ortishi natijasida portlaydi.")

@dp.message(F.text == 'neandertal odam kim?')
async def handler25(message: Message):
    await message.reply("Neandertallar qadimgi odamzod vakillari bo‘lib, hozirgi odamzod ajdodlaridan biri.")

@dp.message(F.text == 'telegram kim yaratgan?')
async def handler26(message: Message):
    await message.reply("Telegram Pavel Durov tomonidan yaratilgan.")

@dp.message(F.text == 'chaqmoq qanday paydo bo‘ladi?')
async def handler27(message: Message):
    await message.reply("Chaqmoq havo zarralari o‘rtasidagi elektr zaryadlar to‘qnashuvi natijasida paydo bo‘ladi.")

@dp.message(F.text == 'mars sayyorasi haqida ayting')
async def handler28(message: Message):
    await message.reply("Mars — qizil sayyora bo‘lib, unda hayot bo‘lishi mumkin deb taxmin qilinadi.")

@dp.message(F.text == 'ko‘rshapalak qushmi?')
async def handler29(message: Message):
    await message.reply("Yo‘q, ko‘rshapalak sut emizuvchi hayvon.")

@dp.message(F.text == 'ekvatorda ob-havo qanday?')
async def handler30(message: Message):
    await message.reply("Ekvatorda iqlim issiq va nam, yil bo‘yi deyarli o‘zgarmaydi.")

@dp.message(F.text == 'suv necha darajada qaynaydi?')
async def handler32(message: Message):
    await message.reply("Suv normal bosimda 100°C da qaynaydi.")

@dp.message(F.text == 'inson yuragi bir kunda necha marta uradi?')
async def handler33(message: Message):
    await message.reply("O‘rtacha inson yuragi kuniga 100,000 martagacha uradi.")

@dp.message(F.text == 'ari qanday asal hosil qiladi?')
async def handler34(message: Message):
    await message.reply("Ari gul nektarini yig‘ib, uni asalga aylantiradi.")

@dp.message(F.text == 'kometalar nima?')
async def handler35(message: Message):
    await message.reply("Kometalar muz, chang va toshdan iborat osmon jismlaridir.")

@dp.message(F.text == 'sag‘ana nima?')
async def handler36(message: Message):
    await message.reply("Sag‘ana — o‘tmishda hukmdorlar yoki zodagonlar dafn etilgan yodgorlik binosi.")

@dp.message(F.text == 'termometr nima o‘lchaydi?')
async def handler37(message: Message):
    await message.reply("Termometr haroratni o‘lchaydi.")

@dp.message(F.text == 'chaqaloqlar nega yig‘laydi?')
async def handler38(message: Message):
    await message.reply("Chaqaloqlar ehtiyojlarini bildirishi uchun yig‘laydi.")

@dp.message(F.text == 'google qachon tashkil topgan?')
async def handler39(message: Message):
    await message.reply("Google 1998-yil 4-sentyabrda tashkil topgan.")

@dp.message(F.text == 'baliqlar uxlaydimi?')
async def handler40(message: Message):
    await message.reply("Ha, baliqlar ham dam oladi, lekin ular ko‘zlarini yumolmaydi.")

@dp.message(F.text == 'nufuzli universitetlar qayerda joylashgan?')
async def handler41(message: Message):
    await message.reply("Eng nufuzli universitetlar AQSh, Britaniya, Kanada va boshqa rivojlangan davlatlarda joylashgan.")

@dp.message(F.text == 'pianino necha tugmachadan iborat?')
async def handler42(message: Message):
    await message.reply("Standart pianinoda 88 tugmacha bo‘ladi.")

@dp.message(F.text == 'tezlik o‘lchov birligi nima?')
async def handler43(message: Message):
    await message.reply("Tezlik odatda km/soat yoki m/s birligida o‘lchanadi.")

@dp.message(F.text == 'osmon nega ko‘k rangda?')
async def handler44(message: Message):
    await message.reply("Osmon quyosh nurlari atmosferada tarqalishi tufayli ko‘k rangda ko‘rinadi.")

@dp.message(F.text == 'dunyodagi eng katta okean qaysi?')
async def handler45(message: Message):
    await message.reply("Tinch okeani dunyodagi eng katta okeandir.")

@dp.message(F.text == 'ko‘zoynak nima uchun kerak?')
async def handler46(message: Message):
    await message.reply("Ko‘zoynak ko‘rishni yaxshilash yoki quyoshdan himoyalanish uchun ishlatiladi.")

@dp.message(F.text == 'yaponiyada texnologiya rivojlanganmi?')
async def handler47(message: Message):
    await message.reply("Ha, Yaponiya dunyodagi eng ilg‘or texnologiyalarga ega davlatlardan biridir.")

@dp.message(F.text == 'oy yer atrofida qancha vaqtda aylanadi?')
async def handler48(message: Message):
    await message.reply("Oy Yer atrofida taxminan 27.3 kunda bir marta aylanadi.")

@dp.message(F.text == 'paxta nima uchun foydali?')
async def handler49(message: Message):
    await message.reply("Paxta tola olish va kiyim-kechak ishlab chiqarishda keng qo‘llaniladi.")

@dp.message(F.text == 'kanada poytaxti qaysi shahar?')
async def handler50(message: Message):
    await message.reply("Kanadaning poytaxti — Ottava shahri.")

@dp.message(F.text == 'xorvachilik haqida malumot')
async def xorvachilik(message: Message):
    await message.reply("Xorvachilik — chorvachilik bilan bog‘liq ishlar, masalan, sigir, qo‘y va echki boqish.")

@dp.message(F.text == 'daraxt haqida malumot')
async def daraxt(message: Message):
    await message.reply("Daraxtlar — havoni tozalovchi va yer yuzining tabiiy go‘zalligini ta’minlovchi o‘simliklar.")

@dp.message(F.text == 'gullar haqida malumot')
async def gullar(message: Message):
    await message.reply("Gullar — go‘zallik va tabiatning bezagi, ko‘plab turlari bor.")

@dp.message(F.text == 'daryo haqida malumot')
async def daryo(message: Message):
    await message.reply("Daryo — yer yuzida oqib o'tadigan katta suv oqimi.")

@dp.message(F.text == 'toshkent viloyati haqida malumot')
async def toshkent_viloyati(message: Message):
    await message.reply("Toshkent viloyati — O‘zbekistonning markaziy qismida joylashgan, sanoat va qishloq xo‘jaligida rivojlangan hudud.")

@dp.message(F.text == 'samarqand viloyati haqida malumot')
async def samarqand_viloyati(message: Message):
    await message.reply("Samarqand viloyati — qadimiy tarixiy shahar va madaniyat markazi, sayyohlar orasida mashhur.")

@dp.message(F.text == 'buxoro viloyati haqida malumot')
async def buxoro_viloyati(message: Message):
    await message.reply("Buxoro viloyati — boy tarixga ega, islomiy me’morchilik obidalari bilan mashhur hudud.")

@dp.message(F.text == 'andijon viloyati haqida malumot')
async def andijon_viloyati(message: Message):
    await message.reply("Andijon viloyati — Farg‘ona vodiysining sharqiy qismida joylashgan, sanoat va dehqonchilik rivojlangan.")

@dp.message(F.text == 'fargona viloyati haqida malumot')
async def fargona_viloyati(message: Message):
    await message.reply("Farg‘ona viloyati — O‘zbekistonning eng gavjum va sermahsul hududlaridan biri.")

@dp.message(F.text == 'namangan viloyati haqida malumot')
async def namangan_viloyati(message: Message):
    await message.reply("Namangan viloyati — Farg‘ona vodiysining shimoliy qismida joylashgan, hunarmandchiligi bilan mashhur.")

@dp.message(F.text == 'navoiy viloyati haqida malumot')
async def navoiy_viloyati(message: Message):
    await message.reply("Navoiy viloyati — O‘zbekistonning markaziy qismida joylashgan, kon sanoati bilan tanilgan.")

@dp.message(F.text == 'xorazm viloyati haqida malumot')
async def xorazm_viloyati(message: Message):
    await message.reply("Xorazm viloyati — qadimiy madaniyat markazlaridan biri, Urganch shahri bu yerda joylashgan.")

@dp.message(F.text == 'qashqadaryo viloyati haqida malumot')
async def qashqadaryo_viloyati(message: Message):
    await message.reply("Qashqadaryo viloyati — janubiy hududlardan biri, neft va gaz sanoati rivojlangan.")

@dp.message(F.text == 'surxondaryo viloyati haqida malumot')
async def surxondaryo_viloyati(message: Message):
    await message.reply("Surxondaryo viloyati — O‘zbekistonning eng janubida joylashgan, iliq iqlimi bilan ajralib turadi.")

@dp.message(F.text == 'sirdaryo viloyati haqida malumot')
async def sirdaryo_viloyati(message: Message):
    await message.reply("Sirdaryo viloyati — kichikroq hudud bo‘lsa-da, qishloq xo‘jaligi bilan faol shug‘ullanadi.")

@dp.message(F.text == 'jizzax viloyati haqida malumot')
async def jizzax_viloyati(message: Message):
    await message.reply("Jizzax viloyati — O‘zbekistonning markaziy qismida joylashgan, tabiati go‘zal va serhosil.")

@dp.message(F.text == 'qarakalpogiston haqida malumot')
async def qaraqalpoq(message: Message):
    await message.reply("Qoraqalpog‘iston Respublikasi — O‘zbekiston tarkibidagi avtonom respublika, o‘ziga xos madaniyati va tabiati bor.")
@dp.message(F.text == 'xayr')
async def xayr(message: Message):
    await message.reply("Xayr! Yana ko‘rishguncha!")

@dp.message(F.text == 'rahmat')
async def raxmat(message: Message):
    await message.reply("Doim xursandman! Yordam kerak bo‘lsa, yozavering.")

@dp.message(F.text == 'salom')
async def salom(message: Message):
    await message.reply("Assalomu alaykum! Men sizga yordam berishga tayyorman.")

@dp.message(F.text == 'menga hammasi bolib nimalarni orgata olasan')
async def nima_haqidaliki(message:Message):
    await message.reply('hayvonlar,ranglar,ovqatlar haqida va boshqa savolarga ham javob beraman')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nGoodbye')
        