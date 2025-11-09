import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    """Bot ilk tetiklendiğinde çalışır."""
    print(f'{bot.user} olarak giriş yaptık')

@bot.command('hello')
async def hello(ctx):
    """İngilizce ne kadar kolay, değil mi?"""
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command('heh')
async def heh(ctx, count_heh = 5):
    """HEHEHEHHHEH"""
    await ctx.send("he" * count_heh)

@bot.command('nasilsin')
async def nasilsin(ctx, count_nasilsin = 1):
    """Nasıl Olduğunu Sorar."""
    await ctx.send("İyiyim ,sen nasılsın? " * count_nasilsin)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Birisi Katıldığında Bildirir."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command('mem')
async def mem(ctx):
    """Ne kadar az mem var."""
    files = os.listdir("images")
    sf = random.choice(files)
    with open(f'images/{sf}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    """Sadece Ördek Fotoğrafı"""
    image_url = get_duck_image_url()
    await ctx.send(image_url)
def get_fox_image_url():
    url = "https://randomfox.ca/floof/"
    res1 = requests.get(url)
    data = res1.json()
    return data['image']
@bot.command('fox')
async def duck(ctx):
    """Ne güzel bir tilki, sence nasıl?"""
    image_url = get_fox_image_url()
    await ctx.send(image_url)
def get_fox2_image_url():
    url = "https://random.dog/woof.json"
    res1 = requests.get(url)
    data = res1.json()
    return data['image']
@bot.command('fox2')
async def fox2(ctx):
    """Genelde Çalışmaz ama Çalışırsa Şanslısın."""
    image_url = get_fox2_image_url()
    await ctx.send(image_url)
@bot.command('kirlilik_nasil_onlenir')
async def kirlilik_nasil_onlenir(ctx, count_kirlilik_nasil_onlenir=1):
    """Kirliliği Önleyebiliyorsan, Önle!"""
    await ctx.send("""1.Geri dönüşüm ve atık azaltma: Kağıt, plastik, cam ve metal gibi maddeleri geri dönüştürmek; tek kullanımlık ürünler yerine yeniden kullanılabilir olanları tercih etmek çevre kirliliğini büyük ölçüde azaltır.

2.Enerji ve su tasarrufu: Gereksiz yere ışıkları açık bırakmamak, suyu boşa akıtmamak ve yenilenebilir enerji kaynaklarını kullanmak doğal kaynakların korunmasını sağlar.

3.Doğayı koruma ve ağaçlandırma: Ağaç dikmek, yeşil alanları korumak ve doğaya zarar veren faaliyetlerden kaçınmak hem havayı temizler hem de ekosistemi dengede tutar.""")
@bot.command("geri_donusum_nedir")
async def geri_donusum_nedir(ctx, count_geri_donusum_nedir=1):
    """Geri Dönüşümün ne olduğunu anla"""
    await ctx.send("""Geri dönüşüm, kullanılmış ya da atık hale gelmiş maddelerin (örneğin plastik, cam, metal, kâğıt gibi) yeniden işlenip kullanıma kazandırılması sürecidir.

Yani çöpe atmak yerine bu maddeler tekrar ham madde haline getirilir ve yeni ürünlerin yapımında kullanılır.
Bu sayede:

Doğal kaynaklar korunur,

Enerji tasarrufu sağlanır,

Çevre kirliliği azalır.

Örneğin, kullanılmış cam şişeler eritilerek yeniden cam şişe yapılabilir; eski kâğıtlar geri dönüştürülüp yeni defter veya gazete olarak kullanılabilir.""")
@bot.command('evde_yapabilecegimiz_3_geridonusum_projesi')
async def evde_yapabilecegimiz_3_geridonusum_projesi(ctx, count_evde_yapabilecegimiz_3_geridonusum_projesi=1):
    """Evde yapamayacağın 3 Proje"""
    await ctx.send("""Pet şişeden saksı yapımı:
Boş plastik şişeleri ortadan kesin, alt kısmını süsleyip küçük bitkiler veya çiçekler için saksı olarak kullanabilirsiniz. Hem eğlenceli hem de doğa dostu bir projedir. 🌱


Eski kavanozdan mumluk:
Bitmiş reçel veya kahve kavanozlarını temizleyip içine mum yerleştirerek dekoratif bir mumluk yapabilirsiniz. Dilerseniz dışını boya veya iplerle süsleyebilirsiniz. 🕯️


Gazete veya dergiden sepet yapımı:
Kullanmadığınız gazete sayfalarını rulo yapıp örerek küçük bir sepet veya kalemlik hazırlayabilirsiniz. Hem kâğıdı değerlendirmiş olursunuz hem de odanıza el yapımı bir eşya eklersiniz. 🧺

""")
bot.run("GİZLİ_TOKEN")
