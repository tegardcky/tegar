from django.db import models
# from django.template.defaultfilters import slugify  
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField

class Kategori(models.Model):
    nama = models.CharField(max_length=200, blank= True, null= False)
    aktif = models.BooleanField(default= True)
    
    # banner_satu = models.ImageField(upload_to='gambar/banner', blank=False, null=True, verbose_name="Gambar Banner (575 x 200 pixel)")   
    banner_satu = ResizedImageField(size=[575, 200], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=True, null=True, verbose_name="Gambar 1 (575 x 200 pixel)")   
    banner_dua = ResizedImageField(size=[575, 200], quality=80, crop=['middle', 'center'] , upload_to='gambar/banner', blank=True, null=True, verbose_name="Gambar 1 (575 x 200 pixel)")
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True) 
    
    class Meta:  
        verbose_name_plural ="Data Kategori"
        
    # def __str__(self):     
    #     return self.nama 
    
    # def __str__(self): 
    #     return '%s, %s, %s' % (self.nama, self.aktif, self.slug)  
    
    def __str__(self): 
        return f"Nama: {self.nama}"  
    
    @property
    def get_produk(self):
        return Produk.objects.filter(kategori__nama=self.nama)



        
    #def save(self, *args, **kwargs):  # new         
    #    if not self.slug: 
    #        self.slug = slugify(self.nama) 
     #   return super().save(*args, **kwargs) 


class Produk(models.Model):
    KETERANGAN=( 
        ('Baru', 'Baru'), 
        ('Lama' , 'Lama'), 
    )
    class Meta:  
        verbose_name_plural ="Data Produk"
    
    kategori = models.ForeignKey(Kategori, null=True, blank=True, related_name="produks", on_delete=models.SET_NULL)
    nama_produk = models.CharField(max_length=200, blank=True, null=True)
    gambar = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/product', blank=False, null=True, verbose_name="Gambar (270 x 250 pixel)") 
    gambar_satu = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/product', blank=True, null=True, verbose_name="Gambar (270 x 250 pixel)") 
    gambar_dua = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/product', blank=True, null=True, verbose_name="Gambar (270 x 250 pixel)")     
    gambar_tiga = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/product', blank=True, null=True, verbose_name="Gambar (270 x 250 pixel)") 
    gambar_empat = ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/product', blank=True, null=True, verbose_name="Gambar (270 x 250 pixel)")     
    gambar_lima= ResizedImageField(size=[270, 250], quality=80, crop=['middle', 'center'] , upload_to='gambar/product', blank=True, null=True, verbose_name="Gambar (270 x 250 pixel)")
    slug = models.SlugField(max_length=200, unique=True)
    # keterangan = models.TextField(max_length=200, blank=True, null=True)
    keterangan = RichTextField(blank=True, null=True)      
    harga = models.IntegerField(blank=True, null=True)     
    no_whatsup = models.CharField(max_length=200, blank=True, null=True)     
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)    
    diskon = models.IntegerField(default=0,  blank=True, null=True, verbose_name="Diskon %")     
    dibeli = models.IntegerField(default=0,  blank=True, null=True)     
    keterangan_barang = models.CharField(max_length=200, null=True, choices=KETERANGAN)
    
    @property     
    def setelah_diskon(self):         
        if self.diskon == 0 : 
            nilai_diskon = self.harga        
        else: 
            jml = self.diskon / 100                
            nilai_diskon = self.harga - (jml * self.harga)         
        return nilai_diskon 
    def __str__(self):
        return self.nama_produk



class Slide(models.Model): 
    class Meta:  
        verbose_name_plural ="Data Slide"
    
    teks_awal = RichTextField(blank=True, null=True)     
    teks_dua = RichTextField(blank=True, null=True)     
    teks_tiga = RichTextField(blank=True, null=True)    
    gambar_slide = models.ImageField(upload_to='gambar/slide', blank=False, null=True, verbose_name="Gambar Slide (475 x 880 pixel)") 
    aktif = models.BooleanField(default=True) 

class Kontak(models.Model):
    
    class Meta:  
        verbose_name_plural ="Data Kontak"
     
    nama = models.CharField(max_length=200, blank=False, null=True)     
    no_whatsup = models.EmailField(max_length=200,blank=False, null=True)     
    email = models.EmailField(max_length=200,blank=False, null=True)    
    subject = models.CharField(max_length=200, blank=False, null=True)    
    isi = models.TextField(max_length=200, blank=False, null=True) 

class Profil(models.Model): 
    
    class Meta:  
        verbose_name_plural ="Data Profil"
        
    nama = models.CharField(max_length=200, blank=False, null=True)    
    # keterangan = models.TextField(max_length=200, blank=True, null=True)
    keterangan = RichTextField(blank=True, null=True)   
    gambar = ResizedImageField(size=[1920, 1200], quality=80, crop=['middle', 'center'] , upload_to='gambar/profil', blank=True, null=True, verbose_name="Gambar (1920 x 1200 pixel)")
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True) 
    
    
class Statis(models.Model): 
    
    class Meta:  
        verbose_name_plural ="Data Statis"
    
    alamat_kami = models.TextField(max_length=200, blank=False, null=True)     
    telpon = models.CharField(max_length=200, blank=False, null=True)     
    email = models.EmailField(max_length=200, blank=False, null=True) 

class ChatID(models.Model):
    chatid = models.CharField(max_length=200, blank=False, null=True)
    nama = models.CharField(max_length=200, blank=False, null=True)
    aktif = models.BooleanField(default= True)
    
    class Meta:
            verbose_name_plural ="Data Chat ID"



